---
type: hub
area: pool
tags: [pool, hub]
---

# Pool de ideas

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

## Rechazadas
```dataview
LIST FROM "pool/rejected"
WHERE type = "idea_card"
SORT file.name
```

## Plantilla
- [[pool/idea_card_template]]

## Enlaces
- [[input/index]]
- [[process/index]]
