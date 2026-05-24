### ch01-jacobian-eigenvalues-img

filename: `figures/imagegen/ch01-jacobian-eigenvalues-img.png`
chapter: 1
placement_target: Fixed Points and Local Stability
status: replace-existing
caption_intent: Show that local stability near a fixed point is diagnosed by the Jacobian spectrum: perturbations decay when eigenvalues lie in the stable half-plane and grow when one direction crosses into instability.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual schematic linking a neural state-space fixed point to the Jacobian eigenvalue plane. The image should make the local perturbation-recovery test visually obvious, contrasting a stable fixed point with an unstable direction.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use three clean zones from left to right: inward spiral flow around a fixed point, a central eigenvalue plane with a vertical stability boundary, and outward saddle-like flow with one growing perturbation direction. Keep the zones visually connected with thin arrows and generous whitespace.
Required visual elements: A fixed point dot with small perturbation arrows decaying inward, an eigenvalue plane with stable points on the left side and one unstable point on the right side, and a second local flow portrait showing an expanding direction. Use high-contrast stable versus unstable colors, such as teal for decay and vermilion for growth. This is a schematic concept diagram, not measured data.
Sparse in-image labels: x*, lambda, Re, Im, stable, unstable.
Style: Clean, modern, textbook-quality scientific diagram with crisp lines, muted background, high contrast, generous whitespace, no watermark, no logos, and no decorative stock imagery.
Avoid: Dense text, exact equations inside the generated image, cluttered vector fields, 3D effects, photorealistic neurons, decorative brain imagery, and any implication that the plotted points are empirical measurements.
"""
overlay_suggestion: Add exact axis labels `Re(lambda)` and `Im(lambda)`, plus optional small overlay conditions `Re(lambda)<0` and `Re(lambda)>0` if the generated text is unreliable.
review_notes: Check that stable eigenvalues are on the left of the vertical boundary, the unstable example has at least one point on the right, and flow arrows clearly show decay versus growth without extra invented labels.

### ch01-attractor-landscape-img

filename: `figures/imagegen/ch01-attractor-landscape-img.png`
chapter: 1
placement_target: Attractors and Basins
status: replace-existing
caption_intent: Explain multistability as a basin geometry: small perturbations remain in the same basin and return to the same attractor, while larger perturbations can cross a boundary and switch to another activity pattern.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual state-space landscape for a clustered neural network with two attractor basins separated by a basin boundary. The diagram should emphasize basin membership, return after a small kick, and switching after a larger kick.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a clean 2D contour or shallow landscape view with two wells, a separatrix ridge between them, and a few simple trajectory arrows. Leave open space around arrows and labels.
Required visual elements: Two attractor wells representing different active-cluster patterns, a clear basin boundary or separatrix, one short perturbation arrow that stays inside a basin and curls back, and one longer perturbation arrow that crosses the boundary into the other basin. This is a schematic concept diagram, not measured data.
Sparse in-image labels: A1, A2, basin, boundary, small, large.
Style: Clean, modern, textbook-quality scientific diagram with high contrast, generous whitespace, readable shapes, no watermark, no logos, and no decorative stock imagery.
Avoid: Dense explanatory text, exact equations in the image, realistic terrain, decorative neural icons, overly complex trajectories, and ambiguous basin boundaries.
"""
overlay_suggestion: Add exact labels `A_1`, `A_2`, and `basin boundary` after generation if needed; keep detailed explanation in the LaTeX caption.
review_notes: Check that the small perturbation remains in the original basin, the large perturbation crosses the separatrix, and the landscape reads as state space rather than a literal physical terrain.

### ch01-lyapunov-stretch-fold-img

filename: `figures/imagegen/ch01-lyapunov-stretch-fold-img.png`
chapter: 1
placement_target: Chaos and Lyapunov Exponents
status: new
caption_intent: Introduce Lyapunov sensitivity by showing nearby initial states that stretch apart along an unstable direction, fold back into a bounded region, and produce separation growth before saturation.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual stretch-and-fold schematic for deterministic chaos in mesoscopic neural state space. The image should show two initially nearby trajectories separating while remaining confined to a bounded attractor-like region.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a left-to-right sequence: two nearly overlapping starting points, a ribbon of state space stretching apart, and a folded bounded flow region. Include a small inset curve showing separation increasing and then saturating, but keep it schematic.
Required visual elements: Two nearby trajectory paths with matching starting marks, visible local stretching, a fold that returns paths into the bounded region, and a compact separation inset. Use arrows to indicate time direction and make the stretching/folding mechanism the main visual. This is a schematic concept diagram, not measured data.
Sparse in-image labels: x, x', Delta, lambda, stretch, fold.
Style: Clean, modern, textbook-quality scientific diagram with crisp curves, high contrast, generous whitespace, no watermark, no logos, and no decorative stock imagery.
Avoid: Exact equations inside the generated image, chaotic-looking clutter, random spaghetti traces, photorealistic backgrounds, 3D tunnels, and any suggestion that the inset is fitted experimental data.
"""
overlay_suggestion: Add exact overlay text `Delta(t)` and optionally `Delta(t) ~ Delta(0) exp(lambda t)` and `lambda > 0` if this precision is needed in the final figure.
review_notes: Check that the two trajectories begin very close, separate visibly before saturation, and remain bounded; avoid outputs that only show noise or an unbounded explosion.

### ch02-spike-filtering-img

filename: `figures/imagegen/ch02-spike-filtering-img.png`
chapter: 2
placement_target: Synaptic Filtering and Shot Noise
status: replace-existing
caption_intent: Show how point-process spike events become continuous activity through synaptic filtering, and how averaging many filtered traces produces a mesoscopic population variable.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic pipeline from discrete spikes to filtered single-neuron activity to a smoothed population activity for a neural cluster. The diagram should teach the transition from point events to continuous mesoscopic variables.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use three aligned horizontal bands or panels: top band with sparse spike ticks, middle band with exponential filter pulses summing into a continuous trace, and bottom band with several faint individual traces averaging into one smoother population trace. Connect bands with simple downward arrows.
Required visual elements: Discrete spike marks, an exponential filter shape, a filtered shot-noise trace, multiple faint neuron traces, and one bold averaged cluster trace. Use restrained color coding and ample spacing. This is a schematic concept diagram, not measured data.
Sparse in-image labels: s_i, epsilon, r_i, R_a, spikes, average.
Style: Clean, modern, textbook-quality scientific diagram with crisp traces, high contrast, generous whitespace, no watermark, no logos, and no decorative stock imagery.
Avoid: Dense text, exact convolution equations in the generated image, raster plots that look like real data, decorative neuron drawings, and excessive tick marks or gridlines.
"""
overlay_suggestion: Add exact labels `s_i(t)`, `epsilon(t)`, `r_i(t)=(epsilon*s_i)(t)`, and `R_a^alpha(t)` after generation if needed.
review_notes: Check that filtering smooths spikes rather than replacing them with unrelated waves, the population trace is visibly smoother than single-neuron activity, and labels remain sparse.

### ch02-noise-scaling-img

filename: `figures/imagegen/ch02-noise-scaling-img.png`
chapter: 2
placement_target: Finite-Size Scaling and the Noise Coordinate
status: replace-existing
caption_intent: Convey that finite-size fluctuations shrink with population size, motivating xi as the natural coordinate for separating noise-driven switching from deterministic mesoscale dynamics.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual finite-size noise scaling diagram for population activity. The image should contrast noisy small-population averages with smoother large-population averages and connect this to a decreasing fluctuation scale.
Composition: 16:10 horizontal composition suitable for a PDF figure. Split the figure into a left comparison of two population activity traces and a right schematic scaling plot. On the left, show the same mean activity with large fluctuations for small population size and smaller fluctuations for large population size. On the right, show a descending envelope or curve for fluctuation size versus increasing N_E, with xi indicated as the derived noise coordinate that decreases as N_E grows.
Required visual elements: Two schematic traces around the same mean level, visible reduction in fluctuation amplitude, a simple scaling plot that decreases from small N_E to large N_E, and a visual connection from larger population size to smaller noise. This is a schematic concept diagram, not measured data.
Sparse in-image labels: N_E, xi, noise, small, large, scaling.
Style: Clean, modern, textbook-quality scientific diagram with high contrast, generous whitespace, restrained colors, no watermark, no logos, and no decorative stock imagery.
Avoid: Exact equations inside the generated image, fake scatter that appears measured, busy axes, decorative backgrounds, and implying the trend was fitted from data.
"""
overlay_suggestion: Add exact overlay labels `xi=1/sqrt(N_E)`, `SD proportional to 1/sqrt(N_E)`, and simple axis labels `N_E` and `fluctuation size` if the generated text is unreliable.
review_notes: Check that the visual trend decreases as N_E increases, with xi treated as decreasing along that direction, and that the small-versus-large population traces share the same mean rather than different regimes.

### ch02-autocorrelation-signatures-img

filename: `figures/imagegen/ch02-autocorrelation-signatures-img.png`
chapter: 2
placement_target: Autocorrelations
status: new
caption_intent: Compare qualitative autocorrelation signatures for point-process spikes, filtered shot noise, and smooth deterministic rate fluctuations, highlighting the zero-lag peak or kink used later as a diagnostic.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual comparison of autocorrelation shapes used in stochastic neural dynamics. The figure should distinguish a spike-train zero-lag impulse, a filtered shot-noise cusp, and a smooth rounded autocorrelation for differentiable rate dynamics.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use three side-by-side mini-panels with aligned horizontal tau axes and a shared visual zero-lag reference line. Keep each panel simple, with one bold curve per panel and enough whitespace to compare shapes at tau=0.
Required visual elements: A narrow vertical zero-lag spike in the first panel, a symmetric cusp-shaped exponential-like curve in the second panel, and a smooth rounded peak with flat slope at zero lag in the third panel. Use subtle color differences and a consistent axis style. This is a schematic concept diagram, not measured data.
Sparse in-image labels: C(tau), tau, spike, filtered, smooth, kink.
Style: Clean, modern, textbook-quality scientific diagram with crisp curves, high contrast, generous whitespace, no watermark, no logos, and no decorative stock imagery.
Avoid: Exact formulas inside the generated image, dense legends, noisy empirical-looking traces, too many curves, and labels that obscure the zero-lag comparison.
"""
overlay_suggestion: Add exact labels `C_s(tau)`, `C_r(tau)`, `C_R(tau)`, `tau=0`, and optional `C'(0)=0` for the smooth panel if needed.
review_notes: Check that the filtered curve has a visible cusp at zero lag, the smooth curve has a rounded top rather than a kink, and the panels do not look like measured simulation results.

### ch03-lif-threshold-reset-img

filename: `figures/imagegen/ch03-lif-threshold-reset-img.png`
chapter: 3
placement_target: The Leaky Integrate-and-Fire Model
status: replace-existing
caption_intent: Show that the LIF neuron has continuous subthreshold voltage dynamics, but spike output is created by a threshold crossing followed by reset. The diagram should make clear that spikes are events generated by voltage, not values of a smooth rate variable.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic LIF threshold-reset teaching diagram. Show a membrane voltage trace integrating upward under input, crossing threshold to emit a spike event, then dropping immediately to reset before beginning another integration cycle. Mark the diagram as conceptual and not measured data.
Composition: 16:10 horizontal composition suitable for a PDF figure, with a dominant voltage-versus-time panel and a compact aligned spike-event row underneath. Use left-to-right time flow, generous whitespace, and clear visual hierarchy.
Required visual elements: Smooth voltage trajectory, horizontal threshold guide, horizontal reset guide, sharp spike tick at threshold crossing, vertical reset drop, small input-current pulses or shaded drive region, and arrows that distinguish threshold crossing from reset.
Sparse in-image labels: `V`, `t`, `V_theta`, `V_r`, `spike`, `reset`
Style: Clean, modern, textbook-quality raster diagram with high contrast, crisp lines, muted scientific colors, generous margins, no watermark, no logos, and no decorative stock imagery.
Avoid: Long equations, dense callout text, realistic neuron anatomy, oscilloscope-like measured-data styling, unreadable tick labels, cluttered spikes, 3D effects, shadows, and decorative backgrounds.
"""
overlay_suggestion: Add exact LaTeX labels `$V_\theta$`, `$V_r$`, and `spike at threshold` after generation if the image text is unreliable.
review_notes: Check that the reset occurs after threshold crossing rather than before it, that the voltage trace is continuous between events, and that the spike row is clearly an event record rather than a second voltage trace.

### ch03-transfer-function-img

filename: `figures/imagegen/ch03-transfer-function-img.png`
chapter: 3
placement_target: Transfer Functions
status: replace-existing
caption_intent: Explain a transfer function as a statistical input-output map from stationary input statistics to expected firing rate. The visual should contrast a hard deterministic threshold with a noise-softened curve and an adapted/GIF curve with reduced gain.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual input-output transfer-function diagram for a spiking neuron. Show firing rate increasing with mean input, with three schematic curves: a sharp deterministic threshold, a smoother noisy LIF response, and an adapted/GIF response with reduced high-drive gain. Make clear this is an average response, not a single voltage trajectory.
Composition: 16:10 horizontal composition suitable for a PDF figure, centered on a clean coordinate plot with a small visual cue for input noise near threshold. Keep the curves spacious and easy to distinguish.
Required visual elements: Horizontal input axis, vertical firing-rate axis, sharp threshold-like curve, smooth noise-softened curve, lower-gain adaptation curve, and a subtle shaded transition band near threshold.
Sparse in-image labels: `mu`, `phi`, `sigma`, `LIF`, `noise`, `adapt`
Style: Clean, modern, textbook-quality raster diagram with generous whitespace, high contrast, restrained color coding for the three curves, no watermark, no logos, and no decorative stock imagery.
Avoid: Exact formulas inside the image, many numeric ticks, fake empirical scatter points, measured-data styling, dense legends, complex axes, decorative neurons, and text-heavy annotations.
"""
overlay_suggestion: Add exact axis labels `$\mu$` and `$\phi(\mu,\sigma)$`, plus curve labels `deterministic`, `noisy LIF`, and `adapted/GIF` after generation if needed.
review_notes: Check that the noisy curve is softened below nominal threshold, the adaptation curve has visibly lower gain at high input, and the diagram does not imply that `phi` is a membrane voltage.

### ch03-gif-adaptation-img

filename: `figures/imagegen/ch03-gif-adaptation-img.png`
chapter: 3
placement_target: Generalized Integrate-and-Fire Models
status: new
caption_intent: Introduce GIF history dependence by showing that each spike can raise an adaptation current and a dynamic threshold, both of which decay over time. The diagram should connect recent spike history to reduced near-term excitability without adding detailed channel biophysics.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic generalized integrate-and-fire adaptation diagram. Show a voltage trace with threshold/reset events, an adaptation current trace that jumps after spikes and decays slowly, and a dynamic threshold trace that rises after spikes then relaxes toward baseline. Mark the figure as conceptual, not measured data.
Composition: 16:10 horizontal composition suitable for a PDF figure, using three vertically aligned time traces with shared left-to-right time axis and small arrows from spike events to the adaptation and threshold traces.
Required visual elements: Top voltage trace with spikes and resets, middle adaptation trace with step-like jumps and exponential decays, lower dynamic-threshold trace with spike-triggered jumps and relaxation, plus light alignment guides linking spikes across traces.
Sparse in-image labels: `V`, `a`, `theta`, `spike`, `reset`, `history`
Style: Clean, modern, textbook-quality raster infographic with high contrast, sparse labels, generous whitespace, consistent line weights, no watermark, no logos, and no decorative stock imagery.
Avoid: Detailed ion-channel cartoons, exact GIF equations in the image, too many spike events, unreadable parameter labels, photorealistic cells, fake measured recordings, and cluttered explanatory text.
"""
overlay_suggestion: Add exact labels `$a(t)$`, `$\theta(t)$`, `$\theta_0$`, `$q_a$`, and `$q_\theta$` after generation if the traces are clear but labels are unreliable.
review_notes: Check that adaptation and threshold increase after spikes and then decay, that these history variables are visually separate from membrane voltage, and that the figure does not look like a conductance-channel model.

### ch04-balance-cancellation-img

filename: `figures/imagegen/ch04-balance-cancellation-img.png`
chapter: 4
placement_target: Mean Balance
status: replace-existing
caption_intent: Show that balanced networks can have large excitatory and inhibitory currents whose mean components nearly cancel, leaving a smaller residual drive near threshold. The visual should shift attention from the large components to the residual fluctuations that drive irregular spiking.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual balanced E/I cancellation diagram. Show large positive excitation and large negative inhibition as structured opposing current traces, with their sum shown separately as a much smaller residual fluctuating near a threshold band. Mark the traces as schematic, not measured data.
Composition: 16:10 horizontal composition suitable for a PDF figure, with two large opposing current components in the upper area and a smaller residual trace below. Use visual alignment so the cancellation relationship is obvious.
Required visual elements: Positive excitatory current trace, negative inhibitory current trace, subtle cancellation arrows toward a residual panel, small residual input fluctuating around a threshold guide, and clear color distinction between E, I, and residual.
Sparse in-image labels: `E`, `I`, `E+I`, `residual`, `threshold`
Style: Clean, modern, textbook-quality raster infographic with generous whitespace, high contrast, crisp traces, restrained scientific palette, no watermark, no logos, and no decorative stock imagery.
Avoid: Exact balance equations in the image, noisy empirical-looking traces, too many overlapping currents, decorative brain imagery, saturated colors, 3D rendering, dense legends, and unreadable axis text.
"""
overlay_suggestion: Add exact labels `$KJr_E$`, `$-gKJr_I$`, `residual input`, and `near threshold` after generation if needed.
review_notes: Check that E and I are both large in magnitude, that inhibition is visually negative or opposing excitation, and that the residual is clearly smaller rather than another large current.

### ch04-sparse-fixed-indegree-img

filename: `figures/imagegen/ch04-sparse-fixed-indegree-img.png`
chapter: 4
placement_target: Sparse Random Connectivity with Fixed In-Degree
status: replace-existing
caption_intent: Explain sparse fixed-in-degree wiring as random source identity with controlled source counts. The diagram should show that a target population receives exactly fixed numbers of excitatory and inhibitory inputs, while the chosen source identities remain quenched.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic sparse fixed-in-degree connectivity diagram for a balanced E/I network. Show many candidate source populations, highlight a fixed number of selected excitatory and inhibitory sources, and route them to one postsynaptic target population. Make clear that the selected identities are random but frozen.
Composition: 16:10 horizontal composition suitable for a PDF figure, with candidate source populations on the left in two organized rows and one target population on the right. Use highlighted arrows only for selected sources and faded styling for unselected sources.
Required visual elements: Row of candidate E sources, row of candidate I sources, fixed selected subset of each row, arrows converging to one target, small count badges for selected E and I inputs, and a subtle indication that unselected candidates do not project.
Sparse in-image labels: `E`, `I`, `K_E`, `K_I`, `target`, `quenched`
Style: Clean, modern, textbook-quality raster infographic with generous whitespace, high contrast, simple node glyphs, clear arrow routing, no watermark, no logos, and no decorative stock imagery.
Avoid: All-to-all connectivity, variable numbers of incoming arrows, hairball graph layouts, exact equations inside the image, tiny node labels, ambiguous arrow direction, decorative neural silhouettes, and random-looking clutter.
"""
overlay_suggestion: Add exact labels `$K_E=fK$`, `$K_I=(1-f)K$`, and `fixed counts, random identities` after generation if the generated count text is unreliable.
review_notes: Check that the number of highlighted E and I inputs appears fixed and countable, that unselected sources are visibly present but inactive, and that the target receives sparse rather than dense all-to-all input.

### ch04-inhibition-stabilized-loop-img

filename: `figures/imagegen/ch04-inhibition-stabilized-loop-img.png`
chapter: 4
placement_target: Inhibition-Stabilized Dynamics
status: new
caption_intent: Show the ISN mechanism: the excitatory subnetwork alone would amplify an excitatory perturbation, but the full E/I loop recruits inhibition that suppresses excitation and stabilizes the fixed point. The diagram should prepare readers to see inhibition as the stabilizing feedback pathway.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual inhibition-stabilized network diagram. Contrast an E-only positive-feedback loop that moves away from a fixed point with a full E/I loop where an excitatory perturbation recruits inhibition and returns activity toward the fixed point. Mark the figure as schematic, not measured data.
Composition: 16:10 horizontal composition suitable for a PDF figure, split into two clean side-by-side panels: left panel for unstable E-only feedback, right panel for stable E/I feedback. Keep the right panel slightly larger or visually emphasized.
Required visual elements: Left E node with self-excitatory loop and outward perturbation arrow, right E and I nodes with E-to-I excitation and I-to-E suppression, a damping return arrow toward a fixed point, and a small state-space inset showing divergence versus return.
Sparse in-image labels: `E`, `I`, `ISN`, `unstable`, `stable`, `feedback`
Style: Clean, modern, textbook-quality raster infographic with high contrast, generous whitespace, clear arrowheads, restrained color coding for excitation and inhibition, no watermark, no logos, and no decorative stock imagery.
Avoid: Full matrix equations inside the image, dense network graphs, ambiguous inhibitory signs, fake simulation data, excessive labels, decorative brain images, 3D effects, and cluttered phase portraits.
"""
overlay_suggestion: Add exact labels `$-1+\phi_E'w_{EE}>0$`, `full E/I Jacobian stable`, `$w_{IE}$`, and `$w_{EI}$` after generation if needed.
review_notes: Check that the E-only panel is unstable while the E/I panel is stable, that inhibition is shown as suppressing excitation rather than exciting it, and that the feedback loop is visually readable at PDF figure size.

### ch05-clustered-connectivity-matrix-img

filename: `figures/imagegen/ch05-clustered-connectivity-matrix-img.png`
chapter: 5
placement_target: Intra-Cluster Potentiation and Inter-Cluster Depression (sec:intra-inter-weights)
status: replace-existing
caption_intent: Show how potentiated diagonal EE blocks and depressed off-diagonal EE blocks create cell assemblies as coarse dynamical units while preserving the idea that the diagram is still about structured neuron-to-neuron recurrence.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic teaching diagram of clustered excitatory connectivity in an E-clustered network with shared inhibition. Emphasize a block matrix whose diagonal blocks are strong within-cluster recurrence and whose off-diagonal blocks are weaker between-cluster recurrence; make clear this is conceptual structure, not measured data.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a large block-matrix heatmap on the left with four or five square cluster blocks, and a compact network abstraction on the right showing several excitatory assemblies coupled to one shared inhibitory pool. Use arrows to connect the matrix blocks to the assembly interpretation.
Required visual elements: high-contrast diagonal blocks, muted off-diagonal blocks, visible block boundaries, a few cluster-circle assemblies, strong self-recurrence cues on assemblies, weak cross-assembly cues, and a shared inhibitory pool drawn as a separate stabilizing node.
Sparse in-image labels: E, I, J_E+, J_E-, Q
Style: clean, modern, textbook-quality lecture-note raster infographic with generous whitespace, crisp edges, restrained color accents, and readable geometry. Use high contrast, no watermark, no logos, no decorative stock imagery.
Avoid: exact equations inside the image, dense legends, decorative neural-network art, photorealistic brains, random-looking measured heatmaps, axis ticks, tiny unreadable labels, and implying the block matrix is experimental data.
"""
overlay_suggestion: Add exact labels after generation if needed: diagonal blocks `\hat J^{EE}` or `J_E+`, off-diagonal blocks `\check J^{EE}` or `J_E-`, and optionally the caption-side equation `\hat J^{EE}+(Q-1)\check J^{EE}=QJ^{EE}`.
review_notes: Check that the diagonal blocks are visibly stronger than off-diagonal blocks, the inhibitory pool is shared rather than cluster-paired, and the figure does not become a generic connectome or decorative brain image.

### ch05-active-inactive-landscape-img

filename: `figures/imagegen/ch05-active-inactive-landscape-img.png`
chapter: 5
placement_target: Multistability (sec:cluster-multistability)
status: replace-existing
caption_intent: Explain active-cluster patterns as metastable basins in a coarse state space, with finite-size fluctuations occasionally pushing the system across a saddle into a different active set.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual basin-landscape diagram for clustered attractor dynamics. Show several metastable basins representing different active-cluster patterns, with a trajectory that dwells in one basin, crosses a saddle under finite-size fluctuation, and settles into another basin. Make the landscape explicitly schematic.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a smooth three-basin landscape or projected state-space surface spanning the full width, with basin minima separated by low ridges and a clear hopping trajectory from left basin to center or right basin.
Required visual elements: three distinct basins, small state marker or trajectory path, one saddle or basin boundary, subtle arrows showing relaxation within basins, a larger arrow showing a noise-driven hop, and simple cluster-state glyphs near each basin with active clusters highlighted.
Sparse in-image labels: S1, S2, S3, saddle, xi
Style: clean, modern, textbook-quality lecture-note raster infographic with generous whitespace, high contrast, no watermark, no logos, and no decorative stock imagery. Use muted basin shading with a bright path arrow so the dynamical story is obvious.
Avoid: photorealistic landscapes, dense equations, long active-set text, overly literal 3D terrain, decorative particles, measured-data styling, and any implication that the system is a true low-dimensional gradient landscape.
"""
overlay_suggestion: Replace generated basin labels if needed with exact active-set examples such as `S={1,4}` and `S={2,3,5}`, plus the fluctuation label `\xi`.
review_notes: Check that the image reads as a schematic high-dimensional projection, that basin hopping is caused by finite-size fluctuation rather than deterministic chaos, and that labels stay sparse and legible.

### ch05-size-dependent-switching-img

filename: `figures/imagegen/ch05-size-dependent-switching-img.png`
chapter: 5
placement_target: Metastable Switching and Finite-Size Noise (sec:finite-size-switching)
status: new
caption_intent: Make the finite-size prediction visually explicit: smaller clusters have larger fluctuation scale and frequent active-set switching, while larger clusters have smaller fluctuations and longer-lived attractor-like states.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic comparison of finite-size metastable switching for small versus large clusters. Show that larger per-cluster population size reduces the noise scale and makes basin crossings rarer, without presenting the curves as measured simulation data.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use two horizontally aligned panels: left panel for smaller clusters with a noisy trajectory crossing between two shallow basins and a rapidly switching two-level activity trace; right panel for larger clusters with smaller fluctuations confined inside one basin and a mostly stable activity trace.
Required visual elements: paired basin cartoons, paired schematic time traces underneath or beside them, visibly larger fluctuation envelope on the small-cluster side, visibly smaller fluctuation envelope on the large-cluster side, and arrows indicating rarer basin crossing as cluster size grows.
Sparse in-image labels: N_c=107, N_c=250, xi, S(t), time
Style: clean, modern, textbook-quality lecture-note raster infographic with generous whitespace, high contrast, no watermark, no logos, no decorative stock imagery. Keep axes minimal and schematic, with no tick marks or numerical claims beyond the sparse labels.
Avoid: exact equations inside the generated image, noisy plots that look like real data, too many traces, unreadable axis labels, photorealistic backgrounds, and suggesting that the two example cluster sizes are universal constants.
"""
overlay_suggestion: Add exact caption or overlay equation after generation if needed: `\xi=1/\sqrt{n_E}`; keep `N_c=107` and `N_c=250` only as illustrative roadmap examples.
review_notes: Check that switching frequency decreases with larger cluster size, that the diagram remains schematic rather than empirical, and that the basin/traces comparison does not imply a change in deterministic parameters other than finite-size scale.

### ch06-random-rate-phase-portrait-img

filename: `figures/imagegen/ch06-random-rate-phase-portrait-img.png`
chapter: 6
placement_target: Random Recurrent Coupling (sec:ch06-random-coupling)
status: replace-existing
caption_intent: Contrast subcritical random-rate dynamics that contract to a fixed point with supercritical dynamics where recurrent amplification creates local expansion, nonlinear folding, and bounded irregular motion.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic phase-portrait comparison for the SCS random rate transition. Show the left regime contracting toward a stable fixed point when recurrent gain is below criticality, and the right regime expanding and folding into bounded irregular motion when recurrent gain is above criticality. Make clear this is a two-dimensional projection of high-dimensional dynamics.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use two side-by-side panels with matching axes and visual scale: left panel has a vector field spiraling or flowing inward to a fixed point; right panel has local expansion arrows, a folded ribbon-like trajectory, and bounded state-space containment.
Required visual elements: stable fixed point on the left, inward arrows, supercritical trajectory on the right, local stretching arrows, nonlinear folding, and a soft boundary indicating bounded activity due to saturation.
Sparse in-image labels: g<1, g>1, x1, x2, lambda<0, lambda>0
Style: clean, modern, textbook-quality lecture-note raster infographic with generous whitespace, high contrast, no watermark, no logos, no decorative stock imagery. Use restrained colors to separate contraction from chaos and keep labels short.
Avoid: exact SCS equations in the image, dense vector fields, chaotic scribbles without folding structure, implying the real SCS state space is only two-dimensional, decorative fractal art, and measured simulation traces.
"""
overlay_suggestion: Add exact labels after generation if needed: `g<g_c`, `g>g_c`, `\lambda_{\max}<0`, `\lambda_{\max}>0`, and projected axes `x_1`, `x_2`.
review_notes: Check that the left panel clearly contracts, the right panel shows both stretching and bounded folding, and the image does not confuse deterministic chaos with unbounded divergence.

### ch06-scs-autocorrelation-transition-img

filename: `figures/imagegen/ch06-scs-autocorrelation-transition-img.png`
chapter: 6
placement_target: Autocorrelations Across the Transition (sec:ch06-autocorrelation-transition)
status: replace-existing
caption_intent: Show autocorrelation as the observable that changes across the SCS transition: fast decay below threshold, broadening near criticality, and a smooth zero-lag chaotic shoulder above threshold.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic autocorrelation comparison across the SCS transition. Show three clean curves: subcritical fast decay, near-critical broad decay, and supercritical chaotic autocorrelation with a smooth rounded peak at zero lag. Explicitly make it a conceptual diagnostic plot, not measured data.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use one wide plot with three color-separated curves over lag, or three small aligned panels sharing the same vertical scale. Reserve whitespace around the zero-lag region so smoothness versus sharp kinks is visually clear.
Required visual elements: central zero-lag peak, curve that decays quickly, broader near-critical curve, smooth chaotic curve, visual indication that correlation width increases near transition, and a subtle callout around zero lag showing no cusp for the chaotic rate curve.
Sparse in-image labels: C(tau), tau, g<1, g~1, g>1, smooth
Style: clean, modern, textbook-quality lecture-note raster infographic with generous whitespace, high contrast, no watermark, no logos, no decorative stock imagery. Use crisp curves, minimal axes, and sparse labels only.
Avoid: exact equations inside the generated image, noisy empirical-looking traces, tick-heavy scientific plotting, sharp cusp on the chaotic curve, long legends, and implying the subcritical curve is self-sustained deterministic chaos.
"""
overlay_suggestion: Add exact labels after generation if needed: `C_r(\tau)`, `g<g_c`, `g\simeq g_c`, `g>g_c`, and `C_r'(0)=0` near the smooth chaotic peak.
review_notes: Check that the supercritical curve is smooth at zero lag, the near-critical curve is visibly broadened, and the subcritical curve is interpreted as decay or response rather than self-sustained chaotic autocorrelation.

### ch06-chaotic-flow-folding-img

filename: `figures/imagegen/ch06-chaotic-flow-folding-img.png`
chapter: 6
placement_target: Lyapunov Diagnostics (sec:ch06-lyapunov)
status: new
caption_intent: Illustrate the Lyapunov mechanism behind deterministic chaos: nearby trajectories separate along expanding directions, then nonlinear saturation folds them back into a bounded region so trajectories diverge without blowing up.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual state-space flow diagram showing stretch-and-fold dynamics for a chaotic rate network. Show a tiny bundle of nearby initial conditions separating along an unstable direction, then folding back inside a bounded region due to nonlinear saturation. Mark the diagram as schematic rather than a measured trajectory.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a left-to-right progression across a single projected state space: small nearby bundle on the left, stretched sheet or ribbon in the center, folded bounded ribbon on the right. Include arrows for the flow direction and leave generous whitespace for later captioning.
Required visual elements: nearby initial points, growing separation, elongated ribbon, folded return path, bounded state-space envelope, and a small diagnostic inset or visual cue for positive Lyapunov growth.
Sparse in-image labels: x(t), delta x, lambda>0, stretch, fold, bounded
Style: clean, modern, textbook-quality lecture-note raster infographic with generous whitespace, high contrast, no watermark, no logos, no decorative stock imagery. Use crisp vector-like forms rendered as raster and restrained color coding for the two nearby trajectories.
Avoid: exact equations in the image, decorative fractals, fluid turbulence imagery, dense phase-space scribbles, unbounded explosion visuals, and any claim that the drawing is a numerical simulation.
"""
overlay_suggestion: Add exact labels after generation if needed: `\delta x(t)`, `\lambda_{\max}>0`, and optionally `\|\delta x(t)\|` for the small growth cue.
review_notes: Check that the mechanism reads as local divergence plus global boundedness, not just tangled lines; ensure the two nearby trajectories are initially close and only later separate.

### ch07-quenched-vs-annealed-disorder-img

filename: `figures/imagegen/ch07-quenched-vs-annealed-disorder-img.png`
chapter: 7
placement_target: Section: Quenched and Annealed Disorder
status: replace-existing
caption_intent: Show that quenched disorder is a frozen recurrent structure that shapes one deterministic vector field, while annealed disorder is redrawn over time or trials and therefore represents a different kind of variability.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual side-by-side comparison of quenched versus annealed disorder in recurrent neural dynamics. The left side should show one fixed random connectivity matrix feeding a stable state-space flow with repeated trajectories shaped by the same frozen geometry. The right side should show a sequence of changing matrices feeding a unit over time or trials, making the input variability look redrawn rather than embedded in one vector field.
Composition: 16:10 horizontal composition suitable for a PDF figure. Divide the canvas into two balanced panels with a clear central gutter; use arrows from matrices to flow or trace sketches, with generous whitespace and a calm textbook layout.
Required visual elements: Left panel: one matrix block with fixed speckled entries, a small state-space path, and multiple trajectories passing through the same flow. Right panel: three small matrix blocks in a time sequence, each slightly different, feeding a simple time trace or representative unit. Make the figure explicitly schematic, not measured data.
Sparse in-image labels: `quenched`, `annealed`, `fixed J`, `new J`, `t`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, crisp vector-like forms rendered as raster, restrained color, generous whitespace, no watermark, no logos, no decorative stock imagery.
Avoid: Dense paragraphs, exact equations, fake numerical data, photorealistic brains, decorative network art, illegible matrix text, cluttered arrows, and any implication that the traces are measured experimental recordings.
"""
overlay_suggestion: If text is unreliable, overlay only `quenched`, `annealed`, `fixed J`, and `new J(t)`; keep the detailed definition of quenched versus annealed disorder in the caption.
review_notes: Check that the quenched side uses the same fixed matrix throughout, while the annealed side visibly redraws the matrix. Check that the visual distinction is structural, not merely two different noise traces.

### ch07-dmft-self-consistency-loop-img

filename: `figures/imagegen/ch07-dmft-self-consistency-loop-img.png`
chapter: 7
placement_target: Section: The DMFT Effective Process
status: replace-existing
caption_intent: Present DMFT as a closure loop: assumed network statistics define an effective stochastic unit, the unit produces mean activity and autocorrelation, and those output statistics must reproduce the input statistics that drove it.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic DMFT self-consistency loop for a random recurrent rate network. The diagram should make clear that a high-dimensional random network is replaced by one representative effective unit driven by a mean input, a static quenched bias, and a dynamic fluctuation, then the unit's output statistics close the loop.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a clockwise loop with four stations: network statistics, effective unit, output traces/statistics, and covariance closure returning to the input. Keep the loop open and readable with broad whitespace.
Required visual elements: A compact random network icon or matrix block, a single effective unit with an input arrow, a small static offset symbol beside a wavy dynamic trace, and an output autocorrelation curve feeding back to the input statistics. Make all curves schematic and smooth.
Sparse in-image labels: `network`, `unit`, `eta0`, `zeta(t)`, `m`, `C(tau)`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, crisp arrows, generous whitespace, no watermark, no logos, no decorative stock imagery.
Avoid: Exact closure equations inside the image, dense explanatory text, fake measured axes, excessive labels, decorative neural-network wallpaper, and ambiguous arrows that do not form a closed loop.
"""
overlay_suggestion: Overlay `eta_0`, `zeta(t)`, `m`, and `C_r(tau)` if needed; reserve equations such as `<eta_0^2>=g^2 m^2` and `<zeta(t)zeta(t+tau)>=g^2 C_r(tau)` for the LaTeX caption or nearby notes.
review_notes: Check that the figure reads as a self-consistency cycle rather than a one-way pipeline. Check that static bias and dynamic fluctuation are visually distinct.

### ch07-static-dynamic-mean-field-split-img

filename: `figures/imagegen/ch07-static-dynamic-mean-field-split-img.png`
chapter: 7
placement_target: Section: The DMFT Effective Process
status: new
caption_intent: Clarify the nonzero-mean DMFT decomposition by separating stationary quantities, including the mean input and static quenched bias, from connected time-dependent fluctuations and their autocorrelation closure.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual split diagram for nonzero-mean DMFT that separates static mean-field components from dynamic connected components. The figure should show that the mean rate produces a mean input and a frozen bias, while deviations around the mean produce a time-varying process with a connected autocorrelation.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use two horizontal lanes or stacked bands: a top static lane with steady blocks and a bottom dynamic lane with wavy traces. Connect the lanes lightly at the representative unit so the split is clear but still part of one effective process.
Required visual elements: Top lane: a steady rate block leading to a mean input and a fixed offset marker. Bottom lane: a fluctuation trace leading to a dynamic input trace and an autocorrelation curve. Include one representative unit in the center receiving both static and dynamic components. Mark the entire figure as schematic through visual style, not large text.
Sparse in-image labels: `m`, `mu`, `eta0`, `zeta(t)`, `C(tau)`
Style: Clean, modern, textbook-quality scientific diagram with generous whitespace, high contrast, restrained color coding for static versus dynamic components, no watermark, no logos, no decorative stock imagery.
Avoid: Full equations in the image, long labels, measured-data styling, noisy decorative traces, excessive color, and any suggestion that the static component fluctuates in time.
"""
overlay_suggestion: Overlay `mu`, `eta_0`, `zeta(t)`, `m`, and `C_r(tau)` if needed; exact raw-moment and connected-covariance equations should remain in the caption or text.
review_notes: Check that the top lane is visibly time-independent and the bottom lane is visibly connected fluctuation dynamics. Check that `eta0` is not drawn as ordinary annealed noise.

### ch08-paired-ei-clusters-img

filename: `figures/imagegen/ch08-paired-ei-clusters-img.png`
chapter: 8
placement_target: Section: Why Cluster Inhibition?
status: replace-existing
caption_intent: Explain a paired E/I cluster as a two-population mesoscale unit with potentiated within-pair E and I motifs and depressed between-pair interactions that preserve balanced recurrent drive.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic of paired excitatory-inhibitory clusters. Each cluster should contain one excitatory population and one inhibitory population, with strengthened within-pair interactions and weaker depressed interactions between distinct pairs. The diagram should make the pair look like a single mesoscale unit rather than two unrelated populations.
Composition: 16:10 horizontal composition suitable for a PDF figure. Arrange three paired clusters across the canvas, each as a compact E/I module, with the central pair emphasized and neighboring pairs slightly smaller. Use arrows for within-pair and between-pair couplings without overcrowding.
Required visual elements: Within each pair, show an E node and an I node with internal arrows. Use thicker arrows for potentiated within-pair couplings and thinner muted arrows for between-pair couplings. Include a subtle block-matrix inset showing strong diagonal pair blocks and weaker off-diagonal blocks. The figure is conceptual and schematic.
Sparse in-image labels: `E`, `I`, `J_E+`, `J_I+`, `J_E-`, `J_I-`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, readable arrows, generous whitespace, no watermark, no logos, no decorative stock imagery.
Avoid: Crowded all-to-all wiring, full equations, long explanatory labels, photorealistic neurons, decorative graph art, and colors that make excitation and inhibition hard to distinguish.
"""
overlay_suggestion: Overlay simple labels `E`, `I`, `J_E+`, `J_I+`, `J_E-`, and `J_I-` if needed; detailed definitions of the potentiation and depression factors should stay in the caption.
review_notes: Check that inhibitory clustering is visibly paired with excitation, not drawn as a homogeneous global inhibitory pool. Check that depressed between-pair interactions are visually weaker than within-pair interactions.

### ch08-quenched-amplification-img

filename: `figures/imagegen/ch08-quenched-amplification-img.png`
chapter: 8
placement_target: Section: Finite Size and Quenched Variability
status: replace-existing
caption_intent: Show why paired E/I networks can amplify quenched variability: mean excitation and inhibition may cancel, but variance squares the large inhibitory coupling and can make inhibitory heterogeneity dominate.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a conceptual comparison of input-variance components in an E-only clustered architecture versus a paired E/I clustered architecture. The E/I case should show a much larger quenched inhibitory contribution because variance depends on squared coupling magnitude, while finite-size variability is shown as a separate shrinking contribution.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use two grouped schematic bars or stacked blocks side by side, with a small balanced-current inset showing large opposing E and I currents cancelling in the mean. Keep the design sparse and explanatory.
Required visual elements: Left group: E-only architecture with mostly excitatory quenched variance and a small finite-size component. Right group: paired E/I architecture with a prominent inhibitory quenched component. Include a small inset where large positive and negative currents nearly cancel, visually separate from the variance bars. Mark the bars as schematic rather than measured.
Sparse in-image labels: `E-only`, `E/I`, `E`, `I`, `kappa`, `xi`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, generous whitespace, restrained color, no watermark, no logos, no decorative stock imagery.
Avoid: Numeric y-axis values, fake data points, dense equations, long labels, visual clutter, and any suggestion that positive and negative variance components cancel.
"""
overlay_suggestion: Overlay `kappa`, `xi`, `E`, and `I` labels if needed; add exact expressions such as `xi=1/sqrt(N_E)` and the squared inhibitory variance term only in LaTeX caption text.
review_notes: Check that the variance display does not imply sign cancellation. Check that the inhibitory contribution is larger because of squared magnitude, not because inhibition is drawn as a negative bar.

### ch08-cluster-rate-unit-img

filename: `figures/imagegen/ch08-cluster-rate-unit-img.png`
chapter: 8
placement_target: Section: Clusters as Effective Rate Units
status: new
caption_intent: Introduce the minimal paired-cluster rate-unit abstraction: spikes from E and I populations are averaged and filtered into two rates whose dynamics are driven by within-pair coupling, quenched inter-pair input, and finite-size fluctuations.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a minimal abstraction diagram showing how a paired E/I spiking cluster becomes an effective two-dimensional cluster-rate unit. The visual should move from microscopic spike rasters through population averaging and filtering into a compact state variable with E and I rate components, then show inputs from other cluster-rate units.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a left-to-right teaching flow: spike rasters on the left, a filter/averaging stage in the middle, and a clean rate-unit icon on the right with incoming and outgoing inter-cluster arrows.
Required visual elements: Two small raster strips for E and I spikes, a simple smoothing/filter icon, two smooth rate traces, a final paired rate unit with internal E/I coupling, a small finite-size fluctuation mark, and a frozen inter-cluster input arrow from neighboring units. Make the figure conceptual and not a measured recording.
Sparse in-image labels: `E`, `I`, `r_E`, `r_I`, `xi`, `kappa`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, generous whitespace, crisp arrows, no watermark, no logos, no decorative stock imagery.
Avoid: Dense derivations, exact equations inside the image, photorealistic cells, decorative stock imagery, fake experimental axes, and ambiguous flow direction from spikes to rates.
"""
overlay_suggestion: Overlay `r_a^E`, `r_a^I`, `xi`, and `kappa` if needed; keep `r_a(t)=(r_a^E,r_a^I)` and `xi=1/sqrt(N_E)` in the caption or surrounding notes.
review_notes: Check that the image clearly shows averaging/filtering before the rate-unit abstraction. Check that `xi` is associated with finite-size fluctuations and `kappa` with frozen inter-cluster input.

### ch09-xi-kappa-plane-img

filename: `figures/imagegen/ch09-xi-kappa-plane-img.png`
chapter: 9
placement_target: Section: The xi-kappa Plane
status: replace-existing
caption_intent: Explain the xi-kappa diagnostic plane as the organizing test for separating finite-size metastable switching from switching that persists when population sampling noise is removed.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic diagnostic phase plane for clustered spiking network dynamics with finite-size amplitude xi on the horizontal axis and quenched heterogeneity kappa on the vertical axis. The visual should show that moving toward smaller xi tests whether switching disappears, slows dramatically, or reaches a kappa-controlled plateau near the large-network limit.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use one large phase-plane plot with four softly colored conceptual regions and a few arrows indicating size-scaling trajectories toward xi near zero. Keep margins generous and the axes uncluttered.
Required visual elements: Horizontal xi axis, vertical kappa axis, a lower finite-size metastability region, an upper region where mesoscopic chaos persists near xi near zero, a mixed intermediate band, and a scaling-test arrow pointing toward the xi near zero edge. Mark the diagram as schematic and conceptual, not measured data.
Sparse in-image labels: `xi`, `kappa`, `finite-size`, `mixed`, `chaos`, `plateau`
Style: Clean, modern, textbook-quality scientific diagram with generous whitespace, high contrast, crisp phase regions, restrained color, no watermark, no logos, no decorative stock imagery.
Avoid: Exact equations inside the image, dense callouts, fake numerical ticks, measured-data heatmaps, ornamental neural backgrounds, cluttered legends, and implying that the region boundaries are empirically measured.
"""
overlay_suggestion: Overlay exact axis labels `xi=1/sqrt(N_E)` and `kappa`, plus optional region labels `finite-size escape`, `mixed`, and `xi -> 0 chaos`; keep switching-time scaling equations in the caption.
review_notes: Check that lower xi is visually associated with increasing network size and that the chaotic region persists near the xi-zero edge. Check that the phase boundaries look schematic rather than like fitted data.

### ch09-perturbation-divergence-img

filename: `figures/imagegen/ch09-perturbation-divergence-img.png`
chapter: 9
placement_target: Section: Perturbation Recovery Versus Divergence
status: replace-existing
caption_intent: Contrast a small perturbation that relaxes inside a metastable basin with a small perturbation that grows exponentially in a chaotic mesoscale flow before saturating.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic perturbation diagnostic comparing metastable recovery with chaotic divergence in clustered spiking networks. The figure should make clear that a subthreshold perturbation decays inside a stable basin, while an infinitesimal perturbation in chaotic mesoscale flow grows before saturating.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use two coordinated panels: a left state-space panel with basins and trajectory pairs, and a right semilog-style distance-versus-time sketch. Keep the panel boundary simple and leave whitespace around arrows and curves.
Required visual elements: Left panel: two nearby trajectories returning together inside one basin and a separate small chaotic-flow path where nearby trajectories separate. Right panel: one decaying distance curve, one exponential-growth curve that saturates, and a thresholded large-jump cue for basin crossing. The plots are conceptual, not measured data.
Sparse in-image labels: `basin`, `decay`, `lambda>0`, `saturation`, `d(t)`, `t`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, crisp traces, generous whitespace, no watermark, no logos, no decorative stock imagery.
Avoid: Full Lyapunov equations in the image, long annotations, real experimental traces, numerical tick marks, too many trajectories, 3D landscapes, and ambiguity between large basin jumps and infinitesimal chaotic divergence.
"""
overlay_suggestion: Overlay `d(t)`, `lambda > 0`, `tau_relax`, and `saturation` if needed; keep `d(t) approx d(0)e^{lambda_max t}` and the full distance definition in LaTeX caption text.
review_notes: Check that the metastable case shows decay for small perturbations, not immediate basin switching. Check that chaotic growth is shown as early exponential divergence followed by bounded saturation.

### ch09-autocorrelation-kink-img

filename: `figures/imagegen/ch09-autocorrelation-kink-img.png`
chapter: 9
placement_target: Section: Autocorrelation Diagnostics and the Zero-Lag Kink
status: replace-existing
caption_intent: Show the zero-lag autocorrelation discriminator: finite-size OU-like noise creates a cusp, smooth deterministic chaos has zero slope at zero lag, and observed traces may mix both components.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic autocorrelation diagnostic comparing finite-size noise, smooth chaotic rates, and a mixed measured autocorrelation. The central teaching point is that the finite-size contribution has a visible zero-lag cusp, while the chaotic contribution is smooth at zero lag.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use three small aligned curve panels or one wide panel with three clearly separated curves. Center the zero-lag vertical guide and keep labels sparse enough for PDF readability.
Required visual elements: A sharp cusp curve centered at tau zero, a smooth broad even curve with a rounded top at tau zero, and a mixed curve showing a broad component with a small cusp. Add a subtle visual indicator that the cusp amplitude shrinks with increasing network size. Make all curves schematic, not measured data.
Sparse in-image labels: `C(tau)`, `tau`, `kink`, `smooth`, `mixed`, `N up`
Style: Clean, modern, textbook-quality scientific diagram with generous whitespace, high contrast, crisp curves, restrained color, no watermark, no logos, no decorative stock imagery.
Avoid: Exact autocorrelation formulas inside the image, dense legends, fake sampled data points, noisy empirical traces, many tick labels, and any implication that the cusp is a generic signature of chaos.
"""
overlay_suggestion: Overlay `C(tau)`, `tau=0`, `finite-size kink`, and `smooth chaos` if needed; keep `A_xi exp(-|tau|/tau_xi)` and derivative equations in the caption or notes.
review_notes: Check that the finite-size curve has a real cusp at zero lag and that the smooth chaotic curve has zero apparent slope at zero lag. Check that the mixed curve does not look like a noisy measurement.

### ch09-regimes-abc-variance-img

filename: `figures/imagegen/ch09-regimes-abc-variance-img.png`
chapter: 9
placement_target: Section: Fully Connected Scaling Regimes A, B, and C
status: replace-existing
caption_intent: Summarize scaling regimes A, B, and C by separating finite-size variance, quenched inter-cluster variance, and whether a many-unit DMFT-like chaos limit is available.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic grouped comparison of fully connected scaling regimes A, B, and C for clustered networks. The diagram should show how finite-size variance, quenched variance, cluster count, and cluster size behave in each limit, emphasizing that regime C is the clean target for macroscopic chaos without finite-size noise.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use three vertical columns labeled A, B, and C, each with a compact network-size icon above and a small stacked variance bar below. Use consistent visual encoding across columns and ample whitespace.
Required visual elements: Regime A: many clusters with fixed small cluster size and nonvanishing finite-size component. Regime B: few large clusters with finite-size component vanished but only a few random couplings. Regime C: many large clusters, finite-size component vanished, quenched variance remaining, and a many-unit DMFT target cue. Make the bars schematic rather than quantitative.
Sparse in-image labels: `A`, `B`, `C`, `xi`, `kappa`, `DMFT`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, simple matrix or cluster icons, crisp stacked bars, generous whitespace, no watermark, no logos, no decorative stock imagery.
Avoid: Full variance equations in the image, numerical bar heights, fake data axes, overloaded legends, excessive cluster dots, photorealistic neuron imagery, and implying that regime B is already a many-unit DMFT limit.
"""
overlay_suggestion: Overlay `Q -> infinity`, `N_c -> infinity`, `xi -> 0`, and `kappa remains` where needed; keep the full variance decomposition and regime definitions in LaTeX text.
review_notes: Check that regime C shows both many clusters and large clusters. Check that finite-size variance is not shown as remaining in C, and that quenched variance is not drawn as a signed quantity that cancels.

### ch10-phase-diagram-dashboard-img

filename: `figures/imagegen/ch10-phase-diagram-dashboard-img.png`
chapter: 10
placement_target: Section: Parameter Axes and Phase Diagrams
status: replace-existing
caption_intent: Synthesize the research phase diagram as a dynamic-regime map over cluster strength and heterogeneity, with classifications based on behavior rather than only mean firing rate.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic research phase-diagram dashboard for clustered spiking networks over cluster strength and quenched heterogeneity. The diagram should classify asynchronous, attractor, chaotic, and possible transient-chaotic regimes and include small observable cues that show the classification is based on dynamics.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a large central phase diagram with a narrow side strip of three miniature diagnostic glyphs. Keep the central map dominant, with clean axes and softly separated regions.
Required visual elements: Horizontal cluster-strength axis, vertical kappa or heterogeneity axis, four conceptual regions for asynchronous irregular activity, activated attractor or finite-size metastability, mesoscopic chaos, and possible transient chaos at strong coupling. Add small diagnostic glyphs for autocorrelation width, perturbation growth, and size scaling. Mark the map as schematic, not measured data.
Sparse in-image labels: `strength`, `kappa`, `AI`, `attractor`, `chaos`, `transient`
Style: Clean, modern, textbook-quality scientific diagram with generous whitespace, high contrast, readable region shapes, restrained color, no watermark, no logos, no decorative stock imagery.
Avoid: Exact equations, long region descriptions, fake heatmap measurements, numerical phase boundaries, decorative neural network art, cluttered legends, and implying transient chaos is established rather than a hypothesis to test.
"""
overlay_suggestion: Overlay exact labels `J_E+ or s`, `kappa`, `AI`, `attractor`, `chaos`, and `transient?`; keep discussion of `xi`, `lambda_max`, and trend predictions in caption text.
review_notes: Check that the figure reads as a dashboard for dynamic classification, not a firing-rate heatmap. Check that the transient-chaotic region is visually marked as tentative.

### ch10-observable-dashboard-img

filename: `figures/imagegen/ch10-observable-dashboard-img.png`
chapter: 10
placement_target: Section: Observable Dashboard
status: replace-existing
caption_intent: Present the common observable dashboard as a compact set of diagnostics combining timescales, state statistics, variability, dimensionality, and instability for regime classification.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic observable dashboard for clustered spiking network simulations. The figure should show that regime classification should combine multiple diagnostics rather than rely on a single example trace.
Composition: 16:10 horizontal composition suitable for a PDF figure. Arrange six compact dashboard tiles in a clean 3-by-2 grid with consistent spacing and no nested cards. Each tile should contain one simple glyph or mini-plot, with a shared visual style.
Required visual elements: Tile for autocorrelation HWHM, tile for cluster lifetimes, tile for active-cluster count distribution, tile for Fano or variability, tile for dimensionality, and tile for perturbation or Lyapunov growth. Use schematic curves and bars only; do not present the dashboard as measured data.
Sparse in-image labels: `tau_i`, `tau_c`, `T_C`, `M(t)`, `Fano`, `lambda`
Style: Clean, modern, textbook-quality scientific diagram with high contrast, crisp mini-plots, generous whitespace, restrained color accents, no watermark, no logos, no decorative stock imagery.
Avoid: Dense formulas inside tiles, fake numerical data, tiny unreadable axes, long explanatory tile titles, photorealistic laboratory imagery, decorative stock dashboards, and visual hierarchy that makes one diagnostic look sufficient by itself.
"""
overlay_suggestion: Overlay exact labels `tau_i`, `tau_c`, `T_C`, `M(t)`, `F_i(T)`, and `lambda_max` if needed; keep HWHM definitions and participation-ratio equations in LaTeX text.
review_notes: Check that all six diagnostics remain legible at PDF figure size and that the mini-plots look schematic. Check that perturbation growth is not confused with an ordinary firing-rate trace.

### ch10-research-workflow-img

filename: `figures/imagegen/ch10-research-workflow-img.png`
chapter: 10
placement_target: Section: Simulation and Theory Workflow
status: new
caption_intent: Show the intended research loop from model choice through simulation, observable diagnostics, scaling tests, theory comparison, and interpretation of dynamic regimes.
imagegen_prompt:
"""
Use case: scientific-educational
Asset type: lecture-note raster infographic
Primary request: Create a schematic research workflow loop for the clustered spiking network program. The figure should connect model architecture, simulation outputs, diagnostic dashboards, scaling experiments, mesoscale or DMFT theory, and final regime interpretation.
Composition: 16:10 horizontal composition suitable for a PDF figure. Use a clockwise loop or left-to-right looped pipeline with six stations, broad arrows, and clear whitespace. The workflow should feel like a rigorous scientific procedure, not a project-management chart.
Required visual elements: Station for choosing E-only or paired E/I architecture, station for selecting parameters, station for simulating spikes and rates, station for computing diagnostics, station for repeating size scaling, station for comparing to theory and interpreting the phase diagram. Include a feedback arrow from interpretation back to model and parameter choice.
Sparse in-image labels: `model`, `parameters`, `simulation`, `diagnostics`, `scaling`, `theory`
Style: Clean, modern, textbook-quality scientific workflow diagram with high contrast, crisp arrows, generous whitespace, restrained color, no watermark, no logos, no decorative stock imagery.
Avoid: Exact equations inside the workflow, long checklist text, software logos, cloud or lab-stock imagery, Gantt-chart styling, fake screenshots, cluttered icons, and presenting the loop as a linear one-pass procedure.
"""
overlay_suggestion: Overlay `model`, `parameters`, `simulation`, `diagnostics`, `scaling`, and `theory` if generated text is unreliable; keep detailed lists of observables and parameters in the chapter text.
review_notes: Check that the workflow forms a loop with feedback from interpretation to model choice. Check that theory comparison is visually connected to both diagnostics and phase-diagram interpretation.
