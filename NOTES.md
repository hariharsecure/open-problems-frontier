# Notes on Methods and Negative Results

*Technical notes accompanying the sequence extensions in this repository. Everything below is
either computed and dual-verified here, or explicitly labeled as a negative/partial result.
No conjecture is claimed solved.*

---

## 1. What this is, and why

This repository is the output of an autonomous research fleet pointed at exact **counting
problems on structured graph families** — the kind of sequences the OEIS marks with keyword
`more` ("wants more terms"). The deliverable is deliberately narrow: **73 new terms across 28
sequences** (42 terms on 19 `more`-flagged sequences, 31 on 9 others), each an exact integer,
each produced by **two independently-written implementations that agree digit-for-digit** and
both reproduce every previously published term.

Why this target? Because it is one of the few places where machine effort converts directly
into verifiable mathematical data: a new term of "maximal matchings in the n×n grid" is not a
theorem, but it is checkable, permanent, and useful downstream (growth-constant estimation,
conjecture testing, formula discovery). The families covered: square/torus/king grids,
triangular grids, the Sierpinski gasket and tetrahedron, Tower-of-Hanoi graphs, Apollonian
networks, Johnson graphs, Fibonacci and Lucas cubes; the counts: matchings (all / maximal /
maximum), dominating sets (plain / total / connected / minimum-total), independent sets, edge
covers, domino tilings.

Equally deliberate: the fleet also spent effort **triaging what is *not* reachable**, and we
publish that triage (§4, and [`findings/`](findings/)). Knowing precisely why a lane is capped
— with the threshold computed — is a result, and it is the part most likely to save someone
else's compute.

## 2. The methods that made infeasible counts feasible

The new terms were not obtained by bigger hardware: everything ran on one desktop machine, in
pure Python with exact big-integer arithmetic (no floating point touches any count). What
moved the frontier was five reformulations, stated here with enough detail to reproduce the
idea; complete specifications are in [`programs/`](programs/).

### 2.1 Boundary / transfer column DP with exact big integers

The workhorse for grid-like families (A287595, A297486, A297489, A321250, A288027, …). To
count, e.g., **maximal matchings in the n×n grid** (A287595), sweep column by column and keep,
per row of the current boundary, one of three states: *matched* (no obligation crosses the
cut), *outgoing horizontal edge*, or *pending* — unmatched, hence its right neighbor **must**
end up matched, since a maximal matching is exactly one whose unmatched vertices form an
independent set. Maximality, a global condition, becomes a local 3-letter constraint on the
cut.

Two engineering facts made n=13 (frontier of ~509,000 states) cheap: (i) pack states at 2
bits/row and build the transfer **once** as a compact CSR operator (every transition has
multiplicity 1, so no value array is needed), then apply it n−1 times; (ii) the first draft,
a dict-of-dicts transition cache, hit ~5.8 GB at n=12 and was killed — the fix dropped the
n=12 peak from 2570 MB to 181 MB. The certified new term:

> A287595 a(13) = 2280413203760054215839279592187056 (643 MB, 443 s; independent engine: 293 MB, 39 s).

A sanity signal we used throughout: log₁₀ a(n)/n² is stable across the old and new terms
(0.196, 0.197, 0.198 at n = 12, 13, 14) — a cheap independent plausibility check on any new
term of a λ^{n²} family.

### 2.2 Orbit/multiset collapse: exchangeable boundary → polynomial algorithm

For A321248 (maximal independent sets in the n×n stacked book graph) the naive boundary is a
full assignment of a 3-valued state to each of n leaf pages — a 3ⁿ frontier, hopeless past
n ≈ 20. The key observation: the leaves are **exchangeable** — the count depends only on *how
many* leaves are in each state (in-set / dominated / pending), not which. Collapsing the
frontier to the multiset (i_IN, i_DOM, i_PEND) with binomial transition multiplicities turns
3ⁿ states into O(n²) and the whole computation into **O(n⁴)**.

The collapse was validated, not assumed: an explicit no-symmetry engine (state = full n-tuple)
reproduces a(1..7) exactly, and brute force over all 2^|V| subsets confirms a(1..4). Result:
**ten** new dual-certified terms, a(16)–a(25), in 0.024 s at 10 MB — and the method scales to
a(60) (a 439-digit number) in about a second. Whenever a family has an exchangeable boundary,
this single observation converts an exponential frontier into a polynomial one.

### 2.3 Value-only reformulation: a ~125 GB wall dissolved to ~55 MB

In the Collatz-adjacent computation of the exact Syracuse minimum masses c_n (Tao's
3-adic mixing constants; see §4.1), the natural forward DP tracks the **joint** state
(exponent-residue r mod L, value V mod 3ⁿ) with L = 2·3ⁿ⁻¹. At n = 8 that is 4374 rows of
bit-packed 3ⁿ-slot vectors, ≈ **125 GB** — over the machine's RAM. A genuine wall, *for that
algorithm*.

The reformulation: the step exponents a_i are i.i.d., hence exchangeable, so reversing them
preserves the law; a Horner nesting from the outer end yields a **value-only** recursion

  W₀ = 0, W_m = 2^{−a_m}(3·W_{m−1} + 1) (mod 3ⁿ), W_n =_d Syracuse variable,

whose state is just one exact path-count per residue — 6561 big-int slots at n = 8. A
telescoping recurrence along the ×2 orbit (2 is a primitive root mod 3ᵏ, so one orbit per
3-adic shell) makes each step O(mod). c₈ took **0.18 s at ~55 MB**, versus the 125 GB
projection — and matched the prior independent computation on the reduced fraction (1312-digit
numerator), the raw min-numerator (10,529 digits), and the argmin residue, exactly. This gave
the dual-verified bound β ≤ 1.47956465.

Two honest notes. The 3V+1 map is many-to-one mod 3ⁿ, so mass must be *accumulated*, not
relabeled — the one real bug in the first draft, caught instantly by the layer-total invariant
Σ_b N = Dᵐ. And the wall was real but **algorithm-specific**: before buying RAM, ask whether
the quantity you need is a marginal of the state you are storing.

### 2.4 Fiedler-vector vertex ordering to cut frontier width

A frontier DP on an arbitrary graph costs ~3^w where w is the frontier width induced by the
vertex elimination order. On Fibonacci/Lucas cubes the standard bandwidth-reducing order
(Cuthill–McKee) gave widths Λ₉ = 23 and Γ₈ = 17 — the Λ₉ run walled above 37 GB. Ordering
vertices by their component in the **Fiedler vector** (the eigenvector of the second-smallest
Laplacian eigenvalue — the relaxation of the minimum-cut-sequence problem) cut the widths to
**19 and 14** respectively. That factor of 3⁴–3³ in state count is the entire difference
between "wall" and "seconds":

- A365580 (dominating sets, Lucas cube) a(9) = 21920816534420071589103 — 346 s, 2.95 GB;
- A298115 (connected dominating sets, Fibonacci cube) a(8) = 3708334309546496 — 82 s, 0.35 GB.

Both had previously been computed only by the *other* lineage; the Fiedler ordering is what
allowed an independent confirmation and hence certification. As a robustness check, the first new
cube term was verified **order-invariant**: identical value under Cuthill–McKee, reverse-CM,
and random-restart orderings with distinct peak-state trajectories.

The general point: for these DPs the vertex order *is* the algorithm, and a spectral ordering
is a one-line change worth trying before declaring a width wall.

### 2.5 Self-similar renormalization over a bounded corner state

Fractal-like families (Sierpinski gasket SG_n, Sierpinski tetrahedron ST_n, Hanoi graph H_n,
Apollonian networks) double their vertex count per level, so any frontier sweep dies — but
they are built by gluing k copies of level n−1 at a **bounded set of corners**. If the count
admits a per-corner state of bounded alphabet, the whole level-n object is summarized by a
tensor with 3 or 4 indices, and one level costs a constant number of tensor contractions,
independent of |V|.

For maximal matchings on SG_n (A374718) the corner alphabet is {M, S, F}: matched inside this
copy; unmatched but locally saturated (may legitimately stay exposed); unmatched with an
unmatched in-copy neighbor (must be matched by the partner copy, else an addable edge
exists). Gluing resolves maximality locally, exactly. The engine computes a(1)–a(10) —
a(10) has 6287 digits — in **0.32 s at ~10 MB**. The same pattern with 4 corners and
vertex-identification gluing gives the Sierpinski tetrahedron results (e.g. A323516
a(4) = 3386054321784720, where the state carries a generating polynomial to extract the
*minimum*-size count); with 3 bridge-edge gluings it gives the Hanoi results (A286017,
A297480, A347505, A321249). The only growth left is the big-integer size of the answer.

The honest boundary of the method: it needs a *bounded* interface. The same triage correctly
ruled out Sierpinski **carpets** and Menger sponges (interface grows with n) — those stay
hard, and we did not attempt to claim them.

## 3. The dual-lineage discipline

Every published term satisfies a fixed gate: **two independently-authored engines** — written
by different models, from the problem definition, without reading each other's code, and
preferably by structurally different algorithms — must (i) reproduce the full published prefix
of the sequence exactly, and (ii) agree digit-for-digit on the new term. Where feasible a
third check (explicit brute-force enumeration on small cases) anchors the *semantics* — that
both engines count the same object the definition names.

Examples of how different the lineages actually are:

- **A287595:** column transfer with (matched/H/pending) row states and CSR application
  (509k states) ⟂ cell-by-cell broken-profile monomer–dimer scan with a carry bit (763k
  states). Same integer.
- **A374718:** renormalization from an SG₂ base with corner alphabet {M,S,F} ⟂ transfer from
  the SG₁ triangle base with per-corner alphabet {unmatched, matched-inside,
  matched-outside} — different base case, different state semantics, different closing test.
- **A323516:** a 4-corner generating-polynomial renormalization ⟂ an independently derived
  transfer *plus* a C++ brute force that examined all 25,211,936 subsets of the 34-vertex
  ST₃ to confirm the gate value 2430 by definition.
- **Fibonacci/Lucas cube dominating sets:** a 3^width frontier DP ⟂ a monotone-CNF model
  counter (Shannon expansion + clause subsumption + component factorization) — not even the
  same algorithmic family.

The discipline has teeth, and the withheld results prove it:

- A287595 **a(14)** was computed by one lineage (with an internal cross-check) but the second
  engine exceeded its memory budget — so a(14) is **not** in this repository.
- Two Fibonacci/Lucas terms spent a session as "single-lineage, not certified" and were
  published only after the Fiedler ordering (§2.4) let the second engine finish.
- A291573 (minimal dominating sets in Fibonacci cubes) is **deferred with a characterized
  obstruction**, not claimed: a per-vertex frontier code provably cannot express the
  existential private-neighbor witness (the natural DP undercounts — 12 vs the true 14
  already on Γ₄ — because a witness can be finalized after its vertex leaves the frontier);
  a correct count needs covering-code/subset-convolution machinery.

Agreement between two engines is not proof — a shared misreading of the definition would pass
it. That is what the prefix gate and the brute-force anchors are for: the prefix pins the
definition to the original author's, and the brute force pins both engines to the definition.
Each term's package states exactly what its independence rests on.

## 4. Negative results, stated as results

### 4.1 The Collatz β→γ transmission is morally tautological

Tao (2019/2020) defines c_n = inf_{3∤b} P(Syrac(ℤ/3ⁿℤ) = b) = 3^{−βn+o(n)}, proves
submultiplicativity (so any computed c_n gives a rigorous **upper bound** on β), and notes
that a good enough bound on β would improve the Krasikov–Lagarias Collatz preimage-density
exponent γ = 0.84 — "in principle achievable numerically." Our fleet computed the exact c_n
ladder (dual-verified through c₈, hence β ≤ 1.4796), and then asked the question that gates
the whole program: **how small must β be for the transmission to beat 0.84?**

Tao states that γ < f(β) with f explicitly computable and f(β) → 1 as β → 1, but gives no
closed form. We derived one from his preimage-counting mechanism — a large-deviation count of
backward Syracuse paths (geometric steps, binary entropy h):

  f(β) = max_{u>0} [ −β·c·u + (1 + u·c)·h(u/(1 + u·c)) ], c = log₂3,

calibrated against the single hard anchor Tao proves: f(1) = 1 (it reproduces it exactly).
Solving f(β\*) = 0.84 gives **β\* ≈ 1.0545**. The exact-DP compute wall is n ≈ 9–10, where
β ≈ 1.43 — which transmits to γ ≈ 0.41, *below even the trivial preimage-tree bound ≈ 0.81*.
Reaching β ≤ 1.0545 requires n ≈ 126, where the DP support is ~10⁶⁰ states. So the numerical
route to beating 0.84 requires certifying that Syracuse mixing is within ~5.5% of perfect —
which is essentially the hard conjecture (β = 1) itself. **The lane is not logically blocked
(the direction of transmission is fine); it is tautologically capped**, and we retired it —
including compute that was already running. The exact c_n values and the β ≤ 1.4796 bound
stand on their own as verified data. Full derivation: [`findings/collatz_beta_gamma_tautological.md`](findings/collatz_beta_gamma_tautological.md).

### 4.2 The transfer-operator spectral hope: refuted in one run

A multi-lens analysis converged on a promising idea: β should be a spectral quantity of the
Syracuse transfer operator 𝓛 on ℤ/3ⁿℤ, with the subdominant eigenvalue converging to β
geometrically rather than the DP's ~1/n crawl. We built 𝓛 exactly; it reproduces c₁, c₂, c₃
to 60 decimal places — the reformulation is *correct*. And the hypothesis is *provably empty*:
every nonzero entry of 𝓛 raises the 3-adic valuation by exactly one, so 𝓛 is
nilpotent-plus-rank-1 and its spectrum is exactly {1} ∪ {0, …, 0}. λ₂ = 0 identically; there
is no gap to read. β lives in the **cocycle norm** (a Lyapunov/large-deviation quantity) of
the valuation-shell blocks — which is precisely what the DP already computes, at the same
cost. A converged, well-motivated lead, tested honestly, killed cleanly — and the structural
fact that killed it (exact n-step nilpotent mixing) is itself a small permanent takeaway that
redirects any future attempt away from eigenvalue methods.

### 4.3 Parity-barrier triage of Goldbach / twin primes

An adversarial review reclassified our Goldbach and twin-prime lanes: both sit behind the
**Selberg parity barrier** — sieve-theoretic methods (and any computation feeding them)
cannot distinguish integers with an odd versus even number of prime factors, and every
computation the fleet could run feeds exactly such methods. This makes the lanes
"would-matter = no *by construction*": no empirical frontier extension can contribute until a
parity-breaking bilinear structure (Friedlander–Iwaniec-style) is in hand, which is a theory
problem, not a compute problem. The honest residue is precise wall statements, plus small
genuinely-exact side results (e.g. certified singular-series constants) that we do not dress
up as conjecture progress. See [`findings/adversarial_walls.md`](findings/adversarial_walls.md).

The common frame for all three: **a lane closed with its threshold computed is worth more
than a lane kept optimistically open.** β\* ≈ 1.055, λ₂ ≡ 0, and "parity-obstructed by
construction" are each checkable claims a future researcher can either rely on or attack.

## 5. Limitations, and what this is not

- **Data, not theory.** These are exact new terms of well-defined sequences and characterized
  walls — no new theorems beyond the small structural facts noted above, and none claimed.
- **No famous problem is touched.** The Collatz-adjacent work *bounds a constant of Tao's*
  (β ≤ 1.4796) and proves the numerical route onward is capped. It does not advance the
  Collatz conjecture, and we say so.
- **Candidate, not accepted, OEIS extensions.** Every term here is an independently
  dual-verified *candidate* b-file extension. OEIS submission is a separate, human-authored,
  editor-reviewed process; nothing in this repository has been through it. Full credit to the
  OEIS and the original sequence authors — this work extends theirs.
- **Verification is bounded.** Dual-lineage exact agreement plus prefix reproduction plus
  brute-force anchors is strong evidence, not a formal proof of program correctness; the
  per-sequence packages state what each certification rests on, including where independence
  is partial.
- **Scope.** The "walls" reported (e.g. Fibonacci cube Γ₉ at frontier width 26) are walls for
  *these methods on commodity hardware under explicit budgets*, honestly measured — not
  impossibility claims.

*Programs for every sequence are in [`programs/`](programs/) (stdlib Python, exact
arithmetic, self-contained: each reproduces the published prefix, then the new terms). The
per-sequence method notes are in [`sequences/`](sequences/); the negative results in
[`findings/`](findings/).*
