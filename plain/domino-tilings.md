# Domino tilings — "cover the board with dominoes"

## What is this counting?

Take a board — a square, an odd square with a hole punched in the middle, a diamond, an Aztec-shaped
region — and cover it completely with 2×1 **dominoes**, no gaps, no overlaps. The question: *how many
different ways can it be tiled?*

Mathematicians also call each tiling a **dimer covering** or a **perfect matching**: every cell gets
paired with exactly one neighbor (the two halves under a domino), and every cell is used. So this
category is really the "everybody-gets-paired" corner of [matchings](matchings.md), on flat board shapes.

## Which sequences fall here (5 sequences, 48 new terms)

| A-number | In plain words |
|---|---|
| A071098 | tilings of a 4n×4n square with n cells removed |
| A071102 | tilings of a diamond board (the "fool's diamond") |
| A071104 | tilings of a variant Aztec-rectangle region |
| A143659 | tilings of an odd square with the center cell removed |
| A270668 | tilings of odd rectangles with a central hole (a whole table of them) |

## The trick that made extending them possible

**Turn tiling-counting into one determinant.** There's a beautiful classical result — the FKT method,
after Fisher, Kasteleyn and Temperley — that works for any *flat* (non-crossing) board: set up a special
table of +1s and −1s describing which cells touch which, take one determinant, and out pops the exact
number of tilings. Counting-by-listing would be hopeless; this is a single exact arithmetic operation, so
these extended fast and far (48 new terms, the most of any category).

**The detective story (A071102).** One of these sequences arrived with *no picture at all* — just a list
of numbers labeled "fool's diamond," with the actual board shape lost. Earlier attempts gave up. Our
scout tracked down the original 1999 research paper, opened the PDF, zoomed into the tiny figure, and
**reconstructed the board shape pixel by pixel** (it turned out to be a diamond). Only then could it
compute 17 new terms — and it checked them *four* independent ways, including against a conjectured
formula. That's the kind of persistence broad searches miss.

*All terms here are computed-and-verified candidate extensions — two independent programs agreed exactly.
No famous problem is involved.*
