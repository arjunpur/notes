# Chapter 14 Figure Metadata

## Figure 14.1: Discrete Distribution Catalog

Saved path: `imagegen-figures/ch14-discrete-distribution-catalog.png`

Pedagogical purpose: Show that discrete distributions are organized by data-generating story, support, parameters, and probability mass, not memorized as unrelated formulas.

Section(s) supported: 14.1 Core discrete distributions.

Exact mathematical objects shown: Bernoulli support \(\{0,1\}\) and parameter \(p\); categorical support \(\{1,\ldots,K\}\) and probability vector \(\pi\); binomial support \(\{0,\ldots,n\}\), parameters \(n,p\), and center near \(np\); Poisson support \(\{0,1,2,\ldots\}\), parameter \(\lambda\), and count bars.

What the reader should notice first: Each distribution starts from a different observation story before becoming a PMF.

Necessary labels: Bernoulli, Categorical, Binomial, Poisson, PMF, support, parameter, \(0\), \(1\), \(k\), \(p\), \(\pi\), \(n,p\), \(\lambda\).

How the text references the figure: Section 14.1 refers to Figure~\(\backslash\)ref\{fig:ch14-discrete-catalog\} when separating discrete distributions by observation type and support.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note figure, wide 16:9 raster diagram. Primary request: Create a clean mathematical diagram titled only with short labels showing a structured catalog of core discrete distributions. Style/medium: precise educational infographic, white background, navy line work, teal and warm gold accents, restrained red highlight, generous whitespace, readable at PDF width, no gradients, no stock-photo realism. Composition/framing: Four small panels in a single row or 2x2 grid. Panel 1: Bernoulli PMF with bars at 0 and 1 labeled 0 and 1, parameter p. Panel 2: Categorical PMF with three bars labeled class 1, class 2, class 3 and probability vector pi. Panel 3: Binomial PMF as bars on 0..n with center near np. Panel 4: Poisson PMF as count bars 0,1,2,... with parameter lambda and a spike-count icon made of small tick marks. Text (verbatim, keep sparse and exact): "Bernoulli", "Categorical", "Binomial", "Poisson", "support", "parameter", "0", "1", "k", "p", "pi", "n,p", "lambda". Constraints: Show probability mass as vertical bars, not smooth curves. Include a subtle arrow from data-generating story to PMF in each panel: coin, class choice, repeated trials, count in window. All text must be large, simple, and spelled correctly. Avoid dense paragraphs, tiny labels, formulas longer than a symbol, decorative icons, and three-dimensional effects.

Teaching caption: Core discrete distributions are best remembered by their stories and supports. Bernoulli models one binary trial; categorical models one class choice; binomial models the number of successes in \(n\) independent Bernoulli trials; Poisson models counts in a fixed window. The vertical bars are probability masses, so their total height-sum is \(1\).

## Figure 14.2: Continuous Density Areas

Saved path: `imagegen-figures/ch14-continuous-density-areas.png`

Pedagogical purpose: Make clear that a continuous density assigns probability by area under the curve, and that support constraints distinguish common families.

Section(s) supported: 14.2 Core continuous distributions.

Exact mathematical objects shown: Uniform density on \([a,b]\); Gaussian density with center \(\mu\), shaded probability interval \([x_1,x_2]\), and a separate scale marker from \(\mu\) to \(\mu+\sigma\); exponential density on \([0,\infty)\) with tail area after \(t\); beta density on \([0,1]\) with different shape possibilities.

What the reader should notice first: Shaded areas, not point heights, represent probabilities.

Necessary labels: Uniform, Gaussian, Exponential, Beta, density, area = probability, \(a\), \(b\), \(x_1\), \(x_2\), \(\mu\), scale \(\sigma\), \(0\), \(1\), \(t\), \(x\).

How the text references the figure: Section 14.2 refers to Figure~\(\backslash\)ref\{fig:ch14-continuous-density-areas\} when explaining probability as accumulated area rather than density height.

Generation method: Built-in ImageGen-produced raster figure, copied into the workspace at the saved path above.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note raster figure, wide 16:9 infographic. Primary request: Create a clean mathematical diagram showing core continuous distributions as densities and probabilities as shaded areas. Style: precise educational infographic, white background, navy axes and line work, teal density curves, warm gold shaded probability regions, restrained red highlights, generous whitespace, readable at PDF width, flat 2D, no gradients. Composition: Four panels in a 2x2 grid. Panel 1: Uniform density on interval [a,b] as a flat rectangle with a shaded subinterval area. Panel 2: Gaussian bell curve centered at mu. Shade a probability interval with endpoints labeled x1 and x2. Add a separate red scale bracket from mu to mu plus sigma labeled "scale sigma" above the curve. The sigma marker must not span the shaded interval. Panel 3: Exponential density starting high at 0 and decaying to the right, with shaded tail probability after t. Panel 4: Beta density on [0,1] with two shapes, one faint U-shaped and one skewed, with endpoints 0 and 1. Exact sparse text labels to include only: Uniform, Gaussian, Exponential, Beta, density, area = probability, a, b, x1, x2, mu, scale sigma, 0, 1, t, x. Constraints: Make all labels large, horizontal, and spelled exactly. Use smooth 2D curves and shaded areas only. Do not include long formulas, paragraphs, 3D effects, decorative gradients, watermarks, tiny tick labels, or extra text.

Teaching caption: Continuous distributions assign probability by area under a density curve. Uniform densities are flat on their support, Gaussian densities concentrate around a mean, exponential densities model nonnegative waiting times, and beta densities model variables constrained to \([0,1]\).

## Figure 14.3: Multivariate Gaussian Ellipses

Saved path: `imagegen-figures/ch14-multivariate-gaussian-ellipses.png`

Pedagogical purpose: Connect the multivariate Gaussian density to the covariance geometry students already know from vectors, quadratic forms, and PCA.

Section(s) supported: 14.3 Multivariate Gaussian distribution.

Exact mathematical objects shown: Mean vector \(\mu\); covariance matrix \(\Sigma\); covariance ellipse; principal axes; variance entries; covariance entries; precision matrix \(\Lambda=\Sigma^{-1}\); \(x_1,x_2\) coordinate axes.

What the reader should notice first: The covariance matrix determines ellipse width and tilt.

Necessary labels: mean \(\mu\), covariance \(\Sigma\), variance, covariance, precision \(\Lambda=\Sigma^{-1}\), principal axes, \(x_1\), \(x_2\).

How the text references the figure: Section 14.3 refers to Figure~\(\backslash\)ref\{fig:ch14-multivariate-gaussian\} when explaining mean, covariance, precision, Mahalanobis distance, and shared variability.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note figure, wide 16:9 raster diagram. Primary request: Create a precise educational diagram of a two-dimensional multivariate Gaussian distribution using covariance ellipses and principal axes. Style/medium: clean mathematical raster illustration, white background, navy axes and contour lines, teal point cloud, warm gold major axis, restrained red minor annotations, generous whitespace, readable at PDF width, no gradients, no 3D rendering. Composition/framing: Left side: 2D scatter cloud with elliptical contours centered at a mean point. Show mean vector as a dot labeled mu. Show two principal axes through the ellipse, one long warm gold axis and one shorter teal/navy axis. Label covariance matrix Sigma near the ellipses. Right side: compact matrix-like visual showing Sigma with entries var x1, cov, cov, var x2, with arrows to ellipse width and tilt. Include a small note for precision matrix Lambda inverse Sigma controlling sharpness. Text (verbatim, keep sparse and exact): "mean mu", "covariance Sigma", "variance", "covariance", "precision Lambda = Sigma^-1", "principal axes", "x1", "x2". Constraints: Make labels large and spelled correctly. Ellipses should be mathematically aligned with the axes, showing positive correlation tilt. Do not use long formulas, paragraphs, 3D surfaces, decorative gradients, or tiny labels.

Teaching caption: A two-dimensional Gaussian is shaped by its mean vector and covariance matrix. The mean \(\mu\) sets the center, \(\Sigma\) sets ellipse width and tilt, and the precision matrix \(\Lambda=\Sigma^{-1}\) controls sharpness in the exponent. Positive covariance tilts the ellipses along a shared-variation direction.

## Figure 14.4: Exponential-Family Map

Saved path: `imagegen-figures/ch14-exponential-family-map.png`

Pedagogical purpose: Show the role of each component in the exponential-family form and connect common distributions to the shared template.

Section(s) supported: 14.4 Exponential families.

Exact mathematical objects shown: \(p(x\mid\eta)=h(x)\exp(\eta^\top T(x)-A(\eta))\); base measure \(h(x)\); sufficient statistic \(T(x)\); natural parameter \(\eta\); log-partition function \(A(\eta)\); normalization to total probability \(1\); Bernoulli, Poisson, Gaussian, and GLM link examples.

What the reader should notice first: \(A(\eta)\) is the normalization term that makes the exponential score into a probability distribution.

Necessary labels: \(p(x\mid\eta)=h(x)\exp(\eta^\top T(x)-A(\eta))\), base measure \(h(x)\), sufficient statistic \(T(x)\), natural parameter \(\eta\), log-partition \(A(\eta)\), normalizes, total probability 1, Bernoulli, Poisson, Gaussian, GLM link.

How the text references the figure: Section 14.4 refers to Figure~\(\backslash\)ref\{fig:ch14-exponential-family-map\} when introducing the exponential-family decomposition and the role of \(A(\eta)\).

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: PDF lecture-note figure, wide 16:9 raster diagram. Primary request: Create a clean conceptual map for exponential families showing how base measure, sufficient statistic, natural parameter, and log-partition function combine to define a normalized distribution. Style/medium: precise educational infographic, white background, navy line work, teal and warm gold accents, restrained red highlights, generous whitespace, readable at PDF width, no gradients, no stock-photo realism. Composition/framing: Center: large equation box with p(x|eta) = h(x) exp( eta dot T(x) - A(eta) ). Four surrounding labeled boxes point into the equation: base measure h(x), sufficient statistic T(x), natural parameter eta, log-partition A(eta). A normalization arrow from A(eta) to total probability 1. Bottom row: three small example tags: Bernoulli, Poisson, Gaussian, each connected to the central equation. Text (verbatim, keep exact): "p(x|eta) = h(x) exp(eta dot T(x) - A(eta))", "base measure h(x)", "sufficient statistic T(x)", "natural parameter eta", "log-partition A(eta)", "normalizes", "total probability 1", "Bernoulli", "Poisson", "Gaussian", "GLM link". Constraints: Use only the exact text above, large and readable. Keep the equation legible. Avoid paragraphs, tiny labels, decorative gradients, stock-photo realism, and extra formulas.

Teaching caption: The exponential-family form separates the roles in a distribution. The sufficient statistic \(T(x)\) extracts data features, the natural parameter \(\eta\) weights those features, the base measure \(h(x)\) handles support-specific factors, and the log-partition function \(A(\eta)\) normalizes the result so total probability is \(1\).
