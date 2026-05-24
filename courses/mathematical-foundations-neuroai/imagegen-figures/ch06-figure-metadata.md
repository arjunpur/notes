# Chapter 6 Figure Metadata

## Figure 6.1: Eigenvectors as invariant directions

- File: `imagegen-figures/ch06-eigen-invariant-directions.png`
- Pedagogical purpose: Show that eigenvectors are special nonzero directions whose image under a square linear map stays on the same line, while ordinary vectors usually change direction.
- Section(s) supported: 6.1 Eigenvalues and eigenvectors.
- Exact mathematical objects shown: A 2D input coordinate grid, the transformed output grid under a linear map \(A\), invariant directions \(v_1,v_2\), scaled outputs \(Av_1=\lambda_1 v_1\), \(Av_2=\lambda_2 v_2\), and a non-eigenvector \(x\) whose output \(Ax\) changes direction.
- What the reader should notice first: The teal and gold arrows keep their directions after the map, while the red arrow does not.
- Necessary labels: `input`, `after A`, `v1`, `v2`, `A v1 = lambda1 v1`, `A v2 = lambda2 v2`, `x`, `A x`.
- How the text references the figure: Section 6.1 uses it to introduce invariant directions before defining \(Av=\lambda v\), then returns to it when discussing dynamics and mixtures of eigenvectors.
- Comprehensive ImageGen prompt: Clean scientific-educational raster diagram on a white background with navy coordinate grids and axes, teal and warm-gold invariant rays, a restrained red ordinary vector, two panels labeled input and after A, transformed grid on the output side, sparse mathematical labels only, readable at PDF width, no decorative gradients, no stock-photo realism, no dense in-image paragraphs.
- Teaching caption: Eigenvectors are directions, not merely arrows. Under \(A\), vectors on an eigenline remain on that line and are only scaled by the corresponding eigenvalue; a generic vector mixes directions and turns.

## Figure 6.2: Quadratic forms as curvature and energy

- File: `imagegen-figures/ch06-quadratic-forms-contours.png`
- Pedagogical purpose: Explain how a symmetric matrix defines level curves of the scalar energy \(q(x)=x^\top A x\), with eigenvectors giving principal axes and eigenvalues controlling curvature.
- Section(s) supported: 6.2 Symmetric matrices and quadratic forms.
- Exact mathematical objects shown: Nested elliptical level sets \(q(x)=1,4,9\) for a form like \(q(x)=4z_1^2+z_2^2\), the vertical short/tight eigen-axis \(q_1\) labeled with large \(\lambda_1\), the horizontal broad/long eigen-axis \(q_2\) labeled with small \(\lambda_2\), and a small bowl inset with the same ellipse footprint.
- What the reader should notice first: The ellipse axes line up with orthogonal eigenvectors; the large-eigenvalue \(q_1\) direction is visibly narrow/tight, while the small-eigenvalue \(q_2\) direction is visibly broad/long.
- Necessary labels: `q(x)=x^T A x`, `q(x)=1`, `q(x)=4`, `q(x)=9`, `q1`, `q2`, `lambda1 large`, `lambda2 small`.
- How the text references the figure: Section 6.2 uses it to connect the spectral theorem with contours, positive definiteness, Hessian curvature, and covariance ellipses.
- Comprehensive ImageGen prompt: Clean scientific-educational raster diagram on a white background with navy elliptical contours, teal and warm-gold orthogonal eigenvectors, sparse labels for level sets and eigenvalues, small bowl inset, precise geometry, generous whitespace, no decorative gradients, no stock-photo realism, no dense in-image paragraphs. Enforce the geometry: `q1` and `lambda1 large` must be on the short/narrow/tight curvature axis, and `q2` and `lambda2 small` must be on the long/broad/shallow axis.
- Precision source: `.agentfarm/course-drafts/chapters/ch06/figure-build/quadratic-forms-contours-source.tex` encodes this axis assignment and was used to regenerate the project PNG.
- Teaching caption: A symmetric matrix becomes easiest to read in its orthonormal eigenbasis: the quadratic form is a weighted sum of squared coordinates, and the eigenvalues set the contour widths and curvature.

## Figure 6.3: SVD input and output axes

- File: `imagegen-figures/ch06-svd-input-output-axes.png`
- Pedagogical purpose: Show SVD as a coordinate story for any matrix: right singular vectors choose input axes, singular values stretch them, and left singular vectors name the output axes.
- Section(s) supported: 6.3 Singular value decomposition.
- Exact mathematical objects shown: Input unit circle, right singular vectors \(v_1,v_2\), a pipeline \(V^\top\), \(\Sigma\), \(U\), an output ellipse, output semi-axes \(\sigma_1 u_1,\sigma_2 u_2\), and a sample vector \(x\mapsto Ax\).
- What the reader should notice first: The unit circle maps to an ellipse whose axes are singular-vector directions.
- Necessary labels: `A = U Sigma V^T`, `v1`, `v2`, `x`, `V^T`, `Sigma`, `U`, `sigma1 u1`, `sigma2 u2`, `A x`.
- How the text references the figure: Section 6.3 uses it to distinguish eigenvectors from singular vectors and to explain rotate-scale-rotate geometry and low-rank approximation.
- Comprehensive ImageGen prompt: Clean scientific-educational raster diagram on a white background, left-to-right unit-circle-to-ellipse map, navy line work, teal and warm-gold singular-vector axes, restrained red example vector, sparse labels only, readable at PDF width, no decorative gradients, no stock-photo realism, no dense in-image paragraphs.
- Teaching caption: SVD gives orthonormal input directions and orthonormal output directions. The singular values are nonnegative gains along those paired directions.

## Figure 6.4: PCA variance geometry

- File: `imagegen-figures/ch06-pca-variance-geometry.png`
- Pedagogical purpose: Show PCA as choosing projection directions that preserve variance and minimize reconstruction error for centered data.
- Section(s) supported: 6.4 Principal component analysis.
- Exact mathematical objects shown: Centered 2D data cloud, mean at the origin, covariance ellipse, principal directions PC1 and PC2, perpendicular projection segments onto PC1, projected points, and a residual reconstruction-error segment.
- What the reader should notice first: PC1 follows the longest direction of the centered cloud, and projection residuals are perpendicular to PC1.
- Necessary labels: `PC1`, `PC2`, `mean = 0`, `reconstruction error`.
- How the text references the figure: Section 6.4 uses it to connect covariance eigenvectors, projection, scores, loadings, and low-dimensional reconstruction.
- Comprehensive ImageGen prompt: Clean scientific-educational raster scatter plot on a white background with navy data points, teal PC1, warm-gold PC2, faint covariance ellipse, gray perpendicular projection segments, restrained red reconstruction-error segment, sparse labels only, readable at PDF width, no decorative gradients, no stock-photo realism, no dense in-image paragraphs.
- Teaching caption: PCA is projection geometry applied to centered data: the first component captures the largest variance, later orthogonal components capture remaining variance, and discarded components become reconstruction error.
