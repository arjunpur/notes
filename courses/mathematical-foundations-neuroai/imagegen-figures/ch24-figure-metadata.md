# Chapter 24 Figure Metadata

No image files were generated in this worker pass, and the chapter source does not include missing `\includegraphics` commands. These are proposed assets for a later image-generation pass.

## `ch24-conditioning-singular-values.png`

- Section(s) supported: 24.1 Conditioning and ill-posedness.
- Pedagogical purpose: Show how a matrix with a tiny singular value amplifies noise in one direction.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout. Subject: unit circle mapped by a matrix to a thin ellipse, with the short singular direction highlighted and a small data perturbation becoming a large solution perturbation. Include labels singular direction, tiny sigma, amplified noise, and kappa. Style: white background, crisp navy line work, teal input circle, gold output ellipse, restrained red perturbation arrow. Sparse in-image labels only. Exact equations should go in captions, not image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."

## `ch24-factorization-decision-map.png`

- Section(s) supported: 24.2 Matrix factorizations in computation.
- Pedagogical purpose: Summarize LU, Cholesky, QR, eigendecomposition, and SVD by task and matrix assumptions.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout. Subject: clean decision map for matrix factorizations: general square solve to LU with pivoting, SPD solve to Cholesky, least squares to QR, modes to eigen, rank/conditioning to SVD. Use small abstract matrix icons and arrows. Style: white background, navy line work, teal task boxes, gold factorization boxes, restrained red warning next to explicit inverse. Sparse in-image labels only. Exact equations should go in captions, not image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."

## `ch24-iterative-solvers-residuals.png`

- Section(s) supported: 24.3 Solving large systems.
- Pedagogical purpose: Visualize residual reduction, Krylov subspace expansion, and preconditioning.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout. Subject: iterative solution of Ax=b with a current estimate, residual arrow r=b-Ax, a sequence of shrinking residual bars, a Krylov basis fan, and a preconditioner reshaping elongated contours into rounder contours. Style: white background, crisp navy axes, teal iterates, gold Krylov directions, restrained red initial residual. Sparse in-image labels only. Exact equations should go in captions, not image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."

## `ch24-discretization-error-stability.png`

- Section(s) supported: 24.4 Simulation, discretization, and error.
- Pedagogical purpose: Compare stable and unstable Euler time steps for a decaying ODE.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout. Subject: exact decaying exponential curve with two Euler approximations: small stable step following the decay and large unstable step oscillating/growing. Add a small time-step ruler with delta t. Style: white background, navy exact curve, teal stable numerical points, restrained red unstable points, gold time-step markers. Sparse in-image labels only. Exact equations should go in captions, not image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."
