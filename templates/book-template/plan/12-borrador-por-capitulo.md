---
type: plan_phase
phase: 9
tags: [plan]
---

# 9. Fase de borrador (por capitulo)

## Objetivo
Escribir un borrador v1 completo desde beats, respetando voz, MRU y deep POV.

## Como actuar (procedimiento)
1. No edites mientras escribes: termina el capitulo.
2. Sigue MRU por escena y mantiene el POV estable.
3. Cualquier hecho nuevo se lista en `## NEW FACTS` para consolidarlo luego en SOT.

## Entradas
- Beats del capitulo: `chapters/chapter_##/beats.md`
- [[bible/style_guide]] y SOT relevante (JIT)

## Salidas (Definition of Done)
- `chapters/chapter_##/drafts/draft_v1.md` completo con `## DRAFT` y `## NEW FACTS`.
- Sin contradicciones evidentes con la SOT (si hay, no avanzar).

## Checklist paso a paso (por capitulo)
- [ ] Abrir beats del capitulo y [[bible/style_guide]].
- [ ] Preparar contexto JIT:
  - [ ] Personajes relevantes.
  - [ ] Lugares relevantes.
  - [ ] Timeline (solo rango relevante).
  - [ ] Glosario (terminos del capitulo).
- [ ] Crear `chapters/chapter_##/drafts/draft_v1.md` (siempre dentro de la carpeta del capítulo).
- [ ] Asegurar estructura del archivo:
  - [ ] Titulo `# Capitulo ##` (o equivalente).
  - [ ] Seccion `## DRAFT`.
  - [ ] Seccion `## NEW FACTS`.
- [ ] (Opcional) Listar escenas al inicio del draft como guia.
- [ ] Escribir escena por escena:
  - [ ] Motivacion externa clara.
  - [ ] Reaccion interna (sensaciones/pensamiento en deep POV).
  - [ ] Accion.
  - [ ] Dialogo (si aplica).
- [ ] Mantener consistencia:
  - [ ] Nombres segun [[bible/glossary]].
  - [ ] POV y tiempo verbal segun [[bible/style_guide]].
  - [ ] Regla de entidades: nombres propios -> enlaces a `bible/` (con alias si hace falta).
- [ ] Cerrar el capitulo con un gancho coherente con beats.
- [ ] Completar `## NEW FACTS`:
  - [ ] Hechos nuevos sobre personajes.
  - [ ] Hechos nuevos sobre lugares.
  - [ ] Terminos nuevos.
  - [ ] Eventos con impacto en timeline.
- [ ] Guardar version (no sobrescribir): si hay cambios grandes -> crear `draft_v2.md` (o `draft_vN.md`) en la carpeta del capítulo.

## Enlaces
- Hub: [[manuscript/index]]
- Anterior: [[plan/11-beats-por-capitulo]]
- Siguiente: [[plan/13-critica-global-post-borradores]]
