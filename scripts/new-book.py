#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import sys
import uuid


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    working_dir = root_dir / "working-books"
    template_dir = root_dir / "template"

    if not working_dir.is_dir():
        print(f"No existe la carpeta working-books en {root_dir}.", file=sys.stderr)
        return 1

    if not template_dir.is_dir():
        print(f"No existe la carpeta template en {root_dir}.", file=sys.stderr)
        return 1

    book_id = ""
    book_dir = None
    for _ in range(10):
        candidate = uuid.uuid4().hex[:12]
        candidate_dir = working_dir / candidate
        if not candidate_dir.exists():
            book_id = candidate
            book_dir = candidate_dir
            break

    if not book_id or book_dir is None:
        print("No se pudo generar un identificador unico.", file=sys.stderr)
        return 1

    shutil.copytree(template_dir, book_dir)
    print(f"Libro creado en: {book_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
