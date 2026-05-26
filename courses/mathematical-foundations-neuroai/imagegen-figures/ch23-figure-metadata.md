# Chapter 23 Figure Metadata

No image files were generated in this worker pass, and the chapter source does not include missing `\includegraphics` commands. These are proposed assets for a later image-generation pass.

## `ch23-computational-graph-chain-rule.png`

- Section(s) supported: 23.1 Computational graphs.
- Pedagogical purpose: Show the graph for \(z=(xy+\sin x)^2\), with forward values and local derivative arrows.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout. Subject: clean computational graph for z=(xy+sin x)^2 with nodes x, y, xy, sin x, sum, square, and arrows showing local derivative labels sparsely. Include a small forward-pass value strip for x=2, y=3 without dense arithmetic. Style: white background, crisp navy line work, teal nodes, warm-gold derivative arrows, restrained red highlight for the two paths from x to output. Sparse in-image labels only. Exact equations should go in the caption, not as dense image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."

## `ch23-forward-reverse-autodiff.png`

- Section(s) supported: 23.2 Forward-mode and reverse-mode autodiff.
- Pedagogical purpose: Contrast tangent propagation forward with adjoint propagation backward on the same graph.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout with two panels. Subject: left panel shows forward-mode tangent dots moving from inputs to output and labeled JVP; right panel shows reverse-mode adjoint arrows moving from scalar loss back to inputs and labeled VJP. Use the same small graph in both panels. Style: white background, navy graph edges, teal primal nodes, gold forward tangents, red backward adjoints. Sparse in-image labels only. Exact equations should go in captions, not image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."

## `ch23-stable-softmax-logsumexp.png`

- Section(s) supported: 23.3 Numerical precision and stability.
- Pedagogical purpose: Explain overflow in naive softmax and stabilization by subtracting the maximum logit.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout. Subject: three logits with one very large value feeding a naive exponentiation path that overflows, contrasted with a stabilized path subtracting max then exponentiating bounded values. Include a compact softmax probability bar output. Style: white background, crisp navy line work, teal stable path, muted gray naive path, restrained red overflow warning. Sparse in-image labels only. Exact equations should go in captions, not image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."

## `ch23-vectorized-batched-affine.png`

- Section(s) supported: 23.4 Vectorization and efficient computation.
- Pedagogical purpose: Show a scalar loop replaced by batched matrix multiplication with explicit batch, input-feature, and output-feature axes.
- Comprehensive ImageGen prompt: "Use case: scientific-educational. Asset type: lecture-note raster infographic for a PDF. Composition: 16:10 horizontal layout. Subject: left side shows many small scalar dot products as repeated loops; right side shows a batch matrix X times W transpose plus broadcast bias producing Y, with axes batch, input feature, output feature. Include a small GPU/BLAS kernel cue as abstract blocks, not a brand logo. Style: white background, navy labels, teal tensors, gold contracted feature axis, red highlight for broadcast bias axis. Sparse in-image labels only. Exact equations should go in captions, not image text. Avoid logos, watermarks, decorative stock imagery, and pseudo-data presented as real data."
