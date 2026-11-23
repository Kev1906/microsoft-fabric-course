#!/usr/bin/env python3
"""Valida una sesión del Microsoft Fabric Master Course.

Uso:
    python .opencode/skills/fabric-day-generator/scripts/check_day.py 4
    python .opencode/skills/fabric-day-generator/scripts/check_day.py --all

Comprueba:
- Existencia de lección, laboratorio y solución con el naming del curso.
- IDs duplicados, enlaces locales rotos, anclas inexistentes.
- Un solo <h1> y jerarquía de headings.
- Secciones obligatorias de la lección.
- Presencia de 3 misiones y de rúbrica.
- Fecha de verificación de documentación.
- Referencias desde index.html y enlaces cruzados.
- Restos markdown del mismo día.

Sin dependencias externas. Código de salida 1 si hay errores.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "index.html"

REQUIRED_LESSON_MARKERS = [
    "Recuperación activa",
    "Modelo mental",
    "Demo guiada",
    "Lo que un senior ve",
    "DP-700",
    "Laboratorio",
    "Errores frecuentes",
    "Drill de entrevista",
    "Teach-back",
    "Repetición espaciada",
    "Entregable",
    "Referencias",
    "Docs verificadas:",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.headings: list[int] = []
        self.lang = ""
        self.title = ""
        self.text_chunks: list[str] = []
        self._in_title = False
        self._skip_text = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value for key, value in attrs}
        if tag == "html" and data.get("lang"):
            self.lang = data["lang"] or ""
        if tag == "title":
            self._in_title = True
        if tag in {"script", "style"}:
            self._skip_text += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(int(tag[1]))
        if data.get("id"):
            self.ids.append(data["id"] or "")
        if tag in {"a", "link", "script", "img", "source"}:
            target = data.get("href") or data.get("src")
            if target:
                self.links.append((tag, target))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag in {"script", "style"} and self._skip_text:
            self._skip_text -= 1

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if not self._skip_text:
            self.text_chunks.append(data)


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def check_page(path: Path, day: int) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    parser = parse(path)
    text = " ".join(parser.text_chunks)

    if parser.lang != "es":
        warnings.append('La etiqueta <html> debería declarar lang="es".')

    if not parser.title.strip():
        warnings.append("Falta un <title> con contenido.")

    duplicates = [value for value, count in Counter(parser.ids).items() if count > 1]
    if duplicates:
        errors.append(f"IDs duplicados: {', '.join(sorted(duplicates))}")

    h1_count = parser.headings.count(1)
    if h1_count != 1:
        errors.append(f"Debe haber exactamente un <h1>; hay {h1_count}.")

    previous = 0
    for level in parser.headings:
        if previous and level > previous + 1:
            warnings.append(f"Salto de heading h{previous} a h{level}.")
            break
        previous = level

    for tag, target in parser.links:
        if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
            continue
        parsed = urlparse(target)
        if parsed.scheme and parsed.scheme not in {"file"}:
            continue
        relative = unquote(parsed.path)
        if not relative:
            continue
        resolved = (path.parent / relative).resolve()
        if not resolved.exists():
            errors.append(f"Enlace local roto en <{tag}>: {target}")
            continue

        if tag == "a" and parsed.fragment:
            if not resolved.is_file() or resolved.suffix.lower() not in {".html", ".htm"}:
                continue
            fragment = unquote(parsed.fragment)
            if fragment not in parse(resolved).ids:
                errors.append(f"Ancla inexistente: {target}")

    if path.parent.name == "lessons":
        for marker in REQUIRED_LESSON_MARKERS:
            if marker.lower() not in text.lower():
                errors.append(f"Falta la sección o marcador obligatorio: {marker}")
        if not re.search(r"Docs verificadas:\s*20\d{2}-\d{2}-\d{2}", text):
            errors.append("Falta una fecha real con formato 'Docs verificadas: YYYY-MM-DD'.")

    if path.parent.name == "exercises":
        missions = len(re.findall(r'class="mission"', path.read_text(encoding="utf-8")))
        if missions != 3:
            errors.append(f"El laboratorio debe tener 3 misiones; encontré {missions}.")

    if path.parent.name == "solutions":
        if "Rúbrica" not in text:
            errors.append("La solución debe incluir una rúbrica.")
        if "score-scale" not in path.read_text(encoding="utf-8"):
            warnings.append("La solución no usa el componente .score-scale.")

    own = path.resolve()
    for folder, label in (("lessons", "lección"), ("exercises", "laboratorio"), ("solutions", "solución")):
        if folder == path.parent.name:
            continue
        candidates = sorted((ROOT / folder).glob(f"dia-{day:02d}-*.html"))
        if not candidates:
            continue
        target = candidates[0].resolve()
        if not any(
            (path.parent / urlparse(link).path).resolve() == target
            for tag, link in parser.links
            if tag == "a" and link and not link.startswith(("#", "http", "mailto:", "tel:"))
        ):
            warnings.append(f"Falta un enlace cruzado a la {label} del día.")

    return errors, warnings


def find_files(day: int) -> dict[str, Path | None]:
    candidates = sorted((ROOT / "lessons").glob(f"dia-{day:02d}-*.html"))
    lesson = candidates[0] if candidates else None
    if len(candidates) > 1:
        print(f"  AVISO: hay varias lecciones para el día {day:02d}: {', '.join(p.name for p in candidates)}")
    return {
        "lección": lesson,
        "laboratorio": ROOT / "exercises" / f"dia-{day:02d}-ejercicios.html",
        "solución": ROOT / "solutions" / f"dia-{day:02d}-solucion.html",
    }


def check_day(day: int) -> int:
    all_errors: list[str] = []
    all_warnings: list[str] = []

    print(f"\nDía {day:02d}")
    print("=" * 64)

    files = find_files(day)
    for label, path in files.items():
        if path is None or not path.exists():
            all_errors.append(f"Falta {label}: {path.relative_to(ROOT) if path else 'sin archivo'}")
            continue
        errors, warnings = check_page(path, day)
        print(f"\n{label}: {path.relative_to(ROOT)}")
        if not errors and not warnings:
            print("  OK")
        for error in errors:
            print(f"  ERROR: {error}")
        for warning in warnings:
            print(f"  AVISO: {warning}")
        all_errors.extend(f"{path.name}: {error}" for error in errors)
        all_warnings.extend(f"{path.name}: {warning}" for warning in warnings)

    legacy = []
    for folder in ("lessons", "exercises", "solutions"):
        for candidate in (ROOT / folder).glob(f"dia-{day:02d}*.md"):
            legacy.append(candidate.relative_to(ROOT))
    if legacy:
        all_warnings.append("Hay recursos markdown del mismo día: " + ", ".join(map(str, legacy)))

    if INDEX.exists():
        index_text = INDEX.read_text(encoding="utf-8")
        if f"dia-{day:02d}" not in index_text:
            all_warnings.append(f"index.html no menciona el día {day:02d}.")
    else:
        all_errors.append("Falta index.html.")

    print("\n" + "-" * 64)
    if all_errors:
        print(f"RESULTADO: {len(all_errors)} error(es), {len(all_warnings)} aviso(s).")
        return 1
    print(f"RESULTADO: OK con {len(all_warnings)} aviso(s).")
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Valida una sesión del Fabric Master Course.")
    parser.add_argument("day", nargs="?", type=int, help="Número de día, por ejemplo 4")
    parser.add_argument("--day", dest="day_flag", type=int, help="Número de día")
    parser.add_argument("--all", action="store_true", help="Valida todos los días publicados")
    args = parser.parse_args()

    if args.all:
        days = sorted(
            int(match.group(1))
            for path in (ROOT / "lessons").glob("dia-*.html")
            if (match := re.fullmatch(r"dia-(\d{2})-.*\.html", path.name))
        )
        if not days:
            print("No hay lecciones publicadas.")
            return 1
        return max(check_day(day) for day in days)

    day = args.day_flag or args.day
    if day is None:
        parser.error("Indica un día, por ejemplo: check_day.py 4")
    return check_day(day)


if __name__ == "__main__":
    sys.exit(main())
