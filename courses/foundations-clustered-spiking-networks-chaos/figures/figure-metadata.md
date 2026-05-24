# Figure Metadata

This course now uses 31 Codex imagegen / GPT-image-model raster teaching
diagrams under `figures/imagegen/`. The earlier deterministic raster diagrams
remain in `figures/` for provenance only; the chapter TeX and
`source/structure.json` point to `figures/imagegen/...`.

The reviewed prompt catalog was produced by Agentfarm run
`agentfarm-brief-codex-imagegen-diagram-regen-20260518-122330` and is stored in
`source/imagegen_prompts/catalog.json` and `source/imagegen_prompts/catalog.md`.
Each final image has a sibling `.source.txt` file recording the original Codex
generated-image cache path. The images were normalized after generation to a
common 2400 by 1500 PNG canvas for consistent PDF rendering. The QA contact
sheet is `source/imagegen_prompts/imagegen-contact-sheet.png`.

No source-roadmap figures, previous lecture-note figures, SVG diagrams, or
PIL-only deterministic diagrams are referenced by the final PDF figure blocks.

## Chapter 1

- `figures/imagegen/ch01-jacobian-eigenvalues-img.png`
  - Role: replace existing Jacobian-spectrum stability figure.
  - Caption intent: local stability near a fixed point is read from the Jacobian eigenvalues.
- `figures/imagegen/ch01-attractor-landscape-img.png`
  - Role: replace existing attractor-basin figure.
  - Caption intent: small perturbations return inside a basin, while large perturbations can cross a boundary.
- `figures/imagegen/ch01-lyapunov-stretch-fold-img.png`
  - Role: new figure.
  - Caption intent: nearby trajectories stretch, fold, and separate before saturation in a bounded chaotic flow.

## Chapter 2

- `figures/imagegen/ch02-spike-filtering-img.png`
  - Role: replace existing spike-filtering figure.
  - Caption intent: point-process spikes become continuous filtered activity and then mesoscopic population variables.
- `figures/imagegen/ch02-autocorrelation-signatures-img.png`
  - Role: new figure.
  - Caption intent: compare spike, filtered-shot-noise, and smooth-rate autocorrelation signatures.
- `figures/imagegen/ch02-noise-scaling-img.png`
  - Role: replace existing finite-size scaling figure.
  - Caption intent: finite-size fluctuations shrink like `1/sqrt(N_E)`.

## Chapter 3

- `figures/imagegen/ch03-lif-threshold-reset-img.png`
  - Role: replace existing LIF threshold-reset figure.
  - Caption intent: continuous voltage dynamics produce discrete spike events through threshold and reset.
- `figures/imagegen/ch03-transfer-function-img.png`
  - Role: replace existing transfer-function figure.
  - Caption intent: input statistics map to expected firing rate, with noise and adaptation changing gain.
- `figures/imagegen/ch03-gif-adaptation-img.png`
  - Role: new figure.
  - Caption intent: GIF history variables raise adaptation current and dynamic threshold after spikes.

## Chapter 4

- `figures/imagegen/ch04-balance-cancellation-img.png`
  - Role: replace existing balance figure.
  - Caption intent: large excitatory and inhibitory currents nearly cancel, exposing residual fluctuations.
- `figures/imagegen/ch04-sparse-fixed-indegree-img.png`
  - Role: replace existing fixed-in-degree figure.
  - Caption intent: selected source identities are random but source counts are controlled.
- `figures/imagegen/ch04-inhibition-stabilized-loop-img.png`
  - Role: new figure.
  - Caption intent: inhibitory feedback stabilizes an excitatory loop that would be unstable alone.

## Chapter 5

- `figures/imagegen/ch05-clustered-connectivity-matrix-img.png`
  - Role: replace existing clustered-connectivity figure.
  - Caption intent: potentiated diagonal EE blocks and depressed off-diagonal EE blocks define assemblies.
- `figures/imagegen/ch05-active-inactive-landscape-img.png`
  - Role: replace existing active/inactive basin figure.
  - Caption intent: active-cluster states are metastable basins with finite-size fluctuation-driven hops.
- `figures/imagegen/ch05-size-dependent-switching-img.png`
  - Role: new figure.
  - Caption intent: smaller clusters switch more often because their finite-size fluctuation scale is larger.

## Chapter 6

- `figures/imagegen/ch06-random-rate-phase-portrait-img.png`
  - Role: replace existing SCS phase-portrait figure.
  - Caption intent: subcritical rate dynamics contract, while supercritical dynamics stretch, fold, and remain bounded.
- `figures/imagegen/ch06-scs-autocorrelation-transition-img.png`
  - Role: replace existing SCS autocorrelation figure.
  - Caption intent: correlations broaden near criticality and become smooth in the chaotic rate regime.
- `figures/imagegen/ch06-chaotic-flow-folding-img.png`
  - Role: new figure.
  - Caption intent: Lyapunov growth comes from local divergence plus nonlinear global confinement.

## Chapter 7

- `figures/imagegen/ch07-quenched-vs-annealed-disorder-img.png`
  - Role: replace existing quenched/annealed disorder figure.
  - Caption intent: quenched disorder is a fixed vector-field feature, while annealed disorder is redrawn.
- `figures/imagegen/ch07-static-dynamic-mean-field-split-img.png`
  - Role: new figure.
  - Caption intent: separate static mean/bias terms from connected dynamic DMFT fluctuations.
- `figures/imagegen/ch07-dmft-self-consistency-loop-img.png`
  - Role: replace existing DMFT loop figure.
  - Caption intent: the effective unit must reproduce the mean and autocorrelation statistics used to drive it.

## Chapter 8

- `figures/imagegen/ch08-paired-ei-clusters-img.png`
  - Role: replace existing paired-cluster figure.
  - Caption intent: paired E/I clusters are two-population mesoscale units with structured intra-pair and depressed inter-pair couplings.
- `figures/imagegen/ch08-cluster-rate-unit-img.png`
  - Role: new figure.
  - Caption intent: E and I spike trains are averaged and filtered into a two-dimensional cluster-rate variable.
- `figures/imagegen/ch08-quenched-amplification-img.png`
  - Role: replace existing quenched-variance amplification figure.
  - Caption intent: inhibitory heterogeneity can dominate variance because squared inhibitory coupling magnitudes are large.

## Chapter 9

- `figures/imagegen/ch09-xi-kappa-plane-img.png`
  - Role: replace existing diagnostic plane figure.
  - Caption intent: organize finite-size switching and quenched-disorder chaos in the `xi`-`kappa` plane.
- `figures/imagegen/ch09-perturbation-divergence-img.png`
  - Role: replace existing perturbation figure.
  - Caption intent: perturbations recover inside a basin but grow exponentially in chaotic mesoscale flow.
- `figures/imagegen/ch09-autocorrelation-kink-img.png`
  - Role: replace existing autocorrelation-kink figure.
  - Caption intent: finite-size noise gives a cusp, while deterministic chaotic rates are smooth at zero lag.
- `figures/imagegen/ch09-regimes-abc-variance-img.png`
  - Role: replace existing A/B/C scaling figure.
  - Caption intent: separate finite-size variance, quenched variance, and the many-unit DMFT limit.

## Chapter 10

- `figures/imagegen/ch10-phase-diagram-dashboard-img.png`
  - Role: replace existing phase-diagram figure.
  - Caption intent: classify dynamic regimes over cluster strength and heterogeneity.
- `figures/imagegen/ch10-observable-dashboard-img.png`
  - Role: replace existing observable dashboard figure.
  - Caption intent: combine timescales, state statistics, variability, dimensionality, and instability.
- `figures/imagegen/ch10-research-workflow-img.png`
  - Role: new figure.
  - Caption intent: show the loop from model choice to simulation, diagnostics, scaling, theory comparison, and interpretation.
