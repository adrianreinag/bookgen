# Sistema de ideacion de libros con Claude Code

## Proposito
Este template crea ideas solidas para libros y entrega 5 semillas finalistas listas para el book-template.

## Principios no negociables
- `handoff/finalists/` contiene las 5 salidas (seed .md y .json) y es la SOT.
- Si se elige una final para book-template, sincronizarla en `handoff/seed.md` y `handoff/seed.json`.
- Separacion de fases: brief -> divergencia -> scoring -> expansion -> handoff (concurso opcional).
- No escribir prosa de libro ni capitulos.
- Completar `PLAN.md` en orden y marcar tareas.
- Salidas en Markdown y ASCII.
- Plantilla agnostica de genero: el brief define el sesgo creativo.
- Tras completar el brief, generar 20 ideas (pool inicial) y pasar a scoring sin consultar al usuario.
- Para generar cada idea usar la skill `idea-randomizer`.
- La skill `idea-contest` es opcional (solo si generas un pool grande y quieres reducirlo rapido).
- Generar ideas una por una y ejecutar el randomizer una vez por idea.
- Los paquetes de aleatoriedad no se repiten; si se repiten, re-ejecutar.
- Cambiar al menos 2 listas entre ideas consecutivas.
- El paquete de aleatoriedad debe impactar la idea, no ser decorativo (se permite descartar picks que no encajen, con motivo).
- Trazabilidad obligatoria: `process/exploration_log.md`, `process/scoring_matrix.md`, `process/decision_log.md`.
- (Opcional si hay concurso) Guardar rondas en `process/contest_round_XX.json`.
- Cada idea debe incluir un parrafo con el posible argumento de la novela.

## Flujo de trabajo recomendado (fractal)
1. Brief: completar `input/brief.md`, `input/audience.md`, `input/constraints.md`.
2. Divergencia: generar 20 ideas una por una con un parrafo de argumento usando la skill `idea-randomizer`.
3. Scoring: puntuar las 20 ideas, ordenar y seleccionar Top 5.
4. Expansion: desarrollar Top 5 con detalle.
5. Handoff: completar 5 seeds en `handoff/finalists/`.

## Ejecucion autonoma (sin consultas)
- Si el brief, publico y restricciones estan completos, no pedir confirmacion.
- Generar 20 ideas en archivos individuales, una por una, con su randomizer y parrafo de argumento.
- Registrar cada idea en `process/exploration_log.md`.
- Puntuar las 20 ideas y seleccionar Top 5.
- Decidir ganadoras por criterios internos y continuar hasta completar `handoff/finalists/`.

## Roles y responsabilidades
- Orchestrator: coordina el plan, valida formatos, no inventa contenidos.
- Brainstormer: genera ideas divergentes con riesgo creativo.
- Curator: filtra, refina, selecciona y evita cliches.
- Analyst: valida fit de mercado y audiencia.
- Archivist: mantiene la SOT y registra decisiones.

## Politica de SOT y actualizaciones
- Si cambia una finalista, actualizar su seed en `handoff/finalists/`.
- Si se elige una final para book-template, actualizar `handoff/seed.json` y `handoff/seed.md`.
- Registrar listas usadas, picks y seed en `process/exploration_log.md`.

## Contexto JIT
- Cargar solo brief, una idea a la vez durante divergencia, las 20 ideas al puntuar y 5 finalistas en handoff.
- Evitar cargar todas las ideas a la vez; resumir si es necesario.

## Calidad y criterios
- Logline fuerte: protagonista + objetivo + obstaculo + apuestas.
- High concept: pitch tipo "X se encuentra con Y".
- Conflicto sostenible para una novela completa.
- Originalidad y evitacion de cliches de IA.
- Priorizar riesgo creativo y combinaciones no obvias.
- Variedad estructural: evitar loglines o argumentos con el mismo esqueleto.
- El argumento posible debe incluir protagonista, objetivo, obstaculo y apuestas.
- Claridad de publico y tono.
- Gancho visual o conceptual inmediato.

## Convenciones de archivos
- Ideas base: `ideas/approved/` (20 archivos Markdown).
- Nombre sugerido: `idea_001.md` ... `idea_020.md`.
- Cada idea usa `ideas/idea_card_template.md` y completa todos los campos con bullets concisos, salvo el argumento.
- Cada idea incluye un parrafo en `Argumento posible` explicando la premisa de la novela.
- Cada idea registra su `Paquete de aleatoriedad` con seed, listas y picks.
- (Opcional) Pool para concurso: `ideas/contest/` y descartes: `ideas/rejected/`.
- (Opcional) Rondas de concurso: `process/contest_round_XX.json`.
- Matriz de scoring: `process/scoring_matrix.md`.
- Decision log: `process/decision_log.md`.
- Handoff finalistas: `handoff/finalists/seed_01.md` ... `seed_05.md` y sus `.json`.
- Handoff final (opcional): `handoff/seed.md` y `handoff/seed.json`.

## Comandos conceptuales
- `generate-ideas [20]`: fase divergente.
- `randomize [listas]`: obtener picks aleatorios para divergencia.
- `expand-idea [id]`: expansion de candidato.
- `score-approved`: puntuar las 20 ideas.
- `select-top5`: ranking y seleccion de finalistas.
- `build-finalists`: preparar seeds para las 5 finalistas.
- `finalize-seed`: copiar la ganadora final a `handoff/seed.*`.
- (Opcional) `contest-draw`: tomar 5 ideas aleatorias de `ideas/contest/`.
- (Opcional) `contest-resolve`: mover ganadora a `ideas/approved/` y descartadas a `ideas/rejected/`.

## Concurso operativo (opcional)
- Usar solo si decides generar un pool grande en `ideas/contest/` y reducirlo rapidamente.
- Ejecutar rondas de 5 ideas hasta vaciar `ideas/contest/`.
- Evaluar cada idea de la ronda con los criterios de `toolkit/evaluation.md`.
- Elegir una ganadora por ronda y moverla a `ideas/approved/`.
- Mover las otras cuatro a `ideas/rejected/`.
- Ejemplo: con 100 ideas en `ideas/contest/`, el resultado esperado es 20 aprobadas y 80 rechazadas.

## Inicio rapido
- Completar `input/brief.md`.
- Generar 20 ideas una por una con su randomizer y parrafo de argumento en `ideas/approved/`.
- Puntuar las 20 ideas y elegir Top 5.
- Expandir Top 5 dentro de sus archivos en `ideas/approved/`.
- Completar `handoff/finalists/` para las 5 finalistas.
- Si hay ganadora final, completar `handoff/seed.md`, `handoff/seed.json` y `handoff/style_guide.md`.
