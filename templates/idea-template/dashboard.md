---
type: dashboard
idea_id: "{{IDEA_ID}}"
tags: [dashboard]
---

# Dashboard

## Areas
- [[input/index]]
- [[pool/index]]
- [[process/index]]
- [[handoff/index]]

## Aprobadas
```dataview
LIST FROM "pool/approved"
WHERE type = "idea_card"
SORT file.name
```

## Contest (opcional)
```dataview
LIST FROM "pool/contest"
WHERE type = "idea_card"
SORT file.name
```

## Finalistas
```dataview
LIST FROM "handoff/finalists"
WHERE type = "seed"
SORT file.name
```

## Logs y decisiones
```dataview
LIST FROM "process"
WHERE type = "process"
SORT file.mtime DESC
```

## Tareas abiertas
```dataview
TASK FROM ""
WHERE !completed
```
