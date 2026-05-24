# Chapter 16 Figure Metadata

## Figure 16.1: LLN and CLT Sample Means

Saved path: `imagegen-figures/ch16-lln-clt-sample-means.png`

Pedagogical purpose: Show that the law of large numbers and central limit theorem describe two complementary features of repeated sampling: stabilization of the sample mean and Gaussian shape of standardized fluctuations.

Section(s) supported: 16.1 Law of large numbers and central limit theorem.

Exact mathematical objects shown: Independent draws \(X_1,\ldots,X_n\); sample mean \(\bar X_n\); target mean \(\mu\); error scale \(1/\sqrt n\); standardized variable \(z=\sqrt n(\bar X_n-\mu)/\sigma\); normal approximation.

What the reader should notice first: Sample-mean paths stabilize near \(\mu\), but the remaining standardized errors form an approximately normal histogram.

Necessary labels: iid draws, sample mean Xbar_n, target mean mu, LLN: stabilizes, noise scale 1/sqrt(n), CLT: Normal approx, z.

How the text references the figure: Section 16.1 refers to Figure~\(\backslash\)ref\{fig:ch16-lln-clt\} when separating stabilization from fluctuation.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note figure, wide 16:9 raster diagram. Primary request: Create a clean mathematical diagram showing the law of large numbers and central limit theorem for repeated sampling. Style/medium: precise educational infographic, white background, navy line work, teal and warm gold accents, restrained red highlights, generous whitespace, readable at PDF width, no decorative gradients, no stock-photo realism. Composition/framing: Three connected panels from left to right. Left panel: many small independent draws X1, X2, ..., Xn represented as simple dots or cards flowing into a sample mean bar labeled Xbar_n. Middle panel: a line plot of sample mean versus n, several teal paths stabilizing toward a horizontal gold line labeled mu, with a shrinking band labeled 1/sqrt(n). Right panel: histogram of standardized means forming a bell curve labeled Normal approx, with horizontal axis labeled z. Text (verbatim, keep sparse and exact): "iid draws", "sample mean Xbar_n", "target mean mu", "LLN: stabilizes", "noise scale 1/sqrt(n)", "CLT: Normal approx", "z". Constraints: Make all labels large and accurately spelled. Show stabilization and bell-curve approximation visually. Do not include long formulas, paragraphs, tiny tick labels, 3D effects, decorative icons, or stock imagery.

Teaching caption: The law of large numbers and central limit theorem describe two views of the same repeated-sampling process. The sample mean \(\bar X_n\) stabilizes near the true mean \(\mu\), while its standardized error \(\sqrt n(\bar X_n-\mu)/\sigma\) approaches a normal distribution under the usual iid finite-variance assumptions.

## Figure 16.2: Modes of Convergence

Saved path: `imagegen-figures/ch16-modes-of-convergence.png`

Pedagogical purpose: Distinguish almost sure, \(L^p\), probability, and distributional convergence, and show the implication directions that students need for limit theorems and inference.

Section(s) supported: 16.2 Modes of convergence.

Exact mathematical objects shown: Nodes for \(X_n\xrightarrow{a.s.}X\), \(X_n\to X\) in \(L^p\), \(X_n\xrightarrow{p}X\), and \(X_n\xrightarrow{d}X\); arrows for almost sure to probability, \(L^p\) to probability, and probability to distribution; sample-path settling vignette; probability-error vignette for convergence to a constant; law-level convergence vignette.

What the reader should notice first: The arrows point from stronger convergence claims to weaker convergence claims.

Necessary labels: almost sure, L^p, in probability, in distribution, sample paths settle, probability error shrinks, laws converge, stronger, weaker.

How the text references the figure: Section 16.2 refers to Figure~\(\backslash\)ref\{fig:ch16-modes-convergence\} when explaining the implication diagram.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note figure, wide 16:9 raster diagram. Primary request: Create a clean implication diagram comparing modes of convergence for random variables. Style/medium: precise educational infographic, white background, navy line work, teal and warm gold accents, restrained red highlights, generous whitespace, readable at PDF width, no gradients, no stock-photo realism. Composition/framing: Centered diagram with four labeled nodes: almost sure, Lp, in probability, in distribution. Use thick navy arrows showing almost sure -> in probability, Lp -> in probability, in probability -> in distribution. Add one small side vignette: sample paths settling to a target for almost sure. Add another small side vignette: probability error shrinking for convergence in probability to a constant, and keep it visually distinct from a lower law-level convergence vignette. Text (verbatim, keep sparse and exact): "almost sure", "L^p", "in probability", "in distribution", "sample paths settle", "probability error shrinks", "laws converge", "stronger", "weaker". Constraints: Make all labels large and accurately spelled. Arrows must clearly show the implication direction. Do not include long formulas, paragraphs, tiny labels, 3D effects, decorative gradients, or stock imagery.

Teaching caption: Different modes of convergence answer different questions. Almost sure convergence and \(L^p\) convergence each imply convergence in probability, and convergence in probability implies convergence in distribution. The reverse implications generally require extra assumptions.

## Figure 16.3: Concentration Tail Bounds

Saved path: `imagegen-figures/ch16-concentration-tail-bounds.png`

Pedagogical purpose: Make concentration inequalities concrete as tail-probability controls and show how larger sample size narrows high-probability bands for sample means.

Section(s) supported: 16.3 Concentration inequalities.

Exact mathematical objects shown: Tail event \(|\bar X_n-\mu|\geq\epsilon\); mean \(\mu\); deviation \(\epsilon\); Markov, Chebyshev, and Hoeffding inequality hierarchy; shrinking high-probability bands as \(n\) increases.

What the reader should notice first: Concentration inequalities bound shaded tail probability outside an error band.

Necessary labels: sample mean, mu, epsilon, tail probability, Markov, Chebyshev, Hoeffding, with high probability, larger n, smaller band.

How the text references the figure: Section 16.3 refers to Figure~\(\backslash\)ref\{fig:ch16-concentration\} when introducing tail events and high-probability bands.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note figure, wide 16:9 raster diagram. Primary request: Create a clean mathematical diagram explaining concentration inequalities as shrinking tail bounds for a sample mean. Style/medium: precise educational infographic, white background, navy axes and line work, teal and warm gold accents, restrained red highlights, generous whitespace, readable at PDF width, no decorative gradients, no stock-photo realism. Composition/framing: Left panel: bell-shaped distribution centered at mu with shaded red tail regions beyond mu plus epsilon and mu minus epsilon, labeled tail probability. Center panel: stacked inequality ladder with simple labels Markov, Chebyshev, Hoeffding, each pointing to increasingly sharper tail bounds. Right panel: sample size n slider or axis showing confidence band width shrinking as n increases, with three nested bands around mu. Text (verbatim, keep sparse and exact): "sample mean", "mu", "epsilon", "tail probability", "Markov", "Chebyshev", "Hoeffding", "with high probability", "larger n", "smaller band". Constraints: Labels must be large and accurately spelled. Show tails and confidence bands visually, not with dense formulas. Avoid long equations, paragraphs, tiny tick labels, 3D effects, decorative gradients, or stock imagery.

Teaching caption: Concentration inequalities bound the probability of large deviations. Markov uses nonnegativity, Chebyshev uses variance, and Hoeffding uses independence plus bounded observations. For sample means, the high-probability band shrinks as \(n\) grows.

## Figure 16.4: High-Dimensional Geometry

Saved path: `imagegen-figures/ch16-high-dimensional-geometry.png`

Pedagogical purpose: Show that high-dimensional random vectors have structured geometry: norms concentrate, independent directions are nearly orthogonal, and random projections can preserve pairwise distances.

Section(s) supported: 16.4 High-dimensional geometry.

Exact mathematical objects shown: Gaussian vector \(X\in\mathbb R^d\); thin shell of radius \(\sqrt d\); random unit vectors \(U,V\) with \(U^\top V\) near zero; random projection \(f:\mathbb R^d\to\mathbb R^k\); pairwise-distance preservation.

What the reader should notice first: The same concentration principle explains thin shells, near-right angles, and random projection reliability.

Necessary labels: thin shell, radius sqrt(d), near orthogonal, dot product near 0, random projection, d to k, distances mostly preserved, curse, blessing.

How the text references the figure: Section 16.4 refers to Figure~\(\backslash\)ref\{fig:ch16-high-dimensional-geometry\} when introducing norm concentration, near-orthogonality, and random projections.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note figure, wide 16:9 raster diagram. Primary request: Create a clean mathematical diagram showing high-dimensional geometry: norm concentration, near-orthogonality, and random projection preservation. Style/medium: precise educational infographic, white background, navy line work, teal and warm gold accents, restrained red highlights, generous whitespace, readable at PDF width, no decorative gradients, no stock-photo realism. Composition/framing: Three panels in a row. Left panel: high-dimensional Gaussian point cloud represented as many teal dots lying in a thin spherical shell around a center, labeled thin shell radius sqrt(d). Middle panel: two random vectors from origin with angle close to 90 degrees, labeled near orthogonal and dot product near 0. Right panel: random projection from high dimension d to lower dimension k shown as points mapped through a narrow projection gate, pairwise distances before and after indicated by matching brackets. Text (verbatim, keep sparse and exact): "thin shell", "radius sqrt(d)", "near orthogonal", "dot product near 0", "random projection", "d to k", "distances mostly preserved", "curse", "blessing". Constraints: Make all labels large and accurately spelled. Keep the geometry precise and uncluttered. Do not include long formulas, paragraphs, tiny labels, 3D effects, decorative gradients, or stock imagery.

Teaching caption: High-dimensional random geometry has regular structure. Gaussian vectors concentrate in a thin shell of radius about \(\sqrt d\), independent random directions are nearly orthogonal, and random projections from \(d\) dimensions to \(k\) dimensions can preserve many pairwise distances when \(k\) is large enough.
