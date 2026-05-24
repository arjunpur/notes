# Chapter 12 Figure Metadata

All four figures are ImageGen-generated raster PNG assets for Chapter 12, with white background, navy line work, teal mathematical objects, warm-gold accents, and restrained red highlights. The operator figure was regenerated once to avoid fragile Greek-letter label rendering; the selected final asset uses plain-text labels in the image and mathematical notation in the caption.

## Figure 12.1: Function Space Geometry

- Saved path: `imagegen-figures/ch12-function-spaces.png`
- Pedagogical purpose: Introduce functions as vector-like objects with distances, displacements, basis directions, and coordinates.
- Section(s) supported: 12.1 Spaces of functions.
- Exact mathematical objects shown: Two time-domain functions \(f(t)\) and \(g(t)\); the \(L^2\) distance \(\|f-g\|_2\); an abstract coordinate plane with basis axes \(\phi_1,\phi_2\); function-space points \(f,g\); displacement \(f-g\); basis functions \(\phi_1(t),\phi_2(t)\); coefficients \(c_1,c_2\).
- What the reader should notice first: The same curves can be viewed either as signals over time or as points in a function space.
- Necessary labels: `signals`, `function space`, `basis coordinates`, `t`, `f(t)`, `g(t)`, `||f-g||_2`, `phi_1`, `phi_2`, `f`, `g`, `f-g`, `phi_1(t)`, `phi_2(t)`, `c_1`, `c_2`.
- How the text references the figure: Section 12.1 uses Figure~\ref{fig:ch12-function-spaces} to explain \(L^2\) distance, abstract function-space points, displacement \(f-g\), and basis coefficients.
- Teaching caption: Functions can be treated as vector-like objects. The \(L^2\) distance \(\|f-g\|_2\) measures the accumulated squared difference between two curves. In an abstract function space, \(f\) and \(g\) are points and \(f-g\) is their displacement. Choosing basis functions \(\phi_1,\phi_2,\ldots\) gives coordinate coefficients such as \(c_1,c_2\).
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 12 Function Spaces, Operators, and Fourier Analysis
Primary request: Create a precise mathematical diagram introducing spaces of functions by showing functions as vector-like objects with inner products, norms, and basis coefficients.
Scene/backdrop: clean white background, three coordinated panels with generous whitespace.
Subject: left panel: two smooth time-domain curves f(t) and g(t) over the same t axis, with the difference between them subtly shaded and labeled ||f-g||_2. Middle panel: a simple abstract function space coordinate plane with axes phi_1 and phi_2, points labeled f and g, and a short vector from g to f labeled f-g. Right panel: two basis functions phi_1(t) and phi_2(t), with small coefficient bars labeled c_1 and c_2 showing expansion into basis directions.
Style/medium: polished educational raster diagram, precise geometry, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; three panels aligned horizontally; light panel titles only: "signals", "function space", "basis coordinates".
Color palette: white background; navy line work and labels; teal curves and points; warm gold shaded difference and coefficient bars; restrained red for one marked distance arrow.
Text (verbatim): "signals", "function space", "basis coordinates", "t", "f(t)", "g(t)", "||f-g||_2", "phi_1", "phi_2", "f", "g", "f-g", "phi_1(t)", "phi_2(t)", "c_1", "c_2".
Constraints: labels must be large and crisp; use only the listed short labels; the figure should teach that a function can be a point/vector in a space; no dense paragraphs.
Avoid: decorative gradients, tiny labels, photorealism, stock imagery, external logos, extra equations, clutter.
```

## Figure 12.2: Linear Operators On Functions

- Saved path: `imagegen-figures/ch12-linear-operators.png`
- Pedagogical purpose: Show that operators map functions to functions, that kernels act like infinite-dimensional matrices, and that linearity and eigenfunction behavior parallel matrix geometry.
- Section(s) supported: 12.2 Linear operators.
- Exact mathematical objects shown: Input function \(f(t)\), operator \(T\), kernel \(K(t,s)\), output \((Tf)(t)\), linearity of processing sums, and an eigenfunction mode whose shape is preserved while its scale changes.
- What the reader should notice first: The operator box sits between an input curve and an output curve, just as a matrix sits between input and output vectors.
- Necessary labels: `f(t)`, `T`, `K(t,s)`, `Tf(t)`, `linearity`, `operator`, `mode in`, `scaled mode out`, `eigenfunction`.
- How the text references the figure: Section 12.2 uses Figure~\ref{fig:ch12-linear-operators} to connect matrices, kernels, linearity, convolution, and eigenfunctions.
- Teaching caption: A linear operator maps an input function \(f(t)\) to an output function \((Tf)(t)\), much as a matrix maps an input vector to an output vector. Some operators are described by kernels \(K(t,s)\). Linearity means that processing a sum gives the sum of processed signals. An eigenfunction is a mode whose shape is preserved by the operator, up to a scalar factor.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 12 Function Spaces, Operators, and Fourier Analysis
Primary request: Create a precise mathematical diagram explaining a linear operator on functions as an infinite-dimensional analogue of a matrix, with a kernel view and an eigenfunction shape-preservation view.
Scene/backdrop: clean white background, three-part left-to-right flow diagram with generous whitespace.
Subject: top row: an input curve labeled f(t) flows through an operator box labeled T and becomes an output curve labeled Tf(t). Inside the operator box include a faint matrix grid and a small kernel heatmap labeled K(t,s). Below the top row, include a short line labeled linearity with two input curves combined by a plus sign, passing through T, and two corresponding output curves combined by a plus sign. Bottom corner: a sine-shaped input labeled mode in enters T and exits as the same sine shape with taller amplitude labeled scaled mode out, with the word eigenfunction nearby.
Style/medium: polished educational raster diagram, precise mathematical layout, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; main flow across the top; linearity and eigenfunction examples below; arrows clean and navy.
Color palette: white background; navy line work and labels; teal input/output curves; warm gold operator box and kernel accents; restrained red for scaling emphasis.
Text (verbatim): "f(t)", "T", "K(t,s)", "Tf(t)", "linearity", "operator", "mode in", "scaled mode out", "eigenfunction".
Constraints: labels must be large and crisp; use only the listed short labels; visually distinguish input function, operator, and output function; no Greek letters; no dense paragraphs; no equation-like extra text.
Avoid: decorative gradients, tiny labels, photorealism, stock imagery, external logos, extra equations, clutter, misspelled labels.
```

## Figure 12.3: Fourier Decomposition And Spectrum

- Saved path: `imagegen-figures/ch12-fourier-decomposition.png`
- Pedagogical purpose: Make Fourier coefficients visible as coordinates of a signal along sinusoidal modes.
- Section(s) supported: 12.3 Fourier series and Fourier transform.
- Exact mathematical objects shown: Periodic signal \(x(t)\), period \(T\), modes \(k=1,2,3\), partial sum reconstruction, and a sparse spectrum with coefficient magnitudes \(|c_k|\).
- What the reader should notice first: The signal is reconstructed by adding simpler sinusoidal modes, and the spectrum records how much of each mode is present.
- Necessary labels: `x(t)`, `k=1`, `k=2`, `k=3`, `partial sum`, `frequency`, `|c_k|`, `spectrum`, `modes`.
- How the text references the figure: Section 12.3 uses Figure~\ref{fig:ch12-fourier-decomposition} to explain Fourier modes, coefficients, partial sums, spectra, and frequency coordinates.
- Teaching caption: Fourier analysis represents a signal by sinusoidal modes. A periodic signal \(x(t)\) can be approximated by a partial sum of modes \(k=1,2,3,\ldots\). The spectrum records the coefficient magnitude \(|c_k|\), showing which frequency coordinates are large.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 12 Function Spaces, Operators, and Fourier Analysis
Primary request: Create a precise mathematical diagram showing Fourier decomposition: a periodic signal reconstructed from sine/cosine modes and represented by a frequency spectrum.
Scene/backdrop: clean white background, four coordinated panels with generous whitespace.
Subject: top left: a smooth periodic signal labeled x(t). Bottom left: three simpler sinusoidal modes labeled k=1, k=2, k=3 with different amplitudes. Center: a plus-sum visual leading to a reconstructed curve labeled partial sum. Right: a stem spectrum with horizontal axis frequency and vertical bars at k=1, k=2, k=3 labeled |c_k|.
Style/medium: polished educational raster diagram, precise geometry, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; signal and modes on left, reconstruction in center, spectrum on right; arrows show modes combine into signal.
Color palette: white background; navy axes and labels; teal curves; warm gold Fourier modes and spectrum bars; restrained red highlight for the largest coefficient.
Text (verbatim): "x(t)", "k=1", "k=2", "k=3", "partial sum", "frequency", "|c_k|", "spectrum", "modes".
Constraints: labels must be large and crisp; use only the listed short labels; show that coefficients measure how much of each mode is present; keep the spectrum sparse and readable.
Avoid: decorative gradients, tiny labels, photorealism, stock imagery, external logos, dense equations, clutter.
```

## Figure 12.4: Sampling, Aliasing, And Filters

- Saved path: `imagegen-figures/ch12-sampling-aliasing-filters.png`
- Pedagogical purpose: Show how discrete sampling can preserve low frequencies, alias high frequencies, and require anti-alias filtering before digitization or downsampling.
- Section(s) supported: 12.4 Sampling, aliasing, and filters.
- Exact mathematical objects shown: Sampled sequence \(x[n]=x(n\Delta t)\), sampling rate \(f_s\), high-frequency signal sharing samples with a lower-frequency alias, Nyquist limit \(f_s/2\), pre-sampling spectrum with high-frequency content, and low-pass filter response \(H(f)\).
- What the reader should notice first: Sparse sample dots can lie on both a fast sinusoid and a slower alias, so the discrete sequence alone is ambiguous.
- Necessary labels: `sampled signal`, `alias`, `x[n]=x(n Delta t)`, `f_s`, `f_s/2`, `Nyquist`, `frequency`, `H(f)`, `anti-alias filter`, `suppressed`.
- How the text references the figure: Section 12.4 uses Figure~\ref{fig:ch12-sampling-aliasing-filters} to explain discrete samples, the Nyquist threshold, aliasing, spectral overlap, and anti-alias low-pass filtering.
- Teaching caption: Sampling records a continuous signal only at discrete times. Frequencies above the Nyquist limit \(f_s/2\) can appear as lower-frequency aliases. An anti-alias low-pass filter suppresses frequencies above \(f_s/2\) before sampling so that the recorded sequence represents the intended band of the original signal.
- Comprehensive ImageGen prompt:

```text
Use case: scientific-educational
Asset type: lecture notes raster figure for Chapter 12 Function Spaces, Operators, and Fourier Analysis
Primary request: Create a precise mathematical diagram showing sampling, aliasing, Nyquist rate, and anti-alias filtering.
Scene/backdrop: clean white background, four coordinated panels with generous whitespace.
Subject: top left panel: a low-frequency sinusoid with black sample dots on the curve, labeled x[n]=x(n Delta t), showing enough dots to reconstruct. Top right panel: a high-frequency sinusoid with sparse sample dots that line up with a slower dashed sinusoid, labeled alias. Bottom left panel: frequency spectrum before sampling with a vertical marker labeled f_s/2 and high-frequency content beyond it. Bottom right panel: anti-alias low-pass filter response H(f) that passes frequencies below f_s/2 and suppresses content above f_s/2.
Style/medium: polished educational raster diagram, precise geometry, readable at PDF width, no stock-photo realism.
Composition/framing: landscape orientation; two time-domain panels on top, two frequency-domain panels below; consistent axes and sparse labels.
Color palette: white background; navy axes and labels; teal true signal curves; warm gold sample dots and filter passband; restrained red alias/high-frequency warning highlights.
Text (verbatim): "sampled signal", "alias", "x[n]=x(n Delta t)", "f_s", "f_s/2", "Nyquist", "frequency", "H(f)", "anti-alias filter", "suppressed".
Constraints: labels must be large and crisp; use only the listed short labels; show that two different continuous frequencies can share the same samples; no dense paragraphs.
Avoid: decorative gradients, tiny labels, photorealism, stock imagery, external logos, extra equations, clutter.
```
