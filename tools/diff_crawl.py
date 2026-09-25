"""Compare a fresh crawl against the committed baseline (tools/hig-manifest.json).

Prints which HIG pages are new, changed, or removed, with the reference file each maps to,
so only those pages need re-distilling.

Usage:
  python3 diff_crawl.py <crawl_out_dir>            # report only
  python3 diff_crawl.py <crawl_out_dir> --update   # also overwrite the baseline with this crawl
"""
import json
import os
import sys

ROOT = "/design/human-interface-guidelines"
MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hig-manifest.json")

crawl_dir = sys.argv[1]
update = "--update" in sys.argv[2:]

with open(os.path.join(crawl_dir, "pages.json")) as f:
    new_pages = json.load(f)
if any("sha256" not in p for p in new_pages):
    raise SystemExit(f"{crawl_dir}/pages.json has no sha256 fields; re-run tools/crawl.py")


def manifest_of(pages):
    by_path = {p["path"]: p for p in pages}
    has_children = {p["parent"] for p in pages}

    def section(p):
        while p["parent"] != ROOT:
            p = by_path[p["parent"]]
        return p["slug"]

    out = {}
    for p in pages:
        if p["path"] == ROOT:
            continue
        # Section and sub-group pages only list links; they have no reference file.
        ref = None if p["path"] in has_children else f"references/{section(p)}/{p['slug']}.md"
        out[p["path"]] = {"title": p["title"], "sha256": p["sha256"], "reference": ref}
    return out


new = manifest_of(new_pages)
old = {}
if os.path.exists(MANIFEST):
    with open(MANIFEST) as f:
        old = json.load(f)

added = sorted(set(new) - set(old))
removed = sorted(set(old) - set(new))
changed = sorted(p for p in set(new) & set(old) if new[p]["sha256"] != old[p]["sha256"])

for label, paths, src in (("NEW", added, new), ("CHANGED", changed, new), ("REMOVED", removed, old)):
    for p in paths:
        print(f"{label:8} {src[p]['reference'] or '(index page: update INDEX.md / SKILL.md routing)'}  <- {p}")
print(f"new={len(added)} changed={len(changed)} removed={len(removed)} unchanged={len(new) - len(added) - len(changed)}")

if update:
    with open(MANIFEST, "w") as f:
        json.dump(new, f, indent=1, sort_keys=True)
    print(f"baseline updated: {MANIFEST}")
