# Chapter 9 Figure Metadata

All four figures are ImageGen-generated raster PNG assets for Chapter 9, with white background, navy line work, teal mathematical objects, warm gold directional accents, and restrained red highlights. The Jacobian and Hessian figures were regenerated in revision to align notation and curvature semantics with `source/authored-chapters/ch09.tex`. The Figure 9.2 regeneration prompt was also polished so the unit-direction label is plain `u`, not an escaped literal.

## Figure 9.1: Functions as Surfaces and Contours

- Saved path: `imagegen-figures/ch09-functions-surface-contours.png`
- Pedagogical purpose: Show that a scalar-valued function of two variables can be read both as a height surface and as a contour map in input space.
- Section(s) supported: 9.1 Functions of many variables.
- Exact mathematical objects shown: A scalar function \(f:\mathbb{R}^2\to\mathbb{R}\), input coordinates \(x,y\), output height \(z=f(x,y)\), level curves \(f(x,y)=c\), coordinate slices holding \(x\) or \(y\) fixed, and a point \((x_0,y_0)\).
- What the reader should notice first: The same function is being represented twice: once as a surface and once as contours.
- Necessary labels: `z=f(x,y)`, `x`, `y`, `surface`, `contours`, `f(x,y)=c`, `(x0,y0)`, `hold y fixed`, `hold x fixed`.
- How the text references the figure: Section 9.1 uses Figure~\ref{fig:ch09-functions-surface-contours} to explain surfaces, contours, level sets, and coordinate slices.
- Teaching caption: A scalar-valued function of two variables can be viewed as a surface \(z=f(x,y)\) or as a contour map in the input plane. Holding one coordinate fixed gives a one-variable slice through the surface. Contours are level sets: all points on one contour share the same value of \(f\).
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 9 Multivariable Calculus
Primary request: Create a precise mathematical diagram for functions of many variables, showing a scalar-valued function f(x,y) as both a surface over a 2D domain and a contour map.
Scene/backdrop: clean white background, two coordinated panels with generous whitespace.
Subject: left panel: 3D-looking smooth surface z=f(x,y) over an x-y plane, with two highlighted slice curves showing holding y fixed and holding x fixed; right panel: top-down contour map of the same function with labeled axes x and y, contour labels f(x,y)=c, and one marked point (x0,y0).
Style/medium: polished educational raster diagram, precise geometry, no stock-photo realism.
Composition/framing: landscape orientation, readable at PDF width, two panels aligned horizontally with light panel titles only: "surface" and "contours".
Color palette: white background; navy line work; teal surface/contours; warm gold slice curves; restrained red highlight for the marked point and partial-dependence arrows.
Text (verbatim): "z=f(x,y)", "x", "y", "surface", "contours", "f(x,y)=c", "(x0,y0)", "hold y fixed", "hold x fixed".
Constraints: labels must be large and crisp; use only the listed short labels; show contours as level sets; make the surface and contour map visually correspond.
Avoid: decorative gradients, dense paragraphs, tiny text, hand-drawn look, stock imagery, external logos, extra equations.
```

## Figure 9.2: Gradient and Directional Derivative Geometry

- Saved path: `imagegen-figures/ch09-gradient-directional-derivative.png`
- Pedagogical purpose: Make the dot-product meaning of the directional derivative visible and show the gradient as steepest ascent.
- Section(s) supported: 9.2 Gradients and directional derivatives.
- Exact mathematical objects shown: A level curve through \(x_0\), the gradient \(\nabla f(x_0)\), a chosen unit direction \(u\), the projection component giving \(D_u f(x_0)=\nabla f(x_0)^\top u\), and coordinate axes.
- What the reader should notice first: The gradient crosses the level curve orthogonally, while the directional derivative depends on the component of the gradient along \(u\).
- Necessary labels: `x_0`, `u`, `\nabla f(x_0)`, `level curve`, `D_u f(x_0)=\nabla f(x_0)\cdot u`, `steepest ascent`.
- How the text references the figure: Section 9.2 uses Figure~\ref{fig:ch09-gradient-directional-derivative} to explain contour geometry, signs of directional derivatives, and steepest ascent.
- Teaching caption: The gradient \(\nabla f(x_0)\) is perpendicular to the level curve through \(x_0\) and points toward steepest first-order increase. The directional derivative \(D_u f(x_0)\) is the dot product \(\nabla f(x_0)^\top u\), so it is the component of the gradient in the chosen unit direction \(u\).
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 9 Multivariable Calculus
Primary request: Create a precise contour diagram showing gradient and directional derivative geometry for a scalar field f:R^2->R.
Scene/backdrop: clean white background, one large top-down contour plot with generous margins.
Subject: nested smooth contour lines, one point x0, a navy/teal gradient arrow perpendicular to the local contour, a warm gold unit direction arrow u at an oblique angle, and a small projection mark showing the component of the gradient along u. Include a small inset equation label D_u f(x0)=grad f(x0) dot u.
Style/medium: polished educational raster diagram, exact vector geometry, readable at PDF width.
Composition/framing: landscape orientation; contour map centered; arrows originate at the same point; gradient visibly crosses contours at right angle; u arrow tangent-ish but not exactly tangent, so directional derivative is positive but smaller than gradient magnitude.
Color palette: white background; navy axes and labels; teal contour lines and gradient arrow; warm gold u arrow and projection bracket; restrained red point highlight.
Text (verbatim): "x_0", "u", "\nabla f(x_0)", "level curve", "D_u f(x_0)=\nabla f(x_0)\cdot u", "steepest ascent".
Constraints: keep labels short and crisp; show gradient perpendicular to the level curve at x0; show the directional derivative as the dot-product/projection onto u.
Avoid: decorative gradients, dense text, tiny labels, photorealism, stock imagery, extra unrelated equations, clutter.
```

## Figure 9.3: Jacobian as Local Linear Map

- Saved path: `imagegen-figures/ch09-jacobian-local-map.png`
- Pedagogical purpose: Connect vector-valued derivatives to the matrix-as-linear-map viewpoint from Chapter 4.
- Section(s) supported: 9.3 Jacobians and vector-valued functions.
- Exact mathematical objects shown: A nonlinear map \(F:\mathbb{R}^2\to\mathbb{R}^2\), an input point \(x_0\), output point \(F(x_0)\), small input displacements \(\Delta x\) and \(v\), the Jacobian \(J_F(x_0)\), and output displacements \(J_F(x_0)\Delta x\) and \(J_F(x_0)v\).
- What the reader should notice first: A small circular input neighborhood is transformed by the local linear map into a tilted ellipse or parallelogram in output space.
- Necessary labels: `input space`, `output space`, `x_0`, `F(x_0)`, `\Delta x`, `v`, `J_F(x_0)`, `J_F(x_0)\Delta x`, `J_F(x_0)v`, `local linear map`.
- How the text references the figure: Section 9.3 uses Figure~\ref{fig:ch09-jacobian-local-map} to explain the approximation \(F(a+h)\approx F(a)+J_F(a)h\), Jacobian shape, and matrix geometry.
- Teaching caption: The Jacobian \(J_F(x_0)\) is the local linear map that sends small input displacements near \(x_0\) to first-order output displacements near \(F(x_0)\). A small circle of possible input perturbations becomes an ellipse or parallelogram under the linearized map.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 9 Multivariable Calculus
Primary request: Create a precise diagram explaining the Jacobian of a vector-valued map F:R^2->R^2 as the local linear map from small input displacements to output displacements.
Scene/backdrop: clean white background, three-part flow diagram with left input plane, center Jacobian matrix, right output plane.
Subject: left panel: small circular neighborhood around x0 in input space with two small displacement arrows delta x and v; center: a 2 by 2 matrix labeled J_F(x0); right panel: transformed small ellipse/parallelogram around F(x0) in output space with arrows J_F(x0) delta x and J_F(x0)v. Add a faint curved global map arrow labeled F over the panels to distinguish nonlinear F from local linear J_F.
Style/medium: polished educational raster diagram, precise linear algebra geometry, no stock-photo realism.
Composition/framing: landscape orientation; left-to-right mapping; readable labels; generous whitespace.
Color palette: white background; navy axes and text; teal neighborhoods and transformed ellipse; warm gold displacement arrows; restrained red dots at x0 and F(x0).
Text (verbatim): "input space", "output space", "x_0", "F", "F(x_0)", "\Delta x", "v", "J_F(x_0)", "J_F(x_0)\Delta x", "J_F(x_0)v", "local linear map".
Constraints: the right shape should look like a linear image of the left small circle; include a clear matrix in the center but no numerical entries; make labels crisp and sparse.
Avoid: decorative gradients, dense paragraphs, tiny labels, photorealistic objects, extra equations, clutter, external logos.
```

## Figure 9.4: Hessian Curvature

- Saved path: `imagegen-figures/ch09-hessian-curvature.png`
- Pedagogical purpose: Show how Hessian eigenvalues and eigenvectors encode local curvature, minima, saddles, and flat valleys.
- Section(s) supported: 9.4 Hessians and curvature.
- Exact mathematical objects shown: Contours of local quadratic models, Hessian eigenvector directions, positive eigenvalues, mixed-sign eigenvalues, small and large curvature directions, and an ill-conditioned valley whose long axis is the small-curvature/slow direction while the short cross-valley axis is the large-curvature direction.
- What the reader should notice first: Different signs and magnitudes of Hessian eigenvalues produce visibly different contour geometry.
- Necessary labels: `minimum`, `saddle`, `flat valley`, `H positive definite`, `H indefinite`, `lambda_1>0`, `lambda_2>0`, `lambda_+`, `lambda_-`, `small curvature` on the long valley axis, `large curvature` on the short cross-valley axis, `slow direction` on the long valley axis.
- How the text references the figure: Section 9.4 uses Figure~\ref{fig:ch09-hessian-curvature} to explain positive definiteness, saddle geometry, uneven curvature, and optimization difficulty.
- Teaching caption: Hessians classify local quadratic geometry. Positive eigenvalues in all directions give a local minimum shape. Mixed signs give a saddle: some directions curve up and others curve down. Very different positive eigenvalues produce a narrow valley, which makes first-order optimization slow along the small-curvature direction.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 9 Multivariable Calculus
Primary request: Create a precise mathematical diagram explaining Hessian curvature for scalar functions of two variables using quadratic local geometry.
Scene/backdrop: clean white background, three side-by-side panels with generous whitespace.
Subject: panel 1: positive definite Hessian, elliptical contour lines around a minimum, two orthogonal eigenvector arrows, labels lambda1>0 and lambda2>0. Panel 2: indefinite Hessian saddle, hyperbola-like contour lines, one warm gold uphill curvature direction and one restrained red downhill curvature direction, labels lambda+ and lambda-. Panel 3: flat/ill-conditioned valley, long narrow contour ellipses; label the long axis as small curvature and slow direction, and label the short cross-valley axis as large curvature.
Style/medium: polished educational raster diagram, precise contour geometry, readable at PDF width.
Composition/framing: landscape orientation; three equal panels with short headings: "minimum", "saddle", "flat valley".
Color palette: white background; navy line work and labels; teal contour lines; warm gold positive curvature arrows; restrained red negative curvature arrow.
Text (verbatim): "minimum", "saddle", "flat valley", "H positive definite", "H indefinite", "lambda_1>0", "lambda_2>0", "lambda_+", "lambda_-", "small curvature", "large curvature", "slow direction".
Constraints: keep text short and crisp; use contours rather than 3D rendered objects; clearly show curvature directions as Hessian eigenvectors.
Avoid: decorative gradients, dense paragraphs, tiny labels, photorealistic objects, stock imagery, extra equations, clutter.
```
