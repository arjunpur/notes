# Models of Higher Brain Function Figure Metadata

This ledger records Codex-generated raster figures integrated into the canonical
course PDF.

## mhbf-lecture3-bistability-mechanisms.png

- Target section: `Lecture 3: Perceptual Bistability and Multisensory Integration`,
  ambiguity and bistability.
- Visual claim: Bistable perception can be explained as competition between
  interpretations, slow adaptation of the dominant state, noise-driven attractor
  transitions, and approximate sampling of a multimodal posterior.
- Caption: Four linked mechanisms for bistable perception. Competition prevents
  both interpretations from dominating together, adaptation weakens the active
  interpretation, noise can push the system across an attractor barrier, and a
  sampling view interprets switches as visits to different modes of a posterior
  over percepts.
- Status: generated with built-in Codex image generation and copied into the
  course `figures/` directory.
- Sizing notes: integrated at `width=0.96\textwidth`; wide four-panel plate,
  light background.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate explaining perceptual bistability mechanisms for a computational neuroscience lecture.
Style: light background, dark readable labels, restrained accent colors, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four horizontal panels labeled only A, B, C, D. Panel A shows two competing percept populations with mutual inhibition and a single dominant percept. Panel B shows slow adaptation weakening the active population. Panel C shows a double-well attractor landscape with a noisy trajectory crossing from one basin to the other. Panel D shows sequential posterior samples visiting two modes. Use simple arrows, dots, curves, and population icons.
Visual claim: Bistable perception can be explained as competition between interpretations, slow adaptation of the dominant state, noise-driven attractor transitions, and approximate sampling of a multimodal posterior.
Necessary labels, exact text only: A, B, C, D, competition, adaptation, noise, sampling, percept A, percept B
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond perceptual bistability
```

## mhbf-lecture3-cue-integration.png

- Target section: `Lecture 3: Perceptual Bistability and Multisensory Integration`,
  multisensory integration as inference.
- Visual claim: Multisensory integration combines conditionally independent
  evidence by reliability, improves precision when cues share a cause, and should
  be refused when cue conflict is too large.
- Caption: Cue integration as a sequence of inference checks. A hidden state
  causes modality-specific cues, reliable cues pull the fused estimate more
  strongly, psychometric PSEs and thresholds reveal the weights and precision,
  and a causal-inference gate determines whether the cues should be fused or kept
  separate.
- Status: generated with built-in Codex image generation and copied into the
  course `figures/` directory.
- Sizing notes: integrated at `width=0.96\textwidth`; wide four-panel plate,
  light background.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate explaining multisensory cue integration for a computational neuroscience lecture.
Style: light background, dark readable labels, restrained accent colors, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four horizontal panels labeled only A, B, C, D. Panel A shows one hidden world state causing two sensory measurements. Panel B shows two broad/narrow Gaussian cue curves combining into a narrower estimate closer to the reliable cue. Panel C shows psychometric readouts with a PSE shift and a steeper combined threshold curve. Panel D shows a causal inference gate where small cue discrepancy leads to fusion and large discrepancy leads to separation. Use simple icons, arrows, curves, and short labels.
Visual claim: Multisensory integration combines conditionally independent evidence by reliability, improves precision when cues share a cause, and should be refused when cue conflict is too large.
Necessary labels, exact text only: A, B, C, D, hidden state, cue 1, cue 2, fused estimate, PSE, threshold, fuse, separate
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond cue integration
```

## mhbf-lecture4-signal-detection.png

- Target section: `Lecture 4: Decision Making I`, perceptual decisions as noisy
  classification.
- Visual claim: Signal detection separates sensory discriminability from
  decision criterion; false alarms are signal-absent evidence above/right of the
  criterion, and misses are signal-present evidence below/left of the criterion.
- Caption: Signal detection theory separates discriminability from criterion
  placement. Overlapping evidence distributions make errors unavoidable, the
  criterion controls the miss--false-alarm tradeoff, the ROC curve summarizes
  that tradeoff across criteria, and threshold functions are gradual because
  evidence varies across trials.
- Status: generated with built-in Codex image generation and copied into the
  course `figures/` directory.
- Sizing notes: integrated at `width=0.96\textwidth`; wide four-panel plate,
  light background.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate explaining signal detection theory for perceptual decision making, with error regions placed correctly.
Style: light background, dark readable labels, restrained accent colors, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four horizontal panels labeled only A, B, C, D. Panel A shows two overlapping evidence distributions on one evidence axis: a left curve labeled signal absent and a right curve labeled signal present, with a vertical decision criterion. Shade and arrow-label the signal-present left tail below the criterion as miss, and shade and arrow-label the signal-absent right tail above the criterion as false alarm. Panel B shows the same distributions with the criterion shifted, explicitly showing the tradeoff between the miss region on the signal-present left tail and the false alarm region on the signal-absent right tail. Panel C shows an ROC curve traced by moving the criterion, with larger area for better discriminability. Panel D shows a gradual psychometric threshold curve as stimulus increment increases. Use simple curves, arrows, shaded small regions, and short labels.
Visual claim: Signal detection separates sensory discriminability from decision criterion; false alarms are signal-absent evidence above/right of the criterion, and misses are signal-present evidence below/left of the criterion.
Necessary labels, exact text only: A, B, C, D, evidence, signal absent, signal present, criterion, hit, miss, false alarm, ROC, AUC, threshold
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond signal detection
```

## mhbf-lecture4-bayesian-policy.png

- Target section: `Lecture 4: Decision Making I`, Bayesian decisions as
  expected-reward policies.
- Visual claim: Bayesian decision making chooses actions by combining prior,
  likelihood, posterior belief, and rewards into a policy that maximizes
  expected reward.
- Caption: Bayesian expected-reward policy. The hidden state generates noisy
  evidence, the likelihood and prior determine the posterior, rewards convert
  posterior belief into expected value for each action, and the policy chooses
  the action whose expected reward is largest.
- Status: generated with built-in Codex image generation and copied into the
  course `figures/` directory.
- Sizing notes: integrated at `width=0.96\textwidth`; wide four-panel plate,
  light background.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate explaining Bayesian expected-reward decision policy for a computational neuroscience lecture.
Style: light background, dark readable labels, restrained accent colors, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four horizontal panels labeled only A, B, C, D. Panel A shows a hidden world state branching into two possible states and a noisy evidence measurement. Panel B shows likelihood and prior combining into a posterior over the two states. Panel C shows an expected reward comparison for two actions with a vertical decision threshold on the evidence axis. Panel D shows a policy arrow from evidence/posterior to action. Use simple icons, arrows, curves, bars, and short labels.
Visual claim: Bayesian decision making chooses actions by combining prior, likelihood, posterior belief, and rewards into a policy that maximizes expected reward.
Necessary labels, exact text only: A, B, C, D, state, evidence, likelihood, prior, posterior, reward, policy, action, threshold
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond Bayesian expected-reward decision policy
```

## mhbf-lecture4-motor-lottery.png

- Target section: `Lecture 4: Decision Making I`, continuous motor actions and
  motor lotteries.
- Visual claim: In continuous motor decisions, an action is an aim point whose
  noisy outcomes define a motor lottery; optimal planning maximizes expected
  gain while human valuation can distort gains, losses, and probabilities.
- Caption: Continuous motor actions under uncertainty. An intended aim point
  generates a distribution of endpoints, reward and penalty regions assign gains
  and losses to those endpoints, the expected-gain landscape determines the best
  aim, and behavioral caveats such as reference dependence, loss aversion, and
  probability weighting can distort objective reward maximization.
- Status: generated with built-in Codex image generation and copied into the
  course `figures/` directory.
- Sizing notes: integrated at `width=0.96\textwidth`; wide four-panel plate,
  light background.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate explaining continuous motor decisions under uncertainty and reward functions.
Style: light background, dark readable labels, restrained accent colors, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four horizontal panels labeled only A, B, C, D. Panel A shows an aim point on a screen with a cloud of possible movement endpoints caused by motor uncertainty. Panel B shows green target and red penalty regions with different gains/losses. Panel C shows several possible aim points with expected gain shown as a smooth landscape, with the best aim point shifted away from the penalty. Panel D shows behavioral caveats with simple icons for reference level, loss aversion, and probability weighting. Use simple circles, endpoint dots, arrows, and curves.
Visual claim: In continuous motor decisions, an action is an aim point whose noisy outcomes define a motor lottery; optimal planning maximizes expected gain while human valuation can distort gains, losses, and probabilities.
Necessary labels, exact text only: A, B, C, D, aim point, motor uncertainty, target, penalty, expected gain, best aim, reference, loss aversion, probability weighting
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond motor lotteries and reward functions
```

## mhbf-lecture4-sequential-llr.png

- Target section: `Lecture 4: Decision Making I`, sequential evidence
  accumulation and stopping rules.
- Visual claim: Sequential Bayesian decision making updates a log-likelihood
  ratio additively and stops when the expected error cost is smaller than the
  cost of further sampling.
- Caption: Sequential log-likelihood accumulation. Each sample contributes an
  additive update to the log-likelihood ratio, so posterior evidence evolves as
  a random walk. The policy has three regions: choose one state above the upper
  bound, choose the other below the lower bound, and continue sampling while the
  expected value of another sample exceeds its cost.
- Status: generated with built-in Codex image generation and copied into the
  course `figures/` directory.
- Sizing notes: integrated at `width=0.96\textwidth`; wide four-panel plate,
  light background.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate explaining sequential evidence accumulation with log-likelihood ratios and stop-or-continue decisions.
Style: light background, dark readable labels, restrained accent colors, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four horizontal panels labeled only A, B, C, D. Panel A shows a sequence of simple evidence samples arriving one by one. Panel B shows each sample adding a positive or negative increment to a running log-likelihood ratio. Panel C shows the log-likelihood ratio as a random walk between upper and lower decision bounds. Panel D shows three action zones: choose A above the upper bound, continue between the bounds, and choose B below the lower bound. Use simple dots, arrows, plus/minus increments, staircase trace, and horizontal bounds.
Visual claim: Sequential Bayesian decision making updates a log-likelihood ratio additively and stops when the expected error cost is smaller than the cost of further sampling.
Necessary labels, exact text only: A, B, C, D, samples, update, log-likelihood ratio, bound, choose A, choose B, continue, cost
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond sequential log-likelihood accumulation. Spell the action labels exactly as choose A and choose B, not chose A or chose B.
```

## mhbf-lecture4-evidence-accumulation.png

- Target section: `Lecture 4: Decision Making I`, drift-diffusion as the
  continuous limit and archival neural extension.
- Visual claim: Random-dot decisions can be modeled as noisy evidence from
  sensory neurons accumulated into a decision variable until a bound is reached;
  stronger coherence increases drift and shortens reaction time.
- Caption: Evidence accumulation in random-dot decisions and the neural
  extension. Motion coherence controls the strength of momentary evidence, noisy
  evidence is integrated into a decision variable, a decision is made when the
  variable reaches a bound, and variability in drift or noise produces broad
  reaction-time distributions. In the archival neurophysiology framing, MT
  supplies motion evidence and LIP represents target-linked accumulated evidence.
- Status: generated with built-in Codex image generation and copied into the
  course `figures/` directory.
- Sizing notes: integrated at `width=0.96\textwidth`; wide four-panel plate,
  light background.
- Final ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a LaTeX lecture-note PDF, wide teaching plate readable at full page width
Primary request: Create a clean four-panel teaching plate explaining evidence accumulation in random-dot perceptual decisions.
Style: light background, dark readable labels, restrained accent colors, minimal lecture-note style, generous whitespace, no decorative gradients, no stock-photo realism, no dense text
Composition: Four horizontal panels labeled only A, B, C, D. Panel A shows a random-dot motion stimulus with a subset of dots moving coherently toward one target. Panel B shows momentary sensory evidence from MT increasing with motion coherence. Panel C shows a decision variable in LIP accumulating noisy evidence until it reaches an upper or lower decision bound. Panel D shows drift-rate variability creating a heavy-tailed reaction-time distribution. Use simple dots, arrows, traces, and curves.
Visual claim: Random-dot decisions can be modeled as noisy evidence from sensory neurons accumulated into a decision variable until a bound is reached; stronger coherence increases drift and shortens reaction time.
Necessary labels, exact text only: A, B, C, D, coherence, MT, evidence, LIP, decision bound, drift, reaction time
Avoid: equations, derivations, paragraphs, tiny text, legends, watermarks, photorealistic stock imagery, extra concepts beyond evidence accumulation
```
