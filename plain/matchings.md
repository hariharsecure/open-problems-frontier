# Matchings — "pair up the neighbors"

## What is this counting?

Imagine a room full of people, with a line drawn between any two who are friends. A **matching** is a
way of pairing some of them off for a dance, with two rules: you can only pair friends, and nobody
dances twice. The question is always: *how many different valid pairings are there?*

Some flavors change the rules slightly:

- **Maximal matching** — pair people until you're *stuck*: no unpaired-but-could-be-paired couple is
  left standing. (You don't have to pair the most people; you just can't add another pair.)
- **Maximum matching** — the pairings that dance the *most* people possible. How many of those exist?
- **Perfect / dimer** — everybody is paired. Those live in the [domino-tilings](domino-tilings.md)
  note, because covering a board with dominoes *is* a perfect matching.

The shapes we counted on: plain grids, grids wrapped into a donut (a **torus**), chessboards where
kings move to any neighbor, triangular grids, the fractal "triforce" (Sierpinski gasket) and its 3-D
cousin the Sierpinski tetrahedron, the Tower-of-Hanoi puzzle graph, Apollonian networks, Johnson
graphs, and the Fibonacci and Lucas cubes.

## Which sequences fall here (14 sequences, 23 new terms)

| A-number | In plain words |
|---|---|
| A286017 | matchings in the Tower-of-Hanoi graph |
| A287595 | maximal matchings in the n×n grid |
| A291935 | matchings in the Fibonacci cube |
| A292017 | maximum matchings in the Fibonacci cube |
| A292669 | matchings in the Sierpinski tetrahedron |
| A297480 | maximal matchings in the Tower-of-Hanoi graph |
| A297484 | maximal matchings in the Johnson / triangular graph |
| A297485 | maximal matchings in the triangular grid |
| A297486 | maximal matchings in the torus (donut) grid |
| A297489 | maximal matchings on the king-move chessboard |
| A297533 | maximum matchings in the Sierpinski tetrahedron |
| A297558 | maximum matchings in an Apollonian network |
| A374718 | maximal matchings in the Sierpinski gasket (triforce) |
| A387566 | matchings in the Lucas cube |

## The trick that made extending them possible

**Only remember the seam.** Instead of looking at the whole shape at once, sweep it one column (or one
slice) at a time. At any moment you only need to know what's happening right at the boundary between
the "already handled" part and the "not yet" part — who's still waiting for a partner across the cut.
That boundary is small even when the shape is enormous, so the memory stays small too.

The clever bit for *maximal* matchings: "you can't add another pair" sounds like a rule about the whole
picture, but it turns into a tiny local rule at the seam — each spot at the boundary is just *matched*,
*reaching across*, or *unmatched-so-its-neighbor-must-be-matched*. A global condition becomes three
letters of bookkeeping.

For the fractal and puzzle shapes (Sierpinski, Hanoi, Apollonian) there's a sister trick: they're built
by gluing copies of the previous level together at a *handful of corners*, so you summarize each copy by
what happens at those few corners and glue the summaries. The shape doubles in size every level; the
bookkeeping doesn't grow at all.

*All terms here are computed-and-verified candidate extensions — two independent programs agreed exactly.
No famous problem is involved.*
