# Dominating sets — "cover everything with guards"

## What is this counting?

Picture a museum laid out as dots joined by lines. You place **guards** on some of the dots. The rule:
every dot must either *have* a guard or be *next to* one — nothing is left unwatched. A valid guard
placement is a **dominating set**. The question: *how many valid placements are there?*

The variations tighten the rule:

- **Total dominating** — even a guard needs a guard *next door*. (No guard watches only their own spot;
  everyone, guards included, must be covered by someone else.)
- **Connected dominating** — the guards must also form one connected group, able to reach each other.
- **Minimum total dominating** — among the *smallest* total-dominating placements, how many are there?

The shapes: the Tower-of-Hanoi puzzle graph, the Sierpinski tetrahedron, and two elegant families built
from binary strings — the **Fibonacci cubes** and **Lucas cubes** (the strings with no two 1s in a row).

## Which sequences fall here (7 sequences, 10 new terms)

| A-number | In plain words |
|---|---|
| A291920 | dominating sets in the Fibonacci cube |
| A298115 | connected dominating sets in the Fibonacci cube |
| A323516 | minimum total dominating sets in the Sierpinski tetrahedron |
| A347505 | dominating sets in the Tower-of-Hanoi graph |
| A365572 | total dominating sets in the Lucas cube |
| A365580 | dominating sets in the Lucas cube |
| A370573 | connected dominating sets in the Lucas cube |

## The trick that made extending them possible

**Walk through the dots in a smarter order.** These counts also use the "only remember the seam" idea —
process the graph a piece at a time, tracking just the boundary. But for the Fibonacci and Lucas cubes,
the seam was too wide no matter how you sliced it, and the computation ran out of memory.

The fix came from an idea borrowed from network science: the **Fiedler vector**. Think of it as asking
the graph, "if I had to cut you into two balanced halves with as few lines crossing as possible, where's
the natural fault line?" Ordering the dots along that fault line makes the seam as narrow as it can be at
every step. On one cube that single change shrank the boundary enough to take a count from
"won't-fit-in-memory" down to running in a few minutes — and, crucially, let a *second, independent*
program finish too, so the answer could be verified.

The order in which you visit the dots really is the whole ballgame here, and picking the right order is a
one-line change worth trying before declaring something impossible.

*All terms here are computed-and-verified candidate extensions — two independent programs agreed exactly.
No famous problem is involved.*
