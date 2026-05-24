# Chapter 8 Figure Metadata: Limits, Continuity, Derivatives, and Integrals

All Chapter 8 figures were generated with the built-in Codex ImageGen workflow as raster images, then copied into `imagegen-figures/`.

## Figure: `ch08-limits-continuity.png`

- Pedagogical purpose: Separate the idea of a limiting value from the stronger condition of continuity at the point.
- Supports section(s): 8.1 Limits and continuity.
- Exact mathematical objects shown: function graph `y = f(x)`; input `a`; limiting value `L`; left-hand and right-hand approach; removable discontinuity where `lim_{x -> a} f(x)=L` but `f(a)` is different.
- What the reader should notice first: nearby values can approach `L` even when the actual value `f(a)` is not equal to `L`.
- Necessary labels: `limit exists`, `continuity requires f(a)=L`, `x = a`, `L`, `f(a)`, `from left`, `from right`.
- Text reference: Section 8.1 references Figure `\ref{fig:ch08-limits-continuity}` when explaining approach versus actual value.
- Teaching caption: A limit is about approach, while continuity also checks the actual value. In the left panel, values from both sides approach the same height `L` as `x -> a`. In the right panel, the nearby values still approach `L`, but the solid point `f(a)` is elsewhere, so the function is not continuous at `a`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram for limits and continuity, showing function values approaching a limiting value from both sides and contrasting a removable discontinuity.
Style: white background, navy line work, teal curve, warm gold approach arrows/points, restrained red highlight for the missing point and actual function value, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: two balanced panels in one horizontal figure. Left panel titled only "limit exists". Draw coordinate axes in navy with a smooth teal curve approaching an open circle at x = a, y = L. Show warm gold sample points on the curve from the left and right approaching the open circle, with small arrows along the curve pointing toward x = a. Add dashed navy guide lines from x = a and y = L. Right panel titled only "continuity requires f(a)=L". Draw the same smooth teal curve with an open red circle at y = L and, directly above or below at the same x = a, a solid red point labeled f(a). Include a small label L next to the open circle and a small label x = a under the vertical dashed line.
Exact mathematical objects shown: function graph y = f(x), input a, limiting value L, one-sided approach from x<a and x>a, removable discontinuity where lim_{x to a} f(x)=L but f(a) is different.
Necessary labels, exact text only: limit exists, continuity requires f(a)=L, x = a, L, f(a), from left, from right. Keep labels large and legible, placed outside lines where possible. Do not include paragraphs, extra equations, tiny labels, or decorative elements.
Pedagogical goal: the reader should notice first that a limit is about nearby values approaching L, while continuity additionally requires the actual value f(a) to equal that limit.
```

## Figure: `ch08-derivative-local-linearization.png`

- Pedagogical purpose: Show a derivative as the coefficient of the best local linear replacement for a nonlinear function.
- Supports section(s): 8.2 Derivatives as local linearization.
- Exact mathematical objects shown: function `y=f(x)`; expansion point `a`; tangent line; derivative `f'(a)`; local linear model `L(x)=f(a)+f'(a)(x-a)`; small input change `h`; approximate output change `f'(a)h`.
- What the reader should notice first: after zooming in near `a`, the nonlinear curve is well approximated by a line.
- Necessary labels: `global curve`, `local linear model`, `y = f(x)`, `x = a`, `tangent`, `L(x) = f(a) + f'(a)(x-a)`, `h`, `f'(a)h`.
- Text reference: Section 8.2 references Figure `\ref{fig:ch08-derivative-local-linearization}` when explaining tangent slopes and differentials.
- Teaching caption: The derivative is the coefficient of the local linear model. Globally the curve bends, but after zooming near `x=a`, the tangent line `L(x)=f(a)+f'(a)(x-a)` becomes a good replacement. A small input change `h` produces a first-order output change `f'(a)h`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram explaining a derivative as local linearization by zooming into a curve until it looks like its tangent line.
Style: white background, navy line work, teal nonlinear curve, warm gold tangent/local window, restrained red point of expansion, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: two-panel horizontal figure. Left panel titled only "global curve". Draw axes in navy, a smooth teal nonlinear curve y = f(x), a red point at x = a, and a warm-gold tangent line touching the curve at the red point. Add a small translucent warm-gold rectangle around the point to indicate a zoom window. Right panel titled only "local linear model". Show a magnified coordinate patch centered at the same red point. Draw the teal curve nearly overlapping a warm-gold straight tangent line labeled L(x) = f(a) + f'(a)(x-a). Add a small navy run-rise triangle with horizontal leg labeled h and vertical leg labeled f'(a)h.
Exact mathematical objects shown: function y=f(x), expansion point a, derivative f'(a) as slope, tangent line, local linear approximation L(x)=f(a)+f'(a)(x-a), small input change h, output change approximately f'(a)h.
Necessary labels, exact text only: global curve, local linear model, y = f(x), x = a, tangent, L(x) = f(a) + f'(a)(x-a), h, f'(a)h. Keep labels large and legible. Do not include paragraphs, extra formulas, tiny labels, or decorative elements.
Pedagogical goal: the reader should notice first that the derivative is not merely a number to compute; it is the slope of the best local linear replacement for the function near a.
```

## Figure: `ch08-integral-accumulation.png`

- Pedagogical purpose: Connect Riemann sums to a definite integral as accumulated rate-times-width contributions.
- Supports section(s): 8.3 Integrals as accumulation.
- Exact mathematical objects shown: time interval `[a,b]`; rate function `r(t)`; partition width `Delta t`; Riemann rectangles; accumulated area `int_a^b r(t) dt`.
- What the reader should notice first: each rectangle is a small contribution, and the integral is the limiting accumulated total.
- Necessary labels: `t`, `rate r(t)`, `a`, `b`, `Delta t`, `total accumulation`, `integral_a^b r(t) dt`, `rectangles become area`.
- Text reference: Section 8.3 references Figure `\ref{fig:ch08-integral-accumulation}` when defining Riemann sums and accumulation.
- Teaching caption: Integration accumulates many small rate-times-width contributions. Each rectangle contributes approximately `r(t_i) Delta t`. As the partition is refined, the rectangle sum approaches the shaded accumulated quantity `int_a^b r(t) dt`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram explaining an integral as accumulation from Riemann sums to area under a rate curve.
Style: white background, navy line work, teal rate curve, warm gold rectangles, restrained red accumulated total marker, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: one wide figure with a single coordinate plot. Horizontal axis labeled t, vertical axis labeled rate r(t). Draw a smooth teal curve r(t) above the axis from t = a to t = b. Under the curve draw several warm-gold Riemann rectangles of equal width Delta t, with heights touching or nearly touching the curve. Shade the total accumulated area lightly in teal/gold. Add a bracket or arrow along the horizontal interval labeled a to b. Place a restrained red label near the shaded area reading total accumulation. Include the integral formula as a concise label above the shaded area: integral_a^b r(t) dt.
Exact mathematical objects shown: time interval [a,b], rate function r(t), partition width Delta t, rectangle approximation sum r(t_i) Delta t, accumulated area integral from a to b.
Necessary labels, exact text only: t, rate r(t), a, b, Delta t, total accumulation, integral_a^b r(t) dt, rectangles become area. Keep labels large and legible. Do not include paragraphs, extra equations, tiny labels, or decorative elements.
Pedagogical goal: the reader should notice first that integration turns many small rate-times-width contributions into one accumulated quantity.
```

## Figure: `ch08-ode-euler-preview.png`

- Pedagogical purpose: Show an ODE as a local rate rule whose solution follows tangent directions, and connect this to Euler simulation.
- Supports section(s): 8.4 Differential equations preview.
- Exact mathematical objects shown: state `x(t)`; time `t`; derivative `dx/dt`; ODE `dx/dt=f(x,t)`; initial condition `x(0)=x0`; equilibrium; Euler update `x_{k+1}=x_k+Delta t f(x_k,t_k)`.
- What the reader should notice first: the equation gives local slopes, while the trajectory and Euler steps are built from those local slopes.
- Necessary labels: `state changes by rate`, `Euler preview`, `t`, `x(t)`, `x(0)=x0`, `dx/dt`, `equilibrium`, `dx/dt = f(x,t)`, `Delta t`, `x_{k+1}=x_k+Delta t f(x_k,t_k)`.
- Text reference: Section 8.4 references Figure `\ref{fig:ch08-ode-euler-preview}` when introducing solution curves and Euler updates.
- Teaching caption: An ODE specifies local rates, and a solution curve follows those rates from an initial condition. The decay trajectory approaches an equilibrium. Euler's method approximates the trajectory by repeatedly taking small straight steps `x_{k+1}=x_k+Delta t f(x_k,t_k)`.
- ImageGen prompt:

```text
Use case: scientific-educational
Asset type: raster figure for a mathematical lecture-note PDF, readable at 0.9 page width
Primary request: Create a clean academic diagram previewing ordinary differential equations through a state trajectory, vector field arrows, and Euler steps for a decay system.
Style: white background, navy line work, teal exact trajectory, warm gold Euler step segments, restrained red initial condition and equilibrium, generous whitespace, precise geometry, no decorative gradients, no stock-photo realism, no dense text blocks.
Composition: two balanced panels in one horizontal figure. Left panel titled only "state changes by rate". Draw a horizontal time axis labeled t and vertical axis labeled x(t). Mark a red initial point labeled x(0)=x0. Draw a smooth teal decaying curve toward a red dashed horizontal equilibrium line labeled equilibrium. Place small navy tangent arrows along the curve labeled dx/dt. Right panel titled only "Euler preview". Draw the same axes and a lighter teal exact decay curve. Overlay warm-gold piecewise straight segments stepping forward in time, with small gold dots at step endpoints. Label one step width Delta t and one vertical update x_{k+1}=x_k+Delta t f(x_k,t_k). Include a concise ODE label near the top: dx/dt = f(x,t).
Exact mathematical objects shown: state x(t), time t, derivative dx/dt as rate of change, ODE dx/dt=f(x,t), initial condition x(0)=x0, equilibrium, Euler update x_{k+1}=x_k+Delta t f(x_k,t_k).
Necessary labels, exact text only: state changes by rate, Euler preview, t, x(t), x(0)=x0, dx/dt, equilibrium, dx/dt = f(x,t), Delta t, x_{k+1}=x_k+Delta t f(x_k,t_k). Keep labels large and legible. Do not include paragraphs, extra formulas, tiny labels, or decorative elements.
Pedagogical goal: the reader should notice first that a differential equation specifies local rates, and a solution curve is obtained by repeatedly following those local rates from an initial condition.
```
