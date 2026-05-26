# Chapter 19 Figure Metadata

## `ch19-scm-graph-surgery.png`

- Pedagogical purpose: Show the difference between observation and intervention in a structural causal model.
- Section(s) supported: 19.1 Correlation, causation, and structural models.
- Proposed ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic. Create a 16:10 horizontal composition for a PDF showing a causal DAG with confounder Z pointing to X and Y, and X pointing to Y. Left panel labeled observation keeps all arrows and contrasts P(Y|X). Right panel labeled intervention cuts the arrow into X and shows X set externally, contrasting P(Y|do(X)). Use sparse in-image labels only: Z, X, Y, observation, intervention, cut incoming arrows. Put exact equations in the caption, not in the image text. Use clean white background, navy graph lines, teal variables, restrained red cut mark. No logos, no watermarks, no decorative stock imagery, no pseudo-data presented as real data."

## `ch19-front-door-mediator.png`

- Pedagogical purpose: Visualize front-door identification through a measured mediator with unobserved confounding between treatment and outcome.
- Section(s) supported: 19.2 Do-calculus intuition.
- Proposed ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic. Create a 16:10 horizontal PDF composition showing a DAG with unobserved U pointing to X and Y, observed path X to M to Y, and no direct X to Y arrow. Include a two-step flow: effect of X on M, then adjusted effect of M on Y. Sparse labels only: U hidden, X, M, Y, mediator, adjust over X. Exact front-door formula should appear in the caption, not in the image. Clean flat mathematical style, white background, navy arrows, teal observed nodes, muted gray hidden node, warm gold mediator. No logos, watermarks, stock imagery, or fake empirical data."

## `ch19-randomized-neural-intervention.png`

- Pedagogical purpose: Explain random assignment, treatment/control groups, and neural intervention controls.
- Section(s) supported: 19.3 Randomized experiments and neural interventions.
- Proposed ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic. Create a 16:10 horizontal PDF composition showing experimental units randomly split by a coin-like randomizer into stimulation and sham/control groups, then measured on a behavioral outcome. Include a small neural-circuit icon for the intervention target and a separate sham-control path. Sparse labels only: random assignment, stimulation, sham, outcome, blocked by condition. Equations for ATE and standard error should be in the caption, not image text. Clean white background, navy lines, teal treatment, warm gold control, restrained red warning marker for off-target effects. No logos, watermarks, decorative stock imagery, or pseudo-data."

## `ch19-causal-representation-shift.png`

- Pedagogical purpose: Contrast causal features with spurious predictive features across environments.
- Section(s) supported: 19.4 Causal representation learning preview.
- Proposed ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic. Create a 16:10 horizontal composition for PDF showing observations X generated from causal factor C and nuisance/spurious factor S across two environments. Show a representation map phi(X) splitting into stable causal feature and unstable shortcut feature. Sparse labels only: environment 1, environment 2, causal feature, shortcut, stable, shifts. Put any probabilities or invariance equations in the caption, not the image. Use flat clean style, white background, navy arrows, teal stable feature, warm gold shortcut, restrained red shift indicator. No logos, watermarks, stock imagery, or pseudo-data presented as real data."
