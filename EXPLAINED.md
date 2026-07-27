# Explained for everyone

Plain-English notes on what this project actually did — no math background needed. Two honest
distinctions run through it:

- **Computed & verified** = we found exact new numbers and double-checked them two independent ways. (Most of this work.)
- **Proved / shown** = we made a logical argument that *must* be true. (A few of the "findings.")
- **Solved a famous problem** = none. We were honest about that from the start.

---

## The setup, in one paragraph

We pointed an automated research team at hard *counting* problems — questions of the form "how many
ways can you do X on a shape of size n?" Two independently-written programs had to arrive at the **exact
same answer**, digit for digit, or we threw the answer out. The result: **130 new verified numbers
across 40 different sequences**, all published here. No famous conjecture was solved; that was never
realistically on the table, and we say so plainly.

---

## The kinds of problems we extended (and what cracked each)

Think of a **graph** as dots joined by lines. Most of these problems ask "how many ways?" for shapes
that grow — a 5×5 grid, then 6×6, then 7×7 — where the answer explodes into enormous numbers and nobody
had computed the next one.

**Matchings — "pair up the dots."**
Pick some lines so that no dot is used twice (like seating people in pairs where pairs must be friends).
*How many ways?* We counted this for bigger grids, tori (grids wrapped into a donut), and exotic shapes.
**What helped:** process the shape one column at a time and only remember what's happening at the seam
between "done" and "not done" — so the memory stays small even as the shape grows.

**Maximal matchings — "pair up until you're stuck."**
Same, but the pairing has to be one where you *can't* add any more pairs. Slightly trickier bookkeeping;
same column-by-column idea.

**Dominating sets — "cover everything with guards."**
Place guards on some dots so every dot is either a guard or next to one. *How many valid arrangements?*
We pushed this on grids, tori, and two beautiful families called **Fibonacci and Lucas cubes**.
**What helped:** a smarter *ordering* of the dots (using an idea from network science called the Fiedler
vector) shrank the seam enough to make a previously-impossible count fit in memory.

**Spanning trees — "wire up the whole network, no loops."**
Connect every dot into a single network using the fewest lines and no cycles. *How many different such
networks?* **What helped:** a 170-year-old gem called the Matrix-Tree Theorem turns this into a single
(large but exact) arithmetic calculation — cheap and exact, so we extended many of these at once.

**Domino / dimer tilings — "cover the board with dominoes."**
How many ways to tile a board with 2×1 dominoes? **What helped:** a classic result (the FKT method)
turns domino-counting into a matrix determinant — again exact and fast for flat (planar) shapes.

**Independent sets, edge covers, and cousins** — "pick dots with no two connected," "pick lines so every
dot is touched." Same toolbox, different bookkeeping.

**The standout detective story (A071102).** One dimer sequence had *no description at all* in the
database — just numbers, no shape. Prior attempts gave up. Our scout tracked down the original 1999
research paper, opened the PDF, zoomed into the figure at high resolution, and **reconstructed the shape
pixel by pixel** (it turned out to be a diamond). Then it computed 17 new terms and checked them **four
independent ways**, including against a conjectured formula. That's the kind of persistence that finds
what broad searches miss.

---

## The one repeated trick worth understanding

**"Count groups, not individuals."** In one problem the naive method needed to track 3ⁿ possibilities
(astronomical). But many of the pieces were interchangeable — swapping them gave the same picture. So
instead of tracking each arrangement, we tracked *how many of each kind* — collapsing an impossible
3ⁿ count down to something an ordinary laptop finishes in a second. Recognizing hidden sameness is often
what turns "impossible" into "easy."

**And the safety rule:** every single number was produced by two programs written independently (often
one of ours and one by a different AI), using genuinely different methods. If they disagreed by even one
digit, nothing shipped. Several times this caught real bugs before they became wrong "answers."

---

## What we actually *proved* (the honest findings)

These are the logical results — arguments, not just computations.

**The Collatz "3n+1" problem — why we stopped.**
Collatz is the famous puzzle: take a number; if even, halve it; if odd, triple it and add one; repeat.
It *seems* to always reach 1, but no one can prove it. A modern line of attack tries to tighten a
technical quantity (call it β) as a stepping stone. We computed record-tight values of β — **and then
asked the question that mattered: does tightening β actually get you closer to solving Collatz?** We
worked out the exact relationship and **proved it's essentially a dead end**: to make real progress you'd
have to tighten β to a point that is *basically solving the whole conjecture anyway*. So we honestly
**retired** that effort instead of grinding on it. Knowing *why* a road is blocked is a real result.

**Goldbach & twin primes — a known wall.**
These famous prime-number conjectures sit behind something called the *parity barrier* — a well-understood
reason that pure computation *cannot* settle them, no matter how much you compute. We confirmed our
targets are behind that wall, so we didn't waste effort pretending otherwise.

**Matrix multiplication (a computer-science frontier).**
For one open approach, we computed an exact small-case result and **showed that one specific popular
construction cannot beat the known record** — a clean "no" that narrows where the real answer could be.

---

## The honest bottom line

- **Famous problems solved:** 0.
- **What we produced:** 130 new, exact, independently-verified numbers extending 40 real mathematical
  sequences — correct new *data* that other people can use and check.
- **What we mapped:** *which* famous problems are out of reach for this kind of tool, and the precise
  reason each one is capped.
- **The rarest part:** the team was built to *stop* when it hit a wall and say so, rather than dress up a
  dead end as progress. In research, knowing when to quit is underrated — and it's the thing we're
  proudest of.
