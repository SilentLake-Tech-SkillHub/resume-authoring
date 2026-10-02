# Chinese document quality

Use this for Chinese Word/PDF generation and when the user reports garbled text or a defective screenshot.

## Establish the actual defect

Locate the reported file, version, page and viewing surface. Inspect the source text, Word XML and rendered screenshot. A garbled early screenshot and a later fixed candidate are separate evidence. Check the current result; do not call the defect fixed solely because the DOCX text reads correctly.

Distinguish corrupted characters from missing glyphs, unsupported/substituted fonts, layout overlap and literal Markdown. Read text files as strict UTF-8; never repair damaged text by decoding with ignored/replacement errors. Inspect replacement characters, accidental control characters and suspicious private-use glyphs in context. Preserve legitimate symbols only with evidence that the requested font renders them.

## Preflight before presenting screenshots

1. Resolve the document runtime and renderer from the document Skill. Check which Chinese font is available to that renderer and the target viewer. Set Chinese run/style font explicitly or use a verified renderer mapping. Western font settings alone do not establish CJK coverage.
2. For macOS rendering of documents using SimSun, a verified Fontconfig alias to an installed Chinese font such as Songti SC can fix a renderer/font mismatch. Reuse a configured mapping if available; record it in the private run. Do not hard-code one person's absolute font configuration path in this Skill or assume the alias proves native Word/WPS compatibility.
3. Generate the versioned candidate with native bold and hyperlinks. Check that neither `**` nor `[label](url)` appears as document text. Display the intended domain, preserve the hyperlink target, and check paragraph separation.
4. Run `scripts/check_resume_text.py --docx <candidate>`. Supply `--approved-text <private plain-text snapshot>` for approval readback when that snapshot represents the exact intended document. Use an output path inside the private workspace.
5. Render the candidate to all page images using the document Skill. Inspect all pages for Chinese glyphs, screenshots with tofu/blank glyphs, line clipping, photo overlaps, title/date alignment, sparse final pages and unreadable density. Fix the underlying cause and rerender before showing a defective screenshot as a result. Diagnostic screenshots may be identified as such when needed to explain the real issue.
6. Extract rendered PDF text and rerun with `--rendered-text <extracted text>`. Every Word paragraph, including hyperlink display text, must survive extraction. Inspect reported misses rather than silently ignoring them. Page counters or line-break variants can require a documented comparison adjustment.
7. If the defect occurs in native Word/WPS or an in-app preview, verify the corrected exact file in that reported surface. Inspect screenshot evidence after opening it. If the report concerns an early renderer screenshot and the final render already resolves it, record that distinction and recheck the final render. Do not rewrite approved content to fix a font failure.

## Recovery and shipping

Keep earlier files as recovery baselines and create a new candidate for an actual document change. Compare approved claims and numeric values after any repair. Internal rendering PDFs/images stay QA evidence; only the requested deliverable is returned. Word approval precedes delivery PDF export, and PDF approval remains separate. User-reported defects reopen the affected file gate; a checker pass never substitutes for user acceptance.
