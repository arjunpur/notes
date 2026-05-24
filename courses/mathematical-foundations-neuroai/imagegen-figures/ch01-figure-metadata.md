# Chapter 1 ImageGen figure metadata

These are the raster figures currently referenced by Chapter 1. Earlier generated versions are retained in the directory for provenance, but the chapter uses the v2/v4 assets listed here.

## ch01-typed-objects-statements-v4.png

Pedagogical purpose: Make typed mathematical language concrete: observations are not yet models; valid inputs and parameters enter a function through typed ports; outputs cannot be silently reused as inputs.

Sections supported: 1.1 Mathematical objects, statements, and notation.

Exact mathematical objects shown: observation pairs (x, r); input set X; parameter set Theta; deterministic model f_theta with separate x and theta input ports; codomain Y; output r; invalid dashed path from Y back to the x input port.

What the reader should notice first: only x from X and theta from Theta enter the function block; the red path from Y back into the x port is blocked as a type error.

Necessary labels: x, r, X, Theta, Y, f_theta, theta, type error.

Text reference: Section 1.1 references the figure while explaining that a false statement and an ill-typed expression are different.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 1 lecture notes. Primary request: Create a precise, sharp diagram for typed mathematical language with exactly one output codomain Y and no Y box before the function. Scene/backdrop: pure white background, generous margins, no border. Subject: Wide horizontal academic diagram. Far left: a compact observation table with two columns labeled x and r, four rows, where x cells contain simple stimulus icons and r cells contain spike-count dots. Center-left: two typed input sets only: set X in teal containing four stimulus icons, and set Theta in warm gold containing a single parameter dial. Center-right: one function block labeled f_theta. The function block has two clearly separated input ports on its left edge: upper port labeled x, lower port labeled theta. Far right: exactly one codomain set Y in warm gold containing spike-count dots. Draw a solid teal arrow from X to the upper x input port. Draw a solid gold arrow from Theta to the lower theta input port. Draw a solid gold output arrow from the function block to Y labeled r. Draw exactly one red dashed illegal path from a spike-count dot inside Y back to the upper x input port, ending at a red X and the label type error. The red dashed path must end at the x port and must not touch the theta port. Style/medium: clean academic vector-like illustration rendered as PNG; crisp navy line work; teal for X/input; warm gold for Theta/Y/output; restrained red only for type error. Composition/framing: wide landscape; left-to-right flow; aligned ports; enough whitespace between objects; no duplicate codomain; no decorative elements. Color palette: white, navy, teal, warm gold, restrained red. Text (verbatim only): "x", "r", "X", "Theta", "Y", "f_theta", "theta", "type error". Constraints: exact labels only; no paragraphs; no extra equations; no gradients; no shadows; no stock-photo realism; high contrast; readable at PDF width; precise geometry; avoid hand-drawn wobble; no watermark. Avoid: any Y box before the function, duplicate Y boxes, red arrow into theta port, fuzzy symbols, decorative background, dense text, 3D, photorealism.

Caption: Typed notation separates data, valid inputs, parameters, and outputs. A stimulus x in X and parameter theta in Theta can enter the model f_theta, producing a response r in Y. The red dashed path shows a response object from Y being fed into the x-port: this is a type error, not a merely false statement.

## ch01-sets-relations-classes-v2.png

Pedagogical purpose: Show a relation as a concrete subset of a Cartesian product, then show how an equivalence relation turns elements of A into partition blocks.

Sections supported: 1.2 Sets, relations, and logical structure.

Exact mathematical objects shown: set A = {a1, a2, a3, a4}; set B = {b1, b2, b3}; grid A x B; selected relation cells R; one possible pair not in R; two equivalence classes inside A.

What the reader should notice first: R is not a machine that returns one output; it is a pattern of selected cells in A x B.

Necessary labels: A, B, A x B, R, not in R, classes, a1-a4, b1-b3.

Text reference: Section 1.2 references the figure while explaining relations as selected cells in a product grid and equivalence classes as partitions.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 1 lecture notes. Primary request: Create a precise, expressive diagram showing a relation as selected pairs in a Cartesian product and an equivalence relation as a partition. Scene/backdrop: pure white background, generous margins, no border. Subject: Wide landscape with three connected panels. Left panel: two sets A and B as clean vertical point lists, A has four teal points, B has three warm-gold points. Middle panel: a 4 by 3 Cartesian-product grid labeled A x B; selected relation cells are filled with teal-gold rings; unselected cells are pale; one unselected cell has a small restrained red outline to indicate not in R. Add thin guide lines from A and B point lists to grid rows/columns. Right panel: set A redrawn as four teal points grouped into two smooth partition blocks, one teal block containing two points and one warm-gold block containing two points, labeled classes. Style/medium: clean academic vector-like illustration rendered as PNG; navy line work; teal and warm gold accents; restrained red only for non-relation example. Composition/framing: three panels left to right with subtle navy arrows; strong grid geometry; no clutter; labels large and sparse. Color palette: white, navy, teal, warm gold, restrained red. Text (verbatim only): "A", "B", "A x B", "R", "not in R", "classes". Constraints: exact labels only; no paragraphs; no equations beyond labels; no gradients; no shadows; no stock-photo realism; high contrast; readable at PDF width; precise aligned grid; no watermark. Avoid: fuzzy labels, decorative background, dense annotations, 3D, photorealism, hand-drawn wobble.

Caption: A relation is a selected subset of a Cartesian product. The middle grid represents possible pairs in A x B; highlighted cells belong to R, while the red cell is a possible pair not chosen by the relation. The right panel shows how an equivalence relation on A groups elements into classes.

## ch01-proof-methods-v2.png

Pedagogical purpose: Make proof methods feel like ways of eliminating the only failure case of an implication, rather than unrelated formal tricks.

Sections supported: 1.3 Proof methods and mathematical maturity.

Exact mathematical objects shown: implication P -> Q; failure case P and not Q; direct proof path P to Q; contrapositive path not Q to not P; contradiction from P plus not Q to impossibility; induction chain base -> n -> n+1.

What the reader should notice first: the red central failure box P and not Q is what each proof method rules out.

Necessary labels: P, Q, not Q, not P, P and not Q, direct, contrapositive, contradiction, induction, base, n, n+1.

Text reference: Section 1.3 references the figure while explaining why proof methods match the logical shape of the claim.

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 1 lecture notes. Primary request: Create a precise, expressive diagram that teaches proof methods by showing how each method eliminates the failure case of an implication. Scene/backdrop: pure white background, generous margins, no border. Subject: Wide two-row academic diagram. Top center: a large implication lane with node P on left, node Q on right, navy arrow P -> Q. Under it, show the single failure case as a red boxed region labeled P and not Q, with a red X. Around this central lane, four smaller method panels: direct proof follows teal arrows from P through two small unlabeled intermediate dots to Q; contrapositive follows warm-gold arrow from not Q to not P; contradiction shows P plus not Q collapsing into a red contradiction symbol; induction shows base -> n -> n+1 as linked navy tiles. Use clean arrows and clear separation. Style/medium: clean academic vector-like illustration rendered as PNG; navy line work; teal for direct proof; warm gold for contrapositive/induction highlights; restrained red only for failure/contradiction. Composition/framing: balanced landscape; central failure case is visually prominent; four methods arranged as a readable map, not a decorative infographic. Color palette: white, navy, teal, warm gold, restrained red. Text (verbatim only): "P", "Q", "not Q", "not P", "P and not Q", "direct", "contrapositive", "contradiction", "induction", "base", "n", "n+1". Constraints: exact labels only; no paragraphs; no tiny text; no gradients; no shadows; no stock-photo realism; high contrast; readable at PDF width; precise arrow geometry; no watermark. Avoid: fuzzy labels, decorative background, dense annotations, 3D, photorealism, hand-drawn style.

Caption: Common proof methods reorganize the same implication. Direct proof builds a path from P to Q; contrapositive starts from not Q; contradiction occupies and destroys the failure case; induction propagates a base case forward.

## ch01-modeling-compression-v2.png

Pedagogical purpose: Make compression visible as fibers in a raw observation space that collapse to a compact state, then connect that state to prediction error and parameter feedback.

Sections supported: 1.4 Mathematical modeling as compression; backward connection to 1.2 equivalence classes.

Exact mathematical objects shown: raw observation space Omega; representation map pi; fibers/equivalence classes in Omega; compact state space S with state points s; model m_theta; prediction y_hat; target y; residual; loss; feedback to theta.

What the reader should notice first: the fibers in Omega are the details the model treats as equivalent before prediction.

Necessary labels: Omega, pi, S, s, m_theta, theta, y_hat, y, residual, loss.

Text reference: Section 1.4 references the figure while introducing the fitting objective and the sufficiency condition p(y | omega) = p(y | pi(omega)).

Comprehensive ImageGen prompt: Use case: scientific-educational. Asset type: high-resolution raster figure for Chapter 1 lecture notes. Primary request: Create a precise, expressive diagram for mathematical modeling as compression, emphasizing fibers of a representation map and the loss/residual loop. Scene/backdrop: pure white background, generous margins, no border. Subject: Wide landscape. Left: a rich raw observation space Omega drawn as a large cloud of many small neural-trial points, with three faint curved fiber regions grouping points that will be treated as equivalent. Center: a sharp funnel/projection map labeled pi from Omega into a low-dimensional state plane S; on S show three compact points/clusters labeled s. Right: a clean model block labeled m_theta mapping S to prediction y_hat. Far right: target y and predicted y_hat shown as two nearby marks with a red residual bracket between them. Bottom: a simple loss meter labeled loss, with a warm-gold feedback arrow back to theta on the model block. Style/medium: clean academic vector-like illustration rendered as PNG; navy line work; teal for state/valid compression; warm gold for model/parameters; restrained red only for residual/error. Composition/framing: strong left-to-right compression pipeline; fibers in Omega visually show equivalence classes; residual and feedback loop are clear but secondary. Color palette: white, navy, teal, warm gold, restrained red. Text (verbatim only): "Omega", "pi", "S", "s", "m_theta", "y_hat", "y", "residual", "loss", "theta". Constraints: exact labels only; no paragraphs; no extra equations; no gradients; no shadows; no stock-photo realism; high contrast; readable at PDF width; precise geometry; no watermark. Avoid: fuzzy labels, decorative background, dense annotations, 3D, photorealism, messy scatter, hand-drawn wobble.

Caption: Modeling as compression. Fibers in Omega show groups of observations treated as equivalent by pi. The compact state s in S feeds m_theta, while the residual between y_hat and y sends information back through the loss.
