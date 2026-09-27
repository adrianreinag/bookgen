---
type: plan_task_template
phase: 06_Produccion
area: draft
id: TXX
tags: [plan, task, template]
---
# TXX Draft capítulo X (plantilla)

Duplica esta tarea por capítulo (ej: `T04_Draft_CP_03.md`) y escribe el draft en `03_Produccion/CP_XX/Drafts/Draft_v1.md`.

## Objetivo
Escribir el borrador completo del capítulo a partir de beats + estilo, registrando hechos nuevos para migrarlos a la Biblia.

## Entradas
- `03_Produccion/CP_XX/Beats.md`
- `01_Gestion/Estilo.md`
- Biblia (`02_Biblia/Entidades/` + `02_Biblia/Cronologia.md`)

## Checklist
- [ ] Crear `03_Produccion/CP_XX/Drafts/Draft_v1.md` (si no existe).
- [ ] Escribir el capítulo completo siguiendo los beats (sin “saltar” escenas).
- [ ] Mantener consistencia con SOT:
  - [ ] Nombres propios canónicos (o alias autorizado)
  - [ ] Reglas del mundo respetadas
  - [ ] Lugares coherentes (tiempos/distancias)
- [ ] Añadir al final del draft una sección `## NEW FACTS`:
  - [ ] Enumerar hechos nuevos descubiertos al escribir (1 bullet por hecho)
  - [ ] Marcar qué entidad afecta (`CHAR_/LOC_/ORG_/EVT_/...`)
  - [ ] Indicar fuente: `CP_XX Draft_v1`
- [ ] Si hay revisión posterior:
  - [ ] Crear `Draft_v2.md`, `Draft_v3.md`... (no sobrescribir)

## Salidas (Definition of Done)
- `Draft_v1.md` completo + `## NEW FACTS` rellenado.
