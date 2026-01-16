# Obsidian + bookgen

## Objetivo

bookgen ya trabaja con Markdown y carpetas. Eso encaja con Obsidian de forma natural.
La idea es tratar cada libro o idea como un vault independiente, con un home note,
un dashboard y plantillas para crear notas rapido.

## Que se agrega en los templates

- `index.md`: home note con enlaces clave.
- `dashboard.md`: vistas Dataview (opcionales).
- `vault-templates/`: plantillas listas para Obsidian.
- Hubs internos: `bible/index.md`, `structure/index.md`, `manuscript/index.md` (libros) y `input/index.md`, `ideas/index.md`, `process/index.md`, `handoff/index.md` (ideas).

## Setup rapido (por vault)

1. Crea el libro o idea con `scripts/new-book.py` o `scripts/new-idea.py`.
2. Abre la carpeta creada (dentro de `books/` o `ideas/`) como vault en Obsidian.
3. Abre `index.md` y usa los enlaces base.
4. Si usas Templates, apunta la carpeta a `vault-templates/`.
5. El vault incluye `.mcp.json` para Claude Code (MCP-Obsidian).
6. Cada vault se inicializa como repo Git al crearse.

## Plugins recomendados (opcionales)

- Core: Templates, Backlinks, Graph, Outline.
- Community: Dataview (dashboards), Templater (automatizar notas), Longform (manuscrito), QuickAdd (atajos).

## MCP (Claude Code)

Cada vault incluye un `.mcp.json` con **MCP-Obsidian** para que Claude Code pueda leer y escribir
dentro del vault. Requiere `npx` (Node). El path es `.` para que el server use la carpeta actual.

## Convenciones sugeridas

- Notas nuevas de personajes y lugares salen de `vault-templates/`.
- Para escenas, usa `vault-templates/scene.md` y guarda en `manuscript/drafts/`.
- Usa tags o frontmatter si quieres filtrar con Dataview.

## Frontmatter

Las plantillas incluyen `type`, `status` y `tags` para consultas y filtros. Ajustalos segun tu flujo.

## Notas sobre Dataview

Los bloques `dataview` en `dashboard.md` son opcionales. Si el plugin no esta instalado,
Obsidian los muestra como codigo normal. No rompen el vault.

## Motivacion tecnica

- Mantiene el enfoque local-first.
- No obliga a un solo UI: puedes usar Obsidian, CLI o ambos.
- Cada libro queda aislado con su propio grafo.
