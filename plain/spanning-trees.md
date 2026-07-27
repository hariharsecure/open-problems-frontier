# Spanning trees — "wire up the network, no loops"

## What is this counting?

You have a network of dots and the possible cables between them. You want to connect *everything* into a
single piece using just enough cables that there are no redundant loops — pull any cable and something
falls off. That skeleton is a **spanning tree**. The question: *how many different spanning trees does
this network have?* (Even small networks have a startling number of them.)

This is a classic quantity — it shows up in electrical networks, reliability, and random walks — which is
why so many of these came with only a handful of published terms and an obvious "what's next?".

The shapes: "folded" and "halved" cubes, triangular graphs (dots are pairs, joined when they share an
element), a grid wrapped into a donut (**torus**), the king-move chessboard, and the **Bruhat graph** —
a network built from all the ways to reorder a small deck of cards.

## Which sequences fall here (6 sequences, 34 new terms)

| A-number | In plain words |
|---|---|
| A193134 | spanning trees of the folded cube graphs |
| A193135 | spanning trees of the halved cube graphs |
| A193154 | spanning trees of the triangular graphs |
| A212800 | spanning trees of the torus (donut) grid |
| A288957 | spanning trees of the n×n king graph |
| A340398 | spanning trees of the Bruhat graph (reorderings of a deck) |

## The trick that made extending them possible

**A 170-year-old shortcut turns counting into a single sum.** You might expect to *list* trees to count
them — hopeless, there are astronomically many. But the **Matrix-Tree Theorem** (Kirchhoff, 1847) says:
write down a simple table describing which dots connect to which, do one exact arithmetic operation on it
(a determinant), and the answer *is* the number of spanning trees. No listing, no searching — one exact
calculation.

That's why this category produced the most new terms of any (34): once the shortcut applies, extending a
sequence is cheap and exact, so we could push many of them at once. The only thing that grows is the sheer
number of digits in the answer, and exact big-number arithmetic handles that without ever rounding.

*All terms here are computed-and-verified candidate extensions — two independent programs agreed exactly.
No famous problem is involved.*
