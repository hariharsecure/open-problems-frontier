# Findings — the honest negatives

The most useful thing this fleet did may be *knowing when to stop*. These are results about what is
**not** reachable, and why — each one saved compute that would otherwise have been ground into a wall.

## 1. Collatz β-bound improvement is tautological → retired
[`collatz_beta_gamma_tautological.md`](collatz_beta_gamma_tautological.md)

The fleet computed improved rigorous upper bounds on Tao's Syracuse constant β (down to β ≤ 1.4796,
dual-verified). Then it asked the question that matters: *does tightening β actually advance Collatz?*
Deriving Tao's transmission relation and solving it, beating the standing Krasikov–Lagarias bound
(γ = 0.84) would require **β\* ≈ 1.0545** — within ~5% of the perfect-mixing value β = 1, i.e. morally
the conjecture itself (finish line ≈ n = 126 vs a compute wall near n = 9). Verdict: **tautological.**
The β terms are valid rigorous bounds; they are **not** Collatz progress. The grind was retired.

## 2. Goldbach / Twin-prime: the parity barrier
Any finite fleet computation on these is goal-orthogonal by construction (the Selberg parity barrier).
Reproductions of published records are possible and were done as engine checks; genuine progress is not
fleet-reachable. Correctly classified as **closed-at-reproduction**.

## 3. Frontier triage (multi-lens)
[`lens_synthesis.md`](lens_synthesis.md) · [`adversarial_walls.md`](adversarial_walls.md)

Five independent analytical "lenses" (algebraic, analytic, probabilistic, cross-domain, adversarial)
were run over the open partials. They *converged* on reformulating the Collatz β object as the spectrum
of a transfer operator — an attack that, when computed, produced a clean **negative** (the operator is
nilpotent, spectrum {0,1}, no spectral shortcut) plus a structural redirect. Documented honestly:
convergence is a signal, but a converged lead can still be empty, and saying so is the result.

---

*Principle: a well-characterized wall is a contribution. Rigor makes a result trustworthy; honesty about
significance makes it usable.*
