# Sistema de generacion de libros con Claude Code

## Proposito
Este repositorio es un template para crear libros con una arquitectura multi-agente.
La memoria viva del proyecto no es la ventana de contexto, sino el sistema de archivos.
La Fuente de la Verdad (SOT) vive en `bible/` y gobierna toda la estructura y la prosa.

## Principios no negociables
- `bible/` es SOT. No contradigas hechos sin pasar por el archivist.
- Separacion de fases: seed -> outline -> beats -> draft -> final.
- No escribir prosa sin beats aprobados en `structure/beats/`.
- La forma de completar el libro es completar `PLAN.md` paso a paso.
- Hechos nuevos deben registrarse en la biblia (personajes, lugares, reglas, timeline).
- Salidas en Markdown y ASCII.

## Flujo de trabajo recomendado (fractal)
1. Seed: completar `bible/seed.md` y `bible/style_guide.md`.
2. Outline: crear o ajustar `structure/outline.md`.
3. Beats: detallar capitulo en `structure/beats/chapter_##_beats.md`.
4. Draft: escribir borrador en `manuscript/drafts/` desde beats.
5. Consistencia: ejecutar `scan-consistency` y registrar hechos en SOT.
6. Revision: editar en `manuscript/final/` (macro antes que micro).
7. Compilacion: actualizar `manuscript/final/full_manuscript.md`.

## PLAN.md (plan maestro)
- Completar `PLAN.md` de principio a fin, en orden.
- No saltar fases ni tareas.
- Marcar cada tarea al completarla.

## Roles y responsabilidades
- Orchestrator: coordina, valida formatos, no escribe prosa.
- architect: estructura (outline y beats), ritmo y causalidad.
- archivist: continuidad, glosario, timeline, SOT.
- drafter: prosa desde beats, voz y sensorialidad.
- critic: edicion y pulido sin cambiar hechos.

## Politica de SOT y actualizaciones
- Si aparece un hecho nuevo, registrarlo en `bible/` con fuente.
- Personajes: `bible/characters/`.
- Lugares: `bible/locations/`.
- Terminos: `bible/glossary.md`.
- Eventos: `bible/timeline.md`.
- Si hay conflicto, la SOT manda.

## Contexto JIT (just in time)
- Cargar solo lo necesario: capitulo actual, personajes relevantes, lugares, guia de estilo.
- Evitar cargar manuscrito completo.
- Resumir si es necesario y guardar el resumen en SOT o notas.

## Calidad y revision
- MRU: motivacion externa -> reaccion interna -> accion -> dialogo.
- Deep POV: evitar verbos filtro (ver, sentir, oir, pensar).
- Ritmo: alternar escena y secuela; parrafos cortos.
- Macro antes que micro: trama, ritmo, arcos, luego estilo.
- El critic no cambia hechos; reporta inconsistencias al archivist.

## Convenciones de archivos
- Beats: `structure/beats/chapter_##_beats.md`
- Drafts: `manuscript/drafts/chapter_##_v1.md`
- Final: `manuscript/final/chapter_##_final.md`
- Full: `manuscript/final/full_manuscript.md`

## Comandos del proyecto (conceptuales)
- `develop-beats [n]`: generar beats del capitulo n.
- `draft-chapter [n]`: generar borrador desde beats.
- `scan-consistency [n]`: verificar borrador contra la biblia.
- `update-bible`: registrar hechos nuevos en SOT.
- `build-chapter [n]`: pipeline completo (beats -> draft -> scan -> update).

## Inicio rapido
- Completar `bible/seed.md`.
- Definir voz en `bible/style_guide.md`.
- Crear outline en `structure/outline.md`.
- Ejecutar beats del capitulo 1 y pasar a draft.
