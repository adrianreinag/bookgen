---
type: plan_phase
phase: 3
tags: [plan]
---

# 3. Worldbuilding (SOT)

## Objetivo
Crear una base minima del mundo (reglas, lugares, timeline, glosario) que soporte el outline y evite contradicciones.

## Como actuar (procedimiento)
1. Registra todo nombre/termino en glosario antes de usarlo en beats o drafts.
2. Crea solo lo minimo necesario para el acto 1 y la promesa del genero.
3. Si hay decisiones dudosas, conviertelas en preguntas y mandalas a investigacion.

## Entradas
- [[bible/seed]]
- [[bible/style_guide]]

## Salidas (Definition of Done)
- [[bible/glossary]] inicial usable.
- Al menos 1 lugar principal creado en `bible/locations/`.
- [[bible/timeline]] con prehistoria + eventos de acto 1 (macro).

## Checklist paso a paso
- [ ] Glosario:
  - [ ] Crear/actualizar [[bible/glossary]] como índice (los términos canónicos viven en `bible/terms/`).
  - [ ] Definir capitalizacion y ortografia de nombres propios.
  - [ ] Anotar sinonimos prohibidos (para evitar drift de nombres).
- [ ] Reglas del mundo (si aplica):
  - [ ] Definir sistema (magia/tecnologia/politica/reglas sociales).
  - [ ] Definir limitaciones y costos.
  - [ ] Definir reglas inmutables (lo que no se rompe).
  - [ ] Definir “zonas grises” (lo que se puede decidir mas tarde).
- [ ] Lugar principal:
  - [ ] Crear una entidad en `bible/locations/` como `LOC_<slug>.md` usando [[vault-templates/location]].
  - [ ] Definir cultura superficial (costumbres visibles).
  - [ ] Definir cultura profunda (valores, tabues).
  - [ ] Definir restricciones de acceso (quien entra y como).
  - [ ] Definir historia del lugar (2-5 eventos).
  - [ ] Definir conflictos potenciales (3-5).
  - [ ] Enlazar a personajes relevantes (cuando existan).
- [ ] Timeline:
  - [ ] Crear/actualizar [[bible/timeline]].
  - [ ] Registrar prehistoria relevante (solo lo que impacta la historia).
  - [ ] Registrar eventos que conducen al acto 1.
  - [ ] Marcar eventos inciertos como TODO (no inventar sin necesidad).
  - [ ] Para eventos relevantes, crear entidad `bible/events/EVT_<slug>.md` y enlazarla desde la tabla.
- [ ] Verificar coherencia:
  - [ ] No hay contradiccion con la seed (tema, tono, restricciones).
  - [ ] No se introduce worldbuilding que no se vaya a usar.

## Enlaces
- Plantilla: [[vault-templates/location]]
- Anterior: [[plan/05-guia-de-estilo]]
- Siguiente: [[plan/07-personajes-sot]]
