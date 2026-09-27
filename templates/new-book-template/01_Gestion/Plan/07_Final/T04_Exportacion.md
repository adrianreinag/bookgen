---
type: plan_task
phase: 07_Final
id: T04
tags: [plan, task]
---
# T04 Exportación (Word / EPUB / PDF)

## Objetivo
Generar artefactos de entrega a partir del manuscrito final.

## Entradas
- `04_Manuscrito/LIBRO_FINAL.md`

## Checklist
- [ ] Definir formatos de salida necesarios:
  - [ ] DOCX (edición compartida)
  - [ ] EPUB (lectura)
  - [ ] PDF (maquetación simple o revisión)
- [ ] Elegir herramienta:
  - [ ] Pandoc (recomendado) u otra
- [ ] Exportar (ejemplos conceptuales con pandoc):
  - [ ] `pandoc 04_Manuscrito/LIBRO_FINAL.md -o out/LIBRO_FINAL.docx`
  - [ ] `pandoc 04_Manuscrito/LIBRO_FINAL.md -o out/LIBRO_FINAL.epub`
  - [ ] `pandoc 04_Manuscrito/LIBRO_FINAL.md -o out/LIBRO_FINAL.pdf`
- [ ] Verificar resultado:
  - [ ] Saltos de capítulo razonables
  - [ ] Títulos y formato básico correctos

## Salidas (Definition of Done)
- Archivos exportados en `out/` (o carpeta elegida) y listos para entregar.
