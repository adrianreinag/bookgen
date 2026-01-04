# Plan Maestro para crear ideas de libros

Este plan es generico y atomico. Cada tarea puede marcarse al completarla.

## 0. Preparacion del proyecto
- [ ] Confirmar objetivo del proyecto (generar ideas viables).
- [ ] Definir genero y subgenero objetivo.
- [ ] Definir publico objetivo (edad, region, habitos).
- [ ] Definir idioma y registro.
- [ ] Definir numero de ideas (por defecto 10).
- [ ] Definir nivel de riesgo creativo (bajo/medio/alto).
- [ ] Revisar y ajustar `CLAUDE.md` segun el proyecto.
- [ ] Revisar la estructura de carpetas.

## 1. Brief y restricciones (input)
- [ ] Completar `input/brief.md`.
- [ ] Completar `input/audience.md`.
- [ ] Completar `input/constraints.md`.
- [ ] Definir referencias y comparables.
- [ ] Definir limites de tono y contenido.

## 2. Divergencia (generacion de ideas)
- [ ] Definir metodos de ideacion a usar (binomio, what-if, mashup, SCAMPER, oblique).
- [ ] Elegir lente de genero y banco de semillas (si aplica).
- [ ] Registrar una seed de aleatoriedad si aplica en `process/exploration_log.md`.
- [ ] Generar N ideas en `ideas/raw_ideas.md` usando `ideas/idea_card_template.md`.
- [ ] Asegurar variedad en conflicto, mundo y protagonista.
- [ ] Evitar repeticion de tropos o estructuras.

## 3. Expansion de candidatos
- [ ] Seleccionar top 3-5 ideas.
- [ ] Expandir worldbuilding sensorial.
- [ ] Expandir protagonista, antagonista, tema y arco.
- [ ] Definir gancho y punto de entrada narrativo.
- [ ] Guardar expansion en `ideas/shortlist.md`.

## 4. Evaluacion y curaduria
- [ ] Completar `process/scoring_matrix.md`.
- [ ] Registrar observaciones en `process/decision_log.md`.
- [ ] Seleccionar idea ganadora (o top N si aplica).
- [ ] Consolidar la elegida en `ideas/selected.md`.

## 5. Handoff a book-template
- [ ] Completar `handoff/seed.json`.
- [ ] Completar `handoff/seed.md`.
- [ ] Completar `handoff/style_guide.md` (voz y tono preliminar).
- [ ] Verificar consistencia entre `ideas/selected.md` y `handoff/`.

## 6. Validacion final
- [ ] Verificar logline (protagonista + objetivo + obstaculo + apuestas).
- [ ] Verificar conflicto sostenible para novela completa.
- [ ] Verificar originalidad y evitacion de cliches.
- [ ] Confirmar fit con el publico objetivo.
- [ ] Listo para crear libro con `scripts/new-book.py`.
