---
type: plan_phase
phase: 8
tags: [plan]
---

# 8. Fase de beats (por capitulo)

## Objetivo
Desglosar cada capitulo en escenas y beats causales antes de escribir prosa.

## Como actuar (procedimiento)
1. Trabaja capitulo por capitulo siguiendo el outline.
2. Carga solo SOT relevante (contexto JIT) para evitar ruido.
3. Si aparece un hecho nuevo, registralo en SOT con fuente.

## Entradas
- [[structure/outline]] (capitulo objetivo).
- SOT relevante: personajes, lugares, timeline, glosario.

## Salidas (Definition of Done)
- `chapters/chapter_##/beats.md` completo.
- Beats enlazados a outline + SOT.
- Gancho claro al final del capitulo.

## Checklist paso a paso (por capitulo)
- [ ] Crear carpeta del capítulo (si no existe):
  - [ ] `chapters/chapter_##/`
  - [ ] `chapters/chapter_##/drafts/`
  - [ ] `chapters/chapter_##/index.md` (hub del capítulo con links a beats/drafts/final)
- [ ] Crear `chapters/chapter_##/beats.md` usando [[vault-templates/beat]].
- [ ] Aplicar regla de entidades:
  - [ ] Si aparece un nombre propio nuevo, crear entidad en `bible/` (aunque sea `status: stub`).
  - [ ] Enlazar entidades desde beats (no texto suelto).
- [ ] Enlazar al inicio:
  - [ ] [[structure/outline]]
  - [ ] Personajes relevantes (links).
  - [ ] Lugares relevantes (links).
- [ ] Definir meta del capitulo:
  - [ ] POV.
  - [ ] Tiempo (cuando ocurre en timeline).
  - [ ] Objetivo del capitulo (para el protagonista).
  - [ ] Restriccion (que lo limita).
- [ ] Definir escenas (3-6):
  - [ ] Objetivo.
  - [ ] Conflicto.
  - [ ] Resultado / consecuencia.
  - [ ] Cambio de valor (antes/despues).
- [ ] Definir personajes por escena (solo los necesarios).
- [ ] Definir ubicacion por escena (una principal si es posible).
- [ ] Definir objetos/entidades clave por escena y:
  - [ ] Agregar al glosario si es nuevo.
  - [ ] Marcar consistencia de nombre (capitalizacion).
- [ ] Escribir 10-20 beats:
  - [ ] Orden causal.
  - [ ] Acciones observables (evitar abstracciones).
  - [ ] Micro-consecuencias (cada beat cambia algo).
- [ ] Cerrar con gancho:
  - [ ] Pregunta abierta, amenaza, revelacion o decision.
- [ ] Registrar hechos nuevos:
  - [ ] En glosario / timeline / fichas (con fuente “chapter_##_beats”).

## Enlaces
- Plantilla: [[vault-templates/beat]]
- Anterior: [[plan/10-critica-y-replanificacion-global]]
- Siguiente: [[plan/12-borrador-por-capitulo]]
