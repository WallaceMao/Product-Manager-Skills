---
name: wps-quarter-planning
description: Sequence WPS Project Management quarter bets from strategy, opportunity clusters, and solution decisions.
argument-hint: "<quarter, strategic focus, and candidate WPS bets>"
uses:
  - wps-project-management-strategy
  - wps-problem-opportunity-map
  - wps-solution-evaluation
  - wps-quarter-roadmap
outputs:
  - Quarter thesis
  - Sequenced roadmap bets
  - Tradeoffs, risks, and success measures
---

# /wps-quarter-planning

Plan a WPS Project Management quarter with explicit bets, sequencing logic, and edition-aware tradeoffs.

## Invocation

```text
/wps-quarter-planning Q3 planning for WPS Project Management with enterprise execution visibility as the primary focus
```

## Workflow

1. Reconfirm strategic focus with `wps-project-management-strategy`.
2. Convert current demand and research into opportunity-level inputs with `wps-problem-opportunity-map`.
3. Use `wps-solution-evaluation` to pressure-test major option areas.
4. Build the final quarter plan with `wps-quarter-roadmap`.

## Checkpoints

- State the quarter thesis before listing initiatives.
- Explain why each bet is now, next, or later.
- Make clear which edition gets primary investment and which does not.

## Next Steps

- Run `/wps-write-prd` for the top committed bet.
- Run `/wps-design-solution` for any high-importance opportunity that still lacks a recommended approach.

