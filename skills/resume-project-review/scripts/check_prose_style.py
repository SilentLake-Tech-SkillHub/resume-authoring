#!/usr/bin/env python3
"""Read-only prose-style checker for resume wording. Reports rule + position only, never the text.

Rules (see references/prose-style.md):
  negation_contrast  不是…而是 / 并非…而是 / 而非 / 不…也不… / "not X but Y"
  dash               ——, —, or a spaced dash used as a pause (digit ranges are ignored)
  enumeration_comma  four or more 、 inside one comma-delimited segment
  fragment_run       three or more very short sentences in a row (likely subjectless fragments)
"""
import argparse, json, re, sys, zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
SENT_END = "。！？!?"
NEG = [
    re.compile(r"(不是|并非|并不是)[^。！？\n]{0,40}?(而是|而非)"),
    re.compile(r"而非"),
    re.compile(r"不[^。！？\n]{0,20}?也不"),
    re.compile(r"\bnot\b[^.\n]{0,40}?\bbut\b", re.I),
    re.compile(r"\brather than\b", re.I),
]
DASH = [re.compile(r"——|—"), re.compile(r"(?<=\S) [–-] (?=\S)")]
DIGIT_RANGE = re.compile(r"\d\s*[–—-]\s*\d")
MIN_FRAGMENTS, MAX_FRAGMENT_CHARS, MAX_ENUM = 3, 12, 3


def paragraphs_from_docx(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    return ["".join(t.text or "" for t in p.iter(W + "t")) for p in root.iter(W + "p")]


def check(paragraphs):
    hits = []
    for pi, text in enumerate(paragraphs, 1):
        if not text.strip():
            continue
        for pat in NEG:
            for m in pat.finditer(text):
                hits.append({"rule": "negation_contrast", "paragraph": pi, "offset": m.start()})
        for pat in DASH:
            for m in pat.finditer(text):
                around = text[max(0, m.start() - 2): m.end() + 2]
                if DIGIT_RANGE.search(around):
                    continue
                hits.append({"rule": "dash", "paragraph": pi, "offset": m.start()})
        for m in re.finditer(r"[^，,。！？!?；;\n]+", text):
            if m.group().count("、") > MAX_ENUM:
                hits.append({"rule": "enumeration_comma", "paragraph": pi, "offset": m.start()})
        # fragment runs: consecutive sentences that END with terminal punctuation and are very short
        run, run_start, pos = 0, None, 0
        for m in re.finditer(r"[^。！？!?\n]+[。！？!?]", text):
            core = re.sub(r"[\s，,；;：:、。！？!?（）()]", "", m.group())
            if 0 < len(core) <= MAX_FRAGMENT_CHARS:
                run += 1
                run_start = m.start() if run == 1 else run_start
                if run == MIN_FRAGMENTS:
                    hits.append({"rule": "fragment_run", "paragraph": pi, "offset": run_start})
            else:
                run = 0
    summary = {}
    for h in hits:
        summary[h["rule"]] = summary.get(h["rule"], 0) + 1
    return {"hits": hits, "summary": summary, "paragraphs_checked": len([p for p in paragraphs if p.strip()])}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--text", help="UTF-8 plain-text file; one paragraph per line")
    src.add_argument("--docx", help="Word file; paragraph text is read from word/document.xml")
    ap.add_argument("--output", help="write the JSON report here instead of stdout")
    ap.add_argument("--strict", action="store_true", help="exit with status 1 when there is any hit")
    a = ap.parse_args()
    paragraphs = paragraphs_from_docx(a.docx) if a.docx else open(a.text, encoding="utf-8").read().split("\n")
    report = check(paragraphs)
    out = json.dumps(report, ensure_ascii=False, indent=2)
    if a.output:
        open(a.output, "w", encoding="utf-8").write(out + "\n")
    else:
        print(out)
    sys.exit(1 if (a.strict and report["hits"]) else 0)


if __name__ == "__main__":
    main()
