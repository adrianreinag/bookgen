#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import sys
import uuid


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    ideas_dir = root_dir / "ideas"
    template_dir = root_dir / "templates" / "idea-template"

    if not ideas_dir.is_dir():
        print(f"No existe la carpeta ideas en {root_dir}.", file=sys.stderr)
        return 1

    if not template_dir.is_dir():
        print(
            f"No existe la carpeta templates/idea-template en {root_dir}.",
            file=sys.stderr,
        )
        return 1

    idea_id = ""
    idea_dir = None
    for _ in range(10):
        candidate = uuid.uuid4().hex[:12]
        candidate_dir = ideas_dir / candidate
        if not candidate_dir.exists():
            idea_id = candidate
            idea_dir = candidate_dir
            break

    if not idea_id or idea_dir is None:
        print("No se pudo generar un identificador unico.", file=sys.stderr)
        return 1

    shutil.copytree(template_dir, idea_dir)
    print(f"Idea creada en: {idea_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
