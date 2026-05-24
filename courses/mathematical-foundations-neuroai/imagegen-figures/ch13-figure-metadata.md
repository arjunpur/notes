# Chapter 13 Figure Metadata

All four selected figures are ImageGen-generated raster PNG assets for Chapter 13, with a white background, navy line work, teal mathematical objects, warm-gold accents, restrained red highlights, generous whitespace, and labels intended to remain readable at PDF width.

## Figure 13.1: Probability Space And Probability Measure

- Saved path: `imagegen-figures/ch13-probability-space.png`
- Pedagogical purpose: Introduce probability as a measure assigning consistent numbers to events in a sample space, while distinguishing finite probability mass from continuous density integration.
- Section(s) supported: 13.1 Probability as measure of uncertainty.
- Exact mathematical objects shown: Sample space \(\Omega\); events \(A\), \(B\), and \(C\); empty event with probability zero; probability scale \(P\); finite coin-toss outcome space \(\{HH,HT,TH,TT\}\) shown once each in a single-row grid; continuous density with a region probability \(P(X\in R)\).
- What the reader should notice first: Probabilities are assigned to events, not merely to drawings or formulas.
- Necessary labels: `events`, `probability measure`, `finite vs continuous`, `Omega`, `A`, `B`, `C`, `empty`, `P`, `0`, `P(A)`, `P(B)`, `1`, `finite outcomes`, `HH`, `HT`, `TH`, `TT`, `density integrates over regions`, `P(X in R)`, `f(x)`, `a`, `r1`, `r2`, `b`.
- How the text references the figure: Section 13.1 uses Figure~\ref{fig:ch13-probability-space} to separate outcomes, events, and the measure \(P\), and to explain finite versus continuous probability models.
- Teaching caption: A probability model has outcomes \(\Omega\), events such as \(A\), \(B\), and \(C\), and a probability measure \(P\) assigning numbers to events. Finite models often assign mass to individual outcomes. Continuous models usually assign probability to regions by integrating a density over the region.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 13 Probability Spaces and Random Variables
Primary request: Create a precise mathematical diagram introducing probability as a measure of uncertainty on a probability space, without using complement notation in the diagram.
Scene/backdrop: clean white background, three coordinated panels with generous whitespace.
Subject: Left panel: a rounded rectangle sample space labeled "Omega" containing simple outcome dots; three outlined subsets/events labeled "A", "B", and "C". Event A is highlighted teal, event B is warm gold, event C is light navy outline only. Include a tiny empty-set marker labeled "empty" near the corner to suggest probability zero without clutter. Middle panel: a vertical measure scale from 0 to 1 labeled "P" with marks "0", "P(A)", "P(B)", and "1", showing probabilities as sizes assigned to events, not to drawing areas. Right panel: two contrasting small examples: a one-row finite coin-toss outcome grid labeled "finite outcomes" with exactly four cells labeled "HH", "HT", "TH", and "TT", each appearing exactly once; and a smooth density over an interval labeled "density integrates over regions" with a shaded interval labeled "P(X in R)".
Style/medium: polished educational raster diagram, precise geometry, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; three panels aligned horizontally; light panel titles only: "events", "probability measure", "finite vs continuous".
Color palette: white background; navy line work and labels; teal event region; warm gold secondary event and shaded density area; restrained red only for the empty-set marker.
Text (verbatim): "events", "probability measure", "finite vs continuous", "Omega", "A", "B", "C", "empty", "P", "0", "P(A)", "P(B)", "1", "finite outcomes", "HH", "HT", "TH", "TT", "density integrates over regions", "f(x)", "a", "r1", "r2", "b", "P(X in R)".
Constraints: labels must be large and crisp; use only the listed short labels; do not include complement notation anywhere; show the finite coin-toss grid as exactly four outcomes with no duplicated outcomes; make clear that a probability measure assigns numbers to events; no dense paragraphs; no decorative gradients; no tiny labels; no stock imagery; no external logos.
```

## Figure 13.2: Random Variables As Functions

- Saved path: `imagegen-figures/ch13-random-variable-function-v2.png`
- Pedagogical purpose: Show that a random variable is a measurable function from outcomes to values, and that value-space events pull back to sample-space events.
- Section(s) supported: 13.2 Random variables as measurable functions.
- Exact mathematical objects shown: Sample space \(\Omega=\{HH,HT,TH,TT\}\); function \(X\) mapping outcomes to number of heads; value set \(\{0,1,2\}\); preimage event \(\{X=1\}=\{HT,TH\}\); distribution of \(X\) over values \(0,1,2\).
- What the reader should notice first: The event \(\{X=1\}\) is a highlighted subset of outcomes before it becomes a bar in the distribution.
- Necessary labels: `Omega`, `HH`, `HT`, `TH`, `TT`, `X`, `0`, `1`, `2`, `distribution of X`, `{X=1}`, `outcomes`, `values`, `probability`.
- How the text references the figure: Section 13.2 uses Figure~\ref{fig:ch13-random-variable-function} to explain preimages, induced distributions, and the distinction between a random variable and its law.
- Teaching caption: A random variable \(X\) is a function from outcomes to values. For two coin tosses, \(X\) can count the number of heads. The event \(\{X=1\}\) is the preimage \(\{HT,TH\}\) in the sample space. The distribution of \(X\) records the probabilities of the values \(0\), \(1\), and \(2\).
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 13 Probability Spaces and Random Variables
Primary request: Create a precise mathematical diagram explaining a random variable as a measurable function from outcomes to numbers, with correct preimages.
Scene/backdrop: clean white background, three coordinated panels with generous whitespace.
Subject: Left panel: a sample space blob labeled "Omega" with four outcomes in a vertical list: "HH", "HT", "TH", "TT". Middle panel: three value boxes on a number line labeled "0", "1", "2". Draw non-crossing arrows from HH to 2, from HT to 1, from TH to 1, and from TT to 0. Put a red outline around the two outcomes HT and TH, and a matching red bracket around the value 1, both labeled "{X=1}" to show the preimage event. Right panel: a simple bar chart labeled "distribution of X" with bars at 0, 1, 2 and relative heights 1, 2, 1; label the vertical axis "probability" but do not write numeric probabilities.
Style/medium: polished educational raster diagram, precise geometry, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; left-to-right flow from outcomes to values to distribution; arrows clean and navy or teal; no crossing arrows.
Color palette: white background; navy line work and labels; teal mapping arrows; warm gold distribution bars; restrained red for the preimage highlight.
Text (verbatim): "Omega", "HH", "HT", "TH", "TT", "X", "0", "1", "2", "distribution of X", "{X=1}", "outcomes", "values", "probability".
Constraints: labels must be large and crisp; use only the listed short labels; make clear that X is a function and that {X=1} is the set {HT, TH}; no dense paragraphs; no decorative gradients; no tiny labels; no stock imagery; no external logos; no extra outcomes; do not map TH to 0.
```

## Figure 13.3: Joint, Marginal, And Conditional Distributions

- Saved path: `imagegen-figures/ch13-joint-marginal-conditional.png`
- Pedagogical purpose: Teach the table operations behind joint distributions, marginalization, conditioning, and independence.
- Section(s) supported: 13.3 Joint, marginal, and conditional distributions.
- Exact mathematical objects shown: Binary joint table \(p(x,y)\); row and column sums for \(p(x)\) and \(p(y)\); normalized conditional slice \(p(x\mid Y=1)\); independence check \(p(x,y)=p(x)p(y)\).
- What the reader should notice first: Marginals are sums over one axis, while conditionals are normalized slices.
- Necessary labels: `joint p(x,y)`, `X`, `Y`, `p11`, `p10`, `p01`, `p00`, `marginal p(x)`, `marginal p(y)`, `condition on Y=1`, `p(x | Y=1)`, `independence?`, `p(x,y)=p(x)p(y)`.
- How the text references the figure: Section 13.3 uses Figure~\ref{fig:ch13-joint-marginal-conditional} to explain summing rows or columns, normalizing a conditional slice, and checking factorization.
- Teaching caption: A joint table stores probabilities for pairs \((X,Y)\). Marginal distributions come from summing rows or columns. A conditional distribution is a selected row or column slice normalized by its total probability. Independence is the special case where joint probabilities factor into marginal probabilities.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 13 Probability Spaces and Random Variables
Primary request: Create a precise mathematical diagram for joint, marginal, and conditional distributions using a small two-variable table.
Scene/backdrop: clean white background, three coordinated panels with generous whitespace.
Subject: Left panel: a 2 by 2 joint probability table labeled "joint p(x,y)" with row label "X" and column label "Y". Four cells have clean symbolic entries "p11", "p10", "p01", "p00". Highlight one cell in teal. Middle panel: show row sums and column sums leaving the table, labeled "marginal p(x)" and "marginal p(y)", with warm gold arrows from rows and columns to side totals. Right panel: show one highlighted column slice labeled "condition on Y=1" normalized into a two-bar conditional distribution labeled "p(x | Y=1)". Include a small independence check box labeled "independence? p(x,y)=p(x)p(y)".
Style/medium: polished educational raster diagram, precise geometry, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; joint table on left, marginal sums in center, conditional slice on right; arrows clean and sparse.
Color palette: white background; navy grid, axes, and labels; teal highlighted joint cell and conditional slice; warm gold marginal arrows and bars; restrained red question mark in independence box.
Text (verbatim): "joint p(x,y)", "X", "Y", "p11", "p10", "p01", "p00", "marginal p(x)", "marginal p(y)", "condition on Y=1", "p(x | Y=1)", "independence?", "p(x,y)=p(x)p(y)".
Constraints: labels must be large and crisp; use only the listed short labels; show marginalization as summing rows or columns; show conditioning as selecting and normalizing a slice; no dense paragraphs; no decorative gradients; no tiny labels; no stock imagery; no external logos.
```

## Figure 13.4: Random Vectors And Covariance Geometry

- Saved path: `imagegen-figures/ch13-random-vectors-covariance.png`
- Pedagogical purpose: Connect random vectors, mean vectors, covariance matrices, covariance ellipses, and neural population covariance.
- Section(s) supported: 13.4 Random vectors and covariance.
- Exact mathematical objects shown: Random vector samples in \(\mathbb{R}^2\); axes \(X_1,X_2\); mean \(\mu\); deviations \(X-\mu\); covariance ellipse; principal axes; covariance matrix \(\Sigma\) with variance and covariance entries; neural population traces feeding a population scatter.
- What the reader should notice first: Covariance summarizes the geometry of deviations around the mean.
- Necessary labels: `samples of X`, `X1`, `X2`, `mu`, `X-mu`, `covariance ellipse`, `principal axes`, `Sigma`, `var X1`, `cov`, `var X2`, `neural population`.
- How the text references the figure: Section 13.4 uses Figure~\ref{fig:ch13-random-vectors-covariance} to explain deviations, covariance entries, positive semidefinite geometry, covariance ellipses, and neural population covariance.
- Teaching caption: A random vector produces vector-valued samples. The mean \(\mu\) marks the center, deviations \(X-\mu\) point from the center to samples, and the covariance matrix \(\Sigma\) summarizes spread and co-movement. In two dimensions, covariance appears as an ellipse whose principal axes point along high- and low-variance directions.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 13 Probability Spaces and Random Variables
Primary request: Create a precise mathematical diagram showing random vectors, mean vector, covariance matrix, and covariance ellipse geometry.
Scene/backdrop: clean white background, three coordinated panels with generous whitespace.
Subject: Left panel: a 2D scatter cloud of points labeled "samples of X" with axes "X1" and "X2". Mark the center with a teal dot labeled "mu" and draw small centered arrows showing deviations "X-mu". Middle panel: an ellipse around the cloud labeled "covariance ellipse" with a long warm-gold principal axis and a short teal principal axis, plus a small red mark indicating positive correlation. Right panel: a 2 by 2 covariance matrix graphic labeled "Sigma" with entries "var X1", "cov", "cov", "var X2"; beside it a compact neuroscience mapping labeled "neural population" showing two simple firing-rate traces or bars feeding into the scatter.
Style/medium: polished educational raster diagram, precise geometry, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; scatter and ellipse on left/center, covariance matrix and neural mapping on right; use sparse labels and generous whitespace.
Color palette: white background; navy axes, matrix grid, and labels; teal sample points and mean; warm gold ellipse/principal axis; restrained red for correlation/off-diagonal emphasis.
Text (verbatim): "samples of X", "X1", "X2", "mu", "X-mu", "covariance ellipse", "principal axes", "Sigma", "var X1", "cov", "var X2", "neural population".
Constraints: labels must be large and crisp; use only the listed short labels; make clear covariance describes spread and co-movement of a random vector; no dense paragraphs; no decorative gradients; no tiny labels; no stock imagery; no external logos.
```
