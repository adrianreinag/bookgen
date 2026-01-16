#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
import uuid


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def apply_tokens(root: Path, tokens: dict[str, str]) -> None:
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        updated = text
        for key, value in tokens.items():
            if key in updated:
                updated = updated.replace(key, value)
        if updated != text:
            path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Crea un libro nuevo desde plantilla."
    )
    parser.add_argument(
        "--title",
        default="",
        help="Titulo legible del libro (opcional).",
    )
    parser.add_argument(
        "--slug",
        default="",
        help="Nombre de carpeta (opcional, en minusculas y sin espacios).",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    working_dir = root_dir / "books"
    template_dir = root_dir / "templates" / "book-template"

    if not working_dir.is_dir():
        print(f"No existe la carpeta books en {root_dir}.", file=sys.stderr)
        return 1

    if not template_dir.is_dir():
        print(f"No existe la carpeta templates/book-template en {root_dir}.", file=sys.stderr)
        return 1

    book_id = ""
    for _ in range(10):
        candidate = uuid.uuid4().hex[:12]
        if not (working_dir / candidate).exists():
            book_id = candidate
            break

    if not book_id:
        print("No se pudo generar un identificador unico.", file=sys.stderr)
        return 1

    title = args.title.strip()
    book_title = title if title else "Sin titulo"
    slug_source = args.slug.strip() or title
    slug = slugify(slug_source) if slug_source else ""

    folder_name = slug or book_id
    book_dir = working_dir / folder_name
    if slug and book_dir.exists():
        folder_name = f"{slug}-{book_id[:4]}"
        book_dir = working_dir / folder_name
        if book_dir.exists():
            folder_name = book_id
            book_dir = working_dir / folder_name

    if book_dir.exists():
        print(f"Ya existe la carpeta: {book_dir}", file=sys.stderr)
        return 1

    shutil.copytree(template_dir, book_dir)
    apply_tokens(
        book_dir,
        {
            "{{BOOK_ID}}": book_id,
            "{{BOOK_TITLE}}": book_title,
            "{{BOOK_SLUG}}": folder_name,
        },
    )
    print(f"Libro creado en: {book_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
