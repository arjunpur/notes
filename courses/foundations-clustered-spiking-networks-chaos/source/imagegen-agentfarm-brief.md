# Agentfarm Brief: Codex Imagegen Diagram Regeneration

Target course root:
`/Users/arjun/repos/lecture-notes/courses/foundations-clustered-spiking-networks-chaos`

User intent:
Regenerate the course diagrams using the Codex imagegen/GPT image model workflow rather than deterministic SVG, PDF drawing, or PIL-only diagram rendering. The diagrams must explain the material, not decorate it. The final coordinator outside Agentfarm will call the built-in Codex `image_gen` tool, integrate the selected assets into LaTeX, rebuild the PDF, and deploy the Lecture Notes Service.

Agentfarm deliverable:
Create reviewed imagegen prompt/spec files only. Do not generate images, do not edit `chapters/`, do not edit `figures/`, do not edit `main.tex`, do not run LaTeX, and do not deploy.

Required output directory:
`source/imagegen_prompts/`

Required files and write scopes:
- Worker A writes only `source/imagegen_prompts/ch01-02.md`
- Worker B writes only `source/imagegen_prompts/ch03-04.md`
- Worker C writes only `source/imagegen_prompts/ch05-06.md`
- Worker D writes only `source/imagegen_prompts/ch07-08.md`
- Worker E writes only `source/imagegen_prompts/ch09-10.md`
- Final coordinator writes only `source/imagegen_prompts/catalog.md` and `source/imagegen_prompts/catalog.json`

Forbidden scopes for every worker:
- `figures/`
- `chapters/`
- `build/`
- `main.tex`
- `final-report.md`
- `source/structure.json`
- `source/render_image_diagrams.py`

Context to read:
- `source/structure.json`
- `figures/figure-metadata.md`
- The relevant chapter `.tex` files for each worker's chapter range
- `source/roadmap-coverage.md` when a concept is ambiguous

Prompt quality requirements:
- Use case must be `scientific-educational`.
- Asset type must be `lecture-note raster infographic`.
- Request 16:10 horizontal composition suitable for a PDF figure.
- Ask for clean, modern, textbook-quality diagrams with generous whitespace, high contrast, no watermark, no logos, no decorative stock imagery.
- Keep in-image text sparse because image models can distort text. Use at most 3 to 6 short labels per diagram. Put exact equations and detailed explanations in the LaTeX captions or surrounding notes, not inside the generated image.
- Where exact labels matter, specify simple label tokens only, such as `E`, `I`, `J_E+`, `J_I+`, `xi`, `kappa`, `C(tau)`, `lambda`.
- Include a separate `caption_intent` for each diagram that can be used later in LaTeX.
- Include an `overlay_suggestion` field for exact labels or equations that should be added after image generation if the generated text is unreliable.
- Favor conceptual clarity: arrows, basins, state-space paths, matrix blocks, traces, phase diagrams, and diagnostic comparisons.
- Avoid pretending the diagrams are measured data. Mark them as schematic or conceptual in the prompt when appropriate.

Required diagram set:
Regenerate all 22 existing chapter figures, and add at least 8 new diagrams where they help the lecture notes build incrementally. Use these canonical asset ids unless a reviewer identifies a stronger replacement.

Chapter 1:
- `ch01-jacobian-eigenvalues-img`
- `ch01-attractor-landscape-img`
- New: `ch01-lyapunov-stretch-fold-img`

Chapter 2:
- `ch02-spike-filtering-img`
- `ch02-noise-scaling-img`
- New: `ch02-autocorrelation-signatures-img`

Chapter 3:
- `ch03-lif-threshold-reset-img`
- `ch03-transfer-function-img`
- New: `ch03-gif-adaptation-img`

Chapter 4:
- `ch04-balance-cancellation-img`
- `ch04-sparse-fixed-indegree-img`
- New: `ch04-inhibition-stabilized-loop-img`

Chapter 5:
- `ch05-clustered-connectivity-matrix-img`
- `ch05-active-inactive-landscape-img`
- New: `ch05-size-dependent-switching-img`

Chapter 6:
- `ch06-random-rate-phase-portrait-img`
- `ch06-scs-autocorrelation-transition-img`
- New: `ch06-chaotic-flow-folding-img`

Chapter 7:
- `ch07-quenched-vs-annealed-disorder-img`
- `ch07-dmft-self-consistency-loop-img`
- New: `ch07-static-dynamic-mean-field-split-img`

Chapter 8:
- `ch08-paired-ei-clusters-img`
- `ch08-quenched-amplification-img`
- New: `ch08-cluster-rate-unit-img`

Chapter 9:
- `ch09-xi-kappa-plane-img`
- `ch09-perturbation-divergence-img`
- `ch09-autocorrelation-kink-img`
- `ch09-regimes-abc-variance-img`

Chapter 10:
- `ch10-phase-diagram-dashboard-img`
- `ch10-observable-dashboard-img`
- New: `ch10-research-workflow-img`

Per-diagram output format:

```markdown
### <asset_id>

filename: `figures/imagegen/<asset_id>.png`
chapter: <number>
placement_target: <existing section or nearby subsection>
status: replace-existing | new
caption_intent: <one concise paragraph>
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: ...
Composition: ...
Required visual elements: ...
Sparse in-image labels: ...
Style: ...
Avoid: ...
"""
overlay_suggestion: <exact labels/equations to add after generation if needed, or "none">
review_notes: <known failure modes to check>
```

Final coordinator requirements:
- Merge the five worker files into `source/imagegen_prompts/catalog.md`.
- Create `source/imagegen_prompts/catalog.json` as an array of objects with fields:
  `asset_id`, `filename`, `chapter`, `placement_target`, `status`, `caption_intent`, `imagegen_prompt`, `overlay_suggestion`, `review_notes`.
- Confirm there are at least 30 diagrams total.
- Confirm every existing 22 figure concepts has a replacement prompt.
- Do not edit anything outside `source/imagegen_prompts/`.
