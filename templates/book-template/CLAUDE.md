# Sistema de libros (Obsidian + Claude Code)

## Proposito
Este template crea un libro con una boveda Obsidian por proyecto. La fuente de la verdad
vive en archivos Markdown y el grafo de enlaces mantiene la coherencia. La IA opera sobre
el sistema de archivos, no sobre una ventana de chat.

## Mapa de la boveda
- `index.md`: home note y atajos.
- `dashboard.md`: vistas operativas (Dataview opcional).
- `bible/index.md`: hub de SOT (personajes, lugares, timeline, glosario).
- `structure/index.md`: hub de estructura (outline y beats).
- `manuscript/index.md`: hub de manuscrito (drafts y final).

## Principios no negociables
- `bible/` es la SOT. Ningun draft puede contradecirla.
- Estructura antes que prosa: seed -> outline -> beats -> draft -> final.
- Cada nota debe enlazar a sus fuentes y a sus dependencias.
- Los cambios de hechos se registran en la biblia con su fuente.
- Las secciones `## DRAFT` y `## NEW FACTS` son obligatorias en drafts.
- Markdown y ASCII solamente.

## Metodologia integrada
1. Preparacion: abrir el vault y revisar `index.md`, `dashboard.md` y los hubs.
2. Seed + estilo: completar `bible/seed.md` y `bible/style_guide.md`.
3. Biblia: crear personajes y lugares con plantillas; actualizar `bible/timeline.md` y `bible/glossary.md`.
4. Outline: definir capitulos y enlaces a beats en `structure/outline.md`.
5. Beats: por capitulo en `structure/beats/`; enlazar personajes, lugares y draft.
6. Draft: escribir en `manuscript/drafts/` usando beats y guia de estilo.
7. Consistencia: mover hechos nuevos a la biblia, timeline y glosario.
8. Final: editar en `manuscript/final/` y compilar `full_manuscript.md`.

## PLAN.md (plan maestro)
- Completar `PLAN.md` de principio a fin, en orden.
- No saltar fases ni tareas.
- Marcar cada tarea al completarla.

## Enlaces minimos por nota
- Personajes: link a beats, drafts y lugares relevantes.
- Lugares: link a beats, drafts y personajes.
- Beats: link a outline, draft y biblia.
- Drafts: link a beats, outline, personajes, lugares y guia de estilo.
- Final: link al draft y beats de origen.

## Roles y responsabilidades
- Orchestrator: coordina el plan, valida formatos, no escribe prosa.
- Architect: estructura (outline y beats), ritmo y causalidad.
- Archivist: continuidad, glosario, timeline, SOT.
- Drafter: prosa desde beats, voz y sensorialidad.
- Critic: edicion y pulido sin cambiar hechos.

## Politica de SOT y actualizaciones
- Si aparece un hecho nuevo, registrarlo en `bible/` con fuente.
- Personajes: `bible/characters/`.
- Lugares: `bible/locations/`.
- Terminos: `bible/glossary.md`.
- Eventos: `bible/timeline.md`.
- Investigacion: `bible/research.md`.

## Contexto JIT (just in time)
- Cargar solo lo necesario: capitulo actual, personajes, lugares, guia de estilo.
- Evitar cargar el manuscrito completo.
- Resumir y guardar en la biblia si hace falta.

## Calidad y revision
- MRU: motivacion externa -> reaccion interna -> accion -> dialogo.
- Deep POV: evitar verbos filtro (ver, sentir, oir, pensar).
- Ritmo: alternar escena y secuela; parrafos cortos.
- Macro antes que micro: trama, ritmo, arcos, luego estilo.

## Convenciones de archivos
- Hubs: `bible/index.md`, `structure/index.md`, `manuscript/index.md`.
- Beats: `structure/beats/chapter_##_beats.md`.
- Drafts: `manuscript/drafts/chapter_##_v1.md`.
- Final: `manuscript/final/chapter_##_final.md`.
- Full: `manuscript/final/full_manuscript.md`.

## Comandos del proyecto (conceptuales)
- `develop-beats [n]`: generar beats del capitulo n.
- `draft-chapter [n]`: generar borrador desde beats.
- `scan-consistency [n]`: verificar borrador contra la biblia.
- `update-bible`: registrar hechos nuevos en SOT.
- `build-chapter [n]`: pipeline completo (beats -> draft -> scan -> update).

## Inicio rapido
- Abrir `index.md`.
- Completar `bible/seed.md` y `bible/style_guide.md`.
- Crear outline en `structure/outline.md`.
- Generar beats del capitulo 01 y pasar a draft.
