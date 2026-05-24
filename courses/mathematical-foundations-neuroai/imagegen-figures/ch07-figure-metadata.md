# Chapter 7 Figure Metadata

All four assets are chapter-specific raster PNGs in `imagegen-figures/`. The initial assets were generated with the built-in ImageGen workflow. During revision, Figures 7.1, 7.2, and 7.4 were redrawn from local TikZ sources under `.agentfarm/course-drafts/chapters/ch07/` because exact mathematical labels and index conventions needed deterministic control. Style target: white background, navy line work, teal and warm-gold accents, restrained red highlights, generous whitespace, precise geometry, readable at PDF width, no external images.

## Figure 7.1: Tensor shapes and axes

- Saved path: `imagegen-figures/ch07-tensor-shapes-axes.png`
- Pedagogical purpose: Make tensor order and shape feel like typed axis structure, not merely a larger table of numbers.
- Section(s) supported: 7.1 Tensors and multidimensional arrays.
- Exact mathematical objects shown: scalar, vector, matrix, three-way tensor \(X_{b,t,n}\), trial/time/neuron axes, and a four-axis deep learning image-batch cue with batch/height/width/channel.
- What the reader should notice first: Every highlighted entry is located by one index per axis, and each axis carries a meaning.
- Necessary labels: scalar, vector, matrix, tensor, trial \(b\), time \(t\), neuron \(n\), batch, height, width, channel, \(X[b,t,n]\).
- Text reference: Figure 7.1 is referenced from the beginner setup and core intuition of Section 7.1 to support shape discipline and axis semantics.
- Comprehensive ImageGen prompt: Create a clean educational diagram explaining tensors as multidimensional arrays and axis discipline. Four left-to-right panels on a white background: scalar as a single dot, vector as a one-dimensional row of boxes, matrix as a 2D grid, tensor as a 3D stack of grids with axes labeled trial \(b\), time \(t\), neuron \(n\), and a highlighted entry labeled exactly \(X[b,t,n]\). Add a small 4D deep learning cue with batch, height, width, channel as grouped image-like slabs. Use white background, navy line work, teal and warm-gold accents, restrained red highlight on one selected entry with index labels, generous whitespace, precise geometry, readable at PDF width. No decorative gradients, no stock realism, no dense text, no tiny labels.
- Revision note: The current PNG was redrawn from `.agentfarm/course-drafts/chapters/ch07/ch07-fig-tensor-shapes.tex` to keep the axis labels and highlighted entry consistent as \(X_{b,t,n}\).
- Teaching caption: Tensor notation extends scalar, vector, and matrix indexing to multi-axis arrays. The highlighted neural-recording entry \(X_{b,t,n}\) is specified by one index per axis: trial or batch \(b\), time \(t\), and neuron \(n\). In a deep learning image batch, the axes may be batch, height, width, and channel.

## Figure 7.2: Contraction and einsum

- Saved path: `imagegen-figures/ch07-contraction-einsum.png`
- Pedagogical purpose: Show contraction as the rule "sum over shared indices and keep the free indices."
- Section(s) supported: 7.2 Tensor operations.
- Exact mathematical objects shown: matrix multiplication \(C_{ij}=\sum_k A_{ik}B_{kj}\), the formal higher-order contraction \(C_{i,j,l}=\sum_{k=1}^K A_{i,k,j}B_{k,l}\) for \(A\in\mathbb{R}^{I\times K\times J}\) and \(B\in\mathbb{R}^{K\times L}\), and attention scores \(S=QK^\top\) with feature dimension \(d\) contracted.
- What the reader should notice first: The warm-gold shared index disappears from the output while the teal output axes remain.
- Necessary labels: \(A\), \(B\), \(C\), \(I\), \(J\), \(K\), \(L\), \(k\) shared, sum, \(Q\), \(K^\top\), \(S\), \(d\).
- Text reference: Figure 7.2 is referenced from Section 7.2 when introducing contractions and attention-score einsum patterns.
- Comprehensive ImageGen prompt: Create a clean educational diagram showing tensor contraction as summing over a shared index. Three panels: matrix multiplication with \(A\) shape \(m\times k\), \(B\) shape \(k\times n\), shared \(k\) highlighted, output \(C\) shape \(m\times n\), equation \(C_{ij}=\sum_k A_{ik}B_{kj}\); formal higher-order contraction \(A\in\mathbb{R}^{I\times K\times J}\) and \(B\in\mathbb{R}^{K\times L}\) producing \(C\in\mathbb{R}^{I\times J\times L}\) with equation \(C_{i,j,l}=\sum_{k=1}^K A_{i,k,j}B_{k,l}\), highlighting only the contracted \(K\)-axis; attention-score example \(S=QK^\top\) with shared feature dimension \(d\). White background, navy line work, teal outputs, warm-gold shared-index highlights, precise geometry, sparse readable labels.
- Revision note: The current PNG was redrawn from `.agentfarm/course-drafts/chapters/ch07/ch07-fig-contraction-einsum.tex` so the center panel exactly matches the nearby formal contraction \(C_{i,j,l}=\sum_{k=1}^K A_{i,k,j}B_{k,l}\), with no extra shared free axis.
- Teaching caption: A contraction sums over a shared index and removes that index from the output. Matrix multiplication contracts over \(k\). The middle panel mirrors the formal higher-order example \(C_{i,j,l}=\sum_{k=1}^K A_{i,k,j}B_{k,l}\): only the \(K\)-axis is summed, while \(I,J,L\) remain. Attention scores contract over feature dimension \(d\).

## Figure 7.3: Shape-first derivatives

- Saved path: `imagegen-figures/ch07-shape-first-derivatives.png`
- Pedagogical purpose: Make derivative shapes visible for scalar losses, vector-valued functions, matrix parameters, and the chain rule.
- Section(s) supported: 7.3 Matrix and tensor derivatives.
- Exact mathematical objects shown: scalar loss \(L=f(x)\), vector gradient \(\nabla_x L\), vector function \(y=f(x)\), Jacobian \(J\in\mathbb{R}^{m\times n}\), matrix parameter \(W\), matrix gradient \(\nabla_W L\), Frobenius differential \(dL=\langle\nabla_W L,dW\rangle\), and chain rule \(\nabla_xL=J^\top\nabla_zL\).
- What the reader should notice first: Scalar-loss gradients match the variable shape, while Jacobians carry output axes by input axes.
- Necessary labels: \(\nabla_x L\), \(J\in\mathbb{R}^{m\times n}\), \(dy=Jdx\), \(\nabla_W L\), \(dL=\langle\nabla_W L,dW\rangle\), \(\nabla_x L=J^\top\nabla_z L\), shape mismatch.
- Text reference: Figure 7.3 is referenced from Section 7.3 while defining gradients, Jacobians, Frobenius pairings, and backward chain rules.
- Comprehensive ImageGen prompt: Create a clean educational diagram explaining shape-first matrix calculus. Four panels: scalar loss with vector input and same-shaped gradient; vector function with Jacobian mapping \(dx\) to \(dy\); scalar loss with matrix parameter and same-shaped matrix gradient paired with \(dW\); chain-rule shape pipeline \(x\to z\to L\). White background, navy line work, teal gradients/Jacobians, warm-gold differentials, restrained red shape-mismatch warning, precise geometry, readable equations only, no dense text.
- Teaching caption: Shape-first derivatives keep domains and codomains visible. A scalar loss has a gradient with the same shape as its input. A vector-valued function has a Jacobian. A matrix-parameter loss has a matrix gradient paired with \(dW\). Chain rules transpose Jacobians when moving gradients backward.

## Figure 7.4: Convolution as Toeplitz linear algebra

- Saved path: `imagegen-figures/ch07-convolution-toeplitz.png`
- Pedagogical purpose: Connect the sliding-filter picture to a sparse Toeplitz matrix and to CNN feature maps.
- Section(s) supported: 7.4 Convolution as linear algebra.
- Exact mathematical objects shown: 1D signal \(x_1,\ldots,x_8\) with zero padding, local kernel \(h_{-1},h_0,h_1\), output \(y_1,\ldots,y_8\), formula \(y_t=\sum_{r=-1}^{1} h_rx_{t-r}\), an \(8\times 8\) Toeplitz matrix \(T_h\), sparse nonzero diagonals, 2D image patch, 3 by 3 filter, and output feature map.
- What the reader should notice first: The same kernel weights appear repeatedly along matrix diagonals, so convolution is a linear map with locality and weight sharing.
- Necessary labels: signal \(x\), kernel \(h\), output \(y_1,\ldots,y_8\), \(T_h\in\mathbb{R}^{8\times 8}\), sparse linear map, image, filter, feature map, translation equivariance.
- Text reference: Figure 7.4 is referenced from Section 7.4 to support the equivalence between sliding filters and sparse matrix multiplication.
- Comprehensive ImageGen prompt: Create a clean educational diagram showing convolution as sparse linear algebra. Three panels: 1D signal \(x_1,\ldots,x_8\) with zero padding and a short kernel sliding over adjacent entries, producing outputs \(y_1,\ldots,y_8\); equivalent \(8\times 8\) Toeplitz matrix \(T_h\) multiplying vector \(x\) to produce an eight-entry vector \(y\), with nonzero diagonals highlighted and zeros pale; 2D image patch with a \(3\times3\) filter sliding to produce a feature map, plus a translation-equivariance cue. White background, navy line work, teal outputs, warm-gold kernel weights, restrained red padding boundary, generous whitespace, precise geometry, readable at PDF width, no dense text.
- Revision note: The current PNG was redrawn from `.agentfarm/course-drafts/chapters/ch07/ch07-fig-convolution-toeplitz.tex` to show eight outputs and an \(8\times 8\) zero-padded Toeplitz map.
- Teaching caption: A convolution is a structured sparse linear map. In the one-dimensional \(N=8\) zero-padded schematic, the input \(x_1,\ldots,x_8\) produces eight outputs \(y_1,\ldots,y_8\). The matrix view is \(y=T_hx\), where \(T_h\in\mathbb{R}^{8\times 8}\) is Toeplitz. In two dimensions, the same filter moves across an image to produce a feature map.
