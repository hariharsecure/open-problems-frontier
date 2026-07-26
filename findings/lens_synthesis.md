# Lens panel synthesis — partials (2026-07-25)

5 lenses (algebraic · analytic · probabilistic · cross-domain · adversarial) × 4 levels. The signal is
CONVERGENCE (angles multiple independent lenses hit) and the META-GATE the adversarial lens exposed.

## ★ CONVERGED LEAD — Collatz β as a spectral quantity of the Syracuse transfer operator
FOUR lenses arrived here independently:
- Algebraic: ⟨2⟩ = full unit group mod 3ⁿ ⇒ 𝓛 block-diagonalizes into ~n exact blocks; λ₂ / character-sum certificate.
- Analytic: verified 𝓛 on ℤ/3ⁿℤ reproduces c₁,c₂,c₃ exactly; β = Lyapunov exp of the ⟨2⟩-cocycle; spectral radius may converge to β GEOMETRICALLY vs the DP's ~1/n crawl.
- Probabilistic: Doeblin minorization — measured the newest-3-adic-digit min-mass **δ_n ≈ 0.126 flat for n≤8** (uniform=1/3); a proven floor δ* gives a FINITE-WINDOW β bound (no c_n grind, escapes the RAM wall).
- Cross-domain: it IS a Ruelle operator (Jenkinson–Pollicott); truncating steps a≤E keeps it a valid UPPER bound while integers shrink ~3ⁿn → nE bits ⇒ rigorous **β₁₁–β₁₃ at ~0.4 GB**.
Two payoffs: (a) tighter/faster β; (b) the M16 rate-FLOOR (unit-shell block norm / δ_n floor) — the lower-rate the c_n telescoping PROVABLY can't give.
→ COMPUTE RUNNING: research/M16/transfer_operator/ (spectrum + rate-floor tests; single-lineage).

## ★★ THE GATE (adversarial #1) — does tightening β even MATTER?
The entire c_n/β program (ladder, c₉, spectrum, truncation) is load-bearing on an UNVERIFIED claim: that a
lower β transmits to a better Collatz preimage-density exponent γ. Our cards CONTRADICT each other (Tao:
helps "numerically"; our M09/SOLVE.md: "walled/tautological"). Nobody wrote g(β) and solved g(β*)=0.84.
→ COMPUTE RUNNING: research/M09/transmission/ — extract g(β) from Tao 2019, solve β*, classify:
   (A) β*≈1.3 reachable → lane ALIVE with finish-line n; (B) β*≈1.001 → TAUTOLOGICAL, retire ladder;
   (C) upper-β ↛ lower-γ → logical refutation, retire.
THIS GATES whether the converged spectral/truncation compute is worth finishing. Run it FIRST.

## C07 matmul — exact capacity ceiling (go/no-go)
Converged (cross-domain slice-rank + probabilistic square-capacity + algebraic wreath-headroom): compute the
EXACT capacity ceiling of any cyclic-group STPP. Probabilistic already measured CKSU square-capacity → 2/m → 0
(ω→2 needs →1) ⇒ lane may be DEAD despite escaping the cap-set/slice-rank barrier. Cross-domain: θ_p table
= best ω any STPP in (Z/p)ⁿ can give, vs achieved 2.8155. → Sol-partials is on C07; sharpen it to "prove the
ceiling" — a well-characterized no-go IS the result. (Wreath-headroom numbers single-lineage, need cross-check.)

## Reclassify (honest)
- **M07 Goldbach / M08 Twin-prime:** adversarial — the Selberg PARITY BARRIER makes every fleet computation
  would-matter=✗ by construction. Correctly CLOSED-at-reproduction, not advanceable partials. (Analytic offers a
  safe shippable: certified singular-series constants C₂, 2C₂ to 1000 digits w/ rigorous tail — a real exact
  sub-result, but not conjecture progress.)
- **P05 baryogenesis:** cancellation mechanisms ⇒ no single model-independent eEDM floor exists; residue is a
  per-benchmark survival-cost catalog, not one number.

## Priority order (routed)
1. β→γ TRANSMISSION gate (running) — decides the whole β program.
2. Transfer-operator spectrum + M16 rate-floor (running) — M16 floor matters regardless of the gate.
3. IF gate=A: certified truncation → β₁₁–β₁₃. 4. C07 capacity ceiling (Sol). 5. Reclassify M07/M08/P05.
All load-bearing numbers single-lineage until June's dual-lineage cross-check.
