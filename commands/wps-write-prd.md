---
name: wps-write-prd
description: Create a WPS Project Management PRD by chaining feature design, product requirements, and story scaffolding.
argument-hint: "<WPS feature or initiative to spec>"
uses:
  - wps-feature-design
  - wps-project-management-prd
  - user-story
  - epic-hypothesis
outputs:
  - WPS-specific PRD
  - User stories and requirements
  - Epic hypothesis and release notes
---

# /wps-write-prd

Create a PRD for WPS Project Management that includes edition context, collaboration logic, object rules, and validation.

## Invocation

```text
/wps-write-prd Enterprise project health view for team leads in active execution scenarios
```

## Workflow

1. Build or confirm the solution skeleton with `wps-feature-design`.
2. Write the full WPS-specific document with `wps-project-management-prd`.
3. Draft implementation-facing stories with `user-story`.
4. Frame the initiative as a testable bet with `epic-hypothesis`.

## Checkpoints

- Make edition scope explicit.
- Capture object model and permission logic, not just screen behavior.
- Include instrumentation, guardrails, and rollout risk before calling the PRD done.

## Next Steps

- Run `/wps-quarter-planning` if this initiative is roadmap-ready.
- Run `/prioritize` if the scope must compete for near-term capacity.

