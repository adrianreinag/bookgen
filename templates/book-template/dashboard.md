---
type: dashboard
book_id: "{{BOOK_ID}}"
tags: [dashboard]
---

# Dashboard

## Áreas
- [[plan/index]]
- [[bible/index]]
- [[structure/index]]
- [[chapters/index]]
- [[manuscript/index]]

## Personajes
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/characters"
WHERE type = "character"
SORT id ASC
```

## Lugares
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/locations"
WHERE type = "location"
SORT id ASC
```

## Organizaciones
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/organizations"
WHERE type = "organization"
SORT id ASC
```

## Eventos
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/events"
WHERE type = "event"
SORT id ASC
```

## Objetos
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/objects"
WHERE type = "object"
SORT id ASC
```

## Conceptos
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/concepts"
WHERE type = "concept"
SORT id ASC
```

## Términos
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/terms"
WHERE type = "term"
SORT id ASC
```

## Culturas
```dataview
TABLE id AS ID, name AS Nombre, status AS Estado, file.link AS Nota
FROM "bible/cultures"
WHERE type = "culture"
SORT id ASC
```

## Investigación
```dataview
LIST FROM "bible"
WHERE type = "research"
SORT file.name
```

## Beats
```dataview
LIST FROM "chapters"
WHERE type = "beats"
SORT file.name
```

## Drafts
```dataview
LIST FROM "chapters"
WHERE type = "draft"
SORT file.name
```

## Final
```dataview
LIST FROM "chapters"
WHERE type = "final"
SORT file.name
```

## Últimos cambios
```dataview
LIST FROM ""
SORT file.mtime DESC
LIMIT 10
```

## Tareas abiertas
```tasks
not done
```
