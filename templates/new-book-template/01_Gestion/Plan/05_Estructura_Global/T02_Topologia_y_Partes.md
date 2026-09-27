---
type: plan_task
phase: 05_Estructura_Global
id: T02
tags: [plan, task]
---
# T02 Topología y partes

## Objetivo
Definir la forma del libro (prólogo/epílogo, partes, número de capítulos) y dejar preparado el scaffolding de producción.

## Entradas
- [[01_Gestion/Plan/05_Estructura_Global/T01_Eleccion_Modelo|T01 Elección de modelo]]

## Checklist
- [ ] Definir topología:
  - [ ] ¿Hay prólogo? ¿Hay epílogo?
  - [ ] ¿Hay partes? (Parte I, II, III...)
  - [ ] Número realista de capítulos (no “aproximado”)
- [ ] Definir convención de capítulos:
  - [ ] `CP_01`, `CP_02`, ... (carpetas en `03_Produccion/`)
  - [ ] Archivo de beats: `03_Produccion/CP_XX/Beats.md`
  - [ ] Drafts versionados: `03_Produccion/CP_XX/Drafts/Draft_vN.md`
  - [ ] Final del capítulo: `03_Produccion/CP_XX/Final.md`
- [ ] Crear scaffolding:
  - [ ] Opción A (manual): crear carpetas `03_Produccion/CP_XX/` para todos los capítulos + subcarpeta `Drafts/`
  - [ ] Opción B (script): ejecutar generador (estructura → carpetas/archivos)
    - [ ] `python3 "00_Documentacion y utiles/Scripts/generar_capitulos.py" --vault-root . --count N`
- [ ] Duplicar tareas repetibles del plan:
  - [ ] Duplicar [[01_Gestion/Plan/06_Produccion/01_Beats/TXX_Beats_Capitulo_X|TXX Beats capítulo X]] por cada capítulo
  - [ ] Duplicar [[01_Gestion/Plan/06_Produccion/02_Drafts/TXX_Draft_Capitulo_X|TXX Draft capítulo X]] por cada capítulo

## Salidas (Definition of Done)
- Scaffolding de capítulos creado en `03_Produccion/` (al menos `CP_01` listo).
- Tareas repetibles duplicadas/renombradas para los capítulos reales (si vas a gestionarlas desde el Plan).

## Enlaces
- Producción: `03_Produccion/`
- Siguiente: [[01_Gestion/Plan/05_Estructura_Global/T03_Escaleta_Maestra]]
