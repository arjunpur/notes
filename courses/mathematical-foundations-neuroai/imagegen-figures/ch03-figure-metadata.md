# Chapter 3 ImageGen figure metadata

These are the raster figures referenced by Chapter 3. They were generated one at a time with the built-in Codex ImageGen workflow, inspected, then copied into this course directory.

## ch03-vectors-three-views-v2.png

Pedagogical purpose: Show that one coordinate list can be interpreted as an arrow, a point, or a measured data vector depending on context.

Sections supported: 3.1 Vectors as arrows, points, and data.

Exact mathematical objects shown: vector \(v=(3,2)\) as an arrow from the origin; the same coordinate pair as a point; a data vector \(x\in\mathbb{R}^d\) with entries \(3,2,\dots,x_d\); feature bars aligned with vector coordinates and the final feature labeled as feature \(d\).

What the reader should notice first: the same ordered coordinates support three views, but the modeling context decides what the coordinates mean.

Necessary labels: arrow, point, data, \(O\), \(v\), \((3,2)\), \(3\), \(2\), \(x_d\), feature \(d\), \(x\in\mathbb{R}^d\).

Text reference: Section 3.1 references the figure while explaining how vector arithmetic is shared across arrows, points, and data records.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 3 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise mathematical diagram showing one vector interpreted in three compatible ways: arrow, point, and data vector. Scene/backdrop: pure white background, generous margins, no border. Subject: Three aligned panels left to right, connected by subtle navy arrows. Left panel title label exactly "arrow": draw 2D axes in thin navy with origin O, a navy arrow vector v from O to the point (3,2), and dashed teal coordinate steps 3 along horizontal and 2 along vertical. Middle panel title label exactly "point": draw the same 2D axes and a single teal dot at (3,2) labeled v, with a faint navy radius line from O to the dot. Right panel title label exactly "data": draw a clean vertical column vector with entries 3, 2, ..., x_d, labeled x in R^d; next to it draw a small row of feature bars aligned with the entries, showing labels 3, 2, ..., feature d. Necessary labels, exact text only: "arrow", "point", "data", "O", "v", "(3,2)", "3", "2", "x_d", "feature d", "x in R^d". Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal point/data accents; warm gold coordinate steps and numeric entries; restrained red not needed; no decorative gradients; no shadows; no stock-photo realism. Composition/framing: three clear panels with the same vector idea carried across views; labels large and readable at PDF width; no dense text. Mathematical accuracy: the arrow head and the point must both land at the same coordinate location (3,2) in their panels; the coordinate steps must correspond to 3 horizontally and 2 vertically; the final data-vector entry must be labeled x_d or feature d, not just d, so d is clearly the dimension/index rather than a coordinate value. The reader should notice first that the same ordered coordinates can name a displacement arrow, a point, or a measured data record depending on context. Constraints: exact labels only, no paragraphs, no extra equations, no tiny text, no watermark, no 3D, no hand-drawn wobble, no decorative background.

Caption: One coordinate list, three interpretations. The vector \(v=(3,2)\) can be drawn as a displacement arrow, used as the coordinates of a point, or stored as the first two entries of a data vector \(x\in\mathbb{R}^d\). The mathematics gives the same addition and scaling rules in all three views; the application determines what the coordinates measure.

## ch03-span-subspaces.png

Pedagogical purpose: Make span and the subspace closure tests visible.

Sections supported: 3.2 Vector spaces and subspaces.

Exact mathematical objects shown: two vectors \(u,v\); their span \(\operatorname{span}\{u,v\}\) as a plane through the origin; a generic linear combination \(au+bv\); a line through the origin labeled subspace; an offset parallel line labeled not a subspace.

What the reader should notice first: span produces all linear combinations and a subspace must pass through the origin.

Necessary labels: \(u\), \(v\), \(\operatorname{span}\{u,v\}\), \(au+bv\), subspace, not a subspace, \(O\).

Text reference: Section 3.2 references the figure while proving that span is the smallest subspace containing the generators.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 3 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise diagram explaining vector spaces, span, and subspaces in R^3. Scene/backdrop: pure white background, generous margins, no border. Subject: Left half: draw two teal basis-like arrows u and v from the origin in a 3D-style coordinate frame, and a warm-gold translucent plane through the origin labeled span{u,v}. On the plane, show several small points produced by a u + b v combinations and one arrow labeled a u + b v. Right half: show two small comparison panels. Top comparison panel: a navy line through the origin labeled subspace, with small teal arrows along the line and a check mark. Bottom comparison panel: a parallel line offset away from the origin labeled not a subspace, with the origin O visibly not on the line and a restrained red X. Necessary labels, exact text only: "u", "v", "span{u,v}", "a u + b v", "subspace", "not a subspace", "O". Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal vector accents; warm gold span plane; restrained red only for the X marker; no decorative gradients; no shadows; no stock-photo realism. Composition/framing: left large 3D coordinate frame with plane through origin, right stacked comparison panels; large readable labels; sparse and precise. Mathematical accuracy: the span plane must pass through the origin; u, v, and a u + b v must lie in that plane; the top subspace line must pass through O; the bottom offset line must not pass through O. The reader should notice first that a subspace is closed under linear combinations and must contain the origin. Constraints: exact labels only, no paragraphs, no extra equations, no tiny text, no watermark, no 3D rendering realism, no hand-drawn wobble, no decorative background.

Caption: Span and subspace structure. The plane \(\operatorname{span}\{u,v\}\) contains all linear combinations \(au+bv\) and passes through the origin. A line through the origin is a subspace; a parallel offset line is not, because it fails the zero-vector and scaling tests.

## ch03-norms-distances-angles.png

Pedagogical purpose: Separate size, separation, and directional alignment, and show that different norms have different unit balls.

Sections supported: 3.3 Norms, distances, and angles.

Exact mathematical objects shown: \(\ell_2\) unit ball as a circle; \(\ell_1\) unit ball as a diamond; vector \(x\); points \(x,y\); difference vector \(y-x\); distance segment; vectors \(u,v\); angle \(\theta\); cosine formula.

What the reader should notice first: norm, distance, and angle answer different geometric questions.

Necessary labels: \(O\), \(L_2\), \(L_1\), \(x\), \(y\), norm, distance, \(y-x\), \(u\), \(v\), theta, \(\cos\theta=\langle u,v\rangle/(\|u\|\|v\|)\).

Text reference: Section 3.3 references the figure while introducing norms, distances, and the Cauchy--Schwarz-supported angle formula.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 3 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise diagram comparing norms, distances, and angles in vector geometry. Scene/backdrop: pure white background, generous margins, no border. Subject: Three aligned panels left to right. Left panel: a 2D coordinate plane with two unit balls centered at O: a navy circle labeled L2 and a warm-gold diamond labeled L1; show a teal vector x from O to a point on neither boundary, labeled x, with a small bracket labeled norm. Middle panel: a 2D plane with two points x and y, a straight navy segment between them labeled distance, and a difference arrow labeled y - x. Right panel: two vectors u and v from a common origin with the angle between them highlighted by a warm-gold arc labeled theta; nearby show the equation cos theta = <u,v>/(||u|| ||v||) in large readable math text. Necessary labels, exact text only: "O", "L2", "L1", "x", "y", "norm", "distance", "y - x", "u", "v", "theta", "cos theta = <u,v>/(||u|| ||v||)". Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal vector/point accents; warm gold for L1 diamond and angle arc; restrained red not needed; no decorative gradients; no shadows; no stock-photo realism. Composition/framing: three balanced panels, sparse labels, large readable equation, precise geometric shapes. Mathematical accuracy: the L2 unit ball should be a circle, the L1 unit ball should be a diamond; distance is the length of y - x; angle is between u and v at the shared origin. The reader should notice first that norm measures size from the origin, distance measures separation between two points, and angle measures directional alignment. Constraints: exact labels only, no paragraphs, no extra equations, no tiny text, no watermark, no 3D, no hand-drawn wobble, no decorative background.

Caption: Three measurements on vectors. A norm measures size relative to the origin and depends on the chosen unit ball, such as the circular \(\ell_2\) ball or diamond-shaped \(\ell_1\) ball. A distance is the norm of a difference \(y-x\). An angle compares directions through the normalized inner product.

## ch03-orthogonal-decomposition.png

Pedagogical purpose: Teach projection as explained component plus orthogonal residual, then map that geometry to task subspaces in neural population analysis.

Sections supported: 3.4 Orthogonality and decomposition.

Exact mathematical objects shown: subspace \(W\) as a line through the origin; vector \(x\); projection \(p=\operatorname{proj}_W x\); residual \(r=x-p\); right-angle marker; task subspace plane; task component; residual/noise direction orthogonal to the task subspace.

What the reader should notice first: \(x\) decomposes into a component inside the subspace and a perpendicular residual.

Necessary labels: \(O\), \(W\), \(x\), \(p=\operatorname{proj}_W x\), \(r=x-p\), \(r\perp W\), task subspace, task component, noise/residual.

Text reference: Section 3.4 references the figure while proving the orthogonal decomposition theorem and explaining projection in regression and neural population geometry.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 3 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise diagram teaching orthogonal decomposition and projection onto a subspace. Scene/backdrop: pure white background, generous margins, no border. Subject: Large left panel: a 2D coordinate plane with a teal line through the origin labeled W. Draw a vector x from O to a point above the line. Draw the orthogonal projection p on W as a warm-gold arrow from O along W labeled p = proj_W x. Draw the residual r = x - p as a restrained-red arrow from the endpoint of p straight to the endpoint of x, meeting W at a right angle. Include a small right-angle square at p and label r perp W. Large right panel: a simplified neural-population interpretation with a tilted teal task subspace plane labeled task subspace and a red residual arrow labeled noise/residual orthogonal to the plane, plus a warm-gold projected point labeled task component. Necessary labels, exact text only: "O", "W", "x", "p = proj_W x", "r = x - p", "r perp W", "task subspace", "task component", "noise/residual". Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal subspace accents; warm gold projection/component; restrained red residual; no decorative gradients; no shadows; no stock-photo realism. Composition/framing: left panel dominates with exact projection geometry; right panel smaller but clear; labels large and readable; generous whitespace. Mathematical accuracy: W must pass through O; p must lie on W; x decomposes as x = p + r; r must be perpendicular to W and start at the endpoint of p. The reader should notice first that projection extracts the part inside the subspace and the residual is orthogonal. Constraints: exact labels only, no paragraphs, no extra equations, no tiny text, no watermark, no 3D rendering realism, no hand-drawn wobble, no decorative background.

Caption: Orthogonal decomposition as explained part plus residual. The projection \(p=\operatorname{proj}_W x\) lies inside the subspace \(W\). The residual \(r=x-p\) points from the projection to \(x\) and is perpendicular to \(W\). In neural population geometry, the same picture separates a task component from residual activity outside the task subspace.
