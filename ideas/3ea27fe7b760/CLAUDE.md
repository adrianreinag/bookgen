# Sistema de ideacion de libros con Claude Code

## Proposito
Este template crea ideas solidas para libros y entrega una semilla lista para el book-template.

## Principios no negociables
- `handoff/seed.json` y `handoff/seed.md` son la SOT y deben coincidir.
- Separacion de fases: brief -> divergencia -> concurso -> expansion -> convergencia -> handoff.
- No escribir prosa de libro ni capitulos.
- Completar `PLAN.md` en orden y marcar tareas.
- Salidas en Markdown y ASCII.
- Plantilla agnostica de genero: el brief define el sesgo creativo.
- Tras completar el brief, generar las 100 ideas y ejecutar el concurso sin consultar al usuario.
- Para generar cada idea usar la skill `idea-randomizer`.
- Para el concurso usar la skill `idea-contest`.
- Antes del concurso, cada una de las 100 ideas debe incluir un parrafo con el posible argumento de la novela.

## Flujo de trabajo recomendado (fractal)
1. Brief: completar `input/brief.md`, `input/audience.md`, `input/constraints.md`.
2. Divergencia: generar 100 ideas con un parrafo de argumento usando la skill `idea-randomizer` y tecnicas del toolkit.
3. Concurso: evaluar ideas de 5 en 5 usando la skill `idea-contest` hasta obtener 20 aprobadas.
4. Expansion: desarrollar top 3-5 aprobadas con detalle.
5. Convergencia: evaluar, seleccionar y registrar la decision.
6. Handoff: completar `handoff/seed.md` y `handoff/seed.json`.

## Ejecucion autonoma (sin consultas)
- Si el brief, publico y restricciones estan completos, no pedir confirmacion.
- Generar 100 ideas en archivos individuales con un parrafo de argumento y correr el concurso completo.
- Decidir ganadoras por criterios internos y continuar hasta vaciar `ideas/contest/`.

## Roles y responsabilidades
- Orchestrator: coordina el plan, valida formatos, no inventa contenidos.
- Brainstormer: genera ideas divergentes con riesgo creativo.
- Curator: filtra, refina, selecciona y evita cliches.
- Analyst: valida fit de mercado y audiencia.
- Archivist: mantiene la SOT y registra decisiones.

## Politica de SOT y actualizaciones
- Si cambia la idea elegida, actualizar `handoff/seed.json` y `handoff/seed.md`.
- La idea elegida define el brief final para el book-template.
- Registrar listas usadas y picks en `process/exploration_log.md`.

## Contexto JIT
- Cargar solo brief, 5 ideas en concurso por ronda, ideas aprobadas en evaluacion y archivos de handoff.
- Evitar cargar todas las ideas a la vez; resumir si es necesario.

## Calidad y criterios
- Logline fuerte: protagonista + objetivo + obstaculo + apuestas.
- High concept: pitch tipo "X se encuentra con Y".
- Conflicto sostenible para una novela completa.
- Originalidad y evitacion de cliches de IA.
- Claridad de publico y tono.
- Gancho visual o conceptual inmediato.

## Convenciones de archivos
- Ideas en concurso: `ideas/contest/` (100 archivos Markdown).
- Nombre sugerido: `idea_001.md` ... `idea_100.md`.
- Cada idea usa `ideas/idea_card_template.md` y completa todos los campos con bullets concisos, salvo el argumento.
- Cada idea incluye un parrafo en `Argumento posible` explicando la premisa de la novela.
- Ideas aprobadas: `ideas/approved/`.
- Ideas rechazadas: `ideas/rejected/`.
- Handoff JSON: `handoff/seed.json`.
- Handoff Markdown: `handoff/seed.md`.

## Comandos conceptuales
- `generate-ideas [100]`: fase divergente.
- `randomize [listas]`: obtener picks aleatorios para divergencia.
- `expand-idea [id]`: expansion de candidato.
- `score-ideas`: completar matriz de puntuacion.
- `select-idea`: decision y SOT.
- `build-handoff`: preparar archivos de handoff.
- `contest-draw`: tomar 5 ideas aleatorias de `ideas/contest/`.
- `contest-resolve`: mover ganadora a `ideas/approved/` y descartadas a `ideas/rejected/`.

## Concurso operativo (detalle)
- Ejecutar el concurso solo cuando las 100 ideas incluyan el parrafo de argumento.
- Ejecutar rondas de 5 ideas hasta vaciar `ideas/contest/`.
- Evaluar cada idea de la ronda con los criterios de `toolkit/evaluation.md`.
- Elegir una ganadora por ronda y moverla a `ideas/approved/`.
- Mover las otras cuatro a `ideas/rejected/`.
- Resultado esperado: 20 aprobadas y 80 rechazadas, sin consultas al usuario.

## Inicio rapido
- Completar `input/brief.md`.
- Generar 100 ideas con un parrafo de argumento en `ideas/contest/`.
- Ejecutar el concurso hasta tener 20 aprobadas.
- Expandir 3-5 aprobadas dentro de sus archivos en `ideas/approved/`.
- Elegir ganadora y completar `handoff/seed.md`, `handoff/seed.json` y `handoff/style_guide.md`.
