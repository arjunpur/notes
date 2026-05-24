# Chapter 10 Figure Metadata

All four selected figures are ImageGen-generated, chapter-specific raster PNG assets for Chapter 10, with white background, navy line work, teal mathematical objects, warm gold accents, restrained red highlights, generous whitespace, and labels intended to remain readable at PDF width. Figures 10.2 and 10.4 were regenerated with the built-in ImageGen workflow after reviewer feedback; no programmatic diagram is used as a final asset. All figures are referenced from `source/authored-chapters/ch10.tex`.

## Figure 10.1: Taylor Local Replacement

- Saved path: `imagegen-figures/ch10-taylor-local-models-v2.png`
- Pedagogical purpose: Show Taylor approximation as a local replacement rule, with the quadratic model preserving more local information than the tangent model.
- Section(s) supported: 10.1 Taylor series and local models.
- Exact mathematical objects shown: A nonlinear scalar function \(f(x)\), base point \(a\), displacement \(h\), point \(a+h\), first-order linear model, second-order quadratic model, and local error bracket.
- What the reader should notice first: Near \(a\), the linear and quadratic models share the base point, and the quadratic model tracks the nonlinear curve more closely for a small displacement.
- Necessary labels: `f(x)`, `a`, `a+h`, `h`, `linear`, `quadratic`, `error`, `local replacement`, `zoom near a`.
- How the text references the figure: Section 10.1 uses Figure~\ref{fig:ch10-taylor-local-models} to explain Taylor polynomials as local function replacements.
- Teaching caption: Taylor approximation replaces a nonlinear function by a local model near a base point. The first-order model uses the tangent line, while the second-order model also uses curvature. For small \(h\), the quadratic model typically leaves a smaller local error than the linear model.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 10 Taylor Approximation, Local Geometry, and Manifolds
Primary request: Create a precise mathematical diagram for Taylor approximation as local replacement. The second-order quadratic approximation must be visibly closer to the nonlinear curve than the tangent line at a+h.
Scene/backdrop: clean white background, two coordinated panels with generous whitespace.
Subject: left panel: smooth convex nonlinear curve f(x) with marked base point a, small horizontal displacement h to a+h, tangent line through a labeled linear, and dashed quadratic curve through a labeled quadratic. At a+h, the dashed quadratic point should lie very close to f(a+h), while the linear point is noticeably lower; a small red bracket labeled error should mark the tiny remaining gap between f(a+h) and the quadratic approximation. right panel: zoomed-in neighborhood around a where the nonlinear curve, tangent, and quadratic approximation nearly overlap, with quadratic closest to f.
Style/medium: polished educational raster diagram, precise geometry, no stock-photo realism.
Composition/framing: landscape orientation, two panels aligned horizontally with light panel titles only: "local replacement" and "zoom near a".
Color palette: white background; navy axes and labels; teal nonlinear curve; warm gold tangent/linear model; navy dashed quadratic model; restrained red error bracket and point markers.
Text (verbatim): "f(x)", "a", "a+h", "h", "linear", "quadratic", "error", "local replacement", "zoom near a".
Constraints: labels must be large and crisp; use only the listed short labels; quadratic must be closer to f than linear at a+h; show generous whitespace and readable geometry at PDF width.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealistic objects, stock imagery, extra equations, clutter, external logos.
```

## Figure 10.2: Optimization Local Geometry

- Saved path: `imagegen-figures/ch10-optimization-local-geometry.png`
- Generation method: Built-in ImageGen, generated on 2026-05-14 from the prompt below and copied from `/home/arjun/.codex/generated_images/019e2748-63ce-7bc0-bc23-804792677b96/ig_04589929b177a07b016a05f63cff1081918b00d70ea9073640.png`.
- Pedagogical purpose: Connect Taylor loss models to gradient descent, Hessian curvature, saddle points, flat directions, and conditioning.
- Section(s) supported: 10.2 Local geometry of optimization landscapes.
- Mathematical objects shown: Loss contours near \(\theta_0\), descent direction \(-\nabla L\), Hessian \(H\), high- and low-curvature directions, an anisotropic positive-definite bowl, and a saddle/flat region with a nonconvex direction.
- What the reader should notice first: Different Taylor coefficients produce different local contour geometry: slope, strongly elliptical bowl, and shallow saddle.
- Necessary labels: `slope`, `minimum`, `saddle`, `theta_0`, `-grad L`, `H`, `high curvature`, `low curvature`, `flat direction`, `nonconvex`.
- How the text references the figure: Section 10.2 uses Figure~\ref{fig:ch10-optimization-local-geometry} to discuss first-order descent, Hessian eigenvectors, conditioning, and nonconvex local geometry.
- Teaching caption: Local optimization geometry comes from the Taylor model of a loss. Away from a critical point, the gradient gives the first-order descent direction. Near a minimum, Hessian eigenvectors show high- and low-curvature directions. Near a saddle or flat region, the same local model reveals directions that can be unstable, slow, or nearly unchanged.
- Comprehensive ImageGen prompt used for the current final asset:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 10 Taylor Approximation, Local Geometry, and Manifolds
Primary request: Create a precise contour diagram for local geometry of optimization landscapes using Taylor expansion of a loss near theta_0.
Scene/backdrop: clean white background, three side-by-side panels with generous whitespace.
Subject: panel 1: tilted local landscape contours with point theta_0 and gradient arrow showing first-order descent direction. panel 2: positive definite quadratic bowl contours around a local minimum with Hessian eigenvector arrows labeled high curvature and low curvature. panel 3: saddle/flat direction contours with one uphill direction and one downhill or flat direction, showing nonconvex local geometry. Use contour maps rather than 3D surfaces.
Style/medium: polished educational raster diagram, precise geometry, no stock-photo realism.
Composition/framing: landscape orientation; three equal panels with short headings: "slope", "minimum", "saddle"; arrows originate cleanly at marked points.
Color palette: white background; navy contour lines and labels; teal points and stable directions; warm gold descent/low-curvature arrows; restrained red uphill/negative-curvature highlights.
Text (verbatim): "slope", "minimum", "saddle", "theta_0", "-grad L", "H", "high curvature", "low curvature", "flat direction", "nonconvex".
Constraints: labels must be large and crisp; use only the listed short labels; show contours clearly; make the minimum panel elliptical and the saddle panel visibly different; readable at PDF width.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealistic objects, stock imagery, extra equations, clutter, external logos.
```

## Figure 10.3: Manifold Local Charts And Tangent Spaces

- Saved path: `imagegen-figures/ch10-manifold-local-charts.png`
- Pedagogical purpose: Make "locally flat" concrete through a curve, a surface, local charts, and tangent spaces.
- Section(s) supported: 10.3 Manifolds as locally flat spaces.
- Exact mathematical objects shown: A circle patch, a sphere patch, point \(p\), chart map \(u\), local coordinate segment/square, tangent line, and tangent plane.
- What the reader should notice first: A small curved patch can be mapped to local coordinates and approximated by a tangent line or tangent plane.
- Necessary labels: `curve`, `surface`, `p`, `tangent line`, `tangent plane`, `chart`, `u`, `local coordinates`, `looks flat nearby`.
- How the text references the figure: Section 10.3 uses Figure~\ref{fig:ch10-manifold-local-charts} to introduce charts, tangent spaces, and the idea that manifolds are globally curved but locally Euclidean.
- Teaching caption: A manifold can be curved globally while looking flat nearby. A chart assigns local coordinates to a small patch, and the tangent line or tangent plane gives the best local linear space at a point \(p\). Calculus on manifolds works by moving between curved patches and local coordinates.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 10 Taylor Approximation, Local Geometry, and Manifolds
Primary request: Create a precise educational diagram showing manifolds as spaces that are curved globally but locally flat, using a circle and sphere patch with charts and tangent spaces.
Scene/backdrop: clean white background, two coordinated panels with generous whitespace.
Subject: left panel: unit circle as a curved manifold with a small highlighted arc, a tangent line at point p, and a local coordinate chart u mapping the arc to a short line segment. right panel: sphere surface with a small highlighted patch around p, a tangent plane touching at p, and a chart map to a flat coordinate square labeled local coordinates.
Style/medium: polished educational raster diagram, precise geometry, no stock-photo realism.
Composition/framing: landscape orientation, two panels aligned horizontally with short headings: "curve" and "surface". Show chart arrows from curved patches to flat coordinate views.
Color palette: white background; navy line work and labels; teal manifolds/patches; warm gold tangent line and tangent plane; restrained red point p and chart arrows.
Text (verbatim): "curve", "surface", "p", "tangent line", "tangent plane", "chart", "u", "local coordinates", "looks flat nearby".
Constraints: labels must be large and crisp; use only the listed short labels; make tangent objects visibly touch at p; show that the manifold is globally curved but locally flat; readable at PDF width.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealism, stock imagery, extra equations, clutter, external logos.
```

## Figure 10.4: Lagrange Constraint Geometry

- Saved path: `imagegen-figures/ch10-lagrange-constraint-geometry.png`
- Generation method: Built-in ImageGen, generated on 2026-05-14 from the prompt below and copied from `/home/arjun/.codex/generated_images/019e2748-63ce-7bc0-bc23-804792677b96/ig_04589929b177a07b016a05f68289908191ab72597b017936b8.png`.
- Pedagogical purpose: Show constrained optimality as tangent/normal geometry rather than an algebraic trick.
- Section(s) supported: 10.4 Constrained surfaces and Lagrange geometry.
- Mathematical objects shown: Objective contours \(f\), feasible curve \(g(x,y)=0\), constrained point \(p\), tangent direction, normal direction, aligned gradient directions for \(f\) and \(g\), tangent space \(T_pM\), and the Lagrange condition.
- What the reader should notice first: At the constrained optimum, the objective contour is tangent to the constraint, and the two gradients are parallel normal vectors.
- Necessary labels: `constraint`, `Lagrange geometry`, `g(x,y)=0`, `f contours`, `p`, `tangent`, `normal`, `grad f`, `grad g`, `grad f = lambda grad g`, `T_p M`.
- How the text references the figure: Section 10.4 uses Figure~\ref{fig:ch10-lagrange-constraint-geometry} to derive \(\nabla f=\lambda\nabla g\) from feasible tangent directions.
- Teaching caption: At a constrained optimum, the objective contour is tangent to the feasible surface. The tangent direction gives allowed first-order moves, while \(\nabla g\) is normal to the constraint. If no tangent move can improve \(f\), then \(\nabla f\) has no tangent component, so it lies in the normal direction: \(\nabla f=\lambda\nabla g\).
- Comprehensive ImageGen prompt used for the current final asset:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 10 Taylor Approximation, Local Geometry, and Manifolds
Primary request: Create a precise mathematical diagram for constrained optimization and Lagrange multiplier geometry on a constraint surface.
Scene/backdrop: clean white background, two coordinated panels with generous whitespace.
Subject: left panel: contour lines of objective f(x,y) crossing a circular constraint g(x,y)=0, with a feasible curve highlighted, optimum point p where one contour is tangent to the constraint, tangent direction marked, and normal gradients grad f and grad g aligned. right panel: close-up at p showing tangent space T_p M as a line, normal direction, and the equation idea grad f = lambda grad g represented by two parallel gradient arrows.
Style/medium: polished educational raster diagram, precise geometry, no stock-photo realism.
Composition/framing: landscape orientation, two panels aligned horizontally with headings: "constraint" and "Lagrange geometry".
Color palette: white background; navy contour lines and labels; teal constraint curve and tangent space; warm gold objective gradient arrow; restrained red constraint normal/gradient arrow and optimum point.
Text (verbatim): "constraint", "Lagrange geometry", "g(x,y)=0", "f contours", "p", "tangent", "normal", "grad f", "grad g", "grad f = lambda grad g", "T_p M".
Constraints: labels must be large and crisp; use only the listed short labels; make the objective contour tangent to the constraint at p; show grad f and grad g parallel at p and perpendicular to the tangent line; readable at PDF width.
Avoid: decorative gradients, dense paragraphs, tiny text, photorealistic objects, stock imagery, extra equations, clutter, external logos.
```
