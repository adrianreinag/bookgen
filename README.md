# Bookgen

Sistema local para crear, organizar y exportar libros a EPUB y PDF. Incluye plantillas para ideas y manuscritos, y scripts para arrancar proyectos y generar salidas finales.

## Estructura del proyecto

- `books/`: libros en curso (cada libro vive en su propia carpeta por ID).
- `ideas/`: ideas en exploracion (cada idea es una carpeta por ID).
- `templates/`: plantillas base.
  - `templates/book-template/`: base de libro (bible, estructura, manuscrito).
  - `templates/idea-template/`: base de idea (input, proceso, ideas, handoff, toolkit).
- `scripts/`: utilidades para crear ideas/libros y exportar.
  - `scripts/assets/epub.css`: estilo por defecto para EPUB.

## Flujo recomendado

1. (Opcional) Crear una idea nueva desde plantilla.
2. Crear un libro nuevo desde plantilla.
3. Trabajar bible, estructura y manuscrito.
4. Consolidar el manuscrito final en `manuscript/final/full_manuscript.md`.
5. Exportar a EPUB y PDF.
6. (Opcional) Abrir cada libro o idea como vault independiente en Obsidian.

## Crear una idea

```bash
python3 scripts/new-idea.py
```

Con titulo amigable y carpeta legible:

```bash
python3 scripts/new-idea.py --title "Thriller maritimo"
```

Forzar nombre de carpeta (slug):

```bash
python3 scripts/new-idea.py --slug thriller-maritimo
```

Salida esperada:

```
Idea creada en: /ruta/al/proyecto/ideas/<id>
```

## Crear un libro

```bash
python3 scripts/new-book.py
```

Con titulo amigable y carpeta legible:

```bash
python3 scripts/new-book.py --title "La ciudad del eco"
```

Forzar nombre de carpeta (slug):

```bash
python3 scripts/new-book.py --slug la-ciudad-del-eco
```

Salida esperada:

```
Libro creado en: /ruta/al/proyecto/books/<id>
```

## Estructura de un libro

Dentro de `books/<id>/`:

- `bible/`: personajes, locations, timeline y guias.
- `structure/`: outline y beats por capitulo.
- `manuscript/`:
  - `drafts/`: borradores.
  - `final/`: version final por capitulo y `full_manuscript.md`.
- `assets/`: recursos del libro (por ejemplo `portada.png`).
- `output/`: salidas generadas (EPUB/PDF).

## Obsidian (vaults por libro/idea)

Cada carpeta creada en `books/` o `ideas/` funciona como vault independiente.
Incluye notas `index.md`, `dashboard.md` y plantillas en `vault-templates/`.
Incluye `.mcp.json` para Claude Code (MCP-Obsidian).
Incluye hubs internos para navegar bible/structure/manuscript (libros) e input/ideas/process/handoff (ideas).
Cada vault se inicializa como repo Git al crearse (si `git` esta disponible).

Guia: `docs/obsidian.md`.

## Exportar a EPUB y PDF

Requiere `pandoc` y un motor LaTeX (xelatex, lualatex o pdflatex).

```bash
python3 scripts/export-book.py <id|ruta> "Titulo del libro" --author "Nombre" --lang es
```

Salida:

- `books/<id>/output/Titulo del libro.epub`
- `books/<id>/output/Titulo del libro.pdf`

Notas:

- El manuscrito de entrada es `books/<id>/manuscript/final/full_manuscript.md`.
- Si existe `books/<id>/assets/portada.png`, se usa como portada para EPUB y como primera pagina en PDF.
- Para cambiar el estilo EPUB, usa `--css` o edita `scripts/assets/epub.css`.
- El script no sobreescribe archivos existentes en `output/`.

## Dependencias

- Python 3
- pandoc
- Motor LaTeX para PDF: `xelatex`, `lualatex` o `pdflatex`

## Ejemplos

Exportar usando una ruta directa:

```bash
python3 scripts/export-book.py books/5de923e4c59e "Mi novela" --author "Autor"
```

Usar un CSS alternativo para EPUB:

```bash
python3 scripts/export-book.py 5de923e4c59e "Mi novela" --css /ruta/mi-estilo.css
```
