# TRANSMISSION β→γ — does improving β actually MATTER? (M09 meta-check)

**Verdict: (B) morally tautological → RETIRE the c_n/β program as a Krasikov–Lagarias-beating goal.**
**β\* = 1.0545** (need β within ~5.5% of the conjectured perfect-mixing value β=1). Reachable β≈1.43 (n=9)
transmits to γ≈0.41 — not only short of KL's 0.84 but *below the trivial ~0.81 preimage-tree bound*.
Finish line to beat 0.84 is n≈126 (c_n support ≈10^60 states); the exact-DP compute wall is n≈9–10.

Owner: June (meta-check). Date: 2026-07-25. Analysis-only, ~no compute. Reproduce: `python3 derive_f.py`.

---

## 1. The transmission map g(β) — with citation

**Sourced facts (Tao 2020 blog "Equidistribution of Syracuse random variables and density of
Collatz preimages", 2020-01-25; arXiv:1909.03562 = Tao 2019, *Forum Math. Pi* 2022):**

- `c_n := inf_{b: 3∤b} P(Syrac(ℤ/3ⁿℤ) = b)`, and `c_n = 3^{−βn+o(n)}`, `β ≥ 1`. *(verbatim)*
- Submultiplicativity **`c_{n₁+n₂−1} ≥ c_{n₁} c_{n₂}`**, `c₁=1/3`, `c₂=2/63`. *(verbatim, Lemma 2)*
- **Proposition 3 (the only hard anchor):** *"Suppose that β=1 … Then #{N ≤ x : N ∈ (Syrᴺ)\*(1)} ≫ x^{1−o(1)}."*
- **The transmission, stated but NOT written in closed form:** *"A variant of the argument shows that for
  any value of β, … holds whenever **γ < f(β)**, where **f : [0,1]→[0,1] is an explicitly computable function
  with f(β) → 1 as β → 1**."*
- **The lever, verbatim:** *"In principle, one could then **improve the Krasikov–Lagarias result γ = 0.84 by
  getting a sufficiently good upper bound on β, which is in principle achievable numerically**."*

**Tao gives no closed form for f.** So I DERIVED g=f from his preimage-counting mechanism and **calibrated
it to his one hard anchor f(1)=1** (Prop 3). This is MINE (derived), labelled as such; it is not Tao's
displayed formula — but it (a) reproduces the only value Tao pins, and (b) is corroborated model-free below.

**Derivation (MINE — large-deviation count of backward Syracuse paths).** An n-step preimage N of a fixed
target ↔ a length-n geometric path (a₁…aₙ), aᵢ≥1, P(aᵢ=k)=2^{−k}, total A=Σaᵢ, size `N ~ 2^A/3ⁿ`.
Size ≤ x=2^L ⟹ A ≤ A_max(n)=L+n·log₂3. #length-n paths with sum A ~ C(A−1,n−1) ~ 2^{A·h(n/A)}
(h = binary entropy); the fraction hitting the fixed target residue mod 3ⁿ ~ c_n = 3^{−βn}. Summing,
with n=uL and `c=log₂3=1.585`:

> **g(β) = f(β) = max_{u>0} [ −β·c·u + (1+u·c)·h( u/(1+u·c) ) ]**,  `h(w)=−w log₂w−(1−w)log₂(1−w)`.

**Calibration passes exactly:** `f(1.0) = 1.00000` (argmax u=2.409) → reproduces Tao Prop 3 (β=1 ⟹ x^{1−o(1)}). ✔

## 2. Solve g(β\*) = 0.84 (the Krasikov–Lagarias level)

Bisection on the (monotone-decreasing) f:

> **f(β\*) = 0.84  ⟹  β\* = 1.0545.**

| β | γ = f(β) | note |
|---|---|---|
| 1.0000 | **1.0000** | Tao Prop 3 anchor (calibration) |
| 1.0400 | 0.8756 | |
| **1.0545** | **0.8400** | **← threshold to beat KL 0.84** |
| 1.0600 | 0.8274 | |
| 1.1000 | 0.7476 | already below KL |
| 1.2000 | 0.6032 | |
| **1.4300** | **0.4054** | **reachable at n=9** |
| 1.4796 | 0.3755 | current dual-verified β bound |
| 1.5550 | 0.2980 | n=6 ladder |
| 1.7560 | 0.2532 | prior best (n=4) |

## 3. Classification — (B), with the exact reasoning

The rubric: (A) β\*≈1.3 & reachable; (B) β\*≈1 / only at the limit → tautological; (C) direction mismatch.

- **(C) is REFUTED by Tao himself** and by the math. Submultiplicativity `c_{k(m−1)+1} ≥ c_m^k` gives a
  *rigorous lower bound* `c_N ≥ 3^{−β_{m−1}·N}` for all N in a progression — so a computed **upper** bound
  β ≤ β_n **does** transmit to a rigorous **lower** bound γ ≥ f(β_n). Direction is fine. Not a logical wall.
- **(A) is REFUTED numerically.** β\* = 1.0545, **not** ≈1.3. The reachable end of the ladder (β≈1.43 at n=9)
  maps to **γ ≈ 0.41** — worse than Krasikov–Lagarias 0.84, worse than Korec ~0.79, and *below the trivial
  Applegate–Lagarias preimage-tree bound ~0.81*. The lane does not have a reachable finish line.
- **(B) is CORRECT.** β\*=1.0545 sits within **5.5%** of the conjectured perfect-mixing value β=1. Certifying
  β ≤ 1.055 via exact c_n means proving the Syracuse min-mass mixing is within 5.5% of perfect — which is
  *morally the hard conjecture β=1 itself* (Tao: "I cannot prove β=1"). There is **no genuine shortcut**.

**The finish line, made concrete (why "unreachable").** Using the M16 fit β_n−1 ≈ 2.17·n^{−0.76}
(and M16's proof that n·(β_n−1) is *increasing*, i.e. convergence is **slower than 1/n**, making this an
*under*-estimate of n): reaching β_n ≤ 1.0545 needs **n ≈ 126**. The exact c_n DP has support 2·3^{n−1} ≈
**10^60 states** at n=126. The measured wall: n=5 → 149 s, ~125×/step ⟹ n≈9–10 is the practical ceiling
(β≈1.43 → γ≈0.41). By contrast a *hypothetical* β\*=1.3 would have sat at n≈13 (support ~10^6, feasible) —
that is the world we are NOT in.

## 4. Reconciling the card contradiction (Tao "helps numerically" vs our "walled/tautological")

**Both are right; they describe the same equation from two ends.**
- Tao is **literally correct**: the map is real, finite β>1 suffices (β\*=1.0545 > 1, not β=1), and a numerical
  upper bound on β *does* improve γ. So the fleet must NOT claim (C) "direction-refuted" or "logically
  impossible" — that would be wrong.
- The fleet's **"walled/tautological" is operationally correct**: β\*=1.0545 requires n≈126 while the compute
  wall is n≈9–10 (γ≈0.41 there). Tao's own hedge — *"in principle achievable numerically"* — is load-bearing
  on **"in principle"**: the transmission is a theorem, the *reach* is not. The equation f(β\*)=0.84 ⟹
  β\*≈1.055 is exactly what turns his "in principle" into our "in practice, no": the numerical target lands
  unreachably close to β=1.

## 5. Recommendation

**RETIRE the c_n/β grind and the transfer-operator spectral estimate *as a Krasikov–Lagarias-beating goal.***
This SAVES the fleet compute now running (c₉ grind + transfer-operator spectrum): neither can move γ, because
even β≈1.43 → γ≈0.41 ≪ 0.84, and the 0.84 finish line (β\*=1.055, n≈126, 10^60 states) is astronomically
past the wall. The honest, publishable output is this **well-characterized wall**: *"exact Syracuse mixing to
the feasible n≈9–10 gives β≤1.43, i.e. preimage exponent γ≤~0.41 via Tao's transmission — insufficient to
beat Krasikov–Lagarias 0.84, which would require β≤1.055 (n≈126); the route is tautological, needing
near-perfect mixing."*

**What legitimately survives (not goal-orthogonal):** the *verified exact c₄…c₇/c₉ computation and the
improved rigorous β upper bound* stand on their own as a clean computational result (M09 SOLVE), and **M16's
rate question** (β_n−β\* ≥ c/n via the non-vanishing-defect lemma) is a genuinely-open, honestly-scoped
sub-lemma — just not a KL-beating one. Keep those as their own small results; stop spending compute chasing γ.

---
*Sources:* Tao 2020 blog (terrytao.wordpress.com/2020/01/25/), arXiv:1909.03562; Krasikov–Lagarias
*Acta Arith.* 109 (2003), arXiv:math/0205002 (γ=0.84); Korec 1994 (θ>log3/log4≈0.792); M09 SOLVE.md /
card.md, M16 card.md (β ladder, rate fit). f(β): DERIVED here (`derive_f.py`), calibrated to Tao Prop 3.
