"""Check distilled references against raw pages.

For each non-index page: the reference file exists, and every spec-like number in the raw page
(e.g. 44x44, 4.5:1, 17 pt, 10%, 1024x1024) also appears in the reference. Also reports the ratio of
bold guideline sentences in raw vs. rule bullets in the reference, to flag pages that may have dropped rules.

Usage: python3 verify.py <crawl_out_dir> <skill_dir>
"""
import json
import os
import re
import sys
from collections import defaultdict

crawl_dir, skill_dir = sys.argv[1], sys.argv[2]
ROOT = "/design/human-interface-guidelines"
pages = json.load(open(os.path.join(crawl_dir, "pages.json")))
children = defaultdict(list)
for p in pages:
    children[p["parent"]].append(p)

section_of = {}
for sec in children[ROOT]:
    stack = list(children[sec["path"]])
    while stack:
        p = stack.pop()
        section_of[p["path"]] = sec["slug"]
        stack.extend(children[p["path"]])

SPEC = re.compile(r"\b\d+(?:\.\d+)?(?:\s?[x×]\s?\d+(?:\.\d+)?)+\b|\b\d+(?:\.\d+)?:\d+\b|\b\d+(?:\.\d+)?\s?(?:pt|pts|px|%|ms|mm|Hz|fps)\b")
BOLD_RULE = re.compile(r"^\*\*[^*]{12,}\*\*", re.M)


def norm(s):
    return re.sub(r"\s+", "", s.replace("×", "x").replace("pts", "pt").lower())


problems = 0
for p in pages:
    if p["path"] not in section_of or children[p["path"]]:
        continue
    ref = os.path.join(skill_dir, "references", section_of[p["path"]], p["slug"] + ".md")
    if not os.path.exists(ref):
        print(f"MISSING  {ref}")
        problems += 1
        continue
    raw = open(os.path.join(crawl_dir, "raw", p["slug"] + ".md")).read()
    raw = raw.split("### Change log")[0]
    out = open(ref).read()
    out_n = norm(out)
    missing = sorted({m for m in SPEC.findall(raw) if norm(m) not in out_n})
    rules_raw = len(BOLD_RULE.findall(raw))
    rules_out = len(re.findall(r"^\s*- \*\*", out, re.M))
    ratio = len(out) / max(len(raw), 1)
    flag = missing or (rules_raw and rules_out < 0.85 * rules_raw)
    if flag:
        problems += 1
        print(f"CHECK    {p['slug']}: rules {rules_out}/{rules_raw}, size {ratio:.0%}, missing specs: {missing[:15]}")
print("pages with issues:", problems)
