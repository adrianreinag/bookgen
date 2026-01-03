---
name: develop-beats
description: Convert a chapter summary or outline item into a detailed beat sheet.
inputs:
  - chapter summary or outline entry
  - constraints from bible/style_guide.md
outputs:
  - markdown beat list with 10-20 beats
---

# develop-beats

## When to use
- You have a short chapter summary and need a step-by-step beat sheet.

## Workflow
1. Read the relevant section in `structure/outline.md`.
2. Check constraints in `bible/` (seed, timeline, glossary, characters).
3. Draft 10-20 beats with escalating stakes and clear scene transitions.
4. Validate each beat against the bible.
5. Save to `structure/beats/chapter_##_beats.md`.

## Output format
- Use a numbered list.
- Each beat is one sentence.
- End with a clear chapter hook.
