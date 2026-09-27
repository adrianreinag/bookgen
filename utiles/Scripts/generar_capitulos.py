#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys


def find_vault_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "02_Biblia").is_dir() and (candidate / "03_Produccion").is_dir():
            return candidate
    raise FileNotFoundError(
        "No se pudo detectar la raiz del vault (faltan 02_Biblia/ y 03_Produccion/). "
        "Ejecuta el script desde la raiz del vault o pasa --vault-root."
    )


def write_file(path: Path, content: str, *, force: bool) -> None:
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def beats_template(cp: str) -> str:
    return f"""---\ntype: beats\nchapter: {cp}\nstatus: draft\ntags: [produccion, beats]\n---\n\n# Beats — {cp}\n\n## Propósito del capítulo\n- (Qué cambia al terminar)\n\n## Escenas (3–6)\n### Escena 1\n- Lugar: [[LOC_...]]\n- Personajes: [[CHAR_...]]\n- Objetivo:\n- Conflicto:\n- Resultado:\n\n## Beats causales (10–20)\n- Porque ___, entonces ___.\n\n## Entidades nuevas (si aparecen)\n- (Crear/enlazar `CHAR_/LOC_/ORG_/EVT_/OBJ_/CON_/TERM_/CUL_`)\n"""


def draft_template(cp: str) -> str:
    return f"""---\ntype: draft\nchapter: {cp}\nversion: v1\nstatus: draft\ntags: [produccion, draft]\n---\n\n# Draft — {cp} (v1)\n\n## DRAFT\n\n## NEW FACTS\n- (Hecho nuevo) — Entidad afectada: `CHAR_/LOC_/...` — Fuente: `{cp} Draft_v1`\n"""


def final_template(cp: str) -> str:
    return f"""---\ntype: final\nchapter: {cp}\nstatus: draft\ntags: [produccion, final]\n---\n\n# Final — {cp}\n\n(Versión final del capítulo. Fuente: `Draft_vN.md` + pase editorial.)\n"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera scaffolding de capítulos en 03_Produccion/CP_XX/.")
    parser.add_argument("--vault-root", default="", help="Raíz del vault. Por defecto, auto-detecta desde CWD.")
    parser.add_argument("--count", type=int, required=True, help="Número de capítulos (CP_01..CP_N).")
    parser.add_argument("--include-prologo", action="store_true", help="Crea CP_00 (prólogo).")
    parser.add_argument("--include-epilogo", action="store_true", help="Crea CP_XX adicional como epílogo (CP_{N+1}).")
    parser.add_argument("--force", action="store_true", help="Sobrescribe archivos existentes.")
    parser.add_argument("--dry-run", action="store_true", help="No escribe; solo imprime acciones.")
    args = parser.parse_args()

    if args.count <= 0:
        print("--count debe ser > 0", file=sys.stderr)
        return 2

    start = Path(args.vault_root).resolve() if args.vault_root else Path.cwd().resolve()
    vault_root = find_vault_root(start)
    production_dir = vault_root / "03_Produccion"
    production_dir.mkdir(parents=True, exist_ok=True)

    chapters: list[int] = []
    if args.include_prologo:
        chapters.append(0)
    chapters.extend(list(range(1, args.count + 1)))
    if args.include_epilogo:
        chapters.append(args.count + 1)

    for number in chapters:
        cp = f"CP_{number:02d}"
        chapter_dir = production_dir / cp
        beats_path = chapter_dir / "Beats.md"
        draft_path = chapter_dir / "Drafts" / "Draft_v1.md"
        final_path = chapter_dir / "Final.md"

        if args.dry_run:
            print(f"DIR: {chapter_dir}")
            print(f"  - {beats_path}")
            print(f"  - {draft_path}")
            print(f"  - {final_path}")
            continue

        chapter_dir.mkdir(parents=True, exist_ok=True)
        write_file(beats_path, beats_template(cp), force=args.force)
        write_file(draft_path, draft_template(cp), force=args.force)
        write_file(final_path, final_template(cp), force=args.force)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
