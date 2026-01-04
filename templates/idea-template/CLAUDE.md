# Sistema de ideacion de libros con Claude Code

## Proposito
Este template crea ideas solidas para libros y entrega una semilla lista para el book-template.

## Principios no negociables
- `ideas/selected.md` y `handoff/seed.json` son la SOT y deben coincidir.
- Separacion de fases: brief -> divergencia -> convergencia -> handoff.
- No escribir prosa de libro ni capitulos.
- Completar `PLAN.md` en orden y marcar tareas.
- Salidas en Markdown y ASCII.
- Plantilla agnostica de genero: el brief define el sesgo creativo.

## Flujo de trabajo recomendado (fractal)
1. Brief: completar `input/brief.md`, `input/audience.md`, `input/constraints.md`.
2. Divergencia: generar N ideas usando aleatoriedad del randomizer y tecnicas del toolkit.
3. Expansion: desarrollar top 3-5 con detalle.
4. Convergencia: evaluar, seleccionar y registrar la decision.
5. Handoff: completar `handoff/seed.md` y `handoff/seed.json`.

## Roles y responsabilidades
- Orchestrator: coordina el plan, valida formatos, no inventa contenidos.
- Brainstormer: genera ideas divergentes con riesgo creativo.
- Curator: filtra, refina, selecciona y evita cliches.
- Analyst: valida fit de mercado y audiencia.
- Archivist: mantiene la SOT y registra decisiones.

## Politica de SOT y actualizaciones
- Si cambia la idea elegida, actualizar `ideas/selected.md` y `handoff/seed.json`.
- La idea elegida define el brief final para el book-template.
- Registrar listas usadas y picks en `process/exploration_log.md`.

## Contexto JIT
- Cargar solo brief, shortlist y archivos de handoff.
- Evitar cargar todas las ideas a la vez; resumir si es necesario.

## Calidad y criterios
- Logline fuerte: protagonista + objetivo + obstaculo + apuestas.
- High concept: pitch tipo "X se encuentra con Y".
- Conflicto sostenible para una novela completa.
- Originalidad y evitacion de cliches de IA.
- Claridad de publico y tono.
- Gancho visual o conceptual inmediato.

## Convenciones de archivos
- Ideas crudas: `ideas/raw_ideas.md`.
- Shortlist: `ideas/shortlist.md`.
- Elegida: `ideas/selected.md`.
- Handoff JSON: `handoff/seed.json`.
- Handoff Markdown: `handoff/seed.md`.

## Comandos conceptuales
- `generate-ideas [n]`: fase divergente.
- `randomize [listas]`: obtener picks aleatorios para divergencia.
- `expand-idea [id]`: expansion de candidato.
- `score-ideas`: completar matriz de puntuacion.
- `select-idea`: decision y SOT.
- `build-handoff`: preparar archivos de handoff.

## Inicio rapido
- Completar `input/brief.md`.
- Generar 10 ideas en `ideas/raw_ideas.md`.
- Evaluar y seleccionar en `ideas/shortlist.md`.
- Finalizar `handoff/seed.md` y `handoff/seed.json`.
