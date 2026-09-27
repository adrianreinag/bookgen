#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def pick_pdf_engine() -> str | None:
    for engine in ("xelatex", "lualatex", "pdflatex", "tectonic"):
        if shutil.which(engine):
            return engine
    return None


def run_pandoc(args: list[str]) -> None:
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as exc:
        print("Error ejecutando pandoc.", file=sys.stderr)
        raise SystemExit(exc.returncode)


def extract_draft_section(markdown: str) -> tuple[str | None, list[str]]:
    lines = markdown.splitlines()

    title: str | None = None
    for line in lines:
        if line.startswith("# "):
            title = line.strip()
            break

    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## DRAFT":
            start = i + 1
            break
    if start is None:
        return title, []

    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].strip() == "## NEW FACTS":
            end = i
            break

    draft_lines = lines[start:end]
    while draft_lines and not draft_lines[0].strip():
        draft_lines.pop(0)
    while draft_lines and not draft_lines[-1].strip():
        draft_lines.pop()

    return title, draft_lines


def strip_frontmatter(markdown: str) -> str:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return markdown

    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return "\n".join(lines[idx + 1 :]).lstrip() + "\n"
    return markdown


def iter_latest_chapter_drafts_legacy(drafts_dir: Path) -> list[Path]:
    candidates = sorted(drafts_dir.glob("chapter_*_v*.md"))
    if not candidates:
        return []

    best: dict[str, tuple[int, Path]] = {}
    pattern = re.compile(r"^chapter_(\d{2})_v(\d+)\.md$")
    for path in candidates:
        match = pattern.match(path.name)
        if not match:
            continue
        chapter_id, version_str = match.group(1), match.group(2)
        version = int(version_str)
        current = best.get(chapter_id)
        if current is None or version > current[0]:
            best[chapter_id] = (version, path)

    return [best[k][1] for k in sorted(best.keys())]


def iter_latest_chapter_drafts_chapters(chapters_dir: Path) -> list[Path]:
    if not chapters_dir.is_dir():
        return []

    chapter_dirs = sorted(
        [
            p
            for p in chapters_dir.iterdir()
            if p.is_dir() and p.name.startswith("chapter_")
        ]
    )
    if not chapter_dirs:
        return []

    best: dict[str, tuple[int, Path]] = {}

    chapter_id_pattern = re.compile(r"^chapter_(\d{2})$")
    draft_pattern = re.compile(r"^draft_v(\d+)\.md$")
    legacy_draft_pattern = re.compile(r"^chapter_(\d{2})_v(\d+)\.md$")

    for chapter_dir in chapter_dirs:
        match = chapter_id_pattern.match(chapter_dir.name)
        if not match:
            continue
        chapter_id = match.group(1)

        candidates: list[tuple[int, Path]] = []

        drafts_dir = chapter_dir / "drafts"
        if drafts_dir.is_dir():
            for path in drafts_dir.glob("*.md"):
                dm = draft_pattern.match(path.name)
                if dm:
                    candidates.append((int(dm.group(1)), path))
                    continue
                lm = legacy_draft_pattern.match(path.name)
                if lm and lm.group(1) == chapter_id:
                    candidates.append((int(lm.group(2)), path))

        for path in chapter_dir.glob("draft_v*.md"):
            dm = draft_pattern.match(path.name)
            if dm:
                candidates.append((int(dm.group(1)), path))

        if not candidates:
            continue

        version, best_path = max(candidates, key=lambda item: item[0])
        best[chapter_id] = (version, best_path)

    return [best[k][1] for k in sorted(best.keys())]


def build_manuscript_from_drafts(book_dir: Path) -> str:
    chapters_dir = book_dir / "chapters"
    chapter_files = iter_latest_chapter_drafts_chapters(chapters_dir)
    if not chapter_files:
        drafts_dir = book_dir / "manuscript" / "drafts"
        chapter_files = iter_latest_chapter_drafts_legacy(drafts_dir)
    if not chapter_files:
        raise FileNotFoundError(
            "No se encontraron drafts. Layout soportados:\n"
            f"- Nuevo: {chapters_dir}/chapter_##/drafts/draft_vN.md\n"
            f"- Legacy: {book_dir}/manuscript/drafts/chapter_##_vN.md"
        )

    parts: list[str] = []
    for idx, chapter_path in enumerate(chapter_files):
        title, draft_lines = extract_draft_section(
            chapter_path.read_text(encoding="utf-8")
        )
        if not draft_lines:
            raise ValueError(f"No se encontró sección '## DRAFT' en: {chapter_path}")

        if title:
            if idx > 0:
                parts.append("")
            parts.append(title)
            parts.append("")

        parts.extend(draft_lines)
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def add_latex_chapter_pagebreaks(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    first_heading = True
    for line in lines:
        if line.startswith("# "):
            if not first_heading:
                out.extend(["", "\\clearpage", ""])
            first_heading = False
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


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
    parser.add_argument(
        "--from-drafts",
        action="store_true",
        help="Compila el manuscrito desde drafts (nuevo: `chapters/chapter_##/drafts/draft_vN.md`; legacy: `manuscript/drafts/`) extrayendo solo '## DRAFT'.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Sobrescribe archivos existentes en `output/`.",
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

    final_manuscript_path = book_dir / "manuscript" / "final" / "full_manuscript.md"

    if not shutil.which("pandoc"):
        print(
            "pandoc no esta instalado o no esta en el PATH. Instala pandoc.",
            file=sys.stderr,
        )
        return 1

    output_dir = book_dir / "output"

    epub_file = output_dir / f"{book_name}.epub"
    pdf_file = output_dir / f"{book_name}.pdf"

    if not args.overwrite and (epub_file.exists() or pdf_file.exists()):
        print(f"Ya existen archivos de salida en: {output_dir}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    temp_input_path: Path | None = None
    if args.from_drafts:
        manuscript_md = build_manuscript_from_drafts(book_dir)
        final_manuscript_path.parent.mkdir(parents=True, exist_ok=True)
        final_manuscript_path.write_text(manuscript_md, encoding="utf-8")
    else:
        if not final_manuscript_path.is_file():
            print(
                f"No se encontro el manuscrito final: {final_manuscript_path}",
                file=sys.stderr,
            )
            return 1
        manuscript_md = final_manuscript_path.read_text(encoding="utf-8")

    manuscript_md = strip_frontmatter(manuscript_md)

    manuscript_for_export = add_latex_chapter_pagebreaks(manuscript_md)
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".md",
        delete=False,
        encoding="utf-8",
    ) as tmp:
        tmp.write(manuscript_for_export)
        temp_input_path = Path(tmp.name)
    input_file = temp_input_path

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

    engine = pick_pdf_engine()
    if not engine:
        print(
            "No se encontro un motor PDF (xelatex, lualatex, pdflatex, tectonic). "
            "Instala TeX Live o un motor compatible.",
            file=sys.stderr,
        )
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
        "--variable",
        "title=",
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
    header_tex_path: Path | None = None
    if cover_image.is_file():
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".tex",
            delete=False,
            encoding="utf-8",
        ) as header_tex:
            header_tex.write("\\usepackage{graphicx}\n")
            header_tex_path = Path(header_tex.name)
        pdf_args.extend(["--include-in-header", str(header_tex_path)])
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
        run_pandoc(epub_args)
        run_pandoc(pdf_args)
    finally:
        if cover_tex_path and cover_tex_path.exists():
            cover_tex_path.unlink()
        if header_tex_path and header_tex_path.exists():
            header_tex_path.unlink()
        if temp_input_path and temp_input_path.exists():
            temp_input_path.unlink()
    print(f"Archivos generados en: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
