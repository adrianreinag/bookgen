# Plan Maestro para crear ideas de libros

Este plan es generico y atomico. Cada tarea puede marcarse al completarla.

## 0. Preparacion del proyecto
- [ ] Confirmar objetivo del proyecto (generar ideas viables).
- [ ] Definir genero y subgenero objetivo.
- [ ] Definir publico objetivo (edad, region, habitos).
- [ ] Definir idioma y registro.
- [ ] Definir nivel de riesgo creativo (bajo/medio/alto).
- [ ] Revisar y ajustar `CLAUDE.md` segun el proyecto.
- [ ] Revisar la estructura de carpetas.

## 1. Brief y restricciones (input)
- [ ] Completar `input/brief.md`.
- [ ] Completar `input/audience.md`.
- [ ] Completar `input/constraints.md`.
- [ ] Definir referencias y comparables.
- [ ] Definir limites de tono y contenido.
- [ ] Si todo lo anterior esta completo, continuar sin pedir confirmacion.

## 2. Divergencia (generacion de 100 ideas)
- [ ] Definir metodos de ideacion a usar (binomio, what-if, mashup, SCAMPER, oblique).
- [ ] Elegir lente de genero y listas de palabras (si aplica).
- [ ] Registrar listas usadas y resultado en `process/exploration_log.md`.
- [ ] Generar exactamente 100 ideas (ni mas ni menos) en `ideas/contest/` con un archivo Markdown por idea.
- [ ] Usar `ideas/idea_card_template.md` en cada archivo y completar todos los campos con bullets concisos.
- [ ] Nombrar archivos como `idea_001.md` ... `idea_100.md`.
- [ ] Para cada idea, usar la skill `idea-randomizer`.
- [ ] Asegurar variedad en conflicto, mundo y protagonista.
- [ ] Evitar repeticion de tropos o estructuras.

## 3. Concurso de ideas (100 -> 20)
- [ ] Ejecutar el concurso con la skill `idea-contest`.
- [ ] En cada ronda: seleccionar 5 ideas aleatorias, evaluar una por una y elegir 1 ganadora.
- [ ] Mover la ganadora a `ideas/approved/` y las otras 4 a `ideas/rejected/`.
- [ ] Repetir hasta vaciar `ideas/contest/`.
- [ ] Verificar el conteo final: 20 aprobadas y 80 rechazadas.
- [ ] No pedir confirmacion del usuario durante el concurso.

## 4. Expansion de candidatas aprobadas
- [ ] Seleccionar top 3-5 ideas desde `ideas/approved/`.
- [ ] Expandir worldbuilding sensorial.
- [ ] Expandir protagonista, antagonista, tema y arco.
- [ ] Definir gancho y punto de entrada narrativo.
- [ ] Guardar la expansion dentro de cada archivo en `ideas/approved/`.

## 5. Evaluacion y curaduria
- [ ] Completar `process/scoring_matrix.md`.
- [ ] Registrar observaciones en `process/decision_log.md`.
- [ ] Seleccionar idea ganadora desde `ideas/approved/`.
- [ ] Registrar la idea ganadora en `process/decision_log.md`.

## 6. Handoff a book-template
- [ ] Completar `handoff/seed.json`.
- [ ] Completar `handoff/seed.md`.
- [ ] Completar `handoff/style_guide.md` (voz y tono preliminar).
- [ ] Verificar consistencia entre `handoff/seed.json` y `handoff/seed.md`.

## 7. Validacion final
- [ ] Verificar logline (protagonista + objetivo + obstaculo + apuestas).
- [ ] Verificar conflicto sostenible para novela completa.
- [ ] Verificar originalidad y evitacion de cliches.
- [ ] Confirmar fit con el publico objetivo.
- [ ] Listo para crear libro con `scripts/new-book.py`.
