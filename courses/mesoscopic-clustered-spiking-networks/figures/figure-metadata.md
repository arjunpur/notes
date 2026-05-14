# Figure Metadata: Mesoscopic Theory of Clustered Spiking Networks

All assets in this directory were generated with the built-in Codex `image_gen`
workflow on 2026-05-13, then copied into this course-local `figures/`
directory. The originals remain under `/Users/arjun/.codex/generated_images/`.

Design constraints used throughout:

- Raster PNG assets only; no SVG, TikZ, Mermaid, matplotlib, canvas, or other
  programmatic fallback figures.
- One visual claim per figure.
- Sparse labels only; captions and LaTeX should carry exact equations,
  derivations, and dense definitions.
- Intended use is `\includegraphics[width=0.95\textwidth]{figures/<filename>}`
  unless a narrower width is noted.

## Figure: `meso-variability-decomposition.png`

- Target chapter: Chapter 1, "What are we trying to explain?" Secondary fit:
  Chapter 17 and Chapter 20.
- Visual claim: Spike-count variability can come from both fast irregular
  spiking and slow shared rate fluctuations; stimulus onset can quench the slow
  component without making spikes regular.
- Caption: Trial-to-trial variability has more than one source. Fast irregular
  spike timing affects CV-like measures, while slow trial-level rate envelopes
  inflate spike-count variability and Fano factor. A stimulus can reduce the
  slow envelope, producing variability quenching even when spikes remain
  irregular.
- Status: generated.
- Notes for LaTeX sizing: Use full-width placement, preferably
  `width=0.95\textwidth`. The labels are large enough for page-width display.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic diagram titled only with sparse labels, explaining variability decomposition in cortical spike counts.
Style: white background, navy line work, teal and warm-gold accents, restrained red highlights, minimal surface style matching mathematical lecture notes, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: Three aligned mini-panels from left to right. Left: several horizontal trial rasters with irregular spike ticks; a translucent vertical count window. Middle: the same trials summarized as a slow teal rate envelope plus fast individual spike ticks, visually separating slow rate fluctuations from fast irregular spiking. Right: before/after stimulus onset, the slow envelope narrows after a vertical stimulus marker while spike ticks remain irregular.
Visual claim: spike-count variability can come from both fast irregular spiking and slow shared rate fluctuations; stimulus onset can quench the slow component without making spikes regular.
Necessary labels, exact text only: trials, count window, fast spikes, slow rate, stimulus, quench, FF, CV. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```

## Figure: `meso-lkdoiron-clustered-balanced-network.png`

- Target chapter: Chapter 2, "The Litwin-Kumar & Doiron baseline." Secondary
  fit: Chapter 5 and Chapter 10.
- Visual claim: Strengthened within-cluster excitation creates cluster up/down
  states on top of an inhibitory balanced background.
- Caption: The clustered balanced network keeps the E/I background but makes
  recurrent excitation stronger inside excitatory clusters than between them.
  This creates cluster-level up and down states: active clusters can persist for
  a while, then switch as finite-size fluctuations and inhibition reshape the
  effective input.
- Status: generated.
- Notes for LaTeX sizing: Use `width=0.95\textwidth` or `width=\textwidth`.
  The figure includes a small `time` axis label not listed in the prompt; it is
  visually consistent with the activity strip.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic diagram of the Litwin-Kumar and Doiron clustered balanced network mechanism.
Style: white background, navy line work, teal excitatory clusters, warm-gold inhibitory pool, restrained red highlights for active clusters, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: Two balanced panels. Left panel: a network schematic with several excitatory clusters as teal circles of small nodes; thick curved links inside each cluster labeled strong within; faint links between clusters labeled weak between; one shared inhibitory population in warm gold labeled I pool with broad feedback arrows to all clusters. Right panel: a simple cluster activity strip over time with rows for clusters; two rows enter red up bands while others stay pale down bands, with occasional switching arrows.
Visual claim: strengthened within-cluster excitation creates cluster up/down states on top of an inhibitory balanced background.
Necessary labels, exact text only: E clusters, I pool, strong within, weak between, up, down, switch, activity. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```

## Figure: `meso-ei-balance-cancellation.png`

- Target chapter: Chapter 4, "Balanced networks."
- Visual claim: Balanced networks can have large excitation and inhibition
  while the neuron sees a small fluctuating net drive that produces irregular
  spikes.
- Caption: Balance is a cancellation statement, not a statement that inputs are
  small. Large excitatory and inhibitory currents track one another, leaving a
  much smaller fluctuating net input. That residual fluctuation can push the
  membrane trace across threshold irregularly, giving asynchronous irregular
  spiking without slow cluster metastability by itself.
- Status: generated.
- Notes for LaTeX sizing: Use `width=0.95\textwidth`. This is a good early
  mechanistic plate before formal balance equations.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic diagram explaining excitation-inhibition balance as cancellation of large inputs.
Style: white background, navy line work, teal excitation, warm gold inhibition, restrained red net fluctuation and spikes, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: Left side: many teal excitatory arrows and many warm-gold inhibitory arrows converging onto a simple neuron icon, with both input groups visibly large. Center: stacked time traces, teal excitation above, gold inhibition below, and a small red net trace between them near zero. Right: membrane potential trace hovering below a dashed threshold with irregular red spike marks when fluctuations cross threshold.
Visual claim: balanced networks can have large excitation and inhibition while the neuron sees a small fluctuating net drive that produces irregular spikes.
Necessary labels, exact text only: excitation, inhibition, cancellation, net input, threshold, spikes, balance. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```

## Figure: `meso-refractory-density-flow.png`

- Target chapter: Chapter 8, "Refractory-density and age-structured population
  methods."
- Visual claim: A mesoscopic population can be described by the distribution of
  time since last spike; hazard removes neurons from older ages and returns them
  to age zero as population activity.
- Caption: Refractory-density theory replaces neuron identities by an age
  density over time since last spike. Probability mass drifts to larger ages,
  while the hazard selects part of the density to spike. Those spikes re-enter
  at age zero, and the reset flux is the population activity.
- Status: generated.
- Notes for LaTeX sizing: Use `width=0.95\textwidth`. The lower activity ticks
  are schematic; keep exact renewal equations in LaTeX near the figure.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic diagram explaining refractory-density and age-structured population flow.
Style: white background, navy line work, teal density, warm-gold reset flux, restrained red hazard region, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: One large horizontal axis labeled age. Draw a smooth teal density curve flowing to the right with several small arrows labeled drift. Near the young-age end, show a warm-gold reset bucket or boundary at age zero labeled reset. Along the curve, highlight a red hazard gate where some density leaves the age axis and loops back to reset. Above or below, include a small population activity meter made of sparse vertical ticks receiving the reset flux.
Visual claim: a mesoscopic population can be described by the distribution of time since last spike; hazard removes neurons from older ages and returns them to age zero as population activity.
Necessary labels, exact text only: age, density, drift, hazard, reset, activity, last spike. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```

## Figure: `meso-noise-escape-vs-chaos.png`

- Target chapter: Chapter 12, "The main theory question: multistability or
  mesoscopic chaos?" Secondary fit: Chapter 9 and Chapter 23.
- Visual claim: Finite-size escape should weaken as population size grows,
  whereas deterministic mesoscopic chaos should persist and show sensitivity to
  small perturbations.
- Caption: Noise-driven metastability and mesoscopic chaos make different
  finite-size predictions. If switching is escape over a barrier, increasing
  population size suppresses the fluctuations that drive transitions. If the
  mesoscopic equations are chaotic, irregular wandering and perturbation
  sensitivity can remain in the large-population limit.
- Status: generated.
- Notes for LaTeX sizing: Use full width. The figure is conceptually dense, so
  place it after text has introduced the finite-size scaling question.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic comparison diagram for noise-driven metastable switching versus deterministic mesoscopic chaos.
Style: white background, navy line work, teal stable basins, warm-gold trajectories, restrained red perturbation/noise marks, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: Two side-by-side panels. Left panel: a simple landscape with two teal basins and a barrier; a noisy warm-gold trajectory crosses the barrier only for small N, while a smoother larger-N trajectory remains trapped. Right panel: a phase-space sketch with a folded warm-gold trajectory that keeps wandering inside a bounded region even as N increases; show two nearby red initial points separating. Add a tiny autocorrelation strip under each panel: left strip becomes slower and rarer with larger N; right strip remains irregular.
Visual claim: finite-size escape should weaken as population size grows, whereas deterministic mesoscopic chaos should persist and show sensitivity to small perturbations.
Necessary labels, exact text only: noise escape, small N, large N, barrier, chaos persists, perturb, sensitivity, autocorrelation. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```

## Figure: `meso-rostami-paired-ei-clusters.png`

- Target chapter: Chapter 13, "Spiking attractor model of motor cortex."
  Secondary fit: Chapter 11 and Chapter 14.
- Visual claim: Pairing excitatory and inhibitory clusters creates local
  balance inside each attractor state, making clustered metastability more
  robust to task inputs.
- Caption: E/I clustered attractor models pair each excitatory cluster with a
  structured inhibitory partner. Local feedback can preserve balance inside an
  active state while competition separates candidate attractors. A cue tilts the
  landscape toward one basin without requiring the network to become globally
  regular.
- Status: generated.
- Notes for LaTeX sizing: Use `width=0.95\textwidth`. The repeated "local
  balance" labels are legible; avoid placing this figure too close to another
  label-heavy schematic.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic diagram of Rostami-style paired excitatory-inhibitory clusters in a spiking attractor network.
Style: white background, navy line work, teal excitatory populations, warm-gold inhibitory populations, restrained red active attractor, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: Left panel: four paired cluster modules arranged in a ring; each module contains a teal E cluster and a warm-gold I cluster joined by a local feedback loop. Within each pair, show thick reciprocal arrows labeled local balance. Between modules, show faint competitive arrows. Right panel: a low-dimensional attractor landscape with several basins corresponding to possible targets; one basin is red active and deeper, neighboring basins are pale; a stimulus cue arrow tilts the landscape toward the active basin.
Visual claim: pairing excitatory and inhibitory clusters creates local balance inside each attractor state, making clustered metastability more robust to task inputs.
Necessary labels, exact text only: paired E/I, E, I, local balance, competition, cue, active attractor, robust. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```

## Figure: `meso-phase-diagram-roadmap.png`

- Target chapter: Chapter 23, "Phase diagrams and theory deliverables."
  Secondary fit: Chapter 24 and the course introduction.
- Visual claim: The rotation can be organized as phase-diagram work: sweep
  cluster strengths and size, then classify regimes by microscopic and
  mesoscopic observables.
- Caption: A useful theory artifact is a regime map. Sweeping excitatory and
  inhibitory cluster strength can separate asynchronous, bistable, metastable,
  and chaotic regions. Repeating the sweep across network size tests whether
  observed switching is finite-size noise, deterministic mesoscopic structure,
  or a mixture of both.
- Status: generated.
- Notes for LaTeX sizing: Use `width=0.95\textwidth`. The right-side `N` strip
  is a qualitative finite-size sweep marker; let the caption or nearby prose say
  explicitly that finite-size noise fades as population size increases. The
  bottom row is useful for the practical-project chapters; omit nearby bullet
  duplication in prose.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic phase-diagram roadmap for mesoscopic clustered spiking networks.
Style: white background, navy axes, teal stable regions, warm-gold metastable region, restrained red chaotic/unstable region, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: Main panel: a two-dimensional phase diagram with horizontal axis labeled E cluster strength and vertical axis labeled I cluster strength. Use broad softly separated regions labeled async, bistable, metastable, chaotic. Overlay a navy sweep path with a few dots. Add a small side strip indicating network size N increasing, with finite-size noise fading as N grows. Add a small checklist-like row of three icon labels at the bottom: reproduce, reduce, compare.
Visual claim: the rotation can be organized as phase-diagram work: sweep cluster strengths and size, then classify regimes by microscopic and mesoscopic observables.
Necessary labels, exact text only: E cluster strength, I cluster strength, async, bistable, metastable, chaotic, N, finite-size noise, reproduce, reduce, compare. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```

## Figure: `meso-micro-to-meso-reduction.png`

- Target chapter: Chapter 6, "Why mesoscopic theory?" Secondary fit: Chapter 7
  and Chapter 10.
- Visual claim: Mesoscopic theory keeps population activity variables for
  clusters while replacing individual spike identities by finite-size
  fluctuations.
- Caption: The mesoscopic reduction changes the unit of description. Instead
  of tracking every neuron and spike identity, it groups neurons into cluster
  populations and follows activity variables such as `A1`, `A2`, and `A3`.
  Finite-size noise records the residual variability that remains because each
  population contains finitely many neurons.
- Status: generated.
- Notes for LaTeX sizing: Use `width=0.95\textwidth`. This is the clearest
  opening figure for the mesoscopic-theory part before transfer functions or
  self-consistency equations.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide 16:9 plate readable at full page width
Primary request: Create a clean academic diagram explaining mesoscopic reduction from microscopic spiking neurons to cluster population variables.
Style: white background, navy line work, teal population variables, warm-gold microscopic spikes, restrained red finite-size fluctuations, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text.
Composition: Left panel: many small neuron dots with sparse spike rasters below, labeled microscopic spikes. Middle panel: a grouping bracket collecting neurons into three clusters; each cluster has a smoothed teal activity trace. Right panel: a compact mesoscopic state space with three coordinates or bars labeled A1, A2, A3, plus small red fluctuation bands labeled finite-size noise.
Visual claim: mesoscopic theory keeps population activity variables for clusters while replacing individual spike identities by finite-size fluctuations.
Necessary labels, exact text only: microscopic spikes, cluster populations, activity, A1, A2, A3, finite-size noise, mesoscopic state. Keep labels large and sparse. Do not include equations, derivations, paragraphs, tiny text, legends, or extra symbols.
```
