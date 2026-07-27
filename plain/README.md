# Plain-English notes, by category

If [EXPLAINED.md](../EXPLAINED.md) is the one-read overview, this folder is the next step down:
a short, jargon-free note for **each kind of counting problem** in this repo, plus a one-line
"what is this counting?" for **every single sequence**.

No math background needed. A **graph** here just means dots joined by lines. Almost every problem
below asks the same shape of question: *"how many ways can you do X on a shape of size n?"* — where
the shape grows, the answer explodes into gigantic numbers, and nobody had computed the next one yet.

## Three honest words, used carefully

This whole project keeps three things separate, and so do these notes:

- **Computed & verified** — we found exact new numbers and two independently-written programs agreed
  on them digit-for-digit. This is **almost all** of the work: **137 new terms across 41 sequences.**
- **Proved** — a logical argument that must be true. Only a **few** of the "findings" are this.
- **Solved a famous problem** — **none.** Zero. We say so plainly everywhere.

And one more, because it matters: these are **candidate** extensions. Nothing here has been accepted
into the OEIS — that's a separate, human, editor-reviewed process. We're extending other people's
sequences and we credit them.

## The five categories

| Note | What it counts | Sequences | New terms |
|---|---|---:|---:|
| [Matchings](matchings.md) | pairing up neighbors | 14 | 23 |
| [Dominating sets](dominating-sets.md) | covering everything with guards | 7 | 10 |
| [Spanning trees](spanning-trees.md) | wiring up a network with no loops | 6 | 34 |
| [Domino tilings](domino-tilings.md) | covering a board with dominoes | 5 | 48 |
| [Independent sets & edge covers](independent-sets-and-edge-covers.md) | picking dots / picking lines | 9 | 22 |

Totals: **41 sequences, 137 new computed-and-verified terms.**

Want the whole list at a glance? [by-sequence.md](by-sequence.md) has a one-line plain-English
description of all 41, A-number by A-number.

## The one idea behind all of it

The counts get huge, but the machines stayed ordinary (one desktop). What moved the frontier wasn't
bigger hardware — it was finding, in each family, a way to **stop tracking everything at once**. Sweep
the shape a slice at a time and only remember what's happening at the seam; or notice that many pieces
are interchangeable and count *kinds* instead of individuals; or use a 170-year-old theorem that turns
the whole count into one arithmetic problem. Each category note tells you which trick did the work,
in plain words.

And the safety rule throughout: **two programs, written independently, had to agree exactly, or nothing
shipped.** Several times that caught real bugs before they became wrong "answers."
