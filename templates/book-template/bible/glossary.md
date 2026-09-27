---
type: glossary
status: active
tags: [bible, glossary]
---

# Glosario (index)

Este archivo es un **índice**. Los términos canónicos viven como **entidades** en `bible/terms/`.

Regla: si un término tiene significado especial o reaparece, crea una entidad:
- Ejemplo: [[bible/terms/TERM_termino_clave]]

## Términos (entidades)
```dataview
TABLE id, name, status, first_seen
FROM "bible/terms"
WHERE type = "term"
SORT id ASC
```

## Convención
- Archivo: `bible/terms/TERM_<slug>.md`
- En texto: `[[TERM_<slug>|Forma narrativamente adecuada]]`

## Notas rápidas (opcionales)
- Si necesitas apuntar algo sin crear entidad todavía, déjalo aquí como TODO y conviértelo en entidad en la fase de mantenimiento.

## Enlaces
- [[bible/entities]]
- [[bible/seed]]
- [[bible/timeline]]
