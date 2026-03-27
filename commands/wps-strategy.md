---
name: wps-strategy
description: Build WPS Project Management strategy from edition context through users, scenarios, differentiation, and roadmap direction.
argument-hint: "<WPS Project Management strategic question, stage, and context>"
uses:
  - wps-project-management-strategy
  - problem-statement
  - positioning-statement
  - roadmap-planning
outputs:
  - WPS strategy brief
  - Core strategic choices
  - Strategic risks and non-goals
---

# /wps-strategy

Run a WPS Project Management strategy workflow that forces real choices instead of vague positioning.

## Invocation

```text
/wps-strategy Decide whether WPS Project Management should prioritize enterprise execution depth or personal edition activation next quarter
```

## Workflow

1. Frame the strategic problem with `problem-statement`.
2. Build the WPS-specific strategic view with `wps-project-management-strategy`.
3. Tighten target customer and differentiation with `positioning-statement`.
4. Translate the strategy into roadmap implications with `roadmap-planning`.

## Checkpoints

- Make personal edition vs enterprise edition tradeoffs explicit.
- Name must-win scenarios instead of listing desired capabilities.
- Record strong non-goals so downstream planning stays disciplined.

## Next Steps

- Run `/wps-quarter-planning` to sequence quarter bets.
- Run `/wps-design-solution` once a top opportunity is chosen.

