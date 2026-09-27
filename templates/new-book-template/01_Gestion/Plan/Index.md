---
type: plan_hub
area: gestion
tags: [plan, hub]
---

# Plan maestro (Checklist)

Este índice es el “dashboard” operativo: se ejecuta en orden estricto, marcando cada tarea.

## Reglas de ejecución (obligatorio)
- Seguir el plan en orden estricto (00 → 07). No adelantar fases.
- No pasar a la siguiente tarea hasta completar la actual al 100%.
- Toda iteración crea una nueva versión (v2, v3...) y nunca sobrescribe una versión anterior.
- Regla SOT: la Biblia (`02_Biblia/`) es la fuente de la verdad. El manuscrito no la contradice.
- Si aparece un hecho nuevo (nombre propio, evento, regla), se registra en la Biblia con fuente (capítulo/beat).

## Artefactos (salidas principales)
- Semilla: `01_Gestion/Semilla.md`
- Estilo: `01_Gestion/Estilo.md`
- Cronología: `02_Biblia/Cronologia.md`
- Escaleta/Outline: `03_Produccion/Escaleta.md`
- Capítulos: `03_Produccion/CP_XX/`
- Manuscrito final: `04_Manuscrito/LIBRO_FINAL.md`

## Checklist por fases (en orden)

### 00. Preparación
- [ ] [[01_Gestion/Plan/00_Preparacion/T01_Auditoria_Estructura|T01 Auditoría de estructura]]
- [ ] [[01_Gestion/Plan/00_Preparacion/T02_Parametros_Libro|T02 Parámetros del libro]]

### 01. Semilla
- [ ] [[01_Gestion/Plan/01_Semilla/T01_Origen_y_Logline|T01 Origen y logline]]
- [ ] [[01_Gestion/Plan/01_Semilla/T02_Premisa_Extendida|T02 Premisa extendida]]
- [ ] [[01_Gestion/Plan/01_Semilla/T03_Tema_y_Pregunta_Moral|T03 Tema y pregunta moral]]

### 02. Estilo
- [ ] [[01_Gestion/Plan/02_Estilo/T01_Voz_y_Tono|T01 Voz y tono]]
- [ ] [[01_Gestion/Plan/02_Estilo/T02_POV_y_Tiempo_Verbal|T02 POV y tiempo verbal]]
- [ ] [[01_Gestion/Plan/02_Estilo/T03_Reglas_Escena_MRU|T03 Reglas de escena (MRU)]]
- [ ] [[01_Gestion/Plan/02_Estilo/T04_Protocolo_Deep_POV|T04 Protocolo Deep POV]]
- [ ] [[01_Gestion/Plan/02_Estilo/T05_Sistema_de_Dialogo|T05 Sistema de diálogo]]

### 03. Worldbuilding (Biblia)
- [ ] [[01_Gestion/Plan/03_Worldbuilding/T01_Glosario_Core|T01 Glosario core]]
- [ ] [[01_Gestion/Plan/03_Worldbuilding/T02_Reglas_del_Mundo|T02 Reglas del mundo]]
- [ ] [[01_Gestion/Plan/03_Worldbuilding/T03_Geografia_Lugares_Core|T03 Geografía y lugares core]]
- [ ] [[01_Gestion/Plan/03_Worldbuilding/T04_Culturas_y_Organizaciones|T04 Culturas y organizaciones]]

### 04. Personajes (Biblia)
- [ ] [[01_Gestion/Plan/04_Personajes/T01_Definicion_Personajes|T01 Definición de personajes]]
- [ ] (Repetible) Duplicar [[01_Gestion/Plan/04_Personajes/TXX_Personaje_X|TXX Personaje X]] por cada personaje relevante

### 05. Estructura global
- [ ] [[01_Gestion/Plan/05_Estructura_Global/T01_Eleccion_Modelo|T01 Elección de modelo]]
- [ ] [[01_Gestion/Plan/05_Estructura_Global/T02_Topologia_y_Partes|T02 Topología y partes]]
- [ ] [[01_Gestion/Plan/05_Estructura_Global/T03_Escaleta_Maestra|T03 Escaleta maestra]]

### 06. Producción (ciclo por capítulo)
- [ ] (Prologó si aplica) [[01_Gestion/Plan/06_Produccion/01_Beats/T01_Beats_Prologo|T01 Beats prólogo]]
- [ ] (Ejemplo) [[01_Gestion/Plan/06_Produccion/01_Beats/T02_Beats_Capitulo_1|T02 Beats capítulo 1]]
- [ ] (Repetible) Duplicar [[01_Gestion/Plan/06_Produccion/01_Beats/TXX_Beats_Capitulo_X|TXX Beats capítulo X]] por cada capítulo
- [ ] (Repetible) Duplicar [[01_Gestion/Plan/06_Produccion/02_Drafts/TXX_Draft_Capitulo_X|TXX Draft capítulo X]] por cada capítulo

### 07. Final
- [ ] [[01_Gestion/Plan/07_Final/T01_Compilacion_Manuscrito|T01 Compilación del manuscrito]]
- [ ] [[01_Gestion/Plan/07_Final/T02_Auditoria_Consistencia_SOT|T02 Auditoría consistencia SOT]]
- [ ] [[01_Gestion/Plan/07_Final/T03_Pase_Estilo_Editorial|T03 Pase de estilo editorial]]
- [ ] [[01_Gestion/Plan/07_Final/T04_Exportacion|T04 Exportación]]

## Tareas abiertas (solo Plan)
```tasks
path includes 01_Gestion/Plan
not done
```
