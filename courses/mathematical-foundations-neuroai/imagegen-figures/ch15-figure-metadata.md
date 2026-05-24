# Chapter 15 Figure Metadata

## Figure 15.1: Expectation As Averaging

- Pedagogical purpose: Show expectation as the same probability-weighted averaging operation in discrete and continuous settings, with linearity as the key algebraic property.
- Section(s) supported: 15.1 Expectation as averaging.
- Exact mathematical objects shown: Discrete values \(x=0,1,2,3\), masses \(p(x)=(0.10,0.40,0.30,0.20)\), the mode \(x=1\), the expectation marker \(\mathbb{E}[X]=1.6\), transformed values \(g(x)\), \(\mathbb{E}[g(X)]=\sum_x g(x)p(x)\), density \(p(x)\), curve \(g(x)\), \(\mathbb{E}[g(X)]=\int g(x)p(x)\,dx\), and \(\mathbb{E}[aX+bY]=a\mathbb{E}[X]+b\mathbb{E}[Y]\).
- What the reader should notice first: Probabilities act as averaging weights, and the expected value need not be the most likely value.
- Necessary labels: \(x\), \(p(x)\), \(g(x)\), mode \(x=1\), \(\mathbb{E}[X]=1.6\), \(\mathbb{E}[g(X)]\), \(\sum_x g(x)p(x)\), \(\int g(x)p(x)\,dx\), linearity.
- How the text references the figure: The prose uses Figure~\(\backslash\)ref{fig:ch15-expectation-averaging} to distinguish discrete sums, continuous integrals, and linearity of expectation.
- Comprehensive ImageGen prompt: Create a clean educational raster diagram titled "Expectation as averaging" on a white background. The diagram must explicitly distinguish the mode from the expectation in the discrete example. Layout: three unframed panels with generous whitespace. Left panel: discrete probability mass bars for \(x=0,1,2,3\) with heights \(0.10,0.40,0.30,0.20\). Mark \(x=1\) as "mode \(x=1\)" in navy or teal. Separately mark the balance point with a clear red vertical marker between \(1\) and \(2\) labeled exactly "\(\mathbb{E}[X]=1.6\)"; the red label belongs only to the expectation marker. Middle panel: smooth density \(p(x)\) with shaded weighting and a gold curve \(g(x)\), feeding into an integral expression. Bottom strip: linearity of expectation. Required labels: \(p(x)\), \(x\), \(g(x)\), mode \(x=1\), \(\mathbb{E}[X]=1.6\), \(\mathbb{E}[g(X)]=\sum g(x)p(x)\), \(\mathbb{E}[g(X)]=\int g(x)p(x)\,dx\), linearity, and \(\mathbb{E}[aX+bY]=a\mathbb{E}[X]+b\mathbb{E}[Y]\). Style constraints: navy line work, teal probability bars, warm gold value markers, restrained red only for the expectation balance marker, precise educational infographic style, no gradients, no stock-photo realism, no paragraphs, no watermark.
- Generation note: Replaced after round 2 review with a new built-in ImageGen raster output so the red marker identifies the expectation \(\mathbb{E}[X]=1.6\) and \(x=1\) is labeled as the mode.
- Teaching caption: Expectation is probability-weighted averaging. In the discrete example, the most likely value is the mode \(x=1\), while the balance point is the expectation \(\mathbb{E}[X]=1.6\). For a function of a random variable, \(\mathbb{E}[g(X)]\) is a weighted sum or integral, and linearity says that averaging can pass through addition and scalar multiplication.
- Saved path: `imagegen-figures/ch15-expectation-averaging.png`.

## Figure 15.2: Conditional Expectation

- Pedagogical purpose: Explain conditional expectation by selecting a slice of a joint distribution, renormalizing it, and turning it into a prediction function.
- Section(s) supported: 15.2 Conditional expectation.
- Exact mathematical objects shown: Joint table \(p(x,y)\), values \(X=0,1,2\), values \(Y=\mathrm{low},\mathrm{high}\), highlighted row \(Y=\mathrm{high}\), row sum \(0.60\), conditional distribution \(p(x\mid Y=\mathrm{high})=(1/12,1/4,2/3)\), prediction function \(m(y)=\mathbb{E}[X\mid Y=y]\), \(m(\mathrm{low})=1\), and \(m(\mathrm{high})=19/12\).
- What the reader should notice first: Conditioning on \(Y=\mathrm{high}\) changes the distribution of \(X\), and the resulting conditional mean is a function of the observed value \(Y=y\).
- Necessary labels: \(X\), \(Y\), \(p(x,y)\), condition on \(Y=\mathrm{high}\), row sum \(0.60\), \(p(x\mid Y=\mathrm{high})\), conditional bars \(1/12\), \(1/4\), \(2/3\), and \(m(y)=\mathbb{E}[X\mid Y=y]\).
- How the text references the figure: The prose uses Figure~\(\backslash\)ref{fig:ch15-conditional-expectation} while computing the table example and explaining conditional expectation as prediction from observed information.
- Comprehensive ImageGen prompt: Create a clean educational raster diagram for "Conditional expectation" on a white background. Left panel: a joint table for \(X=0,1,2\) and \(Y=\mathrm{low},\mathrm{high}\), with teal probability cells and the \(Y=\mathrm{high}\) row outlined in warm gold. Middle panel: the selected conditional distribution \(p(x\mid Y=\mathrm{high})\) as three bars after renormalization, labeled exactly \(1/12\), \(1/4\), and \(2/3\), from \((0.05,0.15,0.40)/0.60\). Right panel: prediction function \(m(Y)=\mathbb{E}[X\mid Y]\) with two warm-gold points \(m(\mathrm{low})=1\) and \(m(\mathrm{high})=19/12\). Use navy line work, teal probabilities, warm-gold conditioning, generous whitespace, precise geometry, readable labels, no dense text, no gradients, no stock-photo realism.
- Generation note: Replaced after round 2 review with a new built-in ImageGen raster output; the final Figure 15.2 asset is the ImageGen output saved at the path below.
- Teaching caption: Conditional expectation begins with a joint distribution. Conditioning on \(Y=\mathrm{high}\) selects and renormalizes one row, producing \(p(x\mid Y=\mathrm{high})\). The conditional expectation function \(m(y)=\mathbb{E}[X\mid Y=y]\) is the prediction of \(X\) based only on the observed information \(Y=y\).
- Saved path: `imagegen-figures/ch15-conditional-expectation.png`.

## Figure 15.3: Bayes As Reweighting

- Pedagogical purpose: Make Bayes' theorem visually concrete as prior weights multiplied by likelihoods and normalized by evidence.
- Section(s) supported: 15.3 Bayes' theorem.
- Exact mathematical objects shown: Three hypotheses \(\theta_1,\theta_2,\theta_3\), prior \(p(\theta)=(0.50,0.30,0.20)\), likelihood \(p(x\mid\theta)=(0.10,0.40,0.80)\) for observed \(x\), unnormalized weights \(w(\theta)=(0.05,0.12,0.16)\), evidence \(p(x)=\sum_\theta p(x\mid\theta)p(\theta)=0.33\), and normalized posterior \(p(\theta\mid x)\approx(0.15,0.36,0.48)\).
- What the reader should notice first: A hypothesis with moderate prior can become posterior-dominant if its likelihood for the observed data is much larger.
- Necessary labels: prior, likelihood, evidence, posterior, \(p(\theta)\), \(p(x\mid\theta)\), \(p(\theta\mid x)\), \(p(x)\), \(\theta_1,\theta_2,\theta_3\), \(x\) observed, normalized posterior values below \(1\), and the warning \(p(\theta\mid x)\) not \(p(x\mid\theta)\).
- How the text references the figure: The prose uses Figure~\(\backslash\)ref{fig:ch15-bayes-reweighting} to explain prior-likelihood multiplication, evidence normalization, and the conditional-reversal misconception.
- Comprehensive ImageGen prompt: Create a clean educational raster diagram for "Bayes' theorem as reweighting hypotheses" on a white background. Show prior \(p(\theta)=(0.50,0.30,0.20)\), likelihood \(p(x\mid\theta)=(0.10,0.40,0.80)\), evidence \(p(x)=0.33\), and normalized posterior \(p(\theta\mid x)\approx(0.15,0.36,0.48)\) over \(\theta_1,\theta_2,\theta_3\). All probability axes must run from \(0\) to \(1\), and no posterior bar may exceed \(1\). Add a restrained red warning \(p(\theta\mid x)\) not \(p(x\mid\theta)\). Use navy line work, teal and warm-gold bars, generous whitespace, readable labels, no paragraphs, no gradients, no stock-photo realism.
- Generation note: Replaced after round 2 review with a new built-in ImageGen raster output; the final Figure 15.3 asset is the ImageGen output saved at the path below.
- Teaching caption: Bayes' theorem reweights hypotheses. The prior \(p(\theta)\) is multiplied by the likelihood \(p(x\mid\theta)\) for observed data \(x\), then normalized by the evidence \(p(x)=\sum_\theta p(x\mid\theta)p(\theta)\) to produce the posterior \(p(\theta\mid x)\).
- Saved path: `imagegen-figures/ch15-bayes-reweighting.png`.

## Figure 15.4: Bayesian Decision Risk

- Pedagogical purpose: Show how posterior beliefs and a loss matrix become posterior risks, and how the Bayes action is selected by minimizing risk.
- Section(s) supported: 15.4 Bayesian decision theory.
- Exact mathematical objects shown: Posterior \(p(\theta\mid x)\), states \(\theta_1,\theta_2,\theta_3\), actions \(a_0,a_1\), loss matrix \(L(a,\theta)\), posterior risks \(R(a\mid x)=\mathbb{E}[L(a,\Theta)\mid x]\), and Bayes action \(a^*(x)\).
- What the reader should notice first: The chosen action is the one with the smaller posterior expected loss, not necessarily the action corresponding to the most probable state.
- Necessary labels: \(p(\theta\mid x)\), \(L(a,\theta)\), \(R(a\mid x)\), \(a_0\), \(a_1\), \(\theta_1,\theta_2,\theta_3\), and \(a^*(x)\).
- How the text references the figure: The prose uses Figure~\(\backslash\)ref{fig:ch15-bayesian-decision-risk} when defining posterior risk and Bayes actions.
- Comprehensive ImageGen prompt: Create a clean educational raster diagram for "Bayesian decision theory" on a white background. Left: posterior bars over \(\theta_1,\theta_2,\theta_3\) labeled \(p(\theta\mid x)\). Center: compact loss matrix \(L(a,\theta)\) with actions \(a_0,a_1\) as rows and states as columns, teal cells for low loss and restrained red cells for high loss. Right: posterior risk bars \(R(a\mid x)=\mathbb{E}[L(a,\Theta)\mid x]\) for \(a_0,a_1\), with lower-risk action marked \(a^*(x)\). Use an arrow chain posterior plus loss to risk to action. Use navy line work, teal, warm gold, restrained red, generous whitespace, precise geometry, readable labels, no paragraphs, no gradients, no stock-photo realism.
- Teaching caption: Bayesian decision theory combines posterior beliefs with a loss function. The posterior \(p(\theta\mid x)\) describes uncertainty over states, the loss matrix \(L(a,\theta)\) assigns costs to action-state pairs, and posterior risk \(R(a\mid x)\) averages those costs. The Bayes action \(a^*(x)\) is the action with smallest posterior risk.
- Saved path: `imagegen-figures/ch15-bayesian-decision-risk.png`.
