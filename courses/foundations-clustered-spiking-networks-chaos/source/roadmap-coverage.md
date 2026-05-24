# Roadmap Coverage Audit

Source: `/Users/arjun/Downloads/clusters(6).pdf`, extracted with `pdftotext -layout`.

This file is an audit map, not course prose. It assigns every major roadmap item from the PDF to the chapter and section where the new course must teach it. Chapter workers and the final coordinator should use the `R###` identifiers below as coverage checks.

## Target Chapter Anchors

| Chapter | Course target | Required local section targets |
|---|---|---|
| Ch01 | Dynamical Systems Language | State spaces, flows, fixed points, attractors, stability, Jacobians, bifurcations, multistability, chaos, Lyapunov exponents |
| Ch02 | Stochastic Processes for Neural Dynamics | Spike trains, point processes, Poisson variability, shot noise, filtering, autocorrelation, finite-size scaling |
| Ch03 | Single-Neuron and Population Models | LIF, stochastic LIF, GIF, transfer functions, population firing rates |
| Ch04 | Balanced Excitatory/Inhibitory Networks | Balance, random recurrent networks, asynchronous irregular dynamics, inhibition-stabilized dynamics |
| Ch05 | Clustered Attractor Networks | Cell assemblies, potentiation/depression, active/inactive clusters, metastable switching, E-clustered networks with homogeneous inhibition |
| Ch06 | Random Rate Networks and SCS Chaos | Rate equations, SCS transition, chaotic autocorrelations, self-coupled/MAS-style units, cluster-level rate analogies |
| Ch07 | Mean-Field and Dynamic Mean-Field Theory | Static mean field, self-consistency, effective stochastic processes, quenched vs annealed disorder |
| Ch08 | E/I Clustered Networks | Paired E/I clusters, Tilo notation, potentiated EE/EI/IE/II connections, cluster-strength parameters, finite-size vs quenched variability |
| Ch09 | Diagnosing Multistability Versus Chaos | Scaling tests, perturbation tests, Lyapunov diagnostics, autocorrelation diagnostics, transition-triggered averages |
| Ch10 | The Research Program | Phase diagrams, observables, simulation program, E-only vs E/I comparison, contribution-level research questions |

## Appendix Supplements

| Appendix | Course target | Supplemental role |
|---|---|---|
| App. A | Finite-Size Mesoscopic Theory Bridge | Collects the derivation-level hazard, age-density, renewal/quasi-renewal, finite-size noise, and filtering bridge from LIF/GIF neurons to cluster population equations. |
| App. B | Numerical Diagnostic Protocols | Collects implementation-level run manifests, network generation checks, spike-to-rate filtering, state detection, autocorrelation/HWHM/kink estimation, transition-triggered analysis, Lyapunov protocols, and decision criteria. |

## Coverage Register

| ID | PDF locus | Roadmap content to teach | Course target |
|---|---|---|---|
| R001 | Sec. 1, "Scenarios" | The overall claim: macroscopic chaos in spiking circuits can arise through several scenarios, with the most important one being a many-large-cluster regime that realizes the Sompolinsky-Crisanti-Sommers mechanism without finite-size effects. | Ch10.1, "Roadmap and central claim"; Ch06.1, "Why SCS is the reference mechanism" |
| R002 | Sec. 1.1 | Network organized into `Q` clusters of size `N_c`, total size `N = Q N_c`, with `N_E = gamma N_c` excitatory and `N_I = (1-gamma)N_c` inhibitory neurons per cluster. | Ch08.1, "Cluster indices and population sizes"; Ch04.1 for E/I population proportions |
| R003 | Sec. 1.1, Eq. (1) | Input current `I_a^alpha(t)` as a filtered version of a raw synaptic drive `y_a^alpha(t)`. Explain the convolution over past time. | Ch02.3, "Synaptic filtering as shot-noise convolution"; Ch03.3, "Filtered input current in LIF/GIF neurons" |
| R004 | Sec. 1.1, Eq. (1) | Synaptic kernel `epsilon(t)=tau_s^{-1} exp(-t/tau_s) theta(t)`, its causality, time constant, and normalization. | Ch02.3, "Exponential filters"; Ch03.2 for membrane/synaptic timescale separation |
| R005 | Sec. 1.1, Eq. (2) | Raw input `y_a^alpha(t)` decomposes into intra-cluster sums and inter-cluster sums across presynaptic type `beta` and cluster `b`. | Ch08.2, "Input decomposition: within cluster vs outside cluster" |
| R006 | Sec. 1.1, Eq. (2) | Intra-cluster weights `\hat J^{alpha beta}` and inter-cluster weights `\check J_{ab}^{alpha beta}` must be introduced as distinct mathematical objects. | Ch08.2, "Hat/check notation"; Ch05.2 for potentiation/depression intuition |
| R007 | Sec. 1.1 | Spike train `s_{a,i}^alpha(t)=sum_k delta(t-t_{a,i,k}^alpha)` and spike times `{t_{a,i,k}^alpha}`. | Ch02.1, "Spike trains as point processes"; Ch03.1 for neuron-model output |
| R008 | Sec. 1.1 | Neurons are stochastic LIF units; the course should explain why stochastic single-neuron dynamics are used before applying population/DMFT approximations. | Ch03.1, "Stochastic LIF"; Ch07.4, "Effective stochastic neuron in DMFT" |
| R009 | Sec. 1.2, Eq. (3) | Sparse random subpopulation model: intra-cluster excitatory and inhibitory weights `\hat J^{alpha E}=\hat J`, `\hat J^{alpha I}=-g \hat J`. | Ch04.2, "Excitation-inhibition sign structure"; Ch08.3, "Sparse subpopulation baseline" |
| R010 | Sec. 1.2, Eq. (4) | Inter-cluster weights use adjacency variables `Gamma_{ab}^{alpha beta}` with `\check J_{ab}^{alpha E}=\check J Gamma_{ab}^{alpha E}` and `\check J_{ab}^{alpha I}=-\check g \check J Gamma_{ab}^{alpha I}`. | Ch08.3, "Sparse inter-cluster graph"; Ch07.2 for quenched adjacency |
| R011 | Sec. 1.2 | Fixed in-degree `K`: each population receives `K_E=fK` excitatory and `K_I=(1-f)K` inhibitory inputs from other clusters, with `K << Q`. | Ch04.3, "Sparse balanced recurrence"; Ch08.3, "Fixed-in-degree cluster graph" |
| R012 | Sec. 1.2 | Excitatory and inhibitory inputs paired from the same cluster in the sparse subpopulation model. | Ch08.3, "Subpopulation connectivity constraints" |
| R013 | Sec. 1.2 | Balance choice `\check g = f g/(1-f)` cancels excitation and inhibition in the mean inter-cluster drive. | Ch04.2, "Balance by cancellation"; Ch08.3, "Large-scale cancellation in sparse clusters" |
| R014 | Sec. 1.2, Eq. (5) | Rewriting raw input into inside-cluster and outside-cluster terms; show what each bracket means. | Ch08.3, "Deriving the sparse-cluster input"; Ch04.2 for intuition |
| R015 | Sec. 1.2, Eq. (6) | Population activities `A_a^E(t)` and `A_a^I(t)` are normalized sums of spike trains over excitatory and inhibitory neurons. | Ch02.4, "Population activity from point processes"; Ch08.1 for notation |
| R016 | Sec. 1.2, Eq. (7) | Synaptic input in terms of population activities, including factors `N_E`, `N_I`, `g`, `\check g`, and adjacency matrices. | Ch08.3, "Activity-level input equation"; Ch07.1 for mean-field variables |
| R017 | Sec. 1.2, Eq. (8) | Stationary mean population activities satisfy `<A_a^E>=<A_a^I>=r`; the mean synaptic input is `\bar y=(\hat J+\check J fK)(N_E-gN_I)r`. | Ch04.4, "Balanced stationary mean"; Ch07.1, "Static self-consistency" |
| R018 | Sec. 1.2 | The roadmap assumes identical E/I firing-rate parameters "as in model A of Brunel 2000"; teach this as a simplifying baseline, not a biological identity. | Ch04.3, "Brunel-style random networks"; Ch10.2, "Modeling assumptions to test" |
| R019 | Sec. 1.2, Eq. (9) | In the `Q -> infinity` limit, population activities become asymptotically independent, so input autocovariance is a sum of population autocovariances. | Ch07.3, "Independence and self-averaging"; Ch02.5 for autocovariance definition |
| R020 | Sec. 1.2, Eq. (9) | Input autocorrelation expression `C_y(tau)` contains intra-cluster variance, inter-cluster variance, and the population autocorrelation `C_A(tau)`. | Ch07.3, "Second-order mean field"; Ch08.3 for cluster interpretation |
| R021 | Sec. 1.2, Eq. (10) | DMFT self-consistency: `C_A(tau)=<r(t|y)r(t+tau|y)>-<r(t|y)>^2`, where `r(t|y)` is the LIF firing rate under the effective input. | Ch07.4, "Dynamic mean-field self-consistency loop"; Ch03.4 for transfer functions |
| R022 | Sec. 1.2, Eq. (11) | Large-`K` simplification: inside-cluster input becomes subdominant, leaving `C_y(tau)` proportional to inter-cluster terms times `K C_A(tau)`. | Ch07.5, "Large-connectivity simplification"; Ch08.3 for sparse-cluster scaling |
| R023 | Sec. 1.3 | Tilo notation starts from a classically balanced random network and solves for baseline weights `J_EE`, `J_IE`, `J_EI`, `J_II`. | Ch04.3, "Balanced E/I baseline"; Ch08.4, "Tilo notation" |
| R024 | Sec. 1.3, Eq. (12) | Intra-cluster potentiation: `\hat J_EE=J_E^+J_EE`, `\hat J_IE=J_I^+J_IE`, and inhibitory-targeted terms `\hat J_{\alpha I}=J_I^+J_{\alpha I}`. | Ch08.4, "Potentiated EE, IE, EI, II connections" |
| R025 | Sec. 1.3, Eq. (13) | Inter-cluster depression uses `J_E^-`, `J_I^-` and adjacency matrices for EE, IE, EI, II blocks. | Ch08.4, "Depressed inter-cluster weights"; Ch05.2 for preserving average coupling |
| R026 | Sec. 1.3 | Relation `J_I^+ = 1 + R(J_E^+ - 1)` and depression factor `J^{E,I-}=(Q-J^{E,I+})/(Q-1)`; `R=1` means matched E/I cluster strength and `R=0` leaves inhibition unclustered. | Ch08.4, "Cluster-strength parameters and proportionality R" |
| R027 | Sec. 1.3, Eq. (14) | Full Tilo input equation decomposed into inside-cluster EE, inside-cluster IE, inside-cluster EI/II, outside-cluster EE, outside-cluster IE, and outside-cluster EI/II contributions. | Ch08.5, "Expanded paired-cluster input"; Ch04.2 for sign/cancellation intuition |
| R028 | Sec. 1.3, Figs. 1-4 | Qualitative trace examples compare `N_c=107` and `N_c=250`; the new course should make original teaching figures that communicate finite-size versus robust switching without copying these figures. | Ch08.6, "Example traces as motivation"; Ch09.2, "Network-size scaling diagnostic"; figures owned by chapter workers |
| R029 | Sec. 2 opening | Switching dynamics links to physiological and cognitive phenomena: hidden Markov states, state/context-dependent variability reduction, expectation, decision-making, and attention. | Ch10.1, "Why the distinction matters"; citations in Ch10 references |
| R030 | Sec. 2 opening | Multistability mechanism: many attractors stable as `N -> infinity`, destabilized by finite cluster-size effects; expected for E-clustered networks with homogeneous inhibition. | Ch05.4, "Finite-size destabilized attractors"; Ch09.1, "Multistability hypothesis" |
| R031 | Sec. 2 opening | Mesoscopic chaos mechanism: no stable attractors even as cluster size grows; switching persists at any cluster size; candidate mechanism for paired E/I clusters. | Ch06.2, "Chaos without attractors"; Ch08.7, "E/I clusters as mesoscopic units"; Ch09.1 |
| R032 | Sec. 2 opening | Previous E-cluster mean-field work gives stable `N -> infinity` attractors; Vahid/Rostami-style E/I clustered simulations show robust switching in larger networks. | Ch05.5, "E-clustered homogeneous inhibition"; Ch08.6, "E/I switching observations"; Ch10.3 |
| R033 | Sec. 2 opening | Central Question 1: Does mesoscopic chaos exist in the E/I clustered spiking network? | Ch10.3, "Question 1: existence of mesoscopic chaos" |
| R034 | Sec. 2 opening | Central Question 2: Can multistability and chaos be discriminated in simulations or experiments? | Ch09.1, "Diagnostic problem"; Ch10.3 |
| R035 | Sec. 2 opening | Finite-size noise parameter `xi = 1/sqrt(N_E)` and quenched noise/heterogeneity parameter `kappa`; both must be defined carefully and distinguished. | Ch02.6, "Finite-size fluctuations scale as `1/sqrt(N)`"; Ch08.7, "Quenched cluster variability"; Ch09.2 |
| R036 | Sec. 2 opening | Quenched variability `kappa` can come from binary sparse adjacency `Gamma_{ab}^{alpha beta}=Bernoulli(K/N)` or from heterogeneous weights such as Gaussian inter-cluster draws. | Ch07.2, "Quenched versus annealed disorder"; Ch08.7, "Sources of kappa" |
| R037 | Sec. 2 opening | In the `xi-kappa` plane, small `kappa` gives a single attractor, large `kappa` gives chaos as `xi -> 0`, and finite `xi` can preserve switching across regimes. | Ch09.2, "The `xi-kappa` phase plane"; Ch10.4, "Phase diagram program" |
| R038 | Sec. 2 opening | Switch-time logic: as `xi` decreases, switching first slows because finite-size effects weaken, then reaches a plateau controlled by chaos. | Ch09.2, "Switch-time scaling and plateau test" |
| R039 | Sec. 2 opening | Intermediate regime: multistable finite-`xi` switching and chaotic `xi -> 0` switching can have similar autocorrelation widths, enabling matched comparisons. | Ch09.2, "Matched-timescale comparison"; Ch10.4 |
| R040 | Sec. 2.1 | Zero-lag autocorrelation discriminator: finite-size OU-like noise contributes a kink/nonzero derivative through `exp(-|t|/tau_xi)`, while purely chaotic autocorrelation has vanishing derivative at zero lag. | Ch09.3, "Autocorrelation zero-lag derivative/kink diagnostic"; Ch02.5 for OU covariance |
| R041 | Sec. 2.1 | Experimental caveat: zero-lag derivative tests may be hard in data even if mathematically clean. | Ch09.3, "Practical limits of autocorrelation diagnostics"; Ch10.5 |
| R042 | Sec. 2.1 | Perturbation test: in metastability, small perturbations to an active cluster decay back to the attractor on membrane timescales unless perturbations match finite-size escape noise. | Ch09.4, "Perturbation recovery in multistability"; Ch01.4 for basins |
| R043 | Sec. 2.1 | Perturbation test: in chaos, arbitrarily small perturbations diverge and the network does not relax back to the pre-perturbation configuration. | Ch09.4, "Perturbation divergence in chaos"; Ch01.6 for Lyapunov interpretation |
| R044 | Sec. 2.1 | Large perturbation response timescale in chaos should match the autocorrelation width, not the membrane time. | Ch09.4, "Timescale signature of chaotic recovery" |
| R045 | Sec. 2.1 | Sensitivity can be calculated for a frozen realization of escape noise; this separates deterministic sensitivity from changing noise draws. | Ch09.4, "Frozen-noise perturbation protocol" |
| R046 | Sec. 2.2, Eq. (15) | General notation: populations `alpha,beta in {E,I}`, probabilities `p_{alpha beta}`, population proportions `n_alpha`, and weights scaled as `J_{i_alpha,j_beta}=j_{alpha beta}/sqrt(N)`. | Ch04.2, "Balanced scaling"; Ch08.1, "Population and cluster indices" |
| R047 | Sec. 2.2, Eq. (15) | Clustered notation: `Q` clusters, `N_Q=N/Q`, intra-cluster weights use `\hat j_{alpha beta}`, inter-cluster weights use `\check j_{alpha beta}`. | Ch08.4, "Hat/check notation in `1/sqrt(N)` scaling" |
| R048 | Sec. 2.2 | External input `I_alpha^ext = sqrt(N) i_alpha^ext` enforces the balanced regime with `1/sqrt(N)` recurrent weights. | Ch04.2, "External drive and balance"; Ch07.1 |
| R049 | Sec. 2.2 | The roadmap separates fully connected networks with weight heterogeneity from Erdos-Renyi networks with connectivity heterogeneity. | Ch08.7, "Two sources of quenched variability"; Ch10.4 |
| R050 | Sec. 2.3, Eq. (16) | Fully connected networks set `p_{alpha beta}=1`; all quenched variability is in inter-cluster weights `\check j_{alpha beta} ~ N(1,g_{alpha beta}^2)`, with negative draws excluded by a truncated/handled Gaussian convention that must be verified before stating the exact sampling rule. | Ch08.7, "Gaussian inter-cluster heterogeneity"; Ch07.2; extraction notes |
| R051 | Sec. 2.3 | Scaling regime A: fixed cluster size `N_Q` as `N,Q -> infinity`; finite-size effects remain and quenched inter-cluster variability also contributes. | Ch09.5, "Scaling regime A"; Ch10.4 |
| R052 | Sec. 2.3 | Scaling regime B: interpreted from the heading/prose as fixed number of clusters with `N,N_Q -> infinity`; finite-size effects vanish and only a fixed amount of quenched inter-cluster variability remains. Verify the contradictory extracted `Q=sqrt(N), N_Q=sqrt(N)` body text before chapter prose states the scaling. | Ch09.5, "Scaling regime B"; Ch10.4; extraction notes |
| R053 | Sec. 2.3 | Scaling regime C: many large clusters, e.g. `Q=sqrt(N)`, `N_Q=sqrt(N)`, or `Q=N^gamma`, `N_Q=N^{1-gamma}`; finite-size effects vanish but aggregate quenched variability survives. | Ch09.5, "Scaling regime C"; Ch06.4, "Macroscopic SCS-like chaos from many units" |
| R054 | Sec. 2.3.1, Eqs. (17)-(18) | Regime A variance decomposition for `var(I_alpha)` into outside-cluster quenched weights and finite-size term `c r_alpha/N_Q`; both remain at large `N` when `N_Q` is fixed. | Ch09.5, "Variance decomposition in regime A" |
| R055 | Sec. 2.3.1 | Inhibition-stabilized amplification: quenched variability can be large because inhibitory terms satisfy `j_{alpha I} >> j_{alpha E}`. | Ch04.5, "Inhibition-stabilized amplification"; Ch08.8 |
| R056 | Sec. 2.3.2, Eq. (19) | Regime B variance decomposition under the few-cluster interpretation: finite-size effects vanish, but with few clusters the dynamics is sensitive to the specific inter-cluster draw and lacks a cluster mean-field limit. Treat the printed/extracted scaling as source-ambiguous. | Ch09.5, "Regime B and sample-specific dynamics"; extraction notes |
| R057 | Sec. 2.3.3, Eq. (20) | Regime C variance decomposition: finite-size terms vanish while quenched inter-cluster contribution remains; infinitely many clusters make a true SCS-like macroscopic chaos limit possible. | Ch06.4, "SCS-like macroscopic chaos"; Ch09.5, "Regime C" |
| R058 | Sec. 2.3.4 | Project observable: monitor separate contributions to `var(I)` from quenched variability and finite-size effects, then relate them to autocorrelation time and cluster switch time. | Ch10.4, "Variance-decomposition experiments"; Ch09.6, "Observable dashboard" |
| R059 | Sec. 2.3.5 | Project 1: start from `g_{alpha beta}=0`, map finite-size variance versus `N`, then turn on `g` and separate finite-size from quenched contributions. | Ch10.4, "Fully connected macroscopic chaos project" |
| R060 | Sec. 2.3.5 | Find the critical value of `var(I)` or `g` for the transition to chaos, characterize transition with switching times and autocorrelations as in SCS. | Ch06.3, "SCS transition observables"; Ch10.4 |
| R061 | Sec. 2.3.5 | Estimate Lyapunov exponents for diverging trajectories and test whether switching dynamics is controlled by the Lyapunov exponent. | Ch01.6, "Lyapunov exponents"; Ch09.7, "Mesoscale Lyapunov diagnostics"; Ch10.4 |
| R062 | Sec. 2.4 | Erdos-Renyi variability can generate quenched disorder without weight variability. | Ch08.7, "Connectivity-generated kappa"; Ch07.2 |
| R063 | Sec. 2.4 | ER neuron-level variability: `Prob(J_{i_alpha,j_beta} != 0)=p_{alpha beta}`. | Ch08.7, "Neuron-level Erdos-Renyi variability" |
| R064 | Sec. 2.4 | ER cluster-level variability: `Prob(cluster p and cluster q connected)=p_cl`, with full neuron-level connectivity between connected cluster pairs. | Ch08.7, "Cluster-level Erdos-Renyi variability" |
| R065 | Sec. 2.4.1, Eq. (21) | ER neuron-level `var(I_alpha)` has three terms: outside-cluster connectivity variability, within-cluster connectivity variability, and finite-size effects. | Ch09.5, "ER variance decomposition"; Ch10.4 |
| R066 | Sec. 2.4.2 | ER cluster-level `var(I_alpha)` has outside-cluster connectivity variability and finite-size effects, then should be studied in regimes A/B/C. | Ch09.5, "Cluster-level ER scaling"; Ch10.4 |
| R067 | Sec. 2.5 | E/I clustered networks amplify quenched variability relative to E-only clusters because inhibitory structure contributes strongly in inhibition-stabilized regimes. | Ch08.8, "Why paired E/I clusters amplify kappa"; Ch10.3 |
| R068 | Sec. 3, Aim 1 | Research hypothesis: E/I clustered transitions are driven by quenched inter-cluster variability, whereas E-clustered homogeneous-I transitions are driven by finite-size effects. | Ch10.3, "Mechanism hypothesis"; Ch09.1 |
| R069 | Sec. 3, Aim 2 | Research hypothesis: E/I clustered networks, but not E-clustered networks, exhibit rate chaos when a paired E/I cluster acts like a deterministic rate unit. | Ch06.5, "Clusters as effective rate units"; Ch10.3 |
| R070 | Sec. 3, Aim 2 | Perturbation amplitudes to test: one membrane potential, all neurons in one cluster, one spike, or one spike in all neurons in one cluster. | Ch09.4, "Perturbation protocol ladder"; Ch10.4 |
| R071 | Sec. 3 | Mesoscale Lyapunov exponents are a primary test in the effective theory. | Ch09.7, "Mesoscale Lyapunov exponents"; Ch10.4 |
| R072 | Sec. 3 | Conceptual link: E/I clustered network as biologically plausible SCS rate chaos; a single E/I cluster may resemble a self-coupled MAS/Stern-Abbott-Sompolinsky rate unit. | Ch06.5, "SCS and self-coupled unit analogy"; Ch08.7; Ch10.3 |
| R073 | Sec. 3 note | Transition to chaos in coupled LIF equations is motivating background, but the course must verify the cited `[3,4]` support: [3] supports random-network/rate chaos generally, and [4] appears unrelated to neuroscience. | Ch10.6, "Open bibliographic checks"; extraction notes |
| R074 | Sec. 4.1 | E-clustered model: `N` GIF neurons with `N_E=0.8N`, `N_I=0.2N`, connection probabilities `p_EE=0.2`, `p_EI=p_IE=p_II=0.5`. | Ch03.5, "GIF model"; Ch05.5, "E-clustered network construction"; Ch10.2 |
| R075 | Sec. 4.1 | Balanced weights `J_{alpha beta}` are solved from the balance condition and divided by `sqrt(N)`. | Ch04.2, "Solving balance and scaling weights" |
| R076 | Sec. 4.1 | E-clusters multiply within-cluster EE connections by `J^+`; inter-cluster EE weights are depressed by `J^-=(Q-J^+)/(Q-1)` to preserve mean input. | Ch05.2, "Potentiation and compensating depression" |
| R077 | Sec. 4.1 | E/I clusters pair each E cluster with one I cluster and potentiate corresponding EI, IE, and II connections. | Ch08.4, "Paired E/I clusters" |
| R078 | Sec. 4.1 | Inhibitory clustering is weaker in simulations: `J_I^+ = 1 + R_J(J_E^+ - 1)`, with `R_J=0.75` in the cited simulations. | Ch08.4, "Relative inhibitory cluster strength"; Ch10.2 |
| R079 | Sec. 4.2, Eq. (22) | Alternative E/I network notation: `C_alpha` clusters, `n_alpha=N_alpha/C_alpha`; cluster strength `s_{alpha beta}=J_{alpha beta}^+/C`. | Ch08.4, "Cluster-strength parameter s"; Ch10.4 |
| R080 | Sec. 4.2 | In the E/I network, `C_E=C_I=C`; in the E-only network, inhibitory neurons form one homogeneous population. | Ch05.5 and Ch08.4, "E-only versus E/I architecture" |
| R081 | Sec. 4.2 | Inter-cluster depression factors `J_{c,c'}^-` are drawn from a truncated Gaussian with mean `J^- > 0` and variance `g^2/C`, forming the analogue of quenched variability in a chaotic rate network. | Ch08.7, "Truncated-Gaussian inter-cluster heterogeneity"; Ch06.5 |
| R082 | Sec. 4.3 | Average cluster firing rate `r_c(t)=n_c^{-1} sum_i r_i(t)` is the core mesoscale observable. | Ch03.4, "Population rates"; Ch09.6, "Observable dashboard" |
| R083 | Sec. 4.3, Eqs. (23)-(24) | Single-neuron spike-count autocorrelation `a_i(tau)`, estimated in 5 ms bins with trial average and a shuffled-trial shift predictor; remove central Poisson delta peak to get rate autocorrelation. | Ch02.5, "Autocorrelation and shift predictors"; Ch09.3 |
| R084 | Sec. 4.3 | Autocorrelation time `tau_i` and cluster autocorrelation time `tau_c` are half-width at half-maximum (HWHM), following SCS/MAS-style diagnostics. | Ch06.3, "Chaotic autocorrelation times"; Ch09.3 |
| R085 | Sec. 4.3 | Cluster lifetime `T_C`: distribution of intervals where `r_c(t)>r_0`, with threshold choice requiring explicit reporting. | Ch09.6, "Cluster lifetime distributions"; Ch10.4 |
| R086 | Sec. 4.3 | Distributions of cluster firing rates and counts of active clusters, compared conceptually to Mazzucato-style clustered attractor analyses. | Ch05.4, "Active-cluster states"; Ch09.6 |
| R087 | Sec. 4.3 | Fano factor as a variability observable. | Ch02.2, "Count variability and Fano factor"; Ch09.6 |
| R088 | Sec. 4.3, Eq. (25) | Dimensionality `d=Tr(C)^2/Tr(C^2)` from cluster firing-rate correlation matrix `C_{cc'}`. | Ch09.6, "Dimensionality of cluster activity"; Ch10.4 |
| R089 | Sec. 5.1 | E/I phase hypothesis in `s,g`: small `s` gives balanced asynchronous irregular activity; large `s`, small `g` gives attractor states; large `s`, large `g` gives chaotic rate dynamics. | Ch10.4, "E/I phase diagram"; Ch04.4, Ch05.3, Ch06.3 |
| R090 | Sec. 5.1 | Large `s`, large `g` may also include transient chaos; the course should label this as an open regime rather than an established result. | Ch10.4, "Transient-chaotic regime and uncertainty"; Ch09.7 |
| R091 | Sec. 5.1 | In the E/I chaotic phase, `tau_c` and `T_C` should be insensitive to network size when number of clusters is fixed and cluster size grows. | Ch09.2, "Network-size insensitivity test"; Ch10.4 |
| R092 | Sec. 5.2 | E-only phase hypothesis: small `s` balanced; increasing `s` activates clusters; larger `s` stabilizes clusters completely, leaving a narrow metastable window. | Ch05.5, "E-only clustered attractor phases"; Ch10.3 |
| R093 | Sec. 5.2 | E-only timescales are predicted to be weakly sensitive to `g` and strongly sensitive to cluster size, opposite to E/I clusters. | Ch09.2, "E-only finite-size scaling contrast"; Ch10.3 |
| R094 | Sec. 6 | Metastable attractor states are sets of activated E clusters `{c_1,...,c_M}` with active time `T_C >> tau_m,tau_s`; transitions occur on shorter time `T_tr << T_C`. | Ch05.3, "Metastable cluster states"; Ch09.6 |
| R095 | Sec. 6 | Mechanistic picture of transitions as diffusion between potential wells; use this as intuition and contrast it with chaos, where stable wells need not exist. | Ch01.5, "Energy-landscape intuition and its limits"; Ch09.1 |
| R096 | Sec. 6.1 | Transition-triggered questions: whether fluctuations rise before transitions, which populations drive transitions, and how finite-size versus quenched variability contribute. | Ch09.8, "Transition-triggered analyses"; Ch10.4 |
| R097 | Sec. 6.1 | Transition-triggered variance: split spatial variance of input currents to E neurons in a focused cluster into within-cluster E/I and outside-cluster E/I components. | Ch09.8, "Input-variance decomposition around transitions"; Ch08.5 |
| R098 | Sec. 6.1 | Transition-triggered mean input: split mean input into within/outside and E/I sources; up transitions may be driven by increased excitation or decreased inhibition. | Ch09.8, "Mean-current transition signatures"; Ch04.2 |
| R099 | Sec. 6.1 | Transition-conditioned mean firing-rate direction: for state transition `A -> B`, test growth along `r_B-r_A` and suppression in orthogonal directions. | Ch09.8, "Directional transition-triggered averages"; Ch01.2 for state-space vectors |
| R100 | Sec. 6.1 | Sweep transition-triggered observables over inhibitory cluster parameter `q` and inter-cluster heterogeneity `g`. | Ch10.4, "Observable sweeps over q and g" |
| R101 | Sec. 6.2 | Cross-correlate mean firing rate of a focused cluster with spatial variance of input current at lags from a state transition; remove mean-rate bias and isolate transitions. | Ch09.8, "Cross-correlation alternative to triggered averages" |
| R102 | Sec. 7 | For a fixed network size and parameter set, spiking network and mesoscale theory should match as functions of `q` and `g`. | Ch07.6, "Matching spiking and mesoscale theories"; Ch10.4 |
| R103 | Sec. 7 | Scaling test 1: fix E neurons per cluster `N_c=n_E N/C` and increase number of clusters `C`; finite-size effects survive, so metastability should survive in appropriate regimes. | Ch09.5, "Fixed cluster-size scaling"; Ch10.4 |
| R104 | Sec. 7 | Scaling test 2: fix number of clusters `C` and increase neurons per cluster; finite-size effects vanish, so transitions disappear for homogeneous-I E clusters but not necessarily for paired E/I clusters. | Ch09.5, "Fixed cluster-count scaling"; Ch10.4 |
| R105 | Sec. 7 | Scaling test 3: increase both number of clusters and neurons per cluster; find a scaling that preserves a fixed cluster activation lifetime. | Ch09.5, "Joint scaling for preserved lifetimes"; Ch10.4 |
| R106 | Sec. 8 | Mesoscale Lyapunov exponents have been computed and chaotic properties observed; compare clustered-network chaos with SCS and Stern-Abbott-Sompolinsky/MAS self-coupled-unit dynamics. | Ch09.7, "Mesoscale Lyapunov diagnostics"; Ch06.5 |
| R107 | Sec. 8 | Compare onset of mesoscale chaos with autocorrelation of mean cluster firing rate, as in SCS. | Ch06.3, "SCS autocorrelation transition"; Ch09.3 |

## Reference Coverage Map

| Citation key | PDF reference | Course use |
|---|---|---|
| `amitBrunel1997global` | [1] Amit and Brunel 1997 | Ch05 for persistent structured activity; Ch10 phase language |
| `engelEtAl2016selective` | [2] Engel et al. 2016 | Ch10 motivation for state/context-dependent variability and attention |
| `kadmonSompolinsky2015transition` | [3] Kadmon and Sompolinsky 2015 | Ch06 and Ch09 for transition to chaos in random neural networks and Lyapunov tests |
| `kerenZurMazzucatoOz2008direct` | [4] Keren-Zur, Mazzucato, Oz 2008 | Listed only because it appears in the PDF; coordinator must verify relevance before using |
| `mazzucatoFontaniniLaCamera2015cosyne` | [5] Mazzucato, Fontanini, La Camera 2015 | Ch10 motivation; incomplete conference metadata |
| `mazzucatoEtAl2015dynamics` | [6] Mazzucato et al. 2015 | Ch05 E-clustered multistability; Ch09 active-cluster observables |
| `mazzucatoEtAl2019expectation` | [7] Mazzucato et al. 2019 | Ch10 expectation and variability reduction motivation |
| `recanatesiEtAl2020metastable` | [8] Recanatesi et al. 2020 | Ch10 behavioral action-sequence motivation |
| `rostamiEtAl2020spiking` | [9] Rostami et al. 2020 | Ch08 paired E/I cluster motivation; Ch10 robust switching comparison |
| `schueckerGoedekeHelias2018optimal` | [10] Schuecker, Goedeke, Helias 2018 | Ch02/Ch09 OU-like finite-size autocorrelation/kink comparison |
| `sompolinskyCrisantiSommers1988chaos` | [11] Sompolinsky, Crisanti, Sommers 1988 | Ch06 SCS chaos and DMFT reference point |
| `sternSompolinskyAbbott2014dynamics` | [12] Stern, Sompolinsky, Abbott 2014 | Ch06 MAS/self-coupled analogy and transient chaos |
| `brunel2000dynamics` | Mentioned in Sec. 1.2 and Sec. 4 | Ch04 Brunel-style balanced asynchronous irregular networks |
| `vanVreeswijkSompolinsky1996chaos` | Foundational supplement | Ch04 balanced chaotic/asynchronous background |
| `vanVreeswijkSompolinsky1998chaotic` | Foundational supplement | Ch04 balanced-state theory |
| `renartEtAl2010asynchronous` | Foundational supplement | Ch04 asynchronous irregular decorrelation |
| `litwinKumarDoiron2012slow` | Foundational supplement | Ch05 clustered balanced networks and slow switching |
| `schwalgerDegerGerstner2017towards` | Mentioned in Sec. 4.1 | Ch03 GIF/finite-size population theory |
| `ostojic2014two` | Foundational supplement | Ch04/Ch06 asynchronous irregular regimes and rate chaos context |
| `gerstnerEtAl2014neuronalDynamics` | Foundational supplement | Ch02/Ch03 spike trains, LIF/GIF, population rates |
| `strogatz2015nonlinear` | Foundational supplement | Ch01 dynamical systems and chaos language |
| `dayanAbbott2001theoretical` | Foundational supplement | Ch02/Ch03/Ch04 background reference |

## Coordinator Integration Checks

- Use this file to audit chapters after both review rounds. Each `R###` item should be either explicitly taught or intentionally deferred in `final-report.md`.
- The coverage-critical items most likely to drift in notation are `N_c` versus `N_Q`, `Q` versus `C`, `J_I^+` versus `R_J`, and `g`, `kappa`, `\check g`, `g_{alpha beta}`. Harmonize in frontmatter/notation.
- The new course should not reproduce the PDF figures. For `R028`, teach the qualitative `N_c=107` versus `N_c=250` trace contrast with original schematic/synthetic teaching figures.
- Bibliographic warnings are recorded in `source/pdf-extraction-notes.md`; do not cite the suspicious PDF reference [4], or use [3] (`kadmonSompolinsky2015transition`) as support for the specific coupled-LIF claim, until verified.
- The integrated appendices are supplements to the ten-chapter ladder, not replacements for chapter coverage: App. A supports R003, R007, R008, R015, R021, and R035; App. B supports R058, R061, R070, R083-R088, R096-R101, and R103-R107.
