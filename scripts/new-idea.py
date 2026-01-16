#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
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


def init_git_repo(root: Path) -> None:
    if not shutil.which("git"):
        print("git no esta instalado; se omite git init.", file=sys.stderr)
        return
    try:
        subprocess.run(
            ["git", "init"],
            cwd=root,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        print(f"No se pudo inicializar git en: {root}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Crea una idea nueva desde plantilla."
    )
    parser.add_argument(
        "--title",
        default="",
        help="Titulo legible de la idea (opcional).",
    )
    parser.add_argument(
        "--slug",
        default="",
        help="Nombre de carpeta (opcional, en minusculas y sin espacios).",
    )
    args = parser.parse_args()

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
    for _ in range(10):
        candidate = uuid.uuid4().hex[:12]
        if not (ideas_dir / candidate).exists():
            idea_id = candidate
            break

    if not idea_id:
        print("No se pudo generar un identificador unico.", file=sys.stderr)
        return 1

    title = args.title.strip()
    idea_title = title if title else "Sin titulo"
    slug_source = args.slug.strip() or title
    slug = slugify(slug_source) if slug_source else ""

    folder_name = slug or idea_id
    idea_dir = ideas_dir / folder_name
    if slug and idea_dir.exists():
        folder_name = f"{slug}-{idea_id[:4]}"
        idea_dir = ideas_dir / folder_name
        if idea_dir.exists():
            folder_name = idea_id
            idea_dir = ideas_dir / folder_name

    if idea_dir.exists():
        print(f"Ya existe la carpeta: {idea_dir}", file=sys.stderr)
        return 1

    shutil.copytree(template_dir, idea_dir)
    apply_tokens(
        idea_dir,
        {
            "{{IDEA_ID}}": idea_id,
            "{{IDEA_TITLE}}": idea_title,
            "{{IDEA_SLUG}}": folder_name,
        },
    )
    init_git_repo(idea_dir)
    print(f"Idea creada en: {idea_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
