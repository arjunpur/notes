# Chapter 2 ImageGen figure metadata

These are the raster figures referenced by Chapter 2. The prompts record the intended ImageGen specifications; precision-critical mathematical diagrams were corrected as raster PNGs after review so the visible labels, captions, and metadata match the chapter text.

Round 2 correction note: the Chapter 2 PNGs were raster-corrected with exact LaTeX-rendered mathematical labels after review found ImageGen text artifacts in the function, coordinate-system, and data-transformation figures.

## ch02-functions-as-mappings.png

Pedagogical purpose: Make a function visible as a typed map of individual inputs and as an induced map on subsets through images and preimages.

Sections supported: 2.1 Functions as mappings.

Exact mathematical objects shown: finite domain set \(X=\{x_1,x_2,x_3,x_4\}\); codomain set \(Y=\{y_1,y_2,y_3\}\); arrows for \(f(x_1)=y_1\), \(f(x_2)=y_1\), \(f(x_3)=y_2\), \(f(x_4)=y_3\); subset \(A=\{x_1,x_3\}\subseteq X\); image \(f(A)=\{y_1,y_2\}\subseteq Y\); subset \(B=\{y_1,y_3\}\subseteq Y\); preimage \(f^{-1}(B)=\{x_1,x_2,x_4\}\subseteq X\), with \(x_3\) excluded.

What the reader should notice first: each input has exactly one outgoing arrow, while several inputs may share one output.

Necessary labels: \(X\), \(Y\), \(f\), \(A\), \(f(A)\), \(B\), \(f^{-1}(B)\), \(x_1\), \(x_2\), \(x_3\), \(x_4\), \(y_1\), \(y_2\), \(y_3\).

Text reference: Section 2.1 references the figure while distinguishing images, preimages, and inverse functions.

Comprehensive ImageGen/raster-correction prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 2 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise diagram showing a function as a mapping of individual points and as a mapping of subsets, emphasizing image and preimage. Scene/backdrop: pure white background, generous margins, no border. Subject: Left side: a teal outlined domain set labeled \(X\) containing four points \(x_1,x_2,x_3,x_4\). Right side: a warm-gold outlined codomain set labeled \(Y\) containing three points \(y_1,y_2,y_3\). Draw solid navy arrows from \(x_1\) and \(x_2\) to \(y_1\), from \(x_3\) to \(y_2\), and from \(x_4\) to \(y_3\), showing \(f\) maps each input to exactly one output while different inputs can share an output. Inside \(X\), shade subset \(A\) containing exactly \(x_1\) and \(x_3\); inside \(Y\), shade its image \(f(A)\) containing exactly \(y_1\) and \(y_2\). Also draw restrained-red contours for subset \(B\) in \(Y\) containing exactly \(y_1\) and \(y_3\) and excluding \(y_2\), and draw restrained-red contours for the preimage \(f^{-1}(B)\) in \(X\) containing exactly \(x_1,x_2,x_4\) while clearly excluding \(x_3\). Use separate red components if needed so \(x_3\) is not inside the preimage. Necessary labels, exact mathematical text only: \(X\), \(Y\), \(f\), \(A\), \(f(A)\), \(B\), \(f^{-1}(B)\), \(x_1\), \(x_2\), \(x_3\), \(x_4\), \(y_1\), \(y_2\), \(y_3\). Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal domain accents; warm gold codomain accents; restrained red only for preimage subset; no decorative gradients; no shadows; no stock-photo realism. Composition/framing: two large set ovals side by side with arrows left-to-right; enough whitespace; labels large and readable at PDF width; mathematical geometry must be precise. Make the first visual impression: a function is not just a formula, it moves inputs and induces movement of subsets. Constraints: exact labels only, no paragraphs, no extra equations, no tiny text, no watermark, no 3D, no hand-drawn wobble, no duplicate arrows from one \(x_i\) to multiple \(y_j\).

Caption: A function moves points and induces set-level maps. Each \(x_i\in X\) has exactly one image in \(Y\), but several inputs may share an output. The teal region illustrates an image \(f(A)\). The red contours illustrate the preimage \(f^{-1}(B)=\{x_1,x_2,x_4\}\) of the output-side set \(B=\{y_1,y_3\}\).

## ch02-coordinate-systems.png

Pedagogical purpose: Separate an underlying point from the coordinate numbers used to represent it.

Sections supported: 2.2 Coordinate systems and representations.

Exact mathematical objects shown: one point \(p=(3,2)\); standard coordinate axes \(e_1,e_2\); tilted basis directions \(b_1=(4,0)\), \(b_2=(-1/2,1)\); coordinate description \([p]_E=(3,2)\); coordinate description \([p]_B=(1,2)\); dashed reconstruction \(p=1b_1+2b_2\); change-of-coordinates arrow.

What the reader should notice first: the point \(p\) is drawn once, while two coordinate columns describe it.

Necessary labels: \(p\), \(e_1\), \(e_2\), \(b_1\), \(b_2\), \([p]_E=(3,2)\), \([p]_B=(1,2)\), change coordinates.

Text reference: Section 2.2 references the figure while explaining that coordinate changes alter representations, not the underlying object.

Comprehensive ImageGen/raster-correction prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 2 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise diagram showing the same geometric point represented in two coordinate systems, with a change-of-coordinates arrow. Scene/backdrop: pure white background, generous margins, no border. Subject: A single 2D plane. Draw standard axes \(e_1\) and \(e_2\) in thin navy, horizontal and vertical. Draw a point \(p\) at standard coordinates \((3,2)\) as a dark dot in the first quadrant. Draw vector from origin to \(p\) in navy. Overlay a tilted coordinate frame with basis vectors \(b_1=(4,0)\) in teal and \(b_2=(-1/2,1)\) in warm gold from the same origin. Show dashed coordinate reconstruction that reaches \(p\) by exactly one teal \(b_1\) step from \((0,0)\) to \((4,0)\), then exactly two warm-gold \(b_2\) steps from \((4,0)\) to \((3.5,1)\) and from \((3.5,1)\) to \((3,2)\). On the left of the plane, show a small coordinate column labeled \([p]_E=(3,2)\). On the right, show a small coordinate column labeled \([p]_B=(1,2)\). Between them place a curved navy arrow labeled change coordinates. Make clear the point \(p\) does not move; only the coordinate description changes. Necessary labels, exact mathematical text only: \(p\), \(e_1\), \(e_2\), \(b_1\), \(b_2\), \([p]_E=(3,2)\), \([p]_B=(1,2)\), change coordinates. Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal and warm gold basis accents; restrained red not needed; no decorative gradients; no shadows; no stock-photo realism. Composition/framing: one precise coordinate plane centered, coordinate labels in small side callouts, large readable text, no clutter, enough whitespace. The reader should notice first that one point \(p\) has two coordinate descriptions. Constraints: exact labels only, no paragraphs, no extra equations, no tiny text, no watermark, no 3D, no hand-drawn wobble. Use readable mathematical typography. Avoid making \(p\) appear twice.

Caption: One point, two coordinate descriptions. The dot \(p\) is fixed in the plane. The standard axes \(e_1,e_2\) give \([p]_E=(3,2)\), while one \(b_1\) step and two \(b_2\) steps give \([p]_B=(1,2)\). The change-of-coordinates arrow changes the numerical representation, not the geometric point.

## ch02-data-transformations.png

Pedagogical purpose: Show data preprocessing as an explicit sequence of maps that changes location, scale, and orientation.

Sections supported: 2.3 Transformations of data.

Exact mathematical objects shown: raw data cloud \(X\); mean \(\mu\); centered data \(x-\mu\); scaling by \(D^{-1}\); final linear transformation \(A\); representation \(Z\); pipeline equation \(z=A D^{-1}(x-\mu)\).

What the reader should notice first: the point cloud changes in controlled stages rather than by an informal cleanup step.

Necessary labels: raw \(X\), \(\mu\), center, \(x-\mu\), scale, \(D^{-1}\), transform \(Z\), \(A\), \(z=A D^{-1}(x-\mu)\).

Text reference: Section 2.3 references the figure while deriving mean and covariance transformations under affine maps.

Comprehensive ImageGen/raster-correction prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 2 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise data-transformation diagram showing raw data points becoming centered, scaled, and rotated into a representation space. Scene/backdrop: pure white background, generous margins, no border. Subject: Four panels connected left to right by navy arrows. Panel 1 labeled raw \(X\): a small 2D scatter cloud of teal points offset from the origin, with axes. Show a warm-gold dot labeled \(\mu\) at the cloud center. Panel 2 labeled center: the same cloud shifted so \(\mu\) is at the origin; include a small arrow labeled \(x-\mu\). Panel 3 labeled scale: the cloud stretched/compressed so the axes have comparable spread; include label \(D^{-1}\). Panel 4 labeled transform \(Z\): the cloud rotated into a cleaner coordinate frame with one elongated direction horizontal; include label \(A\). Above the arrows write \(z=A D^{-1}(x-\mu)\). Keep all scatter points simple and readable. Necessary labels, exact mathematical text only: raw \(X\), \(\mu\), center, \(x-\mu\), scale, \(D^{-1}\), transform \(Z\), \(A\), \(z=A D^{-1}(x-\mu)\). Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal points; warm gold for mean and scale markers; restrained red not needed; no gradients; no shadows; no stock-photo realism. Composition/framing: four evenly spaced panels, aligned axes, clear pipeline. The reader should notice first that preprocessing is a sequence of explicit mathematical maps, not cosmetic data cleaning. Constraints: exact labels only, no paragraphs, no extra equations, no tiny text, no watermark, no 3D, no hand-drawn wobble. Avoid using dense scatter or unreadable labels.

Caption: A data transformation as a pipeline of explicit maps. The raw cloud is centered by subtracting \(\mu\), scaled by \(D^{-1}\), and then transformed by \(A\) into a representation \(Z\). Each step changes a different geometric feature: location, units, and orientation.

## ch02-algebraic-structures.png

Pedagogical purpose: Connect algebraic laws to transformations, inverses, composition, and equivariant representations.

Sections supported: 2.4 Algebraic structures.

Exact mathematical objects shown: set \(X\); identity transformation \(\operatorname{id}\); transformations \(g,h\); composition \(h\circ g\); inverse \(g^{-1}\); representation map \(\phi\); representation space \(R\); action \(\rho(g)\); equivariance law \(\phi(gx)=\rho(g)\phi(x)\).

What the reader should notice first: algebraic laws are laws for composing and comparing transformations, not just symbolic rules for numbers.

Necessary labels: \(X\), \(R\), id, \(g\), \(h\), \(h\circ g\), \(g^{-1}\), \(\phi\), \(\rho(g)\), \(\phi(gx)=\rho(g)\phi(x)\).

Text reference: Section 2.4 references the figure while proving that self-maps form a monoid, bijections form a group, and equivariance is a law respected by representations.

Comprehensive ImageGen/raster-correction prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 2 lecture notes, wide landscape 16:9, clean academic lecture-note aesthetic. Primary request: Create a precise diagram showing algebraic structure as transformations with composition, identity, inverse, and equivariance. Scene/backdrop: pure white background, generous margins, no border. Subject: Wide academic diagram with two connected zones. Left zone titled transformations on \(X\): draw a teal set \(X\) with three simple points forming a triangle. Around it draw three transformation arrows labeled id, \(g\), \(h\), where id is a loop, \(g\) is a rotation-like arrow, \(h\) is a flip-like arrow. Between \(g\) and \(h\) draw a small composition arrow labeled \(h\circ g\). Also show a warm-gold arrow labeled \(g^{-1}\) undoing \(g\). Right zone: draw representation space \(R\) with three corresponding feature points. Draw a model block \(\phi\) from \(X\) to \(R\). Show an equivariance square: top arrow \(g\) on \(X\), bottom arrow \(\rho(g)\) on \(R\), vertical arrows \(\phi\), and label \(\phi(gx)=\rho(g)\phi(x)\). Use a small restrained-red \(\times\) beside a mismatched bottom arrow to indicate a broken law, but no extra words. Necessary labels, exact mathematical text only: \(X\), \(R\), id, \(g\), \(h\), \(h\circ g\), \(g^{-1}\), \(\phi\), \(\rho(g)\), \(\phi(gx)=\rho(g)\phi(x)\). Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal set/object accents; warm gold inverse/action accents; restrained red only for broken law marker; no decorative gradients; no shadows; no stock-photo realism. Composition/framing: left half explains group-like transformations by composition; right half shows the same algebraic law transported to representations. Large readable labels, precise arrows, no clutter. Constraints: exact labels only, no paragraphs, no tiny text, no watermark, no 3D, no hand-drawn wobble. Use readable mathematical typography.

Caption: Algebraic structure as lawful transformation. On the left, transformations of \(X\) can be composed, have an identity action, and may have inverses. On the right, an equivariant representation \(\phi\) respects the action: transforming the input by \(g\) and then representing it matches representing it first and applying the corresponding representation-space action \(\rho(g)\).
