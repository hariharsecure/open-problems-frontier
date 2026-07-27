# Contributing — the ticket-driven flow

Every change goes through a tracked ticket, so status is always visible in git.

1. **Open an issue** (Issues tab → pick a template). One request = one issue.
2. **Branch** off `main`: `git switch -c <type>/<short-name>` (`type` ∈ feat/fix/docs).
3. **Build** the change on the branch.
4. **QA** — a change is reviewed from multiple angles before merge: correctness/reproducibility,
   honesty (no overclaiming: computed-and-verified ≠ proved ≠ solved-a-famous-problem), docs
   completeness/best-practices, and readability for a newcomer.
5. **PR → merge to `main`** when QA is green; reference the issue (`Closes #N`).
6. **Version**: production is tagged with SemVer (`vMAJOR.MINOR.PATCH`) + a GitHub Release.

Fast to track: open the issue, watch it move Open → in-branch → PR → merged → released.
