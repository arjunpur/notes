# Chapter 11 Figure Metadata

All four figures are ImageGen-generated raster PNG assets for Chapter 11. The intended house style is white background, navy line work, teal mathematical objects, warm gold accents, restrained red highlights, generous whitespace, and labels readable at PDF width. They are referenced from `source/authored-chapters/ch11.tex`.

## Figure 11.1: Measurable Spaces, Measures, and Simple-Function Integration

- Saved path: `imagegen-figures/ch11-measure-space-integration.png`
- Pedagogical purpose: Show that measure theory has three layers: an underlying space, a sigma-algebra of allowed measurable sets, and a measure assigning consistent sizes to those sets; then connect this to integrals built from simple functions.
- Section(s) supported: 11.1 Why measure theory matters.
- Exact mathematical objects shown: A sample space \(\Omega\), measurable sets \(A,C,D\), complements, countable unions, a measure \(\mu\), a null set \(B\) with \(\mu(B)=0\), total mass \(\mu(\Omega)=1\), and a simple-function integral \(\sum_i c_i\mu(A_i)\).
- What the reader should notice first: The set system \(\mathcal{F}\) is separate from both the space \(\Omega\) and the measure \(\mu\).
- Necessary labels: `Omega`, `F`, `allowed sets`, `complements`, `countable unions`, `mu(A)=0.30`, `mu(B)=0`, `mu(Omega)=1`, `null set`, `integral = sum c_i mu(A_i)`.
- How the text references the figure: Section 11.1 uses Figure~\ref{fig:ch11-measure-space-integration} to explain the roles of \(\Omega\), \(\mathcal{F}\), \(\mu\), null sets, and simple-function integration.
- Teaching caption: A measure-theoretic model has three layers: the space \(\Omega\), the allowed measurable sets \(\mathcal{F}\), and a measure \(\mu\) assigning consistent sizes to those sets. Integrals are built by adding function levels over measurable pieces, first for simple functions and then by limits. Null sets have measure zero even when they are not empty.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 11 Measure, Integration, and Change of Variables
Primary request: Create a precise mathematical diagram explaining why measure theory matters: a measurable space, selected measurable sets, assigned sizes, null sets, and integration as adding weighted set pieces.
Scene/backdrop: clean white background, one wide educational diagram with generous whitespace and four connected mini-panels from left to right.
Subject: Panel 1 shows a sample space Omega as a rounded rectangle containing points and regions. Panel 2 shows a sigma-algebra F as a tidy stack of allowed sets, with complements and unions indicated by small set outlines. Panel 3 shows a measure mu assigning sizes to sets, with labels mu(A)=0.30, mu(B)=0, mu(Omega)=1. Panel 4 shows integration as shaded simple-function levels over sets A1, A2, A3 with small bars labeled sum c_i mu(A_i). Include one restrained red thin set labeled null set.
Style/medium: polished educational raster diagram, precise mathematical infographic, no stock-photo realism.
Composition/framing: landscape orientation, four panels aligned horizontally, readable at PDF width, sparse short labels only.
Color palette: white background; navy line work and labels; teal measurable sets; warm gold measure weights and simple-function bars; restrained red for the null set.
Text (verbatim): "Omega", "F", "allowed sets", "complements", "countable unions", "mu(A)=0.30", "mu(B)=0", "mu(Omega)=1", "null set", "integral = sum c_i mu(A_i)".
Constraints: labels must be large and crisp; use only the listed short labels; diagram should teach that not every subset must be measurable and that measure assigns consistent sizes to allowed sets.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealism, stock imagery, external logos, extra equations, clutter.
```

## Figure 11.2: Densities and High-Dimensional Integration

- Saved path: `imagegen-figures/ch11-densities-high-dim-integration.png`
- Pedagogical purpose: Connect density normalization, region probability, marginalization, grid explosion, and Monte Carlo estimation in one visual grammar.
- Section(s) supported: 11.2 Densities and integration in high dimensions.
- Exact mathematical objects shown: A density \(p(x)\), normalization \(\int p(x)\,dx=1\), a region \(R\) with probability \(\int_R p(x)\,dx\), a marginal \(p(x_1)=\int p(x_1,x_2)\,dx_2\), an \(m^d\)-sized grid, and a Monte Carlo estimator \(N^{-1}\sum_i f(X_i)\).
- What the reader should notice first: Probability comes from integrating density over a region, not from evaluating density at a point.
- Necessary labels: `p(x) >= 0`, `integral p(x) dx = 1`, `R`, `integral_R p(x) dx`, `marginal p(x_1)`, `integral p(x_1,x_2) dx_2`, `m^d grid points`, `Monte Carlo`, `1/N sum f(X_i)`.
- How the text references the figure: Section 11.2 uses Figure~\ref{fig:ch11-densities-high-dim-integration} to explain densities, marginals, the curse of dimensionality for grids, and sample-average integration.
- Teaching caption: A density assigns probability per unit volume. Region probabilities are integrals under the density, marginal densities are obtained by integrating out coordinates, and high-dimensional grid integration grows like \(m^d\). Monte Carlo replaces a full grid by random samples and estimates expectations with sample averages.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 11 Measure, Integration, and Change of Variables
Primary request: Create a precise mathematical diagram for densities and integration in high dimensions: normalized density, marginalization, Monte Carlo samples, and why grids fail as dimension grows.
Scene/backdrop: clean white background, one wide diagram with three coordinated panels and generous whitespace.
Subject: Left panel: smooth 2D density contours p(x1,x2) with shaded probability region R and label integral_R p(x) dx. Middle panel: marginalization, a 2D density projected down to a one-dimensional curve p(x1)=integral p(x1,x2) dx2. Right panel: high-dimensional integration comparison: a sparse regular grid with label m^d grid points beside random Monte Carlo dots with label average f(X_i), plus a small cube expanding into many cells.
Style/medium: polished educational raster diagram, precise mathematical infographic, no stock-photo realism.
Composition/framing: landscape orientation, three panels aligned horizontally, readable at PDF width, sparse short labels only.
Color palette: white background; navy line work and labels; teal density contours and samples; warm gold shaded probability mass; restrained red for grid explosion warning.
Text (verbatim): "p(x) >= 0", "integral p(x) dx = 1", "R", "integral_R p(x) dx", "marginal p(x_1)", "integral p(x_1,x_2) dx_2", "m^d grid points", "Monte Carlo", "1/N sum f(X_i)".
Constraints: labels must be large and crisp; use only the listed short labels; show density as probability per unit volume, not as probability at a point; show Monte Carlo samples as dots under the density.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealism, stock imagery, external logos, extra unrelated equations, clutter.
```

## Figure 11.3: Change of Variables and Jacobian Volume Scaling

- Saved path: `imagegen-figures/ch11-change-of-variables-jacobian.png`
- Pedagogical purpose: Make the density transformation formula visible as conservation of probability mass under local volume scaling.
- Section(s) supported: 11.3 Change of variables.
- Exact mathematical objects shown: Input coordinates \(x_1,x_2\), output coordinates \(y_1,y_2\), an invertible map \(y=T(x)\), the Jacobian matrix \(J_T(x)\), determinant scale \(|\det J_T(x)|\), input density \(p_X(x)\), output density \(p_Y(y)=p_X(x)/|\det J_T(x)|\), and corresponding small volume elements.
- What the reader should notice first: The same small probability mass occupies a transformed cell whose volume changes by the Jacobian determinant.
- Necessary labels: `x-space`, `y-space`, `x`, `y=T(x)`, `J_T(x)`, `|det J_T(x)|`, `p_X(x)`, `p_Y(y)=p_X(x)/|det J_T(x)|`, `mass preserved`.
- How the text references the figure: Section 11.3 uses Figure~\ref{fig:ch11-change-of-variables-jacobian} to explain the local cell argument for the density formula.
- Teaching caption: Under an invertible transformation \(y=T(x)\), a small input volume near \(x\) becomes a transformed volume near \(y\). The Jacobian determinant \(|\det J_T(x)|\) gives the local volume scale. Density changes inversely so that probability mass is preserved.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 11 Measure, Integration, and Change of Variables
Primary request: Create a precise mathematical diagram for the change-of-variables formula, showing a small region transformed by an invertible map and scaled by the Jacobian determinant.
Scene/backdrop: clean white background, one wide diagram with left input space, center mapping arrow with Jacobian matrix, and right output space.
Subject: Left panel: x-space with a small teal square/parallelogram around x, coordinate axes x1 and x2, and a density label p_X(x). Center: curved arrow labeled y=T(x), with a small matrix label J_T(x) and volume scale |det J_T(x)|. Right panel: y-space with the transformed warm gold parallelogram/curved cell around y, axes y1 and y2, and density label p_Y(y)=p_X(x)/|det J_T(x)|. Include one highlighted unit square that becomes a stretched tilted cell.
Style/medium: polished educational raster diagram, precise linear algebra geometry, no stock-photo realism.
Composition/framing: landscape orientation, left-to-right mapping, readable at PDF width, sparse short labels only.
Color palette: white background; navy line work and labels; teal input region; warm gold output region and mapping arrow; restrained red for the determinant scaling annotation.
Text (verbatim): "x-space", "y-space", "x", "y=T(x)", "J_T(x)", "|det J_T(x)|", "p_X(x)", "p_Y(y)=p_X(x)/|det J_T(x)|", "mass preserved".
Constraints: labels must be large and crisp; show the same probability mass before and after transformation; make the output cell visibly stretched/rotated compared with the input cell; avoid suggesting non-invertible folding.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealism, stock imagery, external logos, extra unrelated equations, clutter.
```

## Figure 11.4: Delta Functions and Generalized Functions

- Saved path: `imagegen-figures/ch11-delta-generalized-functions.png`
- Pedagogical purpose: Show the Dirac delta through its action on test functions, as a limit of narrow unit-area bumps, and as an impulse that shifts a convolution kernel.
- Section(s) supported: 11.4 Delta functions and generalized functions.
- Exact mathematical objects shown: A test function \(\varphi(x)\), a point \(x=a\), a delta \(\delta_a\), the action \(\int\delta(x-a)\varphi(x)\,dx=\varphi(a)\), narrow Gaussian approximations with area \(1\), spike impulses \(\delta(t-t_i)\), a kernel \(h(t)\), and the convolution identity \(h*\delta_a=h(t-a)\).
- What the reader should notice first: The delta is defined by what it does to a test function, not as an ordinary finite-height function.
- Necessary labels: `test function phi`, `x=a`, `delta_a`, `integral delta(x-a) phi(x) dx = phi(a)`, `narrow Gaussians`, `area = 1`, `delta(t-t_i)`, `h(t)`, `h * delta_a = h(t-a)`.
- How the text references the figure: Section 11.4 uses Figure~\ref{fig:ch11-delta-generalized-functions} to explain the test-function rule, narrow-Gaussian intuition, and spike-train convolution.
- Teaching caption: The Dirac delta acts on a test function by evaluation: \(\int \delta(x-a)\varphi(x)\,dx=\varphi(a)\). It can be approached by narrow unit-area bumps, and in signal models it represents an ideal impulse whose convolution with a kernel shifts the kernel to the impulse time.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 11 Measure, Integration, and Change of Variables
Primary request: Create a precise mathematical diagram for delta functions and generalized functions: the Dirac delta as an action on test functions, a limit of narrow Gaussians, and a point mass / impulse response.
Scene/backdrop: clean white background, one wide educational diagram with three panels and generous whitespace.
Subject: Left panel: a smooth test function phi(x) curve in teal and a vertical warm-gold spike at x=a labeled delta_a, with annotation integral delta(x-a) phi(x) dx = phi(a). Middle panel: three increasingly narrow Gaussian bumps centered at a, each area 1, converging to a tall spike; include label area=1. Right panel: signal processing / spike train panel showing impulses at times t1,t2,t3 feeding a convolution kernel h(t), with output response curve, labels delta(t-t_i), h(t), h * delta_a = h(t-a).
Style/medium: polished educational raster diagram, precise mathematical infographic, no stock-photo realism.
Composition/framing: landscape orientation, three panels aligned horizontally, readable at PDF width, sparse short labels only.
Color palette: white background; navy axes and labels; teal test function and response curves; warm gold delta spikes and Gaussian bumps; restrained red for the evaluation point a.
Text (verbatim): "test function phi", "x=a", "delta_a", "integral delta(x-a) phi(x) dx = phi(a)", "narrow Gaussians", "area = 1", "delta(t-t_i)", "h(t)", "h * delta_a = h(t-a)".
Constraints: labels must be large and crisp; make clear that delta is not an ordinary finite-height function; show area staying equal to 1 as bumps narrow; keep the impulse response panel simple.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealism, stock imagery, external logos, extra unrelated equations, clutter.
```
