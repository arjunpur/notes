# Chapter 4 Figure Metadata: Matrices as Linear Maps

All Chapter 4 figures were generated with the built-in Codex ImageGen workflow as raster images, then copied into `imagegen-figures/`.

## Figure: `ch04-matrix-transforms-grid.png`

- Pedagogical purpose: Show that a matrix is determined by the images of basis directions and that a whole square/grid follows by linear combination.
- Supports section(s): 4.1 Matrices as arrays and transformations.
- Exact mathematical objects shown: input basis vectors `e1`, `e2`; input vector `x=e1+e2`; linear map `A`; transformed basis vectors `Ae1`, `Ae2`; transformed vector `Ax`; unit square mapped to a parallelogram.
- What the reader should notice first: the columns of `A` are `Ae1` and `Ae2`, and `Ax` is the same coordinate combination after transformation.
- Necessary labels: `O`, `e1`, `e2`, `x`, `Ae1`, `Ae2`, `Ax`, `A`, `input`, `output`.
- Text reference: Section 4.1 references Figure `\ref{fig:ch04-matrix-transforms-grid}` when explaining the column-combination view of `Ax`.
- Caption: A matrix is determined by what it does to basis directions. In the input panel, `x=e1+e2` is the diagonal of the unit square. In the output panel, the square becomes the parallelogram spanned by `Ae1` and `Ae2`, and the same linear combination gives `Ax=Ae1+Ae2`. The columns of the matrix are the transformed basis vectors.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean two-panel academic diagram explaining a 2D matrix as a linear map.
Style: white background, navy line work, teal transformed objects, warm gold input objects, restrained red highlight for one mapped point, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: left panel titled only with the short label "input"; right panel titled only with the short label "output". Use simple vector labels and no paragraphs.
Exact mathematical objects: left panel shows standard axes with origin O, basis arrows e1=(1,0) and e2=(0,1), a gold unit square with corners O, e1, e2, e1+e2, and a red point/vector labeled x at e1+e2. Right panel shows the same linear map A applied to the square: Ae1=(1.2,0.3) and Ae2=(0.6,1.1), the teal parallelogram spanned by Ae1 and Ae2, and the red point/vector labeled Ax at Ae1+Ae2. Include a single navy arrow labeled A between panels.
Necessary labels, exact text only: O, e1, e2, x, Ae1, Ae2, Ax, A, input, output. Keep labels large and legible, placed outside lines where possible.
Pedagogical goal: the reader should immediately see that the columns of A are the images of basis directions, and that the whole square moves by linear combination. Do not draw equations other than the short labels listed. Do not include tiny labels or extra symbols.
```

## Figure: `ch04-composition-change-basis.png`

- Pedagogical purpose: Make the change-of-basis formula feel like a pipeline: reconstruct from coordinates, apply the map, then remeasure in output coordinates.
- Supports section(s): 4.2 Composition, inverses, and change of basis.
- Exact mathematical objects shown: input coordinates `[x]_B`; basis reconstruction by `B`; geometric vector `x`; standard matrix `A`; output vector `Ax`; output remeasurement by `C^{-1}`; output coordinates `[Ax]_C`.
- What the reader should notice first: `C^{-1}AB` is a composition of three meaningful operations, not a mysterious algebraic rearrangement.
- Necessary labels: `B`, `A`, `C^{-1}`, `[x]_B`, `x`, `Ax`, `[Ax]_C`, `input coordinates`, `geometric vector`, `output vector`, `output coordinates`.
- Text reference: Section 4.2 references Figure `\ref{fig:ch04-composition-change-basis}` while deriving `[T(x)]_C=C^{-1}AB[x]_B`.
- Caption: The change-of-basis formula is a composition. Starting with coordinates `[x]_B`, the basis matrix `B` reconstructs the geometric vector `x`. The map `A` sends it to `Ax`. The inverse coordinate matrix `C^{-1}` remeasures the output in the `C`-basis, producing `[Ax]_C=C^{-1}AB[x]_B`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram for composition, inverses, and change of basis in linear algebra.
Style: white background, navy line work, teal and warm gold accents, restrained red highlight, generous whitespace, precise geometry, readable labels, no decorative gradients, no dense text blocks.
Composition: a horizontal three-stage map with four small coordinate panels connected by arrows. Panel 1: a tilted warm-gold input coordinate grid labeled B with a red coordinate vector label [x]_B. Arrow from panel 1 to panel 2 labeled B. Panel 2: standard geometric space with vector x in navy. Arrow from panel 2 to panel 3 labeled A. Panel 3: standard geometric output space with vector Ax in red and a slightly sheared grid. Arrow from panel 3 to panel 4 labeled C^{-1}. Panel 4: teal tilted output coordinate grid labeled C with red coordinate vector label [Ax]_C.
Exact mathematical objects shown: the operation chain [x]_B --B--> x --A--> Ax --C^{-1}--> [Ax]_C. The visual should make clear that B reconstructs the input vector from B-coordinates, A applies the linear map, and C^{-1} remeasures the output in C-coordinates.
Necessary labels, exact text only: B, A, C^{-1}, [x]_B, x, Ax, [Ax]_C, input coordinates, geometric vector, output vector, output coordinates. Keep all labels large and legible. Do not include any additional equations or paragraphs.
Pedagogical goal: the reader should notice first that a change-of-basis matrix is a composition of three maps, not a mysterious symbol manipulation.
```

## Figure: `ch04-rank-null-column-space.png`

- Pedagogical purpose: Show the complementary roles of null space and column space: null-space directions vanish, while outputs live in the column space.
- Supports section(s): 4.3 Rank, null space, and column space.
- Exact mathematical objects shown: a linear map `A: R^3 -> R^2`; null-space plane `N(A)`; null vector `z`; two inputs `x` and `x+z`; shared output `Ax`; column-space line `C(A)`.
- What the reader should notice first: adding a null-space direction does not change the output.
- Necessary labels: `A`, `N(A)`, `C(A)`, `z`, `x`, `x+z`, `Ax`, `0`.
- Text reference: Section 4.3 references Figure `\ref{fig:ch04-rank-null-column-space}` while explaining fibers `x+N(A)` and reachable outputs.
- Caption: Null-space directions disappear, and column-space directions are the reachable outputs. If `z in N(A)`, then `A(x+z)=Ax`, so all points in the same null-space fiber have the same image. The image must lie in `Col(A)`, the subspace spanned by the columns of `A`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram explaining rank, null space, and column space for a linear map A: R^3 -> R^2.
Style: white background, navy line work, teal and warm gold accents, restrained red highlight, generous whitespace, precise geometry, no decorative gradients, no dense text blocks.
Composition: two panels connected by a navy arrow labeled A. Left panel is a simple 3D perspective domain with axes and a warm-gold translucent plane through the origin labeled N(A). Draw a gold vector z lying in N(A). Draw two red points/vectors labeled x and x+z on a line parallel to N(A), showing they differ by the null-space vector z. Right panel is a 2D codomain with a teal line through the origin labeled C(A). Draw one red point/vector on that teal line labeled Ax, and show both x and x+z mapping to the same Ax by using two thin red arrows from the left points toward the right point.
Exact mathematical objects shown: null space N(A) in the domain, column space C(A) in the codomain, the equivalence Ax = A(x+z) when z is in N(A), and the fact that outputs lie in C(A).
Necessary labels, exact text only: A, N(A), C(A), z, x, x+z, Ax, 0. Labels should be large and legible. No paragraphs, no extra equations, no tiny text.
Pedagogical goal: the reader should notice first that null-space directions disappear, while column-space directions are the only reachable outputs.
```

## Figure: `ch04-linear-systems-fitting.png`

- Pedagogical purpose: Connect inconsistent linear systems to least-squares projection onto a column space.
- Supports section(s): 4.4 Linear systems and data fitting.
- Exact mathematical objects shown: column space `Col(X)` as a plane; feature columns `x1`, `x2`; target vector `y`; fitted vector `\hat y`; residual `r=y-\hat y`; right-angle marker showing residual orthogonal to the column space.
- What the reader should notice first: when `y` is outside the reachable subspace, the best fit is the nearest reachable vector and the residual is perpendicular to the subspace.
- Necessary labels: `Col(X)`, `x1`, `x2`, `y`, `\hat y`, `r = y - \hat y`.
- Text reference: Section 4.4 references Figure `\ref{fig:ch04-linear-systems-fitting}` when deriving the normal equations from residual orthogonality.
- Caption: An inconsistent system becomes a closest-fit problem. The model can only produce vectors in `Col(X)`. The target `y` lies outside that plane, so least squares chooses the reachable vector `\hat y=X\hat w` closest to `y`. The residual `r=y-\hat y` is perpendicular to the column space, which gives the normal equations `X^T r=0`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram explaining a linear system and data fitting as projection onto a column space.
Style: white background, navy line work, teal and warm gold accents, restrained red highlight, generous whitespace, precise geometry, no decorative gradients, no dense text blocks.
Composition: one 3D perspective coordinate diagram. Draw a translucent teal plane through the origin labeled Col(X). On the plane, draw two warm-gold spanning arrows labeled x1 and x2. Draw a red target vector y ending above the plane. Draw a teal fitted vector yhat from the origin to the orthogonal foot on the plane. Draw a restrained red residual arrow from yhat upward to y labeled r = y - yhat. Mark a right-angle symbol at the foot to show the residual is orthogonal to the plane. Optionally show a faint dashed vertical from y to yhat.
Exact mathematical objects shown: target y in R^n, column space Col(X), fitted vector yhat in Col(X), residual r = y - yhat perpendicular to Col(X), and feature columns x1, x2 spanning the prediction plane.
Necessary labels, exact text only: Col(X), x1, x2, y, yhat, r = y - yhat. Labels should be large and legible; no paragraphs; no extra formulas; no tiny text.
Pedagogical goal: the reader should notice first that an inconsistent linear system becomes a closest-fit problem by replacing y with its reachable approximation yhat in the column space.
```
