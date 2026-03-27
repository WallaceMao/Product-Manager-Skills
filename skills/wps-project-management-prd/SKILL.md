---
name: wps-project-management-prd
description: Write a WPS Project Management PRD with edition context, object rules, collaboration design, and validation plan. Use for major feature or initiative specs.
intent: >-
  Create a WPS Project Management PRD that extends the repo's generic PRD
  workflow with edition context, collaboration roles, object model impact,
  WPS ecosystem integration points, instrumentation, and release-risk planning.
  Use this when an initiative is real enough to need engineering-ready clarity
  without losing strategic context.
type: workflow
best_for:
  - "Writing a WPS-specific PRD for a major feature or initiative"
  - "Turning a feature design into an execution-ready spec"
  - "Making sure PRDs include edition, role, and object-model logic"
scenarios:
  - "Create a PRD for a new enterprise project health feature in WPS Project Management"
  - "Help me write a PRD that reflects WPS ecosystem integration and collaboration rules"
estimated_time: "60-120 min"
---

## Purpose

Create a WPS Project Management PRD that is specific enough for execution and specific enough to avoid false clarity.

This workflow extends the generic PRD discipline with WPS-specific needs:

- edition context
- role and permission logic
- object model impact
- WPS ecosystem touchpoints
- instrumentation and rollout risk

This is not a page-by-page spec. It is a product requirements document that keeps problem, solution, rules, and measurement aligned.

## Key Concepts

### A WPS PM PRD Needs More Than a Feature Summary

For this product, a strong PRD must cover:

- which edition it belongs to
- who acts and who observes
- which objects are affected
- what state transitions matter
- how WPS integrations shape the experience

### Collaboration Logic Is Part of the Requirement

If a feature changes how a lead, member, and manager interact, that is product logic, not implementation detail.

### Validation Is Part of the Spec

The PRD should make it clear what success looks like after launch and how the team will know quickly if the feature is not working.

### Why This Works

- prevents vague PRDs that ignore WPS-specific context
- improves engineering and design alignment
- reduces rework from missing role/state logic
- keeps release risk visible

### Anti-Patterns

- **Page walkthrough as PRD** — describing screens instead of product logic
- **No object model impact** — ignoring project/task/status relationships
- **No rollout thinking** — shipping without a monitoring or release plan
- **Edition ambiguity** — unclear whether the feature is personal, enterprise, or both

### When to Use This

- Major feature or initiative PRDs
- Cross-functional initiatives
- Features affecting collaboration, object rules, or WPS integrations

### When NOT to Use This

- Tiny bug fixes
- Copy-only tweaks
- Exploration work that is not yet solution-ready

---

### Facilitation Source of Truth

When running this workflow as a guided conversation, use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels
- interruption handling and pause/resume behavior
- numbered recommendations at decision points

This file defines the workflow sequence and WPS-specific content requirements. If there is a conflict, follow this file's domain logic.

## Application

Use `template.md` for the final PRD structure.

### Phase 1: Gather Preconditions

Before drafting, confirm you have:

- problem/opportunity statement
- target edition
- primary role and collaborators
- scenario and non-scenario boundaries
- relevant research inputs

If these are missing, stop and name the gap.

### Phase 2: Define Problem and Strategy Context

Summarize:

- problem statement
- target users
- why now
- strategic fit
- success metric direction

### Phase 3: Define Solution Logic

Document:

- feature overview
- task flow
- object model impact
- roles and permissions
- state transitions
- WPS integration points

### Phase 4: Define Requirements and Edge Cases

Add:

- user stories
- acceptance logic
- edge cases
- out of scope
- dependencies

### Phase 5: Define Validation and Release Plan

Add:

- instrumentation
- primary and guardrail metrics
- rollout approach
- known risks
- open questions

## Examples

See `examples/sample.md`.

### Good PRD Smell

A good WPS PM PRD lets engineering, design, and analytics all answer the same question: "What is supposed to happen, for whom, under which conditions, and how will we know if it worked?"

## Common Pitfalls

- Starting with solution detail before a clean problem statement
- Mixing personal and enterprise rules in one ambiguous flow
- Omitting permission logic
- Forgetting to specify what event data is needed
- Treating rollout risk as an afterthought

## References

- `WPS_PROJECT_MANAGEMENT.md`
- `research/wps-project-management/00-product-overview.md`
- `research/wps-project-management/01-strategy-context.md`
- `research/wps-project-management/02-user-segments.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/05-success-metrics.md`
- `research/wps-project-management/07-domain-terminology.md`
- `research/wps-project-management/08-constraints-and-assumptions.md`
- `../prd-development/SKILL.md`
- `../user-story/SKILL.md`
- `../epic-hypothesis/SKILL.md`
