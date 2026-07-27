# Open Problems Frontier

An autonomous AI research fleet pointed at open **counting problems** — with a hard rule: a result
ships only when **two independently-written implementations (Codex ⟂ Claude) agree on it exactly** and
both reproduce every previously-published term. This repo is the verifiable output.

> **New here / not a mathematician?** Start with [EXPLAINED.md](EXPLAINED.md) — plain-English notes on every kind of problem, in one read.

## The ledger (honest)

| | |
|---:|:---|
| **73** | new terms, **dual-verified** |
| **28** | integer sequences extended (**19** flagged by the OEIS as wanting more terms) |
| **0** | famous conjectures solved |

That last row is not a failure to hide — it's the point. When the fleet analyzed a popular target (an
upper bound on the Collatz/Syracuse constant β), it **proved the improvement was mathematically
tautological** (you'd need β ≤ 1.055, ≈ the conjecture itself) and **retired the effort** rather than
grinding on it. See [`findings/`](findings/).

## What this is

- **New, correct data.** Exact new terms for well-defined combinatorial counting sequences — maximal
  matchings, dominating sets, minimal edge covers, dimer/domino tilings — on structured graph families:
  grids, tori, king/knight graphs, the Sierpinski gasket & tetrahedron, Fibonacci/Lucas cubes, and the
  Tower-of-Hanoi graph. Each is a candidate b-file extension of an existing OEIS sequence.
- **Reproducible.** Every term ships with a self-contained program ([`programs/`](programs/)) that
  reproduces the full published prefix and computes the new term(s).
- **Honest about its limits.** It is incremental *data*, not new *theory*, and it solves no famous
  problem. The [`findings/`](findings/) document the dead ends it characterized and retired.

## What this is **not**

- Not a solution to Collatz, Riemann, or any famous open problem (it solved none).
- Not a claim of new mathematical *theory* — these are correct new *data points*.
- Not (yet) accepted into the OEIS. These are independently-verified **candidate** extensions; OEIS
  submission is a separate, human-authored, editor-reviewed process. Credit to the OEIS and to the
  original sequence authors — this work extends theirs.

## How the verification works

Two independently-authored engines, different algorithms, must produce the **exact same integer** and
both must reproduce the sequence's full published prefix; several terms are additionally checked against
brute-force enumeration on small cases and a third independent method. Exact integer/rational arithmetic
throughout — no floating point in any count. A term that only one engine produced is **not** included.

## Structure

- [`sequences/`](sequences/) — one package per sequence: the exact new b-file lines, the method, and the
  program reference. [`sequences/INDEX.md`](sequences/INDEX.md) lists all 28 (marked `more` = OEIS-flagged
  vs `nonn` = soft-want).
- [`programs/`](programs/) — self-contained, runnable programs (stdlib Python), one per sequence.
- [`findings/`](findings/) — the honest negative results and frontier triage (why certain famous lanes
  are capped), including the Collatz β→γ tautology analysis.

## Methods & findings write-up

See [NOTES.md](NOTES.md) — the reproducible methods and the honest negative results in depth.

## License

Code under MIT; data/text under CC BY 4.0. See [LICENSE](LICENSE).
