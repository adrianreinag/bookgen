---
type: dashboard
book_id: "{{BOOK_ID}}"
tags: [dashboard]
---

# Dashboard

## Areas
- [[bible/index]]
- [[structure/index]]
- [[manuscript/index]]

## Personajes
```dataview
TABLE file.link AS Personaje
FROM "bible/characters"
WHERE type = "character" AND file.name != "_template"
SORT file.name
```

## Lugares
```dataview
TABLE file.link AS Lugar
FROM "bible/locations"
WHERE type = "location" AND file.name != "_template"
SORT file.name
```

## Investigacion
```dataview
LIST FROM "bible"
WHERE type = "research"
SORT file.name
```

## Beats
```dataview
LIST FROM "structure/beats"
WHERE type = "beats"
SORT file.name
```

## Drafts
```dataview
LIST FROM "manuscript/drafts"
WHERE type = "draft"
SORT file.name
```

## Ultimos cambios
```dataview
LIST FROM ""
SORT file.mtime DESC
LIMIT 10
```

## Tareas abiertas
```dataview
TASK FROM ""
WHERE !completed
```
