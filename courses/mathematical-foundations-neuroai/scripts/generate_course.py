#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path
from typing import Any


COURSE_ROOT = Path(__file__).resolve().parents[1]
STRUCTURE_PATH = COURSE_ROOT / "source" / "structure.json"
COURSE_SLUG = "mathematical-foundations-neuroai"
COURSE_TITLE = "Mathematical Foundations for Computational Neuroscience and AI"
AUTHOR = "Arjun Puri"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "section"


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def load_structure() -> dict[str, Any]:
    return json.loads(STRUCTURE_PATH.read_text(encoding="utf-8"))


def chapter_path(chapter: dict[str, Any]) -> Path:
    configured = chapter.get("path")
    if configured:
        return COURSE_ROOT / configured
    number = int(chapter["number"])
    title = str(chapter["title"])
    return COURSE_ROOT / "chapters" / f"ch{number:02d}-{slugify(title)}" / f"ch{number:02d}.tex"


def authored_chapter_path(chapter: dict[str, Any]) -> Path:
    return COURSE_ROOT / "source" / "authored-chapters" / f"ch{int(chapter['number']):02d}.tex"


def chapter_has_authored_source(chapter: dict[str, Any]) -> bool:
    return authored_chapter_path(chapter).exists()


def render_spine_chapter(volume_label: str, volume_title: str, chapter: dict[str, Any]) -> str:
    number = int(chapter["number"])
    lines = [
        f"% {volume_label}: {volume_title}",
        f"\\section{{Chapter {number}: {latex_escape(str(chapter['title']))}}}",
        "",
    ]
    for section in chapter["sections"]:
        lines.extend(
            [
                f"\\subsection{{{latex_escape(str(section['number']))} {latex_escape(str(section['title']))}}}",
                "% Authored lecture text, diagrams, exercises, and references intentionally omitted.",
                "",
            ]
        )
    lines.append(r"\clearpage")
    return "\n".join(lines).rstrip() + "\n"


def iter_volume_chapters(structure: dict[str, Any]):
    for volume in structure["volumes"]:
        for chapter in volume["chapters"]:
            yield volume, chapter


def write_frontmatter() -> None:
    write_text(
        COURSE_ROOT / "frontmatter" / "titlepage.tex",
        textwrap.dedent(
            rf"""
            \begin{{titlepage}}
            \centering
            \vspace*{{0.18\textheight}}
            {{\Huge\bfseries {latex_escape(COURSE_TITLE)}\par}}
            \vspace{{1.5em}}
            {{\Large Lecture Notes Structure\par}}
            \vspace{{2em}}
            {{\large {latex_escape(AUTHOR)}\par}}
            \vfill
            {{\large 2026\par}}
            \end{{titlepage}}
            """
        ).strip()
        + "\n",
    )
    write_text(
        COURSE_ROOT / "frontmatter" / "preface.tex",
        textwrap.dedent(
            r"""
            \section*{Preface}
            \addcontentsline{toc}{section}{Preface}
            These notes are a structured bridge from undergraduate mathematics toward the mathematical language used in modern machine learning, AI, and computational neuroscience.
            """
        ).strip()
        + "\n",
    )
    write_text(
        COURSE_ROOT / "frontmatter" / "notation.tex",
        textwrap.dedent(
            r"""
            \section*{Notation}
            \addcontentsline{toc}{section}{Notation}
            Notation is introduced locally in each chapter. Chapter 1 establishes the typed language used throughout the course.
            """
        ).strip()
        + "\n",
    )


def write_references() -> None:
    write_text(COURSE_ROOT / "backmatter" / "references.bib", "% References intentionally omitted in structure-only mode.\n")


def write_main(structure: dict[str, Any]) -> None:
    inputs: list[str] = []
    for volume in structure["volumes"]:
        inputs.append(rf"\part{{{latex_escape(str(volume['label']))}: {latex_escape(str(volume['title']))}}}")
        for chapter in volume["chapters"]:
            path = chapter_path(chapter).relative_to(COURSE_ROOT).with_suffix("")
            inputs.append(rf"\input{{{path.as_posix()}}}")

    write_text(
        COURSE_ROOT / "main.tex",
        textwrap.dedent(
            rf"""
            \documentclass[11pt]{{article}}
            \usepackage[letterpaper,margin=1in]{{geometry}}
            \usepackage{{fontspec}}
            \usepackage{{unicode-math}}
            \usepackage{{amsmath}}
            \usepackage{{amsthm}}
            \usepackage{{graphicx}}
            \usepackage{{xcolor}}
            \usepackage{{booktabs}}
            \usepackage{{enumitem}}
            \usepackage{{microtype}}
            \usepackage{{hyperref}}
            \usepackage{{bookmark}}
            \emergencystretch=3em
            \setcounter{{tocdepth}}{{3}}
            \setlist{{itemsep=0.25em, topsep=0.35em}}

            \title{{{latex_escape(COURSE_TITLE)}}}
            \author{{{latex_escape(AUTHOR)}}}
            \date{{2026}}

            \begin{{document}}
            \pagenumbering{{gobble}}
            \input{{frontmatter/titlepage}}
            \clearpage
            \pagenumbering{{roman}}
            \tableofcontents
            \clearpage
            \input{{frontmatter/preface}}
            \input{{frontmatter/notation}}
            \clearpage
            \pagenumbering{{arabic}}

            {chr(10).join(inputs)}

            \end{{document}}
            """
        ).strip()
        + "\n",
    )


def write_makefile() -> None:
    write_text(
        COURSE_ROOT / "Makefile",
        textwrap.dedent(
            f"""
            DOC := main
            COURSE_SLUG := {COURSE_SLUG}
            LATEXMK := latexmk
            LATEXMKRC := $(CURDIR)/latexmkrc
            LATEX_CACHE := $(CURDIR)/.tex-cache
            LATEXMK_FLAGS := -norc -r $(LATEXMKRC) -lualatex
            ENV := TEXMFCACHE="$(LATEX_CACHE)" TEXMFVAR="$(LATEX_CACHE)" \\
                   TEXMFCONFIG="$(LATEX_CACHE)" LUAOTFLOAD_CACHE="$(LATEX_CACHE)" \\
                   LUAOTFLOADCACHE="$(LATEX_CACHE)"
            PYTHON ?= python3

            .PHONY: all source pdf clean distclean

            all: pdf

            source:
            \t$(PYTHON) scripts/generate_course.py

            pdf: source
            \t@mkdir -p $(LATEX_CACHE) build
            \t@rm -f build/$(DOC).aux build/$(DOC).bcf build/$(DOC).bbl build/$(DOC).blg build/$(DOC).run.xml build/$(DOC).fdb_latexmk build/$(DOC).fls
            \t$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) $(DOC).tex
            \tcp build/$(DOC).pdf $(DOC).pdf
            \tcp build/$(DOC).pdf $(COURSE_SLUG)-lecture-notes.pdf

            clean:
            \t@mkdir -p $(LATEX_CACHE)
            \t$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) -c $(DOC).tex

            distclean:
            \trm -rf build .tex-cache main.pdf $(COURSE_SLUG)-lecture-notes.pdf
            """
        ).lstrip(),
    )


def write_latexmkrc() -> None:
    write_text(
        COURSE_ROOT / "latexmkrc",
        textwrap.dedent(
            r"""
            $out_dir = 'build';
            $aux_dir = 'build';
            $pdflatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
            $lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
            $pdf_mode = 4;
            """
        ).lstrip(),
    )


def write_chapters(structure: dict[str, Any]) -> None:
    for volume, chapter in iter_volume_chapters(structure):
        source_path = authored_chapter_path(chapter)
        if source_path.exists():
            write_text(chapter_path(chapter), source_path.read_text(encoding="utf-8"))
        else:
            write_text(chapter_path(chapter), render_spine_chapter(str(volume["label"]), str(volume["title"]), chapter))


def write_chapter_map(structure: dict[str, Any]) -> None:
    lectures = []
    for _, chapter in iter_volume_chapters(structure):
        number = int(chapter["number"])
        title = str(chapter["title"])
        lectures.append(
            {
                "lecture_slug": f"chapter-{number:02d}-{slugify(title)}",
                "title": title,
                "slide_filename": f"chapter-{number:02d}.pdf",
                "chapter_paths": [str(chapter_path(chapter).relative_to(COURSE_ROOT))],
                "aliases": [title, f"Chapter {number}"],
            }
        )
    write_text(COURSE_ROOT / "backmatter" / "lecture-chapter-map.json", json.dumps({"lectures": lectures}, indent=2) + "\n")


def write_structure(structure: dict[str, Any]) -> None:
    structure = dict(structure)
    structure["mode"] = "structure-plus-authored-chapters"
    structure["content_policy"] = (
        "Generated prose templates are disabled. Chapter files preserve the volume, "
        "chapter, and section spine unless a durable source file exists under "
        "source/authored-chapters/."
    )
    for _, chapter in iter_volume_chapters(structure):
        status = "authored" if chapter_has_authored_source(chapter) else "spine-only"
        for section in chapter["sections"]:
            section["status"] = status
    write_text(STRUCTURE_PATH, json.dumps(structure, indent=2) + "\n")


def write_readme() -> None:
    write_text(
        COURSE_ROOT / "README.md",
        textwrap.dedent(
            f"""
            # {COURSE_TITLE}

            This course is generated by `scripts/generate_course.py`. The generator
            preserves the course spine from `source/structure.json`. Durable authored
            chapter sources live in `source/authored-chapters/`; when one exists, the
            generator copies it into `chapters/` instead of emitting a spine-only
            placeholder.

            Build:

            ```bash
            make all
            ```
            """
        ).strip()
        + "\n",
    )


def main() -> None:
    structure = load_structure()
    write_frontmatter()
    write_references()
    write_makefile()
    write_latexmkrc()
    write_chapters(structure)
    write_chapter_map(structure)
    write_main(structure)
    write_structure(structure)
    write_readme()


if __name__ == "__main__":
    main()
