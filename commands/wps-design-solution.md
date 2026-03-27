---
name: wps-design-solution
description: Turn a WPS Project Management opportunity into compared solution options and a recommended design direction.
argument-hint: "<WPS problem, target users, and scenario>"
uses:
  - wps-problem-opportunity-map
  - wps-feature-design
  - wps-solution-evaluation
outputs:
  - Problem and opportunity summary
  - Feature design skeleton
  - Recommended solution direction
---

# /wps-design-solution

Move from demand or problem framing into a defensible WPS solution recommendation.

## Invocation

```text
/wps-design-solution Team leads cannot quickly see project risk in enterprise edition without manually chasing updates
```

## Workflow

1. Normalize the problem space with `wps-problem-opportunity-map`.
2. Turn the chosen opportunity into a structured solution skeleton with `wps-feature-design`.
3. Compare viable approaches and recommend one with `wps-solution-evaluation`.

## Checkpoints

- Keep the work anchored to edition, user role, and scenario.
- Compare options at the same altitude; do not compare a tiny tweak against a platform rewrite.
- End with a recommendation and the evidence still needed to validate it.

## Next Steps

- Run `/wps-write-prd` for the recommended option.
- Run `/prioritize` if this solution will compete against other roadmap bets.

