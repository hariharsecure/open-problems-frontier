# Adversarial / Limits lens — M07, M08, M09, M16, C07, P05

**Lens role (scaffold L0→L3):** for each partial name the single LOAD-BEARING assumption of the
current best angle, locate the TRUE wall (why it hasn't moved), and state the one fact/computation
that would REFUTE the current angle. Sharpening what *can't* be done exposes the tractable RESIDUE.
A well-characterized wall IS a result. No conjecture-solving claims; every load-bearing number stays
single-lineage until reproduced.

Ranked by **would-matter × tractability**. Entries 1–3 are the returned residues.

---

## 1. Collatz β→γ TRANSMISSION THRESHOLD  (M09 + M16)  — would-matter HIGH · tractability HIGH

- **Load-bearing assumption.** The entire c_n compute program (exact Syracuse minima c₄…c₉, dual-lineage,
  the joint-engine RAM wall, the β ladder 1.756→1.638→1.555→1.480→…) is load-bearing on the belief that a
  lower rigorous **upper bound** β ≤ β_n *transmits* to a better Collatz preimage-density exponent γ (the
  quantity that would beat Krasikov–Lagarias 0.84). Every card optimizes β downward; none pins the map
  γ = g(β).
- **The true wall.** Two things are asserted but never reconciled in the cards:
  (a) Tao (2020) says improving the numerical β upper bound improves K–L, "in principle achievable
  numerically" — i.e. the transmission EXISTS for finite β; yet
  (b) M09 `SOLVE.md` declares the route "walled/tautological."
  These cannot both be taken on faith. The unexamined joint is a **direction/threshold** question: we hold
  UPPER bounds β ≤ β_n; a preimage-density *lower* bound needs c_n *large* (β *small*, →1). So the usable
  statement is γ ≥ g(β_n) for the worst-case (largest) β in the interval — and the wall is simply whether
  **g(β_n) > 0.84 is reachable before the compute wall.** Nobody has written g down or solved g(β*)=0.84.
- **Refuting fact / first experiment (analysis, ~no compute).** Extract the explicit g(β) from Tao 2019
  (arXiv:1909.03562, the equidistribution⇒preimage step) — the card asserts f is "explicitly computable."
  Then solve **g(β*) = 0.84** for the threshold β*, and compare to the reachable β (≈1.43 at n=9,
  extrapolating the ladder). THREE clean outcomes, all publishable:
  - **β\* ≈ 1.3** → *numerical wall only*: the lane is alive, and c_n compute toward n≈14–18 is a concrete,
    would-matter target (reopens the most-invested lane with a finish line).
  - **β\* ≈ 1.001** → *morally tautological*: beating 0.84 needs β so close to 1 that reaching it is
    equivalent to proving near-perfect mixing (β=1), no genuine shortcut — the honest wall, and it retires
    the c_n ladder as a curiosity.
  - **g gives only an UPPER bound on γ from an upper bound on β** (direction mismatch) → the route is
    *logically* incapable of beating 0.84 with finite β — a hard refutation, not a numerical one.
- **Why it's the top residue.** One literature-read + one algebraic solve either hands the whole Collatz
  compute lane a targeted finish line OR refutes it at the right (logical vs numerical) level. It attacks
  the most compute-invested partial at its single unverified joint.
- **Stress-test of the analytic/spectral lens here:** its instinct (push Tao's characteristic-function /
  Fourier decay further) FAILS the same way — the method is local-in-time (controls only ~c·log N
  iterates); β already packages all the analytic content into one constant, so more Fourier work does not
  move γ. The residue is the *transmission*, not more mixing.

## 2. Collatz rate-lemma: the atomic-defect → mean-defect BOOTSTRAP  (M16)  — would-matter MEDIUM · tractability HIGH

- **Load-bearing assumption.** M16-R ("β_n − β* ≥ c/n", the first positive rate on Tao's β) is reduced by
  the exact identity (★) to **M_n ≥ c > 0** (mean submultiplicativity defect bounded below), and the
  proposed proof route is: bound the *atomic* one-step defect d_n = v₁+v_{n−1}−v_n ≥ δ (empirically ≈1.6),
  then bootstrap d_n ≥ δ ⇒ M_n ≥ c. The card itself flags the bootstrap as "not automatic … aggregates
  with a subtraction that can cancel."
- **The true wall.** Submultiplicativity alone provably gives NO positive rate (perfectly-additive
  counterexample v_m=βm ⇒ all defects 0; plus the uncomputable Fekete modulus). So M16-R needs external
  content, and the *only* proposed bridge is the bootstrap — which is exactly the unproven step.
- **Refuting fact / first experiment (cheap, partly runnable NOW).**
  (i) Compute d₁…d₈ and the pairwise D_{p,q} directly from the EXISTING exact c₁…c₉ (M09/M16 fixtures).
  If any defect trends toward 0, M16-R's premise dies cleanly (a real negative). The card's n≤5 data
  (defects flat in [1.6, 2.3]) already hints "no" — extending to n=9 is a one-script confirmation.
  (ii) The decisive adversarial move: **search for a toy subadditive sequence with d_n ≥ δ > 0 for all n
  yet M_n → 0** (gap decaying faster than 1/n). If one exists, the stated reduction "bounded atomic defect
  ⇒ 1/n rate" is REFUTED, and the residue sharpens to "which aggregate, not the atomic defect, controls
  M_n." This is a small finite search over subadditive sequences — fully fleet-tractable.
- **Stress-test of the probabilistic lens here:** its instinct (model c_n by a random Syracuse walk and
  predict the defect) FAILS — the random model is known to diverge from the deterministic map precisely on
  the exceptional/backward-tree structure (Kontorovich–Lagarias), which is where the defect lives. A
  random-model estimate can never *prove* M_n ≥ c; only the exact convolution can. This is why the exact
  c_n matter and simultaneously why no heuristic closes M16-R.

## 3. Matmul ω — STPP-density go/no-go over Z/N  (C07)  — would-matter MEDIUM · tractability MEDIUM

- **Load-bearing assumption.** The one group-theoretic lane the published cap-set/slice-rank barriers do
  NOT cover (BCCGNSU, verbatim) is unbounded-exponent abelian Z/N. The live hope: a *denser* STPP family
  over growing Z/N packs large independent products and pushes ω down.
- **The true wall (already half-exposed by Sol).** The abelian character bound is intrinsically weak — all
  degrees 1 ⇒ ∑_i n_i^ω ≤ |G|. The known CKSU template gives 2(m−1)^ω ≤ m³, whose exponent → **3, not 2**,
  as m→∞ (Sol verified the Z/16 instance: beats abelian single-TPP, but weaker than Strassen, ω≤2.8155).
  The near-linear (N^{1−o(1)}) tricolored-sum-free sets that make the slice-rank barrier *silent* are
  exactly the sets whose elements are *spread thin* — many tiny blocks, the opposite of what ω→2 needs.
- **Refuting fact / first experiment.** (a) Citation sweep: do BCCGNSU (later §§), ITCS-2023
  (arXiv:2204.03826) or ITCS-2025 (arXiv:2410.14905) already state a CU/STPP lower bound for
  unbounded-exponent abelian groups? A clean yes = no-go, lane closed. (b) If not: take the best KSS/Behrend
  tricolored-sum-free construction in Z/N for small N, attempt to realize it as an STPP family, and measure
  the induced block sizes n_i and the resulting ω from ∑ n_i^ω ≤ N. If blocks stay small (ω→3) for every
  accessible N, the lane is effectively dead — a well-characterized wall. If any family drives ω below the
  CW value 2.3714, that is a genuine lead. The hard, non-closed half is "turn a sum-free set into an STPP
  family with controlled block size" — the real risk, honestly flagged.
- **Stress-test of the algebraic-structural lens here:** its instinct (reach for representation theory /
  character degrees) FAILS on abelian groups precisely because all degrees are 1 — the algebra is trivial
  and the entire content sits in the *additive combinatorics* of the block packing (additive energy /
  STPP-capacity in Z/N). Better-posed sub-question the failure exposes: an additive-energy upper bound on
  STPP blocks in Z/N, which would directly give the no-go.

---

## 4. Goldbach / Twin Prime — the PARITY barrier reclassifies all computational residue  (M07, M08)  — would-matter LOW-MED · tractability HIGH

- **Load-bearing assumption.** That a *computational* sub-result (record extension, OEIS keyword:more term
  such as A352283 a(17)=924, A007508/A045917 reproductions) can be would-matter for these conjectures.
- **The true wall.** Both conjectures share ONE proven obstruction — the **Selberg parity barrier**: sieve
  methods cannot distinguish integers with an even vs odd number of prime factors, so they cannot isolate
  primes-times-prime from primes. Bounded gaps reached 246 (Zhang/Maynard/Polymath) but reaching 2, and
  Goldbach itself, both require *breaking parity*, which no computation touches. The empirical frontiers
  (4·10¹⁸, 10¹⁹) are HPC-only. ⇒ Every fleet-reachable computation is would-matter=✗ **by construction**.
- **Refuting fact / residue.** The angle is already correctly self-refuted (NT_SCOPE: reproduction-grade,
  not extension). The generative residue is to state the wall precisely and ask the ONE parity-respecting
  question: which Goldbach/twin-adjacent statements have *already* broken parity (Friedlander–Iwaniec-style
  bilinear-form results for primes of special form) and whether any has a computable sub-instance. Likely
  none fleet-sized — so the honest output is the reclassification itself: M07/M08 are CLOSED-at-reproduction,
  and no computational residue can matter until a parity-breaking bilinear structure is in hand.
- **Stress-test of the probabilistic lens here:** the Cramér/Hardy–Littlewood random model *predicts* both
  conjectures and even the correct constants — and is exactly why it cannot *prove* them: the heuristic is
  blind to the parity-obstructed cases. Its confident prediction is the tell that the barrier is elsewhere.

## 5. Baryogenesis — there is NO model-independent eEDM floor  (P05)  — would-matter LOW-MED · tractability MEDIUM

- **Load-bearing assumption.** The "triple-lock" angle wants a single quotable number — "the eEDM reach
  that kills un-tuned minimal EWBG."
- **The true wall.** (a) The target is one scalar (η); one number can't discriminate many-parameter models.
  (b) Asymmetric falsifiability: EWBG is testable and being excluded (Sol: BP-SG C2HDM slice predicts
  |d_e|>4.0×10⁻²⁹, already crossed by JILA 4.1×10⁻³⁰), while high-scale leptogenesis makes NO lab
  prediction — so excluding EWBG never *confirms* leptogenesis. (c) Cancellation mechanisms (tuned EDM
  cancellations, extra/secluded/transient CP phases, suppressed light-fermion couplings) mean **every eEDM
  threshold is benchmark-specific** — the sought model-independent floor provably does not exist.
- **Refuting fact / residue.** The "one number" is refuted by (c). The tractable residue is to replace the
  floor with a **survival-cost catalog**: per named benchmark (real-singlet, C2HDM/BP-SG, 2HDM), the amount
  of phase alignment/cancellation (in dB of tuning) required to evade the *current* 4.1×10⁻³⁰ bound, and the
  next-gen reach (ThF⁺ ~10⁻³¹) at which even the tuned island vanishes. Well-posed but literature-heavy;
  would-matter is "rank the live families," not "solve baryogenesis."
- **Stress-test of the cross-domain lens here:** importing a joint-likelihood / model-selection framework
  FAILS because model selection needs *both* candidates to predict; leptogenesis predicts nothing testable.
  The failure re-poses the honest inference as "origin pushed to an untestable scale," not "leptogenesis
  favored" — a cleaner, defensible statement.

---

### One-line ranking
1. **Collatz β→γ threshold** (M09/M16) — derive g(β), solve g(β*)=0.84, classify wall (numerical vs tautological vs direction-refuted). Analysis-only.
2. **Collatz rate bootstrap** (M16) — compute d₁…d₈ from existing c_n; search for a toy subadditive counterexample (d_n≥δ yet M_n→0) that refutes the atomic⇒mean reduction. Cheap.
3. **Matmul STPP-density go/no-go** (C07) — citation sweep, else KSS-sum-free→STPP-block-size→induced-ω over growing Z/N. Well-characterized wall either way.
</content>
</invoke>
