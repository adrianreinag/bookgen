# Sistema de ideacion (Obsidian + Claude Code)

## Proposito
Este template crea ideas solidas para libros y entrega 5 semillas finalistas listas para el
book-template. La boveda integra input, pool, proceso y handoff mediante enlaces.

## Mapa de la boveda
- `index.md`: home note y atajos.
- `dashboard.md`: vistas operativas (Dataview opcional).
- `input/index.md`: brief, publico y restricciones.
- `pool/index.md`: pool de ideas (approved/contest/rejected) y plantilla base.
- `process/index.md`: logs, scoring y decisiones.
- `handoff/index.md`: finalistas y seed final.

## Principios no negociables
- `handoff/finalists/` es la SOT de las 5 finalistas.
- Si hay ganadora final, sincronizar en `handoff/seed.md`.
- Separacion de fases: input -> divergencia -> scoring -> expansion -> handoff.
- No escribir prosa de libro ni capitulos.
- Completar `PLAN.md` en orden y marcar tareas.
- Markdown y ASCII solamente.
- No mantener JSON duplicado; `seed.md` es la unica fuente.

## Metodologia integrada
1. Input: completar `input/brief.md`, `input/audience.md`, `input/constraints.md`.
2. Divergencia: crear 20 ideas en `pool/approved/` usando `pool/idea_card_template.md`.
3. Registro: logear cada idea en `process/exploration_log.md`.
4. Scoring: puntuar en `process/scoring_matrix.md` y registrar Top 5 en `process/decision_log.md`.
5. Expansion: ampliar las 5 ganadoras y completar `handoff/finalists/seed_0X.md`.
6. Handoff: si hay final, completar `handoff/seed.md` y `handoff/style_guide.md`.

## PLAN.md (plan maestro)
- Completar `PLAN.md` de principio a fin, en orden.
- No saltar fases ni tareas.
- Marcar cada tarea al completarla.

## Enlaces minimos por nota
- Idea card: link a inputs y `process/exploration_log.md`.
- Seeds finalistas: link a `process/decision_log.md` y `handoff/index.md`.
- Seed final: link a `process/decision_log.md` y `pool/index.md`.

## Ejecucion autonoma (sin consultas)
- Si input esta completo, generar 20 ideas sin pedir confirmacion.
- Generar ideas una por una con su randomizer.
- Registrar cada idea en el exploration log.
- Puntuar y seleccionar Top 5 y completar handoff.

## Roles y responsabilidades
- Orchestrator: coordina el plan, valida formatos, no inventa contenidos.
- Brainstormer: genera ideas divergentes con riesgo creativo.
- Curator: filtra, refina, selecciona y evita cliches.
- Analyst: valida fit de mercado y audiencia.
- Archivist: mantiene la SOT y registra decisiones.

## Politica de SOT y actualizaciones
- Si cambia una finalista, actualizar `handoff/finalists/`.
- Si se elige una final para book-template, actualizar `handoff/seed.md`.
- Registrar listas usadas, picks y seed en `process/exploration_log.md`.

## Contexto JIT
- Cargar solo input y una idea a la vez durante divergencia.
- Cargar las 20 ideas solo al puntuar.
- Cargar las 5 finalistas durante handoff.

## Calidad y criterios
- Logline: protagonista + objetivo + obstaculo + apuestas.
- High concept: pitch tipo "X se encuentra con Y".
- Conflicto sostenible para una novela completa.
- Originalidad y evitacion de cliches de IA.
- Claridad de publico y tono.

## Convenciones de archivos
- Idea cards: `pool/idea_card_template.md` -> `pool/approved/idea_###.md`.
- Matriz de scoring: `process/scoring_matrix.md`.
- Decision log: `process/decision_log.md`.
- Handoff finalistas: `handoff/finalists/seed_01.md` ... `seed_05.md`.
- Handoff final (opcional): `handoff/seed.md`.

## Comandos conceptuales
- `generate-ideas [20]`: fase divergente.
- `randomize [listas]`: obtener picks aleatorios.
- `score-approved`: puntuar las 20 ideas.
- `select-top5`: ranking y seleccion.
- `build-finalists`: preparar seeds finalistas.
- `finalize-seed`: copiar ganadora final a `handoff/seed.*`.

## Inicio rapido
- Completar `input/brief.md`.
- Generar 20 ideas una por una con randomizer.
- Puntuar y elegir Top 5.
- Completar `handoff/finalists/`.
