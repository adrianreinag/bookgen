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

## 2. Divergencia (20 ideas una por una)
- [ ] Definir metodos de ideacion a usar (binomio, what-if, mashup, SCAMPER, oblique).
- [ ] Elegir lente de genero y listas de palabras (si aplica).
- [ ] Generar ideas de forma individual, no en batch.
- [ ] Ejecutar `idea-randomizer` una vez por idea (ideal con `--emit-meta`) y registrar listas, picks y seed en `process/exploration_log.md`.
- [ ] Generar exactamente 20 ideas (ni mas ni menos) en `pool/approved/` con un archivo Markdown por idea.
- [ ] Usar `pool/idea_card_template.md` en cada archivo y completar todos los campos con bullets concisos, salvo el argumento.
- [ ] Agregar un parrafo explicando el posible argumento de la novela en `Argumento posible`.
- [ ] Asegurar que el argumento incluye protagonista, objetivo, obstaculo y apuestas.
- [ ] Copiar seed, listas y picks en `Paquete de aleatoriedad` de cada idea.
- [ ] Intentar integrar la mayoria de los picks en logline, mundo y argumento (no decorativo).
- [ ] Si algun pick no encaja, se puede descartar, pero registrar cual y por que (mantener trazabilidad).
- [ ] Nombrar archivos como `idea_001.md` ... `idea_020.md` dentro de `pool/approved/`.
- [ ] Para cada idea, usar la skill `idea-randomizer`.
- [ ] Si un paquete de aleatoriedad se repite, re-ejecutar el randomizer.
- [ ] Cambiar al menos 2 listas entre ideas consecutivas.
- [ ] Asegurar variedad en conflicto, mundo y protagonista.
- [ ] Evitar repeticion de tropos o estructuras.
- [ ] Verificar que las 20 ideas incluyen el parrafo de argumento antes de puntuar.

## 3. Scoring y ranking (20 -> 5)
- [ ] Completar `process/scoring_matrix.md` con las 20 ideas.
- [ ] Ordenar por score y seleccionar Top 5.
- [ ] Resolver empates priorizando originalidad y uso del paquete.
- [ ] Registrar Top 5 y razones en `process/decision_log.md`.

## 4. Expansion de finalistas
- [ ] Expandir worldbuilding sensorial de las 5 finalistas.
- [ ] Expandir protagonista, antagonista, tema y arco.
- [ ] Definir gancho y punto de entrada narrativo.
- [ ] Guardar la expansion dentro de cada archivo en `pool/approved/`.

## 5. Handoff a book-template (5 salidas)
- [ ] Completar `handoff/finalists/seed_01.md` ... `seed_05.md`.
- [ ] Si se elige una final, copiarla a `handoff/seed.md`.
- [ ] Completar `handoff/style_guide.md` solo para la final elegida.

## 6. Validacion final
- [ ] Verificar logline (protagonista + objetivo + obstaculo + apuestas).
- [ ] Verificar conflicto sostenible para novela completa.
- [ ] Verificar originalidad y evitacion de cliches.
- [ ] Confirmar fit con el publico objetivo.
- [ ] Si hay final elegida, listo para crear libro con `scripts/new-book.py`.
