# `programs/` — the reproduction scripts

This directory holds the code that **reproduces every result in this repository**. There is one
program per sequence (a few cover a closely-related pair), each a small Python script that first
regenerates the sequence's already-published prefix as a self-check, then computes the **new
term(s)** this project contributes.

Nothing here claims to have *solved* a famous problem — none were. These programs produce
**computed-and-verified data**: exact new terms of well-defined counting sequences, each also
independently reproduced by a second engine (see the dual-lineage note below). "Reproduced by two
engines" and "reproduces the published prefix" is strong evidence, not a formal proof of program
correctness, and none of these terms has been submitted to or accepted by the OEIS — they are
**candidate** b-file extensions. See [`../NOTES.md`](../NOTES.md) and
[`../sequences/INDEX.md`](../sequences/INDEX.md) for the full ledger.

Per [`../sequences/INDEX.md`](../sequences/INDEX.md): **137 certified terms across 41 sequences**
(65 terms on 25 sequences the OEIS flags `keyword:more`; 72 terms on 16 flagged `nonn`).

---

## What one program *is*

Each `aNNNNNN.py.txt` is a standalone Python script (the `.txt` suffix just keeps it renderable in a
browser/on GitHub without executing). A typical file:

1. Encodes the graph family and the object being counted, directly from the sequence's definition.
2. Uses **exact integer / rational arithmetic only** — no floating point ever touches a count.
3. Has an `if __name__ == "__main__":` block that:
   - recomputes the sequence's published terms and checks each against a hard-coded `known`/`KNOWN`
     table (this is the **gate**), then
   - computes and prints the new extension term(s).

To run a program, drop the `.txt`:

```bash
cd programs
cp a288957.py.txt a288957.py     # or: python3 <(cat a288957.py.txt)
python3 a288957.py
```

Some scripts take an optional argument for how far to go, e.g. `python3 a374718.py 9` or a
brute-force cross-check mode `python3 a374718.py brute 3`. When in doubt, read the module docstring
at the top of the file — every program documents its own method, states, and run line.

## Reading the output — the `[OK]` gate

Programs print **one line per term**, comparing what they computed against the published value. Two
output conventions appear across the directory (they mean the same thing):

- Tag style (e.g. `a374718.py.txt`, `a378860.py.txt`):
  ```
  a(1) = 3            [OK]
  a(2) = ...          [OK]
  ...
  a(9) = <big number> [NEW]
  ```
- Boolean/label style (e.g. `a288957.py.txt`, `a340398_formula.py.txt`):
  ```
  n=1 match=True ...
  ...
  ALL 10 KNOWN TERMS REPRODUCED. Now computing a(11)...
  a(11) = <big number>
  ```

What the tags mean:

| marker | meaning |
|---|---|
| `[OK]` / `match=True` | this term equals the **already-published** OEIS value — the reproduction gate passed for it |
| `[NEW]` / `NEW a(n) =` | this is a **new** term this project computed (the actual contribution) |
| `[MISMATCH ...]` | a published term did **not** reproduce; the program aborts (`sys.exit(1)`) and nothing is trusted |

**The gate is pass/fail:** if any published prefix term mismatches, the run stops and the new term is
not to be believed. A clean run means every published term was reproduced *and* the new term was then
computed under the same code path. Several programs also print `peakRSS` / wall-time so you can see
the resource cost.

## Dependencies

- **Python 3.10+** is the tested baseline. No program uses `int.bit_count()` (the 3.10-only method),
  so 3.8/3.9 will very likely work too — but 3.10+ is what these were run under.
- **Standard library only** for the self-contained programs (16 of the 23 files). Modules used:
  `sys`, `time`, `resource`, `math` (`comb`, `factorial`, `isqrt`, `atan2`), `fractions.Fraction`,
  `itertools`, `collections`, `array`, `functools`. No third-party install needed for these.
- **Exceptions — please read before assuming a fresh checkout runs everything:**
  - `a143659.py.txt` optionally imports **`numpy`** and **`sympy`** for its FKT/Kasteleyn algebraic
    lineage (a multi-modular determinant); its second, independent column-transfer lineage in the same
    file is pure stdlib, so the sequence is still reproducible without those packages.
  - **Matrix-Tree programs** — `a288957`, `a212800`, `a193134_a193135`, `a193154_triangular`,
    `a340398_explicit` — do `from bareiss import bareiss_det` via an **absolute `sys.path.insert(...)`
    pointing at a `SCOUT_G` directory that is not included in this repo.** As written they will not run
    on a fresh clone. The missing helper is a single function: `bareiss_det(matrix) -> int`, a
    fraction-free (Bareiss) Gaussian-elimination integer determinant — a short, well-known routine you
    can supply. (For A340398, `a340398_formula.py.txt` is fully self-contained and needs no helper.)
  - **Frontier-DP cube programs** — `a365572`, `a370573` — do `from graphs import fib_cube,
    lucas_cube` and `from frontier import cuthill_mckee`; those two helper modules (graph builders +
    a Cuthill–McKee ordering) must be on `PYTHONPATH`. `a365580.py.txt` and `a291920` coverage is
    self-contained and needs no helper.

If you only want a guaranteed-standalone starting point, pick one of the 16 self-contained files
(e.g. `a287595`, `a374718`, `a321248`, `a365580`, `a340398_formula`).

## How to independently verify a term

1. **Trust the gate, then read past it.** Run the program. Confirm every published term prints `[OK]`
   / `match=True` (the program checks this for you and aborts on any mismatch). The `[NEW]` line(s)
   are the contributed value(s).
2. **Cross-check the prefix against the OEIS.** The `known`/`KNOWN` table hard-coded in each program
   is the published prefix; compare it to the sequence's b-file on oeis.org. If the prefix matches
   OEIS *and* the program reproduces it, the program is counting the right object.
3. **Cross-check the new term against this repo's package.** The certified value is recorded in
   [`../sequences/A NNNNNN.md`](../sequences/) for that sequence; it should match the `[NEW]` line
   exactly, digit for digit.
4. **Small cases: brute force.** Where a program ships a `brute` mode (e.g. `python3 a374718.py
   brute 3`), it enumerates the object directly on small graphs and tags each `[OK]`/`[NEW]` — an
   independent, definition-level check that the transfer/renormalization logic counts what the name
   says.
5. **Best of all: run a second, different program on the same object** if one exists, or reimplement
   from the definition — that is exactly the dual-lineage gate this project imposes on itself.

## The dual-lineage methodology (one paragraph)

Every published term had to be produced by **two independently-authored engines** — written by
different models straight from the problem definition, without reading each other's code, and
preferably by *structurally different algorithms* — that (i) both reproduce the sequence's full
published prefix and (ii) agree on the new term **digit for digit**; where feasible a third check
(explicit brute-force enumeration on small cases) anchors the *semantics* so both engines are pinned
to the same object. A term only one engine produced is **withheld** (e.g. A287595 `a(14)` was
computed by one lineage but the second exceeded its memory budget, so it is not in this repo). The
scripts in this directory are the primary lineage; the second lineage and any brute-force anchor for
each sequence are described in that sequence's package under [`../sequences/`](../sequences/).

## Example programs → sequence & method

| program | sequence(s) | object counted | method |
|---|---|---|---|
| `a288957.py.txt` | A288957 | spanning trees, n×n king graph | **Matrix-Tree** (Bareiss fraction-free determinant of a Laplacian minor)¹ |
| `a212800.py.txt` | A212800 | spanning trees, n×n torus grid | **Matrix-Tree** (Bareiss determinant)¹ |
| `a193134_a193135.py.txt` | A193134, A193135 | spanning trees, folded / halved cube graphs | **Matrix-Tree** (Bareiss determinant)¹ |
| `a193154_triangular.py.txt` | A193154 | spanning trees, triangular graphs | **Matrix-Tree** (Bareiss determinant)¹ |
| `a340398_formula.py.txt` | A340398 | spanning trees, Bruhat/transposition Cayley graph of S_n | **Cayley-graph eigenvalue product** (Kirchhoff via irrep eigenvalues + hook-length formula) — self-contained |
| `a143659.py.txt` | A143659, A270668 | domino (dimer) tilings, holey odd rectangle | **FKT / Kasteleyn** determinant ⟂ column-transfer domino DP² |
| `a071104.py.txt` | A071104 | perfect matchings, Aztec-rectangle variant | exact **column-transfer DP** over a bitmask boundary |
| `a287595.py.txt` | A287595 | maximal matchings, n×n grid | **transfer-DP** with a per-row 3-state (matched / horizontal / pending) boundary |
| `a321248.py.txt` | A321248 | maximal independent sets, n×n stacked book graph | **orbit / multiset-collapse** DP (exchangeable leaves → polynomial time) |
| `a374718.py.txt` | A374718 | maximal matchings, Sierpinski gasket SG_n | **self-similar renormalization** over a 3-corner {M,S,F} state |
| `a378860.py.txt` | A378860 | minimal edge covers, Sierpinski gasket | **renormalization** over a bounded corner state |
| `a365580.py.txt` | A365580, A291920 | dominating sets, Lucas / Fibonacci cubes | **frontier / boundary transfer DP** (Cuthill–McKee vertex order) — self-contained |
| `a297558.py.txt` | A297558, A292429 | maximum matchings, Apollonian network | **transfer** with a matching **generating polynomial** + brute anchor |

¹ needs the external `bareiss_det` helper — see Dependencies. &nbsp; ² the FKT lineage optionally uses
numpy/sympy; the transfer lineage is stdlib-only.

The full list of 23 programs is in this directory; the complete sequence-by-sequence method notes and
the second-lineage descriptions are in [`../sequences/`](../sequences/), and the plain-English tour
of every method is in [`../EXPLAINED.md`](../EXPLAINED.md).


**Helpers:** `bareiss.py`, `graphs.py`, `frontier.py` are bundled here; dependent programs import them directly, no PYTHONPATH needed.
