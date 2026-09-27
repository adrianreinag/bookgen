---
type: plan_task
phase: 07_Final
id: T02
tags: [plan, task]
---
# T02 Auditoría de consistencia SOT

## Objetivo
Auditar que el manuscrito final no contradice la Biblia (SOT) y que todos los hechos nuevos han sido migrados.

## Entradas
- `04_Manuscrito/LIBRO_FINAL.md`
- Biblia: `02_Biblia/` (especialmente `Entidades/` y `Cronologia.md`)

## Checklist
- [ ] Recorrer `## NEW FACTS` de cada `Draft_vN.md` (si existen) y migrar a SOT:
  - [ ] Actualizar entidades afectadas
  - [ ] Actualizar `02_Biblia/Cronologia.md` si hay eventos/fechas relevantes
- [ ] Auditoría de nombres propios:
  - [ ] Todo nombre propio relevante tiene entidad (`CHAR_/LOC_/ORG_/EVT_/OBJ_/CON_/TERM_/CUL_`)
  - [ ] No hay variantes no autorizadas (alias) en el manuscrito
- [ ] Auditoría de reglas:
  - [ ] Ninguna escena viola una regla `CON_*.md`
- [ ] Auditoría temporal:
  - [ ] Orden coherente en `02_Biblia/Cronologia.md`

## Salidas (Definition of Done)
- SOT actualizado y consistente con `04_Manuscrito/LIBRO_FINAL.md`.

## Enlaces
- Cronología: `02_Biblia/Cronologia.md`
- Siguiente: [[01_Gestion/Plan/07_Final/T03_Pase_Estilo_Editorial]]
