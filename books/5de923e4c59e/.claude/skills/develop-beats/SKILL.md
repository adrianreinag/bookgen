---
name: develop-beats
description: Convert a chapter summary into a detailed beat sheet with scene goals.
inputs:
  - structure/outline.md (chapter entry)
  - bible/seed.md, bible/timeline.md
  - relevant bible/characters and bible/locations
outputs:
  - structure/beats/chapter_##_beats.md
---

# develop-beats

## When to use
- You have a chapter summary and need a step by step plan.

## Workflow
1. Read the chapter entry in `structure/outline.md`.
2. Load relevant bible entries (characters, locations, timeline).
3. Choose structure model for the chapter (default: save_the_cat pacing).
4. Break the chapter into 3-6 scenes.
5. For each scene define: goal, conflict, outcome or disaster, value shift, location, time, characters.
6. Expand into 10-20 beats that follow MRU-friendly causality.
7. Add a final hook.
8. Note any new facts for the archivist.

## Output format
- Section: Meta (chapter, POV, time, location, objective).
- Section: Scenes (numbered, each with fields).
- Section: Beats (numbered list).
- Section: New facts (bullet list or "none").
