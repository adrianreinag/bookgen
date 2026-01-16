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


def strip_frontmatter(markdown: str) -> str:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return markdown
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return "\n".join(lines[idx + 1 :]).lstrip() + "\n"
    return markdown


def parse_frontmatter(markdown: str) -> dict[str, str]:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end = idx
            break
    if end is None:
        return {}
    data: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value
    return data


def upsert_frontmatter(markdown: str, updates: dict[str, str]) -> str:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        frontmatter_lines = ["---"]
        for key, value in updates.items():
            frontmatter_lines.append(f"{key}: {value}")
        frontmatter_lines.append("---")
        frontmatter_lines.append("")
        return "\n".join(frontmatter_lines) + markdown.lstrip()

    end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end = idx
            break
    if end is None:
        return markdown

    existing = lines[1:end]
    existing_map = {}
    for i, line in enumerate(existing):
        if ":" not in line:
            continue
        key, _ = line.split(":", 1)
        existing_map[key.strip()] = i

    for key, value in updates.items():
        line = f"{key}: {value}"
        if key in existing_map:
            existing[existing_map[key]] = line
        else:
            existing.append(line)

    return "\n".join(["---", *existing, "---", *lines[end + 1 :]])


def extract_seed_title(markdown: str) -> str:
    frontmatter = parse_frontmatter(markdown)
    title = frontmatter.get("title", "").strip()
    if title:
        return title

    lines = markdown.splitlines()
    for idx, line in enumerate(lines):
        if line.strip().lower().startswith("## titulo"):
            for next_line in lines[idx + 1 :]:
                cleaned = next_line.strip()
                if not cleaned:
                    continue
                if cleaned.startswith("-"):
                    cleaned = cleaned.lstrip("-").strip()
                return cleaned
    return ""


def insert_origen_section(markdown: str, origin: str) -> str:
    if "## Origen" in markdown:
        return markdown

    lines = markdown.splitlines()
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = idx + 1
            payload = [
                "",
                "## Origen",
                f"- Fuente (idea, nota o enlace): {origin}",
                "",
            ]
            new_lines = lines[:insert_at] + payload + lines[insert_at:]
            return "\n".join(new_lines).rstrip() + "\n"

    return f"## Origen\n- Fuente (idea, nota o enlace): {origin}\n\n{markdown.lstrip()}"


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


def ensure_structure_dirs(root: Path) -> None:
    (root / "structure" / "beats").mkdir(parents=True, exist_ok=True)


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
    parser.add_argument(
        "--seed-path",
        default="",
        help="Ruta a un seed.md de idea ganadora (opcional).",
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

    seed_content: str | None = None
    seed_title = ""
    seed_path = Path(args.seed_path) if args.seed_path else None
    if seed_path:
        if not seed_path.is_file():
            print(f"No existe el seed: {seed_path}", file=sys.stderr)
            return 1
        seed_raw = seed_path.read_text(encoding="utf-8")
        seed_title = extract_seed_title(seed_raw)
        seed_body = strip_frontmatter(seed_raw)
        seed_body = insert_origen_section(seed_body, str(seed_path))
        seed_content = upsert_frontmatter(
            seed_body,
            {
                "type": "seed",
                "title": f"\"{seed_title}\"" if seed_title else "\"\"",
                "origin": f"\"{seed_path}\"",
                "status": "draft",
                "tags": "[bible, seed]",
            },
        )

    title = args.title.strip()
    if title:
        book_title = title
    elif seed_title:
        book_title = seed_title
    else:
        book_title = "Sin titulo"
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
    ensure_structure_dirs(book_dir)
    if seed_content:
        seed_content = upsert_frontmatter(
            seed_content,
            {"title": f"\"{book_title}\""},
        )
        seed_target = book_dir / "bible" / "seed.md"
        seed_target.write_text(seed_content, encoding="utf-8")
    init_git_repo(book_dir)
    print(f"Libro creado en: {book_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
