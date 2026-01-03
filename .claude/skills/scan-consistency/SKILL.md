---
name: scan-consistency
description: Verify a draft against the bible for factual consistency.
inputs:
  - manuscript draft or final
  - bible files
outputs:
  - list of issues and suggested fixes
---

# scan-consistency

## When to use
- After a draft is generated or before final edits.

## Workflow
1. Read the draft and extract named entities (people, places, objects).
2. Check each entity against `bible/`.
3. Flag contradictions, missing entries, timeline drift, or style guide violations.
4. Suggest minimal fixes and bible updates.

## Output format
- Markdown table: Issue | Evidence | Fix | Bible update
