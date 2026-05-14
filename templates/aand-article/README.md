# AAND Article Lecture Notes Template

This is the default visual and structural template for new lecture-note courses.
It follows the Acquisition and Analysis of Neural Data Summer notes: an
`article` document, simple `\maketitle`, table of contents, lecture-level
sections, compact typography, inline figures, and mostly unboxed prose.

Use `main.tex` as the course entry point. Keep lecture files written as:

```tex
\section{Lecture 1: Topic}
\subsection{Core idea}
\subsubsection{Detail}
```

The `coursenotes.cls` file exists only as a compatibility bridge for older
courses that still use `\documentclass{coursenotes}` and `\chapter`. New courses
should prefer the explicit `article` preamble in `main.tex`.
