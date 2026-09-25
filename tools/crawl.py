"""Crawl Apple HIG via the DocC JSON API and render every page to Markdown."""
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://developer.apple.com/tutorials/data"
OUT = sys.argv[1]
os.makedirs(os.path.join(OUT, "raw"), exist_ok=True)


def fetch(path):
    url = f"{BASE}{path}.json"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.load(resp)
        except Exception as e:  # retry transient network errors, then re-raise with context
            if attempt == 3:
                raise RuntimeError(f"fetch failed for {url}: {e}") from e
            time.sleep(1.5 * (attempt + 1))


def inline(nodes, refs):
    out = []
    for n in nodes or []:
        t = n.get("type")
        if t == "text":
            out.append(n["text"])
        elif t == "codeVoice":
            out.append(f"`{n['code']}`")
        elif t == "emphasis":
            out.append(f"*{inline(n['inlineContent'], refs)}*")
        elif t == "strong":
            out.append(f"**{inline(n['inlineContent'], refs)}**")
        elif t == "reference":
            r = refs.get(n["identifier"], {})
            title = inline(n.get("overridingTitleInlineContent"), refs) if n.get("overridingTitleInlineContent") else r.get("title", n["identifier"])
            url = r.get("url", "")
            if url.startswith("/"):
                url = "https://developer.apple.com" + url
            out.append(f"[{title}]({url})" if url else title)
        elif t == "link":
            out.append(f"[{n.get('title', n.get('destination'))}]({n.get('destination')})")
        elif t == "image":
            r = refs.get(n["identifier"], {})
            alt = r.get("alt") or ""
            if alt:
                out.append(f"[Image: {alt}]")
        elif t in ("newTerm", "inlineHead", "superscript", "subscript", "strikethrough"):
            out.append(inline(n.get("inlineContent"), refs))
        elif "inlineContent" in n:
            out.append(inline(n["inlineContent"], refs))
    return "".join(out)


def blocks(nodes, refs, depth=0):
    out = []
    for n in nodes or []:
        t = n.get("type")
        if t == "heading":
            out.append("#" * (n.get("level", 2) + 1) + " " + n["text"])
        elif t == "paragraph":
            out.append(inline(n["inlineContent"], refs))
        elif t in ("unorderedList", "orderedList"):
            lines = []
            for i, item in enumerate(n["items"]):
                body = blocks(item["content"], refs, depth + 1).strip().replace("\n", "\n  ")
                bullet = f"{i+1}." if t == "orderedList" else "-"
                lines.append(f"{bullet} {body}")
            out.append("\n".join(lines))
        elif t == "aside":
            body = blocks(n["content"], refs, depth + 1).strip()
            name = n.get("name") or n.get("style", "Note").title()
            out.append("> **" + name + ":** " + body.replace("\n", "\n> "))
        elif t == "table":
            grid = [[blocks(c, refs, depth + 1).strip().replace("\n", " ").replace("|", "\\|") for c in row] for row in n["rows"]]
            # extendedData maps "row_col" -> {rowspan, colspan}; spanned-over cells arrive empty,
            # so copy the spanning cell's text into them to keep every Markdown row self-contained.
            for key, span in (n.get("extendedData") or {}).items():
                r0, c0 = map(int, key.split("_"))
                for r in range(r0, min(r0 + max(span.get("rowspan", 1), 1), len(grid))):
                    for c in range(c0, min(c0 + max(span.get("colspan", 1), 1), len(grid[r]))):
                        if (r, c) != (r0, c0) and not grid[r][c]:
                            grid[r][c] = grid[r0][c0]
            rows = ["| " + " | ".join(cells) + " |" for cells in grid]
            if rows:
                ncol = rows[0].count("|") - 1
                rows.insert(1, "|" + " --- |" * ncol)
            out.append("\n".join(rows))
        elif t == "codeListing":
            out.append("```" + (n.get("syntax") or "") + "\n" + "\n".join(n.get("code", [])) + "\n```")
        elif t == "row":
            for col in n.get("columns", []):
                out.append(blocks(col.get("content"), refs, depth + 1))
        elif t == "tabNavigator":
            for tab in n.get("tabs", []):
                out.append(f"**{tab.get('title')}**\n\n" + blocks(tab.get("content"), refs, depth + 1))
        elif t == "links":
            items = [inline([{"type": "reference", "identifier": i}], refs) for i in n.get("items", [])]
            out.append("\n".join("- " + x for x in items))
        elif t == "termList":
            for it in n.get("items", []):
                out.append(f"**{inline(it['term']['inlineContent'], refs)}**: " + blocks(it["definition"]["content"], refs, depth + 1).strip())
        elif t == "small":
            out.append(inline(n.get("inlineContent"), refs))
        elif t in ("video", "thematicBreak"):
            pass
        elif "content" in n:
            out.append(blocks(n["content"], refs, depth + 1))
        elif "inlineContent" in n:
            out.append(inline(n["inlineContent"], refs))
    return "\n\n".join(x for x in out if x)


def render(d, path):
    refs = d.get("references", {})
    title = d.get("metadata", {}).get("title", path)
    md = [f"# {title}", f"Source: https://developer.apple.com{path}"]
    if d.get("abstract"):
        md.append(inline(d["abstract"], refs))
    for sec in d.get("primaryContentSections", []):
        md.append(blocks(sec.get("content"), refs))
    for ts in d.get("topicSections", []):
        head = ts.get("title")
        if head:
            md.append(f"## {head}")
        md.append("\n".join("- " + inline([{"type": "reference", "identifier": i}], refs) for i in ts["identifiers"]))
    for sec in d.get("seeAlsoSections", []):
        md.append(f"## See also: {sec.get('title','')}")
    return title, "\n\n".join(md) + "\n"


def child_paths(d):
    refs = d.get("references", {})
    paths = []
    for ts in d.get("topicSections", []):
        for i in ts["identifiers"]:
            url = refs.get(i, {}).get("url", "")
            if url.startswith("/design/human-interface-guidelines"):
                paths.append((ts.get("title"), url))
    return paths


pages = []  # (path, parent, group, title)
seen = set()


def visit(path, parent, group):
    if path in seen:
        return []
    seen.add(path)
    d = fetch(path)
    title, md = render(d, path)
    slug = path.rsplit("/", 1)[-1]
    with open(os.path.join(OUT, "raw", slug + ".md"), "w") as f:
        f.write(md)
    pages.append({"path": path, "parent": parent, "group": group, "title": title, "slug": slug, "chars": len(md)})
    return [(p, path, g) for g, p in child_paths(d)]


frontier = [("/design/human-interface-guidelines", None, None)]
with ThreadPoolExecutor(8) as ex:
    while frontier:
        results = list(ex.map(lambda a: visit(*a), frontier))
        frontier = [c for r in results for c in r if c[0] not in seen]
        # de-dup within a level
        uniq = {}
        for c in frontier:
            uniq.setdefault(c[0], c)
        frontier = list(uniq.values())
        print(f"visited={len(seen)} next={len(frontier)}", flush=True)

with open(os.path.join(OUT, "pages.json"), "w") as f:
    json.dump(pages, f, indent=1)
print("total pages", len(pages), "total chars", sum(p["chars"] for p in pages))
