# Sistema de libros (Obsidian + Claude Code)

## Propósito
Este template crea un libro con una bóveda Obsidian por proyecto. La fuente de la verdad
vive en archivos Markdown y el grafo de enlaces mantiene la coherencia. La IA opera sobre
el sistema de archivos, no sobre una ventana de chat.

## Mapa de la bóveda
- `index.md`: home note y atajos.
- `dashboard.md`: vistas operativas (Dataview opcional).
- `bible/index.md`: hub de SOT (personajes, lugares, timeline, glosario).
- `structure/index.md`: hub de estructura (outline).
- `chapters/index.md`: hub de capítulos (unidad de edición por capítulo).
- `manuscript/index.md`: hub de manuscrito (contexto + compilación).

## Principios no negociables
- `bible/` es la SOT. Ningún draft puede contradecirla.
- Estructura antes que prosa: seed -> outline -> beats -> draft -> final.
- Cada nota debe enlazar a sus fuentes y a sus dependencias.
- Los cambios de hechos se registran en la biblia con su fuente.
- Regla de entidades: si algo tiene nombre propio y puede reaparecer, se crea/usa entidad en `bible/` y el manuscrito solo la referencia por enlace.
- Las secciones `## DRAFT` y `## NEW FACTS` son obligatorias en drafts.
- Markdown y ASCII solamente.

## Metodología integrada
1. Preparación: abrir el vault y revisar `index.md`, `dashboard.md` y los hubs.
2. Seed + estilo: completar `bible/seed.md` y `bible/style_guide.md`.
3. Biblia: crear personajes y lugares con plantillas; actualizar `bible/timeline.md` y `bible/glossary.md`.
4. Outline: reescribir el template y definir capítulos reales en `structure/outline.md`.
5. Crítica y replanificación global (iterativa) antes de beats.
6. Beats: por capítulo en `chapters/chapter_##/beats.md`; enlazar personajes, lugares y draft.
7. Draft: escribir en `chapters/chapter_##/drafts/draft_vN.md` usando beats y guía de estilo (v1).
8. Crítica global post-borradores (iterativa) y nuevas versiones (v2, v3...).
9. Consistencia: mover hechos nuevos a la biblia, timeline y glosario.
10. Final: editar en `chapters/chapter_##/final.md` y compilar `manuscript/final/full_manuscript.md`.

## PLAN (plan maestro)
- Plan detallado (Obsidian): `plan/index.md`.
- `PLAN.md` funciona como entrada rápida; la lista viva está en `plan/index.md`.
- Seguir el plan de principio a fin, en orden estricto y sin adelantar tareas.
- No pasar de punto hasta completar al 100% el punto actual.
- Marcar cada tarea al completarla. Si no se sigue el plan, el resultado es incorrecto.
- Los puntos iterativos se repiten hasta aprobarse y se registran en `manuscript/feedback/critique_log.md`.
- Toda revisión crea una nueva versión (v2, v3, v4...) y nunca sobrescribe.

## Enlaces mínimos por nota
- Entidades (CHAR/LOC/ORG/EVT/OBJ/CON/TERM): link a capítulos donde aparecen (via backlinks) y a entidades relacionadas.
- Beats: link a outline, capítulo y biblia.
- Drafts: link a beats, capítulo, outline, personajes, lugares y guía de estilo.
- Final: link al capítulo, draft y beats de origen.

## Roles y responsabilidades
- Orchestrator: coordina el plan, valida formatos, no escribe prosa.
- Architect: estructura (outline y beats), ritmo y causalidad.
- Archivist: continuidad, glosario, timeline, SOT.
- Drafter: prosa desde beats, voz y sensorialidad.
- Critic: crítica estructurada con severidad (obligatorio/recomendado/opcional) y veredicto, sin cambiar hechos.

## Política de SOT y actualizaciones
- Si aparece un hecho nuevo, registrarlo en `bible/` con fuente.
- Personajes: `bible/characters/`.
- Lugares: `bible/locations/`.
- Organizaciones: `bible/organizations/`.
- Eventos (entidades): `bible/events/` (y enlazarlos desde `bible/timeline.md`).
- Objetos: `bible/objects/`.
- Conceptos/reglas: `bible/concepts/`.
- Términos (entidades): `bible/terms/` (el índice es `bible/glossary.md`).
- Investigación: `bible/research.md`.
- Si el libro viene de una idea, registrar el origen en `bible/seed.md`.

## Referencia: entidades
- Guía de uso y convención: `bible/entities.md`.

## Contexto JIT (just in time)
- Cargar solo lo necesario: capítulo actual, personajes, lugares, guía de estilo.
- Evitar cargar el manuscrito completo.
- Resumir y guardar en la biblia si hace falta.

## Calidad y revisión
- MRU: motivación externa -> reacción interna -> acción -> diálogo.
- Deep POV: evitar verbos filtro (ver, sentir, oír, pensar).
- Ritmo: alternar escena y secuela; párrafos cortos.
- Macro antes que micro: trama, ritmo, arcos, luego estilo.

## Convenciones de archivos
- Hubs: `bible/index.md`, `structure/index.md`, `chapters/index.md`, `manuscript/index.md`.
- Capítulo: `chapters/chapter_##/index.md`.
- Beats: `chapters/chapter_##/beats.md`.
- Drafts: `chapters/chapter_##/drafts/draft_vN.md` (v1, v2, v3...).
- Final: `chapters/chapter_##/final.md`.
- Full: `manuscript/final/full_manuscript.md`.

## Comandos del proyecto (conceptuales)
- `develop-beats [n]`: generar beats del capítulo n.
- `draft-chapter [n]`: generar borrador desde beats.
- `scan-consistency [n]`: verificar borrador contra la biblia.
- `update-bible`: registrar hechos nuevos en SOT.
- `build-chapter [n]`: pipeline completo (beats -> draft -> scan -> update).

## Inicio rápido
- Abrir `index.md`.
- Completar `bible/seed.md` y `bible/style_guide.md`.
- Crear outline en `structure/outline.md`.
- Generar beats del capítulo 01 y pasar a draft.
