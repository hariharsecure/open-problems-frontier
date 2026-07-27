# Open Problems Frontier

**Exact new terms for open combinatorial counting sequences — every number confirmed by two independently written programs that agree digit-for-digit, or it doesn't ship.**

> **New here? Not a mathematician?** Start with **[EXPLAINED.md](EXPLAINED.md)** — plain-English notes on every kind of problem here, in one read.

An autonomous research fleet pointed at open **counting problems** ("how many ways can you do X on a shape of size *n*?") on structured graph families. The hard rule: a result is published only when **two independently authored engines — different algorithms, no shared code — produce the exact same integer** and both reproduce every previously published term of the sequence. This repository is the verifiable output.

---

## The ledger (honest)

| Count | What it is |
|---:|:---|
| **137** | new terms, **computed and dual-verified** (exact integers) |
| **41** | OEIS sequences extended — **25** carry the OEIS `more` flag ("wants more terms"), 16 are `nonn` |
| **0** | famous conjectures solved |

That last row is not a failure we're hiding — it's the honest scope. This work produces **correct new data**, not new theory, and it solves no famous open problem. When the fleet hit a wall on a popular target (a Collatz-adjacent bound), it **proved the route was capped** and retired the effort rather than dressing up a dead end. See [`findings/`](findings/).

Three distinctions run through everything here, and we keep them separate:

- **Computed & verified** — the 137 exact new terms, double-checked two independent ways. (Most of this work.)
- **Proved / shown** — a handful of logical results in [`findings/`](findings/) (e.g. why a lane is capped).
- **Solved a famous problem** — **none.** Never claimed.

---

## Quick start (30 seconds)

Every sequence ships with a self-contained program (stdlib Python, exact big-integer arithmetic, no dependencies) that reproduces the full published prefix and then computes the new term(s).

```bash
git clone https://github.com/hariharsecure/open-problems-frontier.git
cd open-problems-frontier

# Pick any program in programs/ and run it:
python3 programs/a374718.py.txt
```

You'll see each term printed with an `[OK]` as the program reproduces the known prefix and then the new terms:

```
a(1) = 3   [OK]
a(2) = 11   [OK]
...
a(8) = 39500622898119972708775991791836711708086527977446...   [OK]
total 0.018s  peakRSS=10MB
```

The `[OK]` lines through `a(8)` are the program re-deriving the sequence's already-published terms from scratch — the correctness check. Terms beyond the last published one are the new, dual-verified contributions. Run any other file in [`programs/`](programs/) the same way.

---

## Repository structure

| Path | What's in it |
|:---|:---|
| [`sequences/`](sequences/) | One package per sequence: the exact new b-file lines, the method, and the program reference. Start at [`sequences/INDEX.md`](sequences/INDEX.md) for the full list and current counts. |
| [`programs/`](programs/) | Self-contained, runnable programs (stdlib Python, exact arithmetic) — one per sequence. Each reproduces the published prefix, then the new terms. |
| [`findings/`](findings/) | The honest negative results and frontier triage — why certain famous lanes are capped, with the threshold computed. Includes the Collatz β→γ tautology analysis and the parity-barrier triage. |
| [`NOTES.md`](NOTES.md) | The reproducible methods and the negative results in technical depth. |
| [`EXPLAINED.md`](EXPLAINED.md) | Plain-English walkthrough of every problem type — no math background needed. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add or check a sequence. |

The families covered: square / torus / king grids, triangular grids, the Sierpinski gasket and tetrahedron, Tower-of-Hanoi graphs, Apollonian networks, Johnson graphs, and Fibonacci / Lucas cubes. The counts: matchings (all / maximal / maximum), dominating sets (plain / total / connected / minimum-total), independent sets, edge covers, spanning trees, and domino / dimer tilings.

---

## How verification works

Every published term clears a fixed gate:

1. **Two independently authored engines** — written from the problem definition by different models, without reading each other's code, and preferably using structurally different algorithms — must agree on the new term **digit-for-digit**.
2. **Both must reproduce the sequence's full published prefix** exactly, pinning both engines to the original author's definition.
3. Where feasible, a **third independent check** (brute-force enumeration on small cases) anchors the *semantics* — confirming both engines count the object the definition actually names.

Exact integer / rational arithmetic throughout — **no floating point touches any count**. A term that only one engine produced is **not** included: several such terms were withheld until a second engine could confirm them, and one was deferred with a characterized obstruction rather than shipped. Dual-lineage agreement is strong evidence, not a formal proof of program correctness; each package states exactly what its certification rests on.

---

## What this is **not**

- **Not a solution to Collatz, Riemann, Goldbach, or any famous open problem.** It solved none, and does not advance any of them. The Collatz-adjacent work *bounds a constant of Tao's* and then proves the numerical route onward is capped — that is a triage result, not conjecture progress.
- **Not new mathematical theory.** These are correct new *data points* — exact terms of well-defined sequences — plus a few small structural facts in the findings.
- **Not accepted into the OEIS.** Every term here is an independently dual-verified **candidate** b-file extension. OEIS submission is a separate, human-authored, editor-reviewed process, and nothing in this repository has been through it.

---

## Credit & license

This work **extends** sequences authored by others and catalogued by the [On-Line Encyclopedia of Integer Sequences (OEIS)](https://oeis.org). Full credit to the OEIS and to the original sequence authors — the candidate extensions here build on theirs.

- **Code:** MIT License
- **Data & text:** CC BY 4.0

See [LICENSE](LICENSE). Copyright © 2026 Harihar Thapa.
