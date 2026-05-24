# Machine Intelligence II Figure Metadata

## figures/ica/bss-unmixing.png

- Target section: Lecture 4, Blind Source Separation.
- Visual claim: ICA treats observed signals as mixtures of latent independent causes, and learning an unmixing transform aims to recover the source coordinates.
- Caption: ICA as blind source separation. Latent source signals are mixed by the unknown matrix \(A\), producing observed mixtures \(x\). The learned unmixing matrix \(W\) tries to recover source coordinates \(\hat{s}\). In EEG-like settings, this can separate neural components from stereotyped artifacts, but the recovered components still require interpretation.
- Status: generated with built-in Codex image_gen.
- Sizing notes: use at `width=0.96\textwidth`; wide four-panel light-background teaching plate.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX Machine Intelligence II lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate for Independent Component Analysis as blind source separation, with only simple words as labels.
Style: light background, dark readable labels, restrained blue, teal, and amber accents, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four labeled panels in one wide horizontal plate. Panel A: two clean latent source waveforms labeled "sources" feed through a square mixing box labeled "mixing" into two observed mixture waveforms labeled "mixtures". Panel B: a two-dimensional scatter cloud in observation space with two oblique source directions labeled "source axes". Panel C: an unmixing box labeled "unmixing" maps observed mixture waveforms back to two separated waveforms labeled "separated". Panel D: a simple EEG sensor row with colored components separated, labeled "EEG example" and "artifact".
Visual claim: ICA treats observed signals as mixtures of latent independent causes, and learning an unmixing transform aims to recover the source coordinates.
Necessary labels, exact text only: "sources", "mixing", "mixtures", "source axes", "unmixing", "separated", "EEG example", "artifact"
Avoid: equations, derivations, mathematical notation, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond blind source separation
```

## figures/ica/whitening-nongaussianity.png

- Target section: Lecture 4, Independence Is Stronger Than Decorrelation.
- Visual claim: PCA removes second-order covariance, whitening leaves only rotations, and ICA chooses the rotation that makes coordinates statistically independent by using non-Gaussian structure.
- Caption: Decorrelation is not independence. PCA rotates the data to remove covariance, whitening rescales the coordinates to unit variance, and ICA still has to choose among the remaining rotations. Non-Gaussian shape supplies the cue that covariance alone cannot provide.
- Status: generated with built-in Codex image_gen.
- Sizing notes: use at `width=0.96\textwidth`; wide four-panel light-background teaching plate.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX Machine Intelligence II lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate showing why ICA needs more than PCA decorrelation.
Style: light background, dark readable labels, restrained teal, blue, and amber accents, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four labeled panels in one wide horizontal plate. Panel A: an elongated correlated data cloud labeled "correlated mixtures". Panel B: the same cloud after PCA rotation with axis-aligned ellipse, labeled "decorrelated". Panel C: a circular whitened cloud with several possible rotation axes drawn through it, labeled "whitened rotations". Panel D: two rotated coordinate choices over a square-like non-Gaussian point cloud, one poor and one aligned with the hidden source axes, labeled "independence cue" and "non-Gaussian shape".
Visual claim: PCA removes second-order covariance, whitening leaves only rotations, and ICA chooses the rotation that makes the coordinates statistically independent by using non-Gaussian structure.
Necessary labels, exact text only: "correlated mixtures", "decorrelated", "whitened", "rotations", "independence cue", "non-Gaussian shape", "PCA", "ICA"
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond decorrelation, whitening, rotation, and non-Gaussianity
```

## figures/ica/identifiability-limits.png

- Target section: Lecture 4, Identifiability Limits.
- Visual claim: ICA can recover independent source directions only up to permutation and scale, and Gaussian sources leave rotations unidentifiable.
- Caption: ICA has unavoidable identifiability limits. The order of recovered sources is arbitrary, their amplitudes require a convention, and Gaussian sources do not reveal a preferred rotation because a spherical Gaussian looks the same from every orthogonal coordinate system.
- Status: generated with built-in Codex image_gen.
- Sizing notes: use at `width=0.96\textwidth`; wide four-panel light-background teaching plate.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX Machine Intelligence II lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate for ICA identifiability limits.
Style: light background, dark readable labels, restrained blue, teal, amber, and gray accents, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four labeled panels in one wide horizontal plate. Panel A: two recovered source traces can swap order, with crossing arrows, labeled "permutation". Panel B: the same source trace shown small and large with a vertical scaling bracket, labeled "scale". Panel C: a circular Gaussian cloud with several equally valid rotated axes, labeled "Gaussian rotation". Panel D: a checklist-style diagnostic panel with three simple icons labeled "order arbitrary", "amplitude arbitrary", "need non-Gaussian".
Visual claim: ICA can recover independent source directions only up to permutation and scale, and Gaussian sources leave rotations unidentifiable.
Necessary labels, exact text only: "permutation", "scale", "Gaussian rotation", "order arbitrary", "amplitude arbitrary", "need non-Gaussian"
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond ICA identifiability limits
```

## figures/ica/mutual-information-factorization.png

- Target section: Lecture 4, Mutual Information As The Independence Objective.
- Visual claim: Mutual information is the KL divergence between the recovered joint density and the product of its marginals; ICA minimizes this residual dependence to choose an independent coordinate system.
- Caption: Mutual information as residual dependence. ICA compares the recovered joint density with the factorized density formed from its one-dimensional marginals. The KL gap is zero only when the recovered coordinates are independent, so minimizing mutual information selects the unmixing coordinates that remove dependence.
- Status: generated with built-in Codex image_gen.
- Sizing notes: use at `width=0.96\textwidth`; wide four-panel light-background teaching plate.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX Machine Intelligence II lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate for ICA mutual information as the independence objective.
Style: light background, dark readable labels, restrained blue, teal, amber, and gray accents, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four labeled panels in one wide horizontal plate. Panel A: a two-dimensional joint density cloud with a diagonal dependence ridge labeled "joint density". Panel B: two one-dimensional marginal density curves beside the same variables labeled "marginals". Panel C: a factorized rectangular product-density view with independent axes and evenly spread contours labeled "factorized model". Panel D: a small divergence gauge or gap between the dependent joint and factorized model labeled "mutual information" and "zero when independent".
Visual claim: Mutual information is the KL divergence between the recovered joint density and the product of its marginals; ICA minimizes this residual dependence to choose an independent coordinate system.
Necessary labels, exact text only: "joint density", "marginals", "factorized model", "mutual information", "zero when independent", "ICA objective"
Avoid: equations, derivations, mathematical notation, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond mutual information, KL divergence intuition, factorization, and independence
```

## figures/ica/infomax-natural-gradient.png

- Target section: Lecture 4, The Infomax Principle and Natural Gradient Learning.
- Visual claim: Infomax ICA chooses an unmixing matrix so nonlinear output variables become as informative as possible, and natural-gradient learning rescales steps to the geometry of linear unmixing matrices.
- Caption: The Infomax ICA pipeline. A linear unmixing layer \(W\) produces estimated sources \(\hat{s}\), componentwise nonlinearities map them to output variables \(\hat{u}\), and maximizing output entropy supplies the learning objective. Natural-gradient learning adjusts the step to the geometry of invertible linear transforms.
- Status: generated with built-in Codex image_gen.
- Sizing notes: use at `width=0.96\textwidth`; wide four-panel light-background teaching plate.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX Machine Intelligence II lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate for Infomax ICA and natural-gradient learning.
Style: light background, dark readable labels, restrained blue, teal, amber, and gray accents, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four labeled panels in one wide horizontal plate. Panel A: observed mixtures feed into a linear unmixing layer labeled "W" with outputs labeled "s_hat". Panel B: each separated signal passes through a monotone sigmoid-like curve labeled "cdf" to outputs labeled "u". Panel C: the transformed outputs spread evenly across a square labeled "high entropy" with sparse points filling the area. Panel D: a parameter-space sketch with a curved manifold, a short ordinary step labeled "gradient", and a corrected tangent step labeled "natural gradient".
Visual claim: Infomax ICA chooses an unmixing matrix so nonlinear output variables become as informative as possible, and natural-gradient learning rescales steps to the geometry of linear unmixing matrices.
Necessary labels, exact text only: "W", "s_hat", "cdf", "u", "high entropy", "gradient", "natural gradient", "data", "learning"
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond Infomax pipeline and natural-gradient geometry
```

## figures/ica/ica-diagnostics.png

- Target section: Lecture 4, Diagnostics For ICA In Practice.
- Visual claim: ICA is judged by convergence of the objective, plausible non-Gaussian marginals, weak remaining dependence between recovered sources, and small reconstruction residuals.
- Caption: Practical ICA diagnostics. The training objective should stabilize, recovered source histograms should show plausible non-Gaussian structure, dependence between components should be weak, and reconstruction residuals should remain small when the learned unmixing matrix is inverted.
- Status: generated with built-in Codex image_gen.
- Sizing notes: use at `width=0.96\textwidth`; wide four-panel light-background teaching plate.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX Machine Intelligence II lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate for practical ICA diagnostics after training.
Style: light background, dark readable labels, restrained blue, teal, amber, and gray accents, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four labeled panels in one wide horizontal plate. Panel A: a rising training curve flattening into a plateau labeled "objective" and "plateau". Panel B: three separated source histograms with different non-Gaussian shapes labeled "source histograms". Panel C: a small off-diagonal dependence heat map with pale off-diagonal cells labeled "dependence check". Panel D: reconstructed mixtures compared with residual traces near zero labeled "reconstruction" and "residuals".
Visual claim: ICA is judged by convergence of the objective, plausible non-Gaussian marginals, weak remaining dependence between recovered sources, and small reconstruction residuals.
Necessary labels, exact text only: "objective", "plateau", "source histograms", "dependence check", "reconstruction", "residuals"
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond ICA diagnostics
```
