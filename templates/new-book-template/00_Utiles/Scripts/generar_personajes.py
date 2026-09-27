#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
import re
from pathlib import Path
import sys
import unicodedata


@dataclass(frozen=True)
class CharacterSpec:
    name: str
    role: str = ""
    aliases: list[str] | None = None


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_value = ascii_value.strip().lower()
    ascii_value = re.sub(r"[^a-z0-9]+", "_", ascii_value)
    return ascii_value.strip("_") or "personaje"


def find_vault_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "02_Biblia").is_dir() and (candidate / "03_Produccion").is_dir():
            return candidate
    raise FileNotFoundError(
        "No se pudo detectar la raiz del vault (faltan 02_Biblia/ y 03_Produccion/). "
        "Ejecuta el script desde la raiz del vault o pasa --vault-root."
    )


def parse_id_number(frontmatter_id: str, prefix: str) -> int | None:
    match = re.fullmatch(rf"{re.escape(prefix)}_(\d{{4}})", frontmatter_id.strip())
    if not match:
        return None
    return int(match.group(1))


def current_max_entity_number(directory: Path, prefix: str) -> int:
    best = 0
    pattern = re.compile(r"^id:\s*([A-Z]+_\d{4})\s*$", re.MULTILINE)
    for path in directory.glob(f"{prefix}_*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        match = pattern.search(text)
        if not match:
            continue
        number = parse_id_number(match.group(1), prefix)
        if number is None:
            continue
        best = max(best, number)
    return best


def read_existing_entity_id(path: Path, prefix: str) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.search(r"^id:\s*([A-Z]+_\d{4})\s*$", text, flags=re.MULTILINE)
    if not match:
        return None
    candidate = match.group(1).strip()
    if parse_id_number(candidate, prefix) is None:
        return None
    return candidate


def load_character_template(script_dir: Path) -> str:
    template_path = script_dir.parent / "Vault Templates" / "CHAR_Template.md"
    if not template_path.is_file():
        raise FileNotFoundError(f"No existe template: {template_path}")
    return template_path.read_text(encoding="utf-8")


def parse_names_file(path: Path) -> list[CharacterSpec]:
    raw = path.read_text(encoding="utf-8").splitlines()
    specs: list[CharacterSpec] = []
    for line in raw:
        cleaned = line.strip()
        if not cleaned:
            continue
        if cleaned.startswith(("#", "<!--")):
            continue
        if cleaned.startswith(("-", "*")):
            cleaned = cleaned.lstrip("-*").strip()
        parts = [p.strip() for p in cleaned.split("|") if p.strip()]
        if not parts:
            continue
        name = parts[0]
        role = ""
        aliases: list[str] = []
        for extra in parts[1:]:
            if extra.lower().startswith("role="):
                role = extra.split("=", 1)[1].strip()
                continue
            if extra.lower().startswith("aliases="):
                rest = extra.split("=", 1)[1]
                aliases = [a.strip() for a in rest.split(",") if a.strip()]
                continue
        specs.append(CharacterSpec(name=name, role=role, aliases=aliases or None))
    return specs


def materialize_character_markdown(
    template: str, *, entity_id: str, name: str, role: str, aliases: list[str]
) -> str:
    updated = template
    updated = re.sub(r"^id:\s*CHAR_\d{4}\s*$", f"id: {entity_id}", updated, flags=re.MULTILINE)
    updated = re.sub(r'^name:\s*""\s*$', f'name: "{name}"', updated, flags=re.MULTILINE)
    if role:
        updated = re.sub(r'^role:\s*""\s*$', f'role: "{role}"', updated, flags=re.MULTILINE)
    if aliases:
        quoted = ", ".join([f'"{a}"' for a in aliases])
        updated = re.sub(r"^aliases:\s*\\[\\]\\s*$", f"aliases: [{quoted}]", updated, flags=re.MULTILINE)
    updated = re.sub(r"^# Personaje: NOMBRE\\s*$", f"# Personaje: {name}", updated, flags=re.MULTILINE)
    return updated.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera fichas de personajes (SOT).")
    parser.add_argument("--vault-root", default="", help="Raíz del vault. Por defecto, auto-detecta desde CWD.")
    parser.add_argument(
        "--out-dir",
        default="",
        help="Directorio de salida. Por defecto: 02_Biblia/Entidades/Personajes",
    )
    parser.add_argument("--names", nargs="*", default=[], help="Nombres de personajes.")
    parser.add_argument("--from-file", default="", help="Archivo (txt/md) con 1 personaje por línea.")
    parser.add_argument("--force", action="store_true", help="Sobrescribe si existe el archivo.")
    parser.add_argument("--dry-run", action="store_true", help="No escribe archivos; solo imprime acciones.")
    args = parser.parse_args()

    start = Path(args.vault_root).resolve() if args.vault_root else Path.cwd().resolve()
    vault_root = find_vault_root(start)

    if args.out_dir:
        candidate = Path(args.out_dir)
        out_dir = candidate if candidate.is_absolute() else (vault_root / candidate)
    else:
        out_dir = vault_root / "02_Biblia" / "Entidades" / "Personajes"
    out_dir.mkdir(parents=True, exist_ok=True)

    script_dir = Path(__file__).resolve().parent
    template = load_character_template(script_dir)

    specs: list[CharacterSpec] = []
    if args.from_file:
        specs.extend(parse_names_file(Path(args.from_file).resolve()))
    for name in args.names:
        cleaned = name.strip()
        if cleaned:
            specs.append(CharacterSpec(name=cleaned))

    if not specs:
        print("No hay personajes. Usa --names o --from-file.", file=sys.stderr)
        return 2

    created = 0
    next_number = current_max_entity_number(out_dir, "CHAR") + 1
    for spec in specs:
        filename = f"CHAR_{slugify(spec.name)}.md"
        path = out_dir / filename
        if path.exists() and not args.force:
            print(f"SKIP (existe): {path}")
            continue

        entity_id = read_existing_entity_id(path, "CHAR") if args.force and path.exists() else None
        if entity_id is None:
            entity_id = f"CHAR_{next_number:04d}"
            next_number += 1
        aliases = spec.aliases or []
        content = materialize_character_markdown(
            template,
            entity_id=entity_id,
            name=spec.name,
            role=spec.role,
            aliases=aliases,
        )
        if args.dry_run:
            print(f"CREATE: {path} (id={entity_id})")
            continue

        path.write_text(content, encoding="utf-8")
        created += 1
        print(f"OK: {path} (id={entity_id})")

    if created == 0 and not args.dry_run:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
