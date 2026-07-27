# Independent sets & edge covers — "pick dots / pick lines"

## What is this counting?

Two mirror-image questions, both about choosing a set on a graph of dots and lines.

**Independent set — pick dots, no two touching.** Choose some dots so that no line runs directly between
any two you picked. (Think: seat guests so no two who dislike each other sit adjacent.) A **maximal**
independent set is one you can't add anybody to — every leftover dot is blocked by someone you already
chose. *How many such sets are there?*

**Edge cover — pick lines so every dot is touched.** Choose some lines so that every single dot has at
least one chosen line hanging off it. A **minimal** edge cover is one with no wasted line — remove any and
some dot goes uncovered. *How many are there?*

(A small, pretty fact used here: on any graph, the number of independent sets equals the number of
**vertex covers** — the two are just complements of each other — which is why one sequence counts "both.")

The shapes: plain grids, grids wrapped into a donut (**torus**), a "stacked book" graph, the Tower-of-Hanoi
puzzle graph, the Sierpinski gasket (triforce) and tetrahedron, and the Fibonacci and Lucas cubes.

## Which sequences fall here (9 sequences, 22 new terms)

| A-number | In plain words |
|---|---|
| A288027 | minimal edge covers of the n×n grid |
| A288490 | independent sets (= vertex covers) of the Tower-of-Hanoi graph |
| A297051 | edge covers of the Fibonacci cube |
| A297230 | edge covers of the Sierpinski tetrahedron |
| A321248 | maximal independent sets of the n×n stacked-book graph |
| A321249 | maximal independent sets of the Tower-of-Hanoi graph |
| A321250 | maximal independent sets of the torus (donut) grid |
| A364745 | edge covers of the Lucas cube |
| A378860 | minimal edge covers of the Sierpinski gasket (triforce) |

## The trick that made extending them possible

**Count the kinds, not the individuals.** These use the same "only remember the seam" sweep as the other
categories — but one of them (the stacked-book graph, A321248) had a boundary that looked hopeless: the
naive method needed to track 3-to-the-n possibilities, astronomically many.

The saving observation: many of those possibilities are *interchangeable*. The book's pages are alike, so
swapping two of them gives the exact same picture. Instead of tracking *which* pages are in which state,
just track *how many* are in each state. That collapses an impossible 3-to-the-n count down to something an
ordinary laptop finishes in a fraction of a second (it produced **ten** new terms here). Recognizing hidden
sameness is often the whole difference between "impossible" and "easy."

*All terms here are computed-and-verified candidate extensions — two independent programs agreed exactly.
No famous problem is involved.*
