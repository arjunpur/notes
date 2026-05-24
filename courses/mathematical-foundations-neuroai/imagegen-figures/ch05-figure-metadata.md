# Chapter 5 Figure Metadata: Orthogonality, Projections, and Least Squares

All Chapter 5 figures were generated with the built-in Codex ImageGen workflow as raster images, then copied into `imagegen-figures/`.

## Figure: `ch05-projection-best-approximation.png`

- Pedagogical purpose: Show projection as the nearest point in a subspace and make residual orthogonality visually unavoidable.
- Supports section(s): 5.1 Projection as best approximation.
- Exact mathematical objects shown: subspace `S`; spanning directions `u1`, `u2`; target vector `y`; projected vector `p = P_S y`; residual `r = y - p`; right-angle marker for `r perpendicular S`; nearby nonoptimal candidate points in `S`.
- What the reader should notice first: the projection is the closest allowed vector, and the leftover residual is perpendicular to the entire subspace.
- Necessary labels: `S`, `u1`, `u2`, `y`, `p = P_S y`, `r = y - p`, `nearest point`.
- Text reference: Section 5.1 references Figure `\ref{fig:ch05-projection-best-approximation}` when explaining nearest-point geometry and residual orthogonality.
- Caption: Projection is a nearest-point statement. The subspace `S` contains all allowed approximations. The target `y` lies outside `S`, so the projection `p=P_Sy` is the closest point in `S`. The residual `r=y-p` is perpendicular to the whole subspace, not merely to the drawn basis arrows `u1` and `u2`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram for orthogonal projection as best approximation onto a subspace.
Style: white background, navy line work, translucent teal subspace, warm gold basis directions, restrained red highlight for the target and residual, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: one 3D perspective coordinate diagram. Draw a translucent teal plane through the origin labeled S. On the plane draw two warm-gold spanning arrows labeled u1 and u2. Draw a red vector y from the origin ending above the plane. Draw a teal vector p from the origin to the orthogonal foot of y on S, labeled p = P_S y. Draw a red residual arrow from p to y labeled r = y - p. Add a small navy right-angle square at p showing r is perpendicular to S. Include a faint dashed vertical segment from y to p. Show a few light gray candidate points on S farther away from y, with thin gray distance segments, to indicate p is the closest point.
Exact mathematical objects shown: subspace S, target vector y, projection p = P_S y in S, residual r = y - p in S^perp, basis directions u1 and u2 spanning S, and nearest-point geometry.
Necessary labels, exact text only: S, u1, u2, y, p = P_S y, r = y - p, nearest point. Keep labels large and legible, placed outside lines where possible. Do not include paragraphs, extra equations, tiny labels, or decorative elements.
Pedagogical goal: the reader should notice first that projection replaces y by the closest reachable vector p in the subspace, and the leftover residual is perpendicular to every direction in the subspace.
```

## Figure: `ch05-least-squares-regression.png`

- Pedagogical purpose: Connect the familiar scatterplot residual view to the observation-space projection view of least squares.
- Supports section(s): 5.2 Least-squares regression.
- Exact mathematical objects shown: scalar feature axis `x`; response axis `y`; observed data points; fitted line/vector `\hat y = X\hat\beta`; scalar residual `e_i`; column space `Col(X)`; response vector `y`; fitted vector `\hat y`; residual vector `e = y - \hat y`; right-angle marker for `e perpendicular Col(X)`.
- What the reader should notice first: individual vertical residuals are entries of one residual vector, and least squares makes that vector orthogonal to the prediction subspace.
- Necessary labels: `data space`, `observation space`, `x`, `y`, `\hat y = X\hat\beta`, `e_i`, `Col(X)`, `\hat y`, `e = y - \hat y`.
- Text reference: Section 5.2 references Figure `\ref{fig:ch05-least-squares-regression}` when deriving the normal equations from residual orthogonality.
- Caption: Least squares has two simultaneous views. In data space, residuals are vertical errors from observed responses to the fitted line. In observation space, those scalar residuals are entries of one vector `e=y-\hat y`. The fitted vector `\hat y=X\hat\beta` is the projection of `y` onto `Col(X)`, so `X^T e=0`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean two-panel academic diagram explaining least-squares regression as both vertical residuals in data space and orthogonal projection in observation space.
Style: white background, navy line work, teal fitted objects, warm gold data/features, restrained red residual highlights, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: Left panel titled only "data space". Draw horizontal axis labeled x and vertical axis labeled y. Place six warm-gold data points roughly near an upward sloping trend. Draw a teal fitted line labeled yhat = X beta-hat. Draw short red vertical residual segments from each point to the fitted line, label one residual e_i. Right panel titled only "observation space". Draw a translucent teal plane through the origin labeled Col(X), a red vector y ending above the plane, a teal vector yhat ending at the orthogonal foot on the plane, and a red residual arrow from yhat to y labeled e = y - yhat. Add a small right-angle marker at yhat.
Exact mathematical objects shown: design matrix column space Col(X), response vector y in R^n, fitted vector yhat = X beta-hat in Col(X), residual vector e = y - yhat orthogonal to Col(X), and scalar residuals e_i as vertical errors in the scatterplot view.
Necessary labels, exact text only: data space, observation space, x, y, yhat = X beta-hat, e_i, Col(X), yhat, e = y - yhat. Keep all labels large and legible; use beta-hat in plain readable math text if possible. Do not include paragraphs, extra formulas, tiny labels, or decorative elements.
Pedagogical goal: the reader should notice first that ordinary regression residuals are entries of one residual vector, and least squares chooses the fitted vector in Col(X) with the shortest residual.
```

## Figure: `ch05-gram-matrix-similarity.png`

- Pedagogical purpose: Make a Gram matrix feel like a geometry table whose cells correspond to pairwise vector comparisons.
- Supports section(s): 5.3 Gram matrices and similarity.
- Exact mathematical objects shown: vectors `x1`, `x2`, `x3`, `x4`; angle `theta_12`; Gram matrix `G`; diagonal entries `||x_i||^2`; off-diagonal entries `<x_i,x_j>`; highlighted pair `<x1,x2>`.
- What the reader should notice first: diagonal cells measure length, off-diagonal cells measure alignment, and the table is symmetric because inner products are symmetric.
- Necessary labels: `O`, `x1`, `x2`, `x3`, `x4`, `theta_12`, `G`, `<x1,x2>`, `||x_i||^2`, `pairwise inner products`.
- Text reference: Section 5.3 references Figure `\ref{fig:ch05-gram-matrix-similarity}` when explaining how Gram entries encode lengths, angles, and distances.
- Caption: A Gram matrix stores geometry one pair at a time. Each cell `G_ij` is the inner product `<x_i,x_j>`. Diagonal cells store squared lengths, while off-diagonal cells store alignment. Once `G` is known, distances among all vectors and angles between nonzero vectors can be recovered from these pairwise entries.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram explaining a Gram matrix as pairwise inner products and similarity geometry.
Style: white background, navy line work, teal and warm gold accents, restrained red highlight, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: two balanced panels connected by a thin navy arrow. Left panel: a 2D vector space with origin O and four vectors x1, x2, x3, x4 drawn from the origin. Use warm gold for x1 and x2, teal for x3 and x4. Show the angle theta_12 between x1 and x2 with a small arc. Use a restrained red highlight on x1 and x2 to show their pairwise comparison. Right panel: a square 4 by 4 Gram matrix heatmap labeled G. Cell (1,2) and cell (2,1) are highlighted in restrained red and labeled <x1,x2>. Diagonal cells are marked ||x_i||^2. Off-diagonal cells use light teal/gold shading to indicate similarities.
Exact mathematical objects shown: vectors x1 through x4, pairwise inner product <x_i,x_j>, angle theta_12, Gram matrix G with entries G_ij = <x_i,x_j>, diagonal entries as squared norms.
Necessary labels, exact text only: O, x1, x2, x3, x4, theta_12, G, <x1,x2>, ||x_i||^2, pairwise inner products. Keep labels large and legible; no paragraphs; no tiny text; no extra equations beyond these labels.
Pedagogical goal: the reader should notice first that the Gram matrix is not an arbitrary table: each cell records a geometric comparison between two vectors, with diagonals measuring length and off-diagonals measuring alignment.
```

## Figure: `ch05-qr-stable-fitting.png`

- Pedagogical purpose: Show QR as a change from correlated columns to an orthonormal basis, with `R` storing the coordinate bookkeeping.
- Supports section(s): 5.4 QR decomposition and stable fitting.
- Exact mathematical objects shown: original columns `a1`, `a2`; orthogonalization by removing `proj_{q1} a2`; orthonormal directions `q1`, `q2`; matrix `Q = [q1 q2]`; upper-triangular matrix `R` with entries `r11`, `r12`, `r22`; triangular least-squares solve `R beta = Q^T y`.
- What the reader should notice first: QR keeps the same column space but replaces a fragile correlated basis with perpendicular unit directions.
- Necessary labels: `columns of A`, `orthogonalize`, `A = QR`, `a1`, `a2`, `q1`, `q2`, `Q = [q1 q2]`, `R`, `r11`, `r12`, `r22`, `solve R beta = Q^T y`.
- Text reference: Section 5.4 references Figure `\ref{fig:ch05-qr-stable-fitting}` when explaining Gram-Schmidt and why QR improves least-squares computation.
- Caption: QR decomposition replaces correlated columns by orthonormal directions. The original columns `a1,a2` span the same space as `q1,q2`, but the `q`-directions are perpendicular and unit length. The triangular matrix `R` records the coordinates of the original columns in the `Q`-basis, so least squares becomes the triangular solve `R\hat\beta=Q^T y`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram explaining QR decomposition and stable least-squares fitting.
Style: white background, navy line work, teal orthonormal directions, warm gold original columns, restrained red highlights, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: three linked panels in one horizontal figure. Left panel titled only "columns of A": draw two nearly aligned warm-gold vectors a1 and a2 from the origin, showing an ill-conditioned pair. Middle panel titled only "orthogonalize": show a1 becoming q1 and a2 split into a projection along q1 plus a perpendicular leftover; use a small right-angle marker on the perpendicular component. Right panel titled only "A = Q R": draw two teal perpendicular unit arrows q1 and q2 from the origin, label Q = [q1 q2], and place a small upper-triangular matrix icon labeled R with entries r11 r12 r22. Add a small note-like label solve R beta = Q^T y, but keep it as a single equation label, not a paragraph.
Exact mathematical objects shown: original columns a1 and a2 of A, orthonormal columns q1 and q2 of Q, upper triangular R, the factorization A = Q R, and the stable least-squares equation R beta = Q^T y.
Necessary labels, exact text only: columns of A, orthogonalize, A = Q R, a1, a2, q1, q2, Q = [q1 q2], R, r11, r12, r22, solve R beta = Q^T y. Keep labels large and legible; no paragraphs; no tiny text; no extra equations beyond these labels.
Pedagogical goal: the reader should notice first that QR replaces a difficult correlated column basis by perpendicular unit directions, while R records how the original columns are assembled from those directions.
```
