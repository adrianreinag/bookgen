---
type: plan_phase
phase: 15
tags: [plan]
---

# 15. Compilacion y cierre (global)

## Objetivo
Dejar un manuscrito final compilado y listo para exportacion/publicacion.

## Como actuar (procedimiento)
1. Confirma que todos los capitulos finales existen.
2. Compila `full_manuscript.md` y revisa orden e indice.
3. Haz un pase de consistencia global (glosario + timeline).

## Entradas
- Capitulos finales: `chapters/chapter_##/final.md`
- SOT y logs al dia

## Salidas (Definition of Done)
- `manuscript/final/full_manuscript.md` actualizado (indice + contenido).
- Titulo final definido.
- Export listo (si aplica).

## Checklist paso a paso
- [ ] Confirmar que existen todos los `chapters/chapter_##/final.md`.
- [ ] Confirmar que cada capitulo final enlaza a:
  - [ ] Su draft de origen.
  - [ ] Sus beats (si aplica).
- [ ] Actualizar indice en [[manuscript/final/full_manuscript]].
- [ ] Concatenar capitulos finales en `full_manuscript.md` (orden del outline).
- [ ] Definir titulo final y escribirlo en `full_manuscript.md`.
- [ ] Verificacion global:
  - [ ] Nombres consistentes (glosario).
  - [ ] Timeline consistente (orden y causalidad).
  - [ ] Personajes consistentes (rasgos y relaciones).
- [ ] Renombrar carpeta del libro en `books/` usando minusculas y guiones (si aplica).
- [ ] Export (opcional):
  - [ ] Usar `templates/book-template/scripts/export-book.py` (si el proyecto lo usa).

## Enlaces
- Inicio: [[plan/index]]
- Anterior: [[plan/17-revision-editorial]]
