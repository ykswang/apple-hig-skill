"""Build references/INDEX.md from the crawl manifest (pages.json + raw/*.md).

Usage: python3 build_index.py <crawl_out_dir> <skill_dir>
"""
import json
import os
import sys
from collections import defaultdict

crawl_dir, skill_dir = sys.argv[1], sys.argv[2]
ROOT = "/design/human-interface-guidelines"

with open(os.path.join(crawl_dir, "pages.json")) as f:
    pages = json.load(f)

children = defaultdict(list)
for p in pages:
    children[p["parent"]].append(p)

# Crawl order is nondeterministic (thread pool); restore the site's menu order, which is the
# order the parent page lists its children.
by_path = {p["path"]: p for p in pages}
for parent, kids in children.items():
    slug = by_path[parent]["slug"] if parent in by_path else "human-interface-guidelines"
    with open(os.path.join(crawl_dir, "raw", slug + ".md")) as f:
        listing = f.read()
    kids.sort(key=lambda k: listing.find(f"https://developer.apple.com{k['path']})"))


def abstract(slug):
    # render() in crawl.py writes: "# Title", blank, "Source: ...", blank, abstract
    with open(os.path.join(crawl_dir, "raw", slug + ".md")) as f:
        lines = [l.strip() for l in f.read().split("\n\n")]
    return lines[2] if len(lines) > 2 and not lines[2].startswith(("#", "[", "-")) else ""


def entry(p, section):
    rel = f"{section}/{p['slug']}.md"
    if not os.path.exists(os.path.join(skill_dir, "references", rel)):
        raise SystemExit(f"missing reference file for {p['path']}: references/{rel}")
    return f"- [{p['title']}]({rel}) — {abstract(p['slug'])}"


out = [
    "# Apple HIG reference index",
    "",
    "Every page of Apple's Human Interface Guidelines, distilled. Open only the files relevant to the task.",
    "",
]
for sec in children[ROOT]:
    section = sec["slug"]
    out += [f"## {sec['title']}", "", f"_{abstract(section)}_", ""]
    for p in children[sec["path"]]:
        if children[p["path"]]:  # sub-group (e.g. Components → Menus and actions)
            out += [f"### {p['title']}", ""]
            out += [entry(c, section) for c in children[p["path"]]]
            out.append("")
        else:
            out.append(entry(p, section))
    out.append("")

with open(os.path.join(skill_dir, "references", "INDEX.md"), "w") as f:
    f.write("\n".join(out))
print("pages indexed:", sum(1 for l in out if l.startswith("- [")))
