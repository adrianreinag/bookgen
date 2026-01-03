# Bookgen

Sistema local para crear, organizar y exportar libros a EPUB y PDF.

## Estructura del proyecto

- `template/`: base del libro (bible, estructura, manuscrito).
- `working-books/`: libros en proceso (cada libro es una carpeta).
- `output/`: libros exportados (EPUB y PDF).
- `scripts/`: utilidades para crear y exportar libros.
  - `scripts/assets/epub.css`: estilos para EPUB.

## Flujo recomendado

1. Crear un libro nuevo desde la plantilla.
2. Escribir y editar el manuscrito dentro de `working-books/<id>`.
3. Completar la revision final y compilar el manuscrito.
4. Definir el titulo final y renombrar la carpeta del libro (slug).
5. Exportar a EPUB y PDF en `output/<titulo>`.

## Paso a paso

### 1) Crear un libro nuevo

Ejecuta el script y toma el ID que devuelve.

```bash
./scripts/new-book.py
```

Salida esperada:

```
Libro creado en: /ruta/al/proyecto/working-books/<id>
```

### 2) Escribir el manuscrito

Trabaja dentro de `working-books/<id>/` usando los archivos del template:

- `manuscript/drafts/`: borradores.
- `manuscript/final/`: version final por capitulo.
- `manuscript/final/full_manuscript.md`: manuscrito completo.

El plan maestro esta en `template/PLAN.md`.

### 3) Cierre y titulo final

Cuando el libro ya este listo:

- Define el titulo final.
- Escribe el titulo en `manuscript/final/full_manuscript.md`.
- Renombra la carpeta del libro a un slug en minusculas y con guiones.
  - Ejemplo: `mi-novela`.

### 4) Exportar a EPUB y PDF

Requiere `pandoc` y un motor LaTeX (xelatex/lualatex/pdflatex).

```bash
./scripts/export-book.py <id|ruta> "Titulo del libro" --author "Nombre" --lang es
```

Esto genera:

- `output/Titulo del libro/Titulo del libro.epub`
- `output/Titulo del libro/Titulo del libro.pdf`

Para ajustar el estilo EPUB, edita `scripts/assets/epub.css`.

## Dependencias

- Python 3
- pandoc
- Un motor LaTeX para PDF: `xelatex`, `lualatex` o `pdflatex`

## Notas

- El script de exportacion evita sobreescribir archivos existentes.
- Puedes pasar una ruta completa al libro en lugar del ID.
