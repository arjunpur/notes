# Scaffold/style plan

Course: Mesoscopic Theory of Clustered Spiking Networks: Foundations for a Rotation with Tilo Schwalger

Slug: `mesoscopic-clustered-spiking-networks`

Course root: `courses/mesoscopic-clustered-spiking-networks/`

Canonical PDF target: `courses/mesoscopic-clustered-spiking-networks/mesoscopic-clustered-spiking-networks-lecture-notes.pdf`

This file is a planner artifact only. It intentionally does not create or edit `main.tex`, `Makefile`, LaTeX style files, frontmatter, backmatter, chapters, appendices, figures, build outputs, site files, or Bodhi registry files.

## Reference conventions read

- Bodhi lecture-notes skill: canonical output is one LaTeX/PDF course, no separate plain-language companion page.
- Bodhi lecture-notes docs: manual edits should be followed by `refresh-preview` once the PDF is buildable and registry/config are settled.
- Lecture-notes repo README: each course is self-contained and buildable from its own directory with `make all`.
- `courses/models-of-neural-systems`: best structural match for this course because it uses `coursenotes`, `\chapter`, parts, `keyequation`, `chaptersummary`, and `conceptquestions`.
- `courses/mathematical-foundations-neuroai`: useful as a long-outline example, but its generated article scaffold is less compatible with the current mesoscopic chapter drafts, which already use `\chapter`.

## Recommended scaffold

Use the `models-of-neural-systems` course as the style and build source:

- copy/adapt `coursenotes.cls`
- copy/adapt `coursenotes-macros.sty`
- copy/adapt `coursenotes-environments.sty`
- copy/adapt `latexmkrc`
- copy/adapt `Makefile`
- create `main.tex` with `\documentclass{coursenotes}`, `\usepackage{coursenotes-macros}`, and `\usepackage{coursenotes-environments}`

Reason: the existing mesoscopic chapter drafts use `\chapter`, `\section`, `keyequation`, `aside`, `chaptersummary`, and `conceptquestions`. The `coursenotes` compatibility class maps chapter-style source into the minimal article surface used by current Bodhi notes.

Avoid using the `mathematical-foundations-neuroai/scripts/generate_course.py` pattern unless the final coordinator deliberately converts all chapter files to article-style `\section{Chapter N: ...}` source. Mixing that generated article scaffold with chapter-style worker output is a high LaTeX risk.

## Intended directory layout

```text
courses/mesoscopic-clustered-spiking-networks/
  Makefile
  latexmkrc
  coursenotes.cls
  coursenotes-macros.sty
  coursenotes-environments.sty
  main.tex
  frontmatter/
    titlepage.tex
    preface.tex
    notation.tex
  chapters/
    ch01-scientific-problem/ch01.tex
    ch02-litwin-kumar-doiron-baseline/ch02.tex
    ch03-single-neuron-models/ch03.tex
    ch04-balanced-networks/ch04.tex
    ch05-clustered-spiking-networks/ch05.tex
    ch06-why-mesoscopic-theory/ch06.tex
    ch07-mean-field-reductions/ch07.tex
    ch08-refractory-density-age-structured/ch08.tex
    ch09-stochastic-mesoscopic-equations/ch09.tex
    ch10-mesoscopic-excitatory-clustering/ch10.tex
    ch11-e-to-ei-clustered-networks/ch11.tex
    ch12-multistability-or-mesoscopic-chaos/ch12.tex
    ch13-spiking-attractor-motor-cortex/ch13.tex
    ch14-rostami-to-litwin-kumar-doiron/ch14.tex
    ch15-stabilized-supralinear-networks/ch15.tex
    ch16-spiking-ssn-gif-neurons/ch16.tex
    ch17-variability-quenching-conductance-shunting/ch17.tex
    ch18-dynamical-systems-essentials/ch18.tex
    ch19-stochastic-processes/ch19.tex
    ch20-measuring-variability-metastability/ch20.tex
    ch21-reproducing-baselines/ch21.tex
    ch22-building-ei-mesoscopic-extension/ch22.tex
    ch23-phase-diagrams-theory-deliverables/ch23.tex
    ch24-final-rotation-artifact/ch24.tex
  appendices/
    appA-notation-dictionary/appA.tex
    appB-paper-reading-guide/appB.tex
    appC-minimal-code-recipes/appC.tex
  figures/
    figure-metadata.md
    *.png
  backmatter/
    mathematical-synthesis.tex
    references.bib
    lecture-chapter-map.json
```

Current note for the final coordinator: this checkout already contains untracked chapter, appendix, and figure files produced by other workers. Treat them as external work and integrate them, but do not assume the set is complete.

## Main file integration order

Use `\include{...}` for chapters, matching `models-of-neural-systems`. This lets LaTeX write per-chapter aux files under `build/chapters/...` when the Makefile precreates those directories.

Expected high-level order:

```latex
\documentclass{coursenotes}
\usepackage{coursenotes-macros}
\usepackage{coursenotes-environments}

\usepackage[backend=biber, style=alphabetic, maxbibnames=99]{biblatex}
\addbibresource{backmatter/references.bib}

\providecommand{\index}[1]{}

\title{Mesoscopic Theory of Clustered Spiking Networks\\[0.5em]
  \large Foundations for a Rotation with Tilo Schwalger}
\author{Arjun Puri}
\date{2026}

\begin{document}
\frontmatter
\input{frontmatter/titlepage}
\tableofcontents
\input{frontmatter/preface}
\input{frontmatter/notation}

\mainmatter
% parts and chapter includes from chapter-paths.json

\backmatter
\appendix
\include{appendices/appA-notation-dictionary/appA}
\include{appendices/appB-paper-reading-guide/appB}
\include{appendices/appC-minimal-code-recipes/appC}
\input{backmatter/mathematical-synthesis}
\printbibliography[heading=bibintoc]
\end{document}
```

If the compatibility class does not define `\appendix`, the coordinator should add a minimal definition in the class or avoid `\appendix` and label appendices explicitly. Do this in the shared style file only in the final integration step.

## Frontmatter checklist

`frontmatter/titlepage.tex`

- Title should be the full course title, with the subtitle on a separate line.
- Use the restrained `models-of-neural-systems` title page style.
- Suggested affiliation line: `Bernstein Center for Computational Neuroscience, Berlin`.
- Suggested date: `2026`.

`frontmatter/preface.tex`

- Explain the rotation purpose: bridge clustered spiking simulations, mesoscopic population theory, and the finite-size versus chaos question.
- State prerequisites: calculus, linear algebra, probability, introductory spiking neuron models.
- State the method: every major concept defines objects, equations, term interpretations, observables, and what to compute next.
- Explicitly say no separate companion page exists; this PDF is the canonical artifact.

`frontmatter/notation.tex`

- Keep concise tables for indices, microscopic spiking variables, mesoscopic population variables, coupling symbols, observables, and finite-size scaling.
- Defer the full dictionary to Appendix A.

## Backmatter checklist

`backmatter/references.bib`

- Add only verified bibliography entries.
- Do not guess citations from memory.
- Keep placeholder prose in chapters where exact paper metadata is still unresolved.

`backmatter/mathematical-synthesis.tex`

- Short synthesis rather than a new chapter.
- Tie together the three central reductions: microscopic spikes to population activity, deterministic attractors to finite-size switching, and E-only clusters to paired E/I clusters.

`backmatter/lecture-chapter-map.json`

- This is needed for Bodhi registry integration when lecture slide inputs exist.
- Use real slide filenames only after the source lecture PDFs are available.
- Until lecture inputs exist, leave a documented empty or placeholder map for later ingestion; do not invent `chapter-XX-...pdf` slide mappings.
- Any populated entry should point to exactly the chapter path in `chapter-paths.json`.

## Makefile and build command

Recommended `Makefile` adaptation:

- Set `DOC := main`.
- Set `COURSE_SLUG := mesoscopic-clustered-spiking-networks`.
- Use the same `LATEXMK`, `LATEXMKRC`, cache variables, and `LATEXMK_FLAGS` as `models-of-neural-systems` or `mathematical-foundations-neuroai`.
- Precreate `build`, `.tex-cache`, all `build/chapters/<chapter-dir>`, and all `build/appendices/<appendix-dir>`.
- Copy `build/main.pdf` to both `main.pdf` and `mesoscopic-clustered-spiking-networks-lecture-notes.pdf`.

Build command from the course root:

```bash
make all
```

Expected final PDF:

```text
courses/mesoscopic-clustered-spiking-networks/mesoscopic-clustered-spiking-networks-lecture-notes.pdf
```

## Registry fields for coordinator

Suggested canonical entry in `/Users/arjun/Projects/bodhi/lecture-notes/config/courses.json`, only if the final coordinator is assigned registry edits:

```json
{
  "course_slug": "mesoscopic-clustered-spiking-networks",
  "display_name": "Mesoscopic Theory of Clustered Spiking Networks",
  "repo_path": "${HOME}/repos/lecture-notes/courses/mesoscopic-clustered-spiking-networks",
  "repo_remote": "https://github.com/arjunpur/lecture-notes.git",
  "obsidian_course_dir": "${HOME}/knowledge/5 - Projects/5.3 - BCCN/Courses/Mesoscopic Theory of Clustered Spiking Networks",
  "obsidian_pdf_target": "${HOME}/knowledge/5 - Projects/5.3 - BCCN/Courses/Mesoscopic Theory of Clustered Spiking Networks/Mesoscopic Theory of Clustered Spiking Networks - Lecture Notes.pdf",
  "public_slug": "mesoscopic-clustered-spiking-networks",
  "entry_tex": "main.tex",
  "build_command": ["make", "all"],
  "build_output_pdf": "mesoscopic-clustered-spiking-networks-lecture-notes.pdf",
  "chapter_map_path": "${HOME}/repos/lecture-notes/courses/mesoscopic-clustered-spiking-networks/backmatter/lecture-chapter-map.json",
  "support_paths": [
    "${HOME}/repos/lecture-notes/courses/mesoscopic-clustered-spiking-networks/figures/figure-metadata.md"
  ]
}
```

The exact Obsidian paths should be confirmed by the coordinator before committing registry changes.

## Notation conventions

Use these conventions across chapters unless a source paper requires a local exception:

- Neuron indices: `i,j`.
- Cluster indices: `k,\ell` or `\alpha,\beta`; pick one per chapter and define it. Prefer `k,\ell` for cluster labels in broad exposition and `\alpha,\beta` for equations already using Greek population indices.
- Population type: `a,b \in \{E,I\}`.
- Total neurons: `N`; excitatory and inhibitory counts: `N_E`, `N_I`.
- Cluster count: `K` or `Q`; choose one globally during final integration. Existing drafts use both, so coordinator should normalize. Recommended: `K` for number of clusters and `N_k` for cluster size.
- Cluster set: `\mathcal{C}_k`.
- Spike train: `s_i(t)=\sum_m \delta(t-t_i^m)`. If a chapter uses `x_i(t)`, define it and consider normalizing to `s_i(t)`.
- Conditional intensity or hazard: `\lambda_i(t)` for neuron-level intensity, `h(a,t)` for age-dependent hazard.
- Raw population activity: `A_k(t)=N_k^{-1}\sum_{i\in\mathcal{C}_k}s_i(t)`.
- Filtered population rate: `r_k(t)` or `r_k^a(t)`.
- Transfer function: `\Phi_a(\cdot)` for population type `a`.
- Microscopic coupling: `J_{ij}`.
- Mesoscopic coupling: `W_{k\ell}^{ab}`.
- Excitatory cluster strength: `J_+` or `g_E`; choose one globally. Recommended: use `J_+` when discussing Litwin-Kumar/Doiron-style strengthened E-to-E coupling, and `g_E,g_I` for phase diagrams.
- Fano factor: `F(T)=\operatorname{Var}[N(T)]/\mathbb{E}[N(T)]`.
- Coefficient of variation: `CV=\sqrt{\operatorname{Var}[T_{\mathrm{ISI}}]}/\mathbb{E}[T_{\mathrm{ISI}}]`.
- Finite-size scaling: noise amplitude should be written as `N_k^{-1/2}` when the fluctuating unit is cluster `k`.

Add any missing macros to `coursenotes-macros.sty` only during final integration. Likely useful additions: `\Cov`, `\Corr`, `\Prob`, `\FF`, `\CV`, `\1`, `\abs`, `\norm`.

## Figure integration

Use generated raster figures only. Keep exact equations and derivations in LaTeX, not inside images.

Observed generated assets already present in `figures/`:

- `meso-variability-decomposition.png`
- `meso-lkdoiron-clustered-balanced-network.png`
- `meso-ei-balance-cancellation.png`
- `meso-micro-to-meso-reduction.png`
- `meso-refractory-density-flow.png`
- `meso-noise-escape-vs-chaos.png`
- `meso-rostami-paired-ei-clusters.png`
- `meso-phase-diagram-roadmap.png`

Use `figures/figure-metadata.md` as the source of captions and figure intent. Suggested figure placements:

- Chapter 1: variability decomposition.
- Chapter 2: Litwin-Kumar/Doiron clustered balanced network.
- Chapter 4: E/I balance cancellation.
- Chapter 6: micro-to-meso reduction.
- Chapter 8: refractory-density flow.
- Chapter 12: noise escape versus chaos.
- Chapter 13: paired E/I clusters.
- Chapter 23: phase-diagram roadmap.

If a chapter has a figure slot without an existing raster asset, leave a visible LaTeX TODO comment or remove the slot. Do not create SVG/TikZ fallback figures.

## Chapter quality contract

Each substantial chapter should use this local pattern:

1. `\chapter{...}` and a short italic orientation paragraph.
2. Sections with compact prose and one concept per paragraph.
3. Equations only when they support an argument.
4. After each important equation, a term-by-term interpretation in prose or a `keyequation` legend.
5. At least one paragraph bridging microscopic mechanisms to mesoscopic variables.
6. A `chaptersummary` table or concise takeaways.
7. A `conceptquestions` list that asks the learner to compute, compare, or diagnose.

The six priority chapters should be complete before broad polishing:

- Chapter 2: The Litwin-Kumar & Doiron baseline.
- Chapter 4: Balanced networks.
- Chapter 7: Mean-field reductions of spiking networks.
- Chapter 9: Stochastic mesoscopic equations.
- Chapter 11: From E-clustered to E/I-clustered networks.
- Chapter 12: Multistability or mesoscopic chaos.

## Integration risks

- The checkout already contains untracked worker outputs in forbidden directories. Final coordinator should inspect all untracked files before adding shared scaffold files.
- Existing drafts use mixed symbols (`Q` and `K`, `A_\alpha` and `r_\alpha`, `x_i` and `s_i`). Notation cleanup is needed before build signoff.
- Some chapter and appendix files contain explicit citation TODOs. Do not convert these to citations until bibliography metadata is verified.
- `\appendix` support may be missing in the copied `coursenotes.cls`.
- Makefile must precreate build aux directories for every chapter and appendix included with `\include`.
- Long course title may overflow the title page if copied directly without line breaks.
- Figure paths must be consistent. Prefer `\includegraphics{figures/<file>.png}` unless the coordinator sets `\graphicspath`.
- If `biblatex` is enabled, `biber` must be available in the local TeX environment.
- Registry and preview refresh are outside worker scope and should be done once the PDF builds.

## Final coordinator checklist

1. Inspect all worker outputs under `courses/mesoscopic-clustered-spiking-networks/` and confirm no worker overwrote another worker's files.
2. Copy/adapt the MNS style/build scaffold into the new course root.
3. Create frontmatter and backmatter files.
4. Create or complete all missing chapter and appendix files listed in `chapter-paths.json`.
5. Create `main.tex` with parts and includes in the exact order from `chapter-paths.json`.
6. Normalize notation across chapters, especially cluster index, cluster count, spike-train symbol, and population activity symbol.
7. Resolve citations into `backmatter/references.bib`; keep unresolved claims as TODOs rather than fabricated citations.
8. Insert only existing raster figures, using captions from `figures/figure-metadata.md`.
9. Remove or comment out any figure slots whose raster asset does not exist.
10. Run `make all` from the course root.
11. Fix LaTeX errors and warnings that indicate missing files, missing labels, or broken citations.
12. Confirm `main.pdf` and `mesoscopic-clustered-spiking-networks-lecture-notes.pdf` are created.
13. If registry edits are assigned, add the course entry and validate paths.
14. Run Bodhi preview refresh after manual repo edits:

```bash
cd /Users/arjun/Projects/bodhi
python3 lecture-notes/lecture_notes.py refresh-preview
```

15. If Bodhi workflow code was touched, run:

```bash
cd /Users/arjun/Projects/bodhi
python3 -m unittest discover -s tests -p 'test_lecture_notes.py'
```

16. Final report should include changed files, PDF path, preview/deploy status, validation commands and results, unresolved citation TODOs, unresolved figure TODOs, and suggested next Agent Farm run if the full outline remains uneven.
