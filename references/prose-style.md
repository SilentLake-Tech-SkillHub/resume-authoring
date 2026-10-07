# Prose style: keep the wording from sounding machine-written

Read this before drafting, revising or compressing any resume wording, in Chinese or English. It applies to the resume text itself. It does not govern how you talk to the person in chat. The rules below sit on top of the existing ones in [writing and layout](writing-and-layout.md), [project review](../skills/resume-project-review/SKILL.md) and [compression](../skills/resume-compression/SKILL.md).

Each rule names the pattern, why it reads as machine-written, and what to do instead. Fix a pattern by restating the content more directly, never by deleting a fact.

## 1. Negation-contrast frames

Patterns: `不是……而是……`, `并非……而是……`, `而非……`, `不……也不……`, "not X but Y", "rather than X, Y".

Why: the frame spends half a sentence on something nobody claimed, and it appears again and again in generated text. In a resume it also reads as arguing with a doubt the reader never had.

Do: state the positive claim directly. "不是简单的问答，而是按事实与图表逐步展开的分析" becomes "按事实与图表逐步展开分析"。Keep a negation only when the person's own source states a real limitation that changes how the claim must be read (for example, a feature is planned and not launched). Even then, put it as a plain statement of status, not as a contrast frame.

## 2. Dashes

Patterns: `——`, `—`, ` - ` used as a pause, an aside or a dramatic turn inside a sentence.

Why: a dash is the easiest way to splice two thoughts together, so generated text overuses it.

Do: use a comma, a colon after a label the person approved, or split into two sentences. Keep dashes only where the accepted format requires them: date ranges such as `2021.06–2021.09`, and fixed headings or labels the person approved.

## 3. Enumeration commas (顿号)

Pattern: `、` chaining many items, joining whole clauses, or inserted between parts that are not parallel.

Why: a long run of `、` makes a list look complete without saying anything about how the items relate, and it hides which item the person actually owned.

Do:
- Use `、` only for short, parallel items of the same kind and level inside one sentence, and keep each run to about four items.
- Do not use `、` to connect full clauses or verb-object phrases. Use a comma, or two sentences, or one sentence with a clear sequence.
- When there are more than four items, group them ("接入 GPT、Claude 等主流模型") or keep the ones that carry evidence and drop the rest.
- Do not mix `、` and `，` at random inside one list.

## 4. Runs of subjectless fragments

Pattern: three or more very short sentences or clauses in a row, none with a stated actor, such as "独立建库。整合血缘。主导 Agent。比较框架。选用 SDK。"

Why: each fragment drops the actor and the link to the next one, so the reader cannot tell who decided what, or why. Generated text produces this rhythm when it tries to sound dense.

Do: write one complete sentence, or two, per bullet, with a clear action, its object and the connection between steps (purpose, sequence, cause). Omitting the subject inside a single complete sentence is normal in Chinese and fine when the actor is clear from the project heading. Chopping a bullet into a string of clipped fragments is not.

## 5. Patterns covered elsewhere

Keep applying these existing rules: no slogans or generic phrases such as "AI赋能" or "提升体验", no stack lists in place of an explanation, no defensive prose or hypothetical gaps, no repeated `Label:` prefixes, no chains of arrows or equations, and no overcorrecting into chatty first-person narration.

## 6. Check before you show a draft

Run the plain-text checker on the draft wording and fix what it reports:

```bash
python3 scripts/check_prose_style.py --text draft.txt        # from skills/resume-project-review/
```

It reports the rule and the position of each hit, never the text itself, so the report is safe to keep next to private drafts. A hit is a prompt to re-read that sentence, not an automatic error: a real date range or an approved label can trigger a match. After the checker is clean, read the whole project aloud once. A passing check does not replace that reading.

The checker covers the mechanical parts of rules 1 to 4: the frames, dash characters, long enumeration runs and runs of very short sentences. It cannot judge whether a sentence is concrete, evidenced or honest. Those remain the reviewer's job under the other references.
