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

## 2. Divergencia (100 ideas una por una)
- [ ] Definir metodos de ideacion a usar (binomio, what-if, mashup, SCAMPER, oblique).
- [ ] Elegir lente de genero y listas de palabras (si aplica).
- [ ] Generar ideas de forma individual, no en batch.
- [ ] Ejecutar `idea-randomizer` una vez por idea (ideal con `--emit-meta`) y registrar listas, picks y seed en `process/exploration_log.md`.
- [ ] Generar exactamente 100 ideas (ni mas ni menos) en `ideas/contest/` con un archivo Markdown por idea.
- [ ] Usar `ideas/idea_card_template.md` en cada archivo y completar todos los campos con bullets concisos, salvo el argumento.
- [ ] Agregar un parrafo explicando el posible argumento de la novela en `Argumento posible`.
- [ ] Asegurar que el argumento incluye protagonista, objetivo, obstaculo y apuestas.
- [ ] Copiar seed, listas y picks en `Paquete de aleatoriedad` de cada idea.
- [ ] Integrar los picks en logline, mundo y argumento (no decorativo).
- [ ] Nombrar archivos como `idea_001.md` ... `idea_100.md`.
- [ ] Para cada idea, usar la skill `idea-randomizer`.
- [ ] Si un paquete de aleatoriedad se repite, re-ejecutar el randomizer.
- [ ] Cambiar al menos 2 listas entre ideas consecutivas.
- [ ] Asegurar variedad en conflicto, mundo y protagonista.
- [ ] Evitar repeticion de tropos o estructuras.
- [ ] No iniciar el concurso hasta que las 100 ideas incluyan el parrafo de argumento.

## 3. Concurso de ideas (100 -> 20)
- [ ] Ejecutar el concurso con la skill `idea-contest`.
- [ ] Guardar cada ronda en `process/contest_round_XX.json`.
- [ ] Verificar que las 100 ideas tienen parrafo de argumento antes de la primera ronda.
- [ ] En cada ronda: seleccionar 5 ideas aleatorias, evaluar una por una y elegir 1 ganadora.
- [ ] Mover la ganadora a `ideas/approved/` y las otras 4 a `ideas/rejected/`.
- [ ] Repetir hasta vaciar `ideas/contest/`.
- [ ] Verificar el conteo final: 20 aprobadas y 80 rechazadas.
- [ ] No pedir confirmacion del usuario durante el concurso.

## 4. Scoring y ranking (20 -> 5)
- [ ] Completar `process/scoring_matrix.md` con las 20 aprobadas.
- [ ] Ordenar por score y seleccionar Top 5.
- [ ] Resolver empates priorizando originalidad y uso del paquete.
- [ ] Registrar Top 5 y razones en `process/decision_log.md`.

## 5. Expansion de finalistas
- [ ] Expandir worldbuilding sensorial de las 5 finalistas.
- [ ] Expandir protagonista, antagonista, tema y arco.
- [ ] Definir gancho y punto de entrada narrativo.
- [ ] Guardar la expansion dentro de cada archivo en `ideas/approved/`.

## 6. Handoff a book-template (5 salidas)
- [ ] Completar `handoff/finalists/seed_01.md` ... `seed_05.md`.
- [ ] Completar `handoff/finalists/seed_01.json` ... `seed_05.json`.
- [ ] Completar `meta.source_idea` y `meta.finalist_rank` en cada seed JSON.
- [ ] Si se elige una final, copiarla a `handoff/seed.md` y `handoff/seed.json`.
- [ ] Completar `handoff/style_guide.md` solo para la final elegida.
- [ ] Verificar consistencia entre `handoff/seed.json` y `handoff/seed.md` si existe final.

## 7. Validacion final
- [ ] Verificar logline (protagonista + objetivo + obstaculo + apuestas).
- [ ] Verificar conflicto sostenible para novela completa.
- [ ] Verificar originalidad y evitacion de cliches.
- [ ] Confirmar fit con el publico objetivo.
- [ ] Si hay final elegida, listo para crear libro con `scripts/new-book.py`.
