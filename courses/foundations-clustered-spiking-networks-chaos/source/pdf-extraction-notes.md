# PDF Extraction Notes

## Extraction

- Source PDF: `/Users/arjun/Downloads/clusters(6).pdf`
- Command used before drafting: `pdftotext -layout '/Users/arjun/Downloads/clusters(6).pdf' -`
- Extracted length: 908 text lines.
- Document title in extraction: `Macroscopic chaos in spiking circuits`
- Document date in extraction: `June 17, 2020`
- Extracted page count visible in text: 21 pages.

## Section Inventory

- Sec. 1, Scenarios
- Sec. 1.1, Spiking network model - general setup
- Sec. 1.2, Sparse, random network of subpopulations
- Sec. 1.3, E/I clustered network: formulation using Tilo's notations
- Sec. 1.4, Luca's notes
- Sec. 2, Ideas
- Sec. 2.1, Testing if switching dynamics is chaotic or multistable
- Sec. 2.2, Notations
- Sec. 2.3, Fully connected networks
- Sec. 2.3.1, A: Many clusters with fixed size
- Sec. 2.3.2, B: Few clusters with large size
- Sec. 2.3.3, C: Many clusters with large size
- Sec. 2.3.4, Projects
- Sec. 2.3.5, Project 1: macroscopic chaos in fully connected network
- Sec. 2.4, Erdos-Renyi networks
- Sec. 2.4.1, a: Erdos-Renyi neurons
- Sec. 2.4.2, b: Erdos-Renyi clusters
- Sec. 2.5, E vs. EI networks
- Sec. 3, Aims
- Sec. 4, Methods
- Sec. 4.1, E- and E/I-clustered network
- Sec. 4.2, E/I network
- Sec. 4.3, Observable
- Sec. 5, Results
- Sec. 5.1, E/I network
- Sec. 5.2, E network
- Sec. 6, OLD STUFF: The mechanism driving state transitions
- Sec. 6.1, Transition-triggered variability
- Sec. 6.2, Cross-correlation
- Sec. 7, Scaling properties of state transitions
- Sec. 8, Chaos in the mesoscale theory
- References [1]-[12]

## Extraction Quirks and Notation Warnings

- The PDF uses both `Q` and `C` for cluster count. The first half uses `Q`; methods/results later use `C`. The coordinator should harmonize notation while preserving both source conventions in the notation table.
- The PDF uses both `N_c` and `N_Q=N/Q` for cluster size. The course should explain the equivalence or reserve one symbol for the final notation.
- The extracted text around Sec. 1.3 has line breaks inside equations (12)-(14). The coverage file maps the mathematical roles rather than copying raw extracted formatting.
- The line defining the chaos limit says "for xi -> there's a transition"; context indicates `xi -> 0`.
- The PDF alternates `R`, `Rj`, and `R_J` for the inhibitory-clustering proportionality factor. Treat these as the same intended parameter unless the coordinator finds otherwise.
- The PDF states "expiatory" where context requires "excitatory".
- The PDF says "inter-clusters weights" where context requires inter-cluster weights.
- The PDF says "than neurons" in the Erdos-Renyi cluster section; context requires "then neurons".
- The zero-lag autocorrelation diagnostic depends on distinguishing an OU-like finite-size contribution `exp(-|t|/tau_xi)` from a smooth deterministic-chaotic autocorrelation. This should be taught carefully because raw binned spike data can obscure the derivative at zero lag.
- Sec. 2.3 says the Gaussian inter-cluster weights are truncated when a draw is negative, but the extracted wording does not establish whether the implementation resamples, zeros/clips, or samples from a formally truncated normal distribution. Chapter prose should say only that negative weights are excluded until the convention is verified.
- Sec. 2.3.2 has a source ambiguity for fully connected regime B. The heading/prose says "Few clusters with large size," consistent with fixed `Q` and `N_Q -> infinity`, but the extracted body says `Q=sqrt(N), N_Q=sqrt(N)`, duplicating the case-C scaling. The coordinator should verify the PDF/source before teaching regime B's exact scaling.

## Bibliographic Warnings

- The PDF cites references [3,4] while discussing transitions to chaos in coupled LIF equations. Reference [3], `kadmonSompolinsky2015transition`, supports transitions to chaos in random neural networks generally but should not be treated as verifying that specific coupled-LIF claim without source verification. Reference [4], `kerenZurMazzucatoOz2008direct`, appears to be a high-energy physics paper, "Direct mediation and a visible metastable supersymmetry breaking sector," and is likely a mistaken or stale reference.
- PDF reference [5], `mazzucatoFontaniniLaCamera2015cosyne`, is a CoSyNe abstract. The extracted metadata has no abstract number, poster number, DOI, or page range.
- PDF reference [8], `recanatesiEtAl2020metastable`, is listed as an arXiv preprint `arXiv:2001.09600`. The coordinator may choose to update to a later peer-reviewed citation if one is intended, but the BibTeX preserves the PDF source.
- PDF reference [9], `rostamiEtAl2020spiking`, is listed as a 2020 bioRxiv preprint. The extracted metadata has no DOI. Verify before final publication if a later article exists.
- Schwalger et al. 2017 is mentioned in Sec. 4.1 but not included in the PDF references. I added `schwalgerDegerGerstner2017towards` as the likely intended GIF/finite-size population reference.

## Internal Review Round 1: Mathematical and Source Grounding

Checks applied:

- Confirmed that the map includes every numbered PDF equation family (1)-(25) and assigns each to a teaching location.
- Confirmed that finite-size variability and quenched variability are not conflated: `xi=1/sqrt(N_E)` is mapped separately from `kappa`, Gaussian inter-cluster weight heterogeneity, sparse adjacency, neuron-level ER variability, and cluster-level ER variability.
- Confirmed that the fully connected regimes A/B/C include the finite-size term, the quenched term, the sample-specific few-cluster caveat, and the SCS-like many-large-cluster limit.
- Confirmed that the E/I versus E-only comparison includes the inhibitory amplification mechanism `j_{alpha I} >> j_{alpha E}` and the opposite network-size sensitivity predictions.
- Confirmed that diagnostic claims are mapped as tests rather than asserted results: zero-lag autocorrelation, perturbation recovery/divergence, switch-time plateaus, and Lyapunov exponents.

Revisions applied after round 1:

- Added separate coverage items for the fixed in-degree sparse subpopulation model, the large-`K` simplification, and the `Q -> infinity` independence assumption.
- Added explicit mapping for variance-decomposition observables and for transition-triggered decomposition into within/outside E/I current components.
- Added bibliographic warnings for incomplete or suspicious PDF references.
- Added source-ambiguity warnings for regime-B scaling, negative Gaussian draw handling, and the `[3,4]` coupled-LIF citation.

## Internal Review Round 2: Pedagogy and Course Continuity

Checks applied:

- Confirmed that each roadmap item points to a precise chapter/section target rather than only to a whole chapter.
- Confirmed that foundational prerequisites are assigned before advanced uses: spike trains/filtering before filtered current equations, balance before Tilo notation, dynamical systems before perturbation and Lyapunov diagnostics, SCS before E/I-clustered SCS analogies.
- Confirmed that observables are assigned to Ch09 as diagnostic tools and to Ch10 as research-program outputs, avoiding duplication as chapter prose.
- Confirmed that figure-sensitive source material is described qualitatively and flagged for original teaching figures, not source-figure reuse.
- Confirmed that unclear source claims are labeled as hypotheses or open regimes, especially transient chaos and the coupled-LIF citation.

Revisions applied after round 2:

- Added a target-chapter anchor table to help chapter workers preserve the incremental course sequence.
- Added coordinator integration checks for notation drift and for the `N_c=107` versus `N_c=250` trace examples.
- Added foundational references for dynamical systems, spike-train/neuron theory, balanced networks, clustered networks, and SCS/rate chaos so chapter citations have a stable baseline.

## Coordinator Notes

- `source/roadmap-coverage.md` currently contains 107 mapped roadmap items.
- `backmatter/references.bib` currently contains 22 BibTeX entries.
- The course should cite the PDF's old aims/methods/results material as research-program motivation, not as finalized results unless the coordinator verifies the underlying simulations.
- The coordinator should verify the suspicious reference [4] and the precise role of [3], `kadmonSompolinsky2015transition`, in the coupled-LIF claim, then decide whether to remove or limit those chapter citations even though [4] remains listed in BibTeX for source completeness.
