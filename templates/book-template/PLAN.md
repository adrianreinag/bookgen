# Plan Maestro para escribir un libro completo

Este plan es generico y atomico. Cada tarea puede marcarse al completarla.

## Reglas de ejecucion (obligatorio)
- Seguir el plan en orden estricto, paso a paso.
- No adelantar fases ni tareas. Si no se sigue el plan, el resultado es incorrecto.
- Marcar cada tarea al completarla.
- No pasar al siguiente punto hasta completar al 100% el punto actual.
- Si un punto es iterativo, repetir el ciclo hasta aprobarlo y documentar cada ronda.
- Toda revision crea una nueva version (v2, v3, v4...) y nunca sobrescribe una version anterior.
- Si hay replanificacion, actualizar `PLAN.md` de inmediato.

## 0. Preparacion del proyecto
- [ ] Confirmar objetivo del libro (ficcion o no ficcion).
- [ ] Definir audiencia objetivo.
- [ ] Definir longitud objetivo (palabras).
- [ ] Definir idioma y registro.
- [ ] Definir nivel de uso de IA (ideacion, estructura, borrador, edicion).
- [ ] Revisar y ajustar `CLAUDE.md` segun el proyecto.
- [ ] Revisar la estructura de carpetas.
- [ ] Crear carpeta de contexto: `manuscript/context/`.
- [ ] Crear archivo de resumen vivo: `manuscript/context/story_so_far.md`.
- [ ] Crear log de memoria: `manuscript/context/memory_log.json`.
- [ ] Crear carpeta de feedback: `manuscript/feedback/`.
- [ ] Crear log de critica: `manuscript/feedback/critique_log.md`.
- [ ] Definir formato de registro de fuentes (APA, MLA, notas).

## 1. Semilla (seed)
- [ ] Escribir logline en `bible/seed.md`.
- [ ] Redactar premisa extendida (4 parrafos).
- [ ] Definir tema central (mentira y verdad).
- [ ] Definir pregunta moral.
- [ ] Definir protagonista (want, need, herida).
- [ ] Definir antagonista o fuerza opuesta.
- [ ] Definir genero y subgenero.
- [ ] Definir tropos obligatorios.
- [ ] Definir tropos a evitar.
- [ ] Definir POV.
- [ ] Definir tiempo verbal.
- [ ] Definir distancia narrativa.
- [ ] Definir target word count.
- [ ] Definir estructura (three act / save the cat / kisho ten ketsu).
- [ ] Definir restricciones del mundo.
- [ ] Definir restricciones de tono.
- [ ] Definir necesidades de investigacion.
- [ ] Redactar preguntas de worldbuilding a resolver.

## 2. Guia de estilo
- [ ] Definir voz.
- [ ] Definir tono.
- [ ] Definir referencias literarias.
- [ ] Definir ejemplos positivos (modelos de voz).
- [ ] Definir ejemplos negativos (lo que no se debe hacer).
- [ ] Definir longitud promedio de frases.
- [ ] Definir longitud promedio de parrafos.
- [ ] Definir reglas de dialogo.
- [ ] Definir palabras prohibidas.
- [ ] Definir muletillas a evitar.
- [ ] Definir reglas de descripcion sensorial.
- [ ] Confirmar MRU y deep POV.
- [ ] Guardar en `bible/style_guide.md`.

## 3. Worldbuilding (SOT)
- [ ] Crear glosario base en `bible/glossary.md`.
- [ ] Definir reglas del mundo (magia/tecnologia) si aplica.
- [ ] Definir limitaciones y costos del sistema.
- [ ] Definir reglas inmutables (fisicas o magicas).
- [ ] Crear al menos 1 lugar principal en `bible/locations/`.
- [ ] Definir cultura superficial del lugar.
- [ ] Definir cultura profunda del lugar.
- [ ] Definir restricciones de acceso.
- [ ] Definir historia del lugar.
- [ ] Definir conflictos potenciales del lugar.
- [ ] Crear timeline inicial en `bible/timeline.md`.
- [ ] Registrar eventos prehistoria.
- [ ] Registrar eventos de acto 1.

## 4. Personajes (SOT)
- [ ] Crear ficha de protagonista.
- [ ] Definir herida o fantasma.
- [ ] Definir mentira y verdad.
- [ ] Definir deseo externo y necesidad interna.
- [ ] Definir arco en 3 pasos (inicio, medio, final).
- [ ] Definir voz (lexico, sintaxis, muletillas).
- [ ] Definir apariencia clave.
- [ ] Definir habilidades y debilidades.
- [ ] Definir inventario clave.
- [ ] Definir relaciones.
- [ ] Definir tipo de eneagrama.
- [ ] Crear ficha de antagonista.
- [ ] Repetir el mismo set de campos.
- [ ] Crear fichas de secundarios necesarios.

## 5. Investigacion y fuentes
- [ ] Crear archivo de fuentes: `bible/research.md`.
- [ ] Listar temas a investigar.
- [ ] Priorizar temas criticos para la historia.
- [ ] Buscar fuentes primarias o confiables.
- [ ] Registrar cada fuente con enlace y nota.
- [ ] Resumir hallazgos clave en bullets.
- [ ] Marcar datos que deben verificarse mas adelante.

## 6. Estructura global (Architect)
- [ ] Analizar `bible/seed.md` para determinar ritmo y longitud.
- [ ] Definir topologia del libro (prologo, capitulos, epilogo).
- [ ] Calcular numero estimado de capitulos.
- [ ] Redactar `structure/outline.md` completo con resumen por capitulo.
- [ ] TAREA CRITICA: actualizar este `PLAN.md` desplegando beats y drafts para el numero real de capitulos.
- [ ] Confirmar que este punto esta 100% completo antes de pasar al 7.

## 7. Critica y replanificacion global (iterativa)
- [ ] Confirmar que el punto 6 esta completo al 100%.
- [ ] Invocar al Critic para revisar seed, guia de estilo, SOT y estructura completa.
- [ ] Recibir reporte estructurado con severidad (obligatorio / recomendado / opcional) y veredicto.
- [ ] Aplicar cambios necesarios y actualizar `PLAN.md` si hay replanificacion.
- [ ] Reinvocar al Critic y repetir el ciclo hasta obtener veredicto "APTO PARA BEATS".
- [ ] Registrar cada ronda en `manuscript/feedback/critique_log.md`.

## 8. Fase de Beats (ciclo iterativo por capitulo)
- [ ] Crear `structure/beats/chapter_XX_beats.md` usando `vault-templates/beat.md`.
- [ ] Cargar SOT relevante (personajes, lugares, timeline, glosario).
- [ ] Definir meta del capitulo (POV, tiempo, objetivo).
- [ ] Definir escenas (3-6) con objetivo, conflicto y resultado.
- [ ] Definir cambio de valor por escena.
- [ ] Definir personajes por escena.
- [ ] Definir ubicacion por escena.
- [ ] Definir objetos o entidades clave por escena.
- [ ] Escribir 10-20 beats en orden causal.
- [ ] Cerrar con gancho.
- [ ] Registrar hechos nuevos para la biblia.

## 9. Fase de Borrador (ciclo iterativo por capitulo)
- [ ] Leer beats y guia de estilo.
- [ ] Preparar contexto JIT (solo archivos necesarios).
- [ ] Listar escenas al inicio del draft.
- [ ] Redactar escenas siguiendo MRU.
- [ ] Continuar hasta completar el capitulo.
- [ ] Etiquetar objetos o entidades clave (si se usa RAG por tags).
- [ ] Registrar hechos nuevos en seccion "NEW FACTS".
- [ ] Guardar en `manuscript/drafts/chapter_XX_v1.md`.

## 10. Critica global del libro (post-borradores, iterativa)
- [ ] Confirmar que todos los capitulos tienen borrador `chapter_XX_v1.md`.
- [ ] Invocar al Critic para revisar el libro completo (todos los borradores).
- [ ] Recibir reporte estructurado con severidad y veredicto.
- [ ] Aplicar cambios creando nuevas versiones por capitulo: `chapter_XX_v2.md`, `chapter_XX_v3.md`, etc (no sobrescribir).
- [ ] Reinvocar al Critic y repetir el ciclo hasta que solo queden mejoras opcionales.
- [ ] Registrar cada ronda en `manuscript/feedback/critique_log.md`.

## 11. Critica y revision del borrador (por capitulo, si se necesita)
- [ ] Invocar al Critic para revisar un capitulo especifico.
- [ ] Recibir reporte estructurado con severidad.
- [ ] Realizar ajustes necesarios.
- [ ] Guardar en la siguiente version incremental: `manuscript/drafts/chapter_XX_vN.md`.

## 12. Consistencia y SOT (por capitulo)
- [ ] Ejecutar scan-consistency del capitulo.
- [ ] Resolver contradicciones detectadas.
- [ ] Actualizar `bible/characters/` si hay hechos nuevos.
- [ ] Actualizar `bible/locations/` si hay hechos nuevos.
- [ ] Actualizar `bible/glossary.md` si hay terminos nuevos.
- [ ] Actualizar `bible/timeline.md` con eventos nuevos.

## 13. Lectura progresiva y memoria (por capitulo)
- [ ] Ejecutar lectura progresiva del capitulo.
- [ ] Registrar criticas en `manuscript/feedback/critique_log.md`.
- [ ] Actualizar `manuscript/context/story_so_far.md` con resumen denso (CoD).
- [ ] Actualizar `manuscript/context/memory_log.json` con eventos clave.

## 14. Revision editorial (por capitulo)
- [ ] Revision macro (trama, ritmo, arcos).
- [ ] Revision de escenas y secuelas.
- [ ] Revision de coherencia de voz.
- [ ] Revision de dialogo (subtexto, muletillas).
- [ ] Revision micro (verbos filtro, adverbios, pasiva).
- [ ] Guardar en `manuscript/final/chapter_XX_final.md`.
- [ ] Redactar notas de edicion y change log.

## 15. Compilacion y cierre (global)
- [ ] Actualizar indice en `manuscript/final/full_manuscript.md`.
- [ ] Concatenar capitulos finales.
- [ ] Definir titulo final del libro.
- [ ] Escribir el titulo en `manuscript/final/full_manuscript.md`.
- [ ] Renombrar la carpeta del libro en `books` usando minusculas y guiones.
- [ ] Verificar consistencia global.
- [ ] Verificar continuidad en timeline y glosario.
- [ ] Exportar o preparar para publicacion (si aplica).
