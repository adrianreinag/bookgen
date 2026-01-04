#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def pick_pdf_engine() -> str | None:
    for engine in ("xelatex", "lualatex", "pdflatex"):
        if shutil.which(engine):
            return engine
    return None


def run_pandoc(args: list[str]) -> None:
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as exc:
        print("Error ejecutando pandoc.", file=sys.stderr)
        raise SystemExit(exc.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Exporta un libro final a EPUB y PDF con formato mejorado."
    )
    parser.add_argument(
        "book_ref",
        help="ID en books o ruta al libro final.",
    )
    parser.add_argument(
        "book_name",
        help="Nombre del libro (titulo y nombre de archivos de salida).",
    )
    parser.add_argument(
        "--author",
        default="",
        help="Autor para metadatos (opcional).",
    )
    parser.add_argument(
        "--lang",
        default="es",
        help="Idioma para metadatos (default: es).",
    )
    parser.add_argument(
        "--css",
        default="",
        help="Ruta opcional a un CSS para EPUB.",
    )

    args = parser.parse_args()
    book_name = args.book_name.strip()

    if not book_name:
        print("El nombre del libro no puede estar vacio.", file=sys.stderr)
        return 1

    if "/" in book_name or "\\" in book_name:
        print("El nombre del libro no puede contener '/' o '\\'.", file=sys.stderr)
        return 1

    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    books_dir = root_dir / "books"

    book_ref_path = Path(args.book_ref)
    if book_ref_path.is_dir():
        book_dir = book_ref_path.resolve()
    else:
        book_dir = (books_dir / args.book_ref).resolve()

    if not book_dir.is_dir():
        print(f"No existe el libro: {book_dir}", file=sys.stderr)
        return 1

    input_file = book_dir / "manuscript" / "final" / "full_manuscript.md"
    if not input_file.is_file():
        print(f"No se encontro el manuscrito final: {input_file}", file=sys.stderr)
        return 1

    if not shutil.which("pandoc"):
        print("pandoc no esta instalado o no esta en el PATH.", file=sys.stderr)
        return 1

    output_dir = book_dir / "output"

    epub_file = output_dir / f"{book_name}.epub"
    pdf_file = output_dir / f"{book_name}.pdf"

    if epub_file.exists() or pdf_file.exists():
        print(f"Ya existen archivos de salida en: {output_dir}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    common_args = [
        "--standalone",
        "--toc",
        "--toc-depth=2",
        "--metadata",
        f"title={book_name}",
        "--metadata",
        f"lang={args.lang}",
    ]
    if args.author:
        common_args.extend(["--metadata", f"author={args.author}"])

    cover_image = book_dir / "assets" / "portada.png"
    css_path = (
        Path(args.css)
        if args.css
        else script_dir / "assets" / "epub.css"
    )

    epub_args = [
        "pandoc",
        str(input_file),
        *common_args,
        "-o",
        str(epub_file),
    ]
    if css_path.is_file():
        epub_args.extend(["--css", str(css_path)])
    if cover_image.is_file():
        epub_args.extend(["--epub-cover-image", str(cover_image)])

    run_pandoc(epub_args)

    engine = pick_pdf_engine()
    if not engine:
        print("No se encontro un motor PDF (xelatex, lualatex, pdflatex).", file=sys.stderr)
        return 1

    pdf_args = [
        "pandoc",
        str(input_file),
        *common_args,
        "--pdf-engine",
        engine,
        "--variable",
        "fontsize=12pt",
        "--variable",
        "linestretch=1.3",
        "--variable",
        "geometry:margin=1in",
        "-o",
        str(pdf_file),
    ]

    if engine in {"xelatex", "lualatex"}:
        pdf_args.extend(
            [
                "--variable",
                "mainfont=TeX Gyre Pagella",
                "--variable",
                "sansfont=TeX Gyre Heros",
                "--variable",
                "monofont=DejaVu Sans Mono",
            ]
        )

    cover_tex_path: Path | None = None
    if cover_image.is_file():
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".tex",
            delete=False,
            encoding="utf-8",
        ) as cover_tex:
            cover_tex.write(
                "\\thispagestyle{empty}\n"
                "\\begin{center}\n"
                "\\includegraphics[width=\\textwidth,height=\\textheight,keepaspectratio]"
                f"{{\\detokenize{{{cover_image.as_posix()}}}}}\n"
                "\\end{center}\n"
                "\\clearpage\n"
            )
            cover_tex_path = Path(cover_tex.name)
        pdf_args.extend(["--include-before-body", str(cover_tex_path)])

    try:
        run_pandoc(pdf_args)
    finally:
        if cover_tex_path and cover_tex_path.exists():
            cover_tex_path.unlink()
    print(f"Archivos generados en: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
