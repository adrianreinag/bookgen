---
type: plan_phase
phase: 11
tags: [plan]
---

# 11. Critica y revision (por capitulo)

## Objetivo
Corregir problemas focalizados por capitulo sin perder control de versiones.

## Como actuar (procedimiento)
1. Pide critica con inputs minimos (capitulo + estilo + SOT relevante).
2. Aplica cambios solo en una nueva version del capitulo.
3. Si un cambio afecta hechos, actualiza SOT en paralelo (o antes).

## Entradas
- Un `chapters/chapter_##/drafts/draft_vN.md`
- [[bible/style_guide]] y SOT relevante

## Salidas (Definition of Done)
- Nueva version `chapter_##_v(N+1).md` con cambios aplicados.
- Registro de hallazgos si fueron relevantes.

## Checklist paso a paso
- [ ] Seleccionar capitulo objetivo y version actual.
- [ ] Preparar inputs:
  - [ ] Draft del capitulo.
  - [ ] [[bible/style_guide]].
  - [ ] Personajes y lugares relevantes.
  - [ ] Glosario y timeline (rango relevante).
- [ ] Invocar al Critic para el capitulo.
- [ ] Aplicar cambios obligatorios creando nueva version.
- [ ] Aplicar recomendados si no rompen la promesa.
- [ ] Registrar en [[manuscript/feedback/critique_log]] si hubo decisiones importantes.
 - [ ] Si el capitulo cambia orden/funcion en el libro:
  - [ ] Actualizar [[structure/outline]].
  - [ ] Revisar beats de capitulos adyacentes (causalidad).

## Enlaces
- Agente: [[.claude/agents/critic]]
- Anterior: [[plan/13-critica-global-post-borradores]]
- Siguiente: [[plan/15-consistencia-y-sot]]
