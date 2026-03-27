---
name: wps-quarter-roadmap
description: Build a quarter roadmap for WPS Project Management across strategy, opportunity clusters, and solution bets. Use when planning the next quarter's investments.
intent: >-
  Create a WPS Project Management quarterly roadmap that links strategy,
  opportunities, solution bets, sequencing, risks, and success metrics. Use this
  when converting the product's current strategic choices into a quarter plan
  that is specific enough to guide execution without collapsing into a feature
  dump.
type: workflow
best_for:
  - "Building the next quarter roadmap for WPS Project Management"
  - "Sequencing product bets after strategy and opportunity work"
  - "Turning research and solution ideas into a coherent plan"
scenarios:
  - "Help me plan the next quarter roadmap for WPS Project Management"
  - "We have strategy and demand inputs; now we need a quarter plan with sequencing"
estimated_time: "60-90 min"
---

## Purpose

Create a quarterly roadmap for WPS Project Management that reflects real choices rather than a polished backlog.

The roadmap should answer:

- what this quarter is trying to prove or improve
- which opportunity areas deserve investment
- which bets are now, next, or later
- how personal and enterprise edition priorities interact
- what risks and dependencies could break the plan

This is not a feature list. It is a strategic sequencing tool.

## Key Concepts

### Quarter Roadmaps Need a Thesis

If the roadmap has initiatives but no quarter theme or logic, it is just organized noise.

### Sequencing Matters

Some bets create learning. Some bets create capability. Some bets should wait until the product proves a prior assumption.

### Edition Planning Should Be Explicit

WPS Project Management may need different quarter goals by edition:

- personal edition: activation and repeat use
- enterprise edition: collaboration depth and team retention

If the roadmap mixes them without a rationale, it will be hard to execute and harder to evaluate.

### Why This Works

- aligns roadmap to current product reality
- keeps opportunity work connected to delivery
- prevents quarter plans from becoming stakeholder wish lists
- makes dependencies and risks visible early

### Anti-Patterns

- **Everything is P0** — no sequencing discipline
- **Roadmap by request source** — sales asks, leadership asks, design asks
- **Edition blur** — one roadmap pretending all user environments need the same work
- **No learning logic** — initiatives are listed without saying what they prove

### When to Use This

- Quarterly planning
- After strategy and opportunity mapping
- Before cross-functional planning and commitment

### When NOT to Use This

- Sprint planning
- When the strategic focus is still unresolved
- When there are no validated or at least coherent opportunities to sequence

---

### Facilitation Source of Truth

When running this workflow as a guided conversation, use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol.

This file defines the roadmap sequence and WPS-specific decision logic. If there is a conflict, follow this file's domain logic.

## Application

Use `template.md` for the final roadmap artifact.

### Phase 1: Confirm the Quarter Thesis

State:

- what this quarter is mainly trying to improve or prove
- which edition or scenario gets primary focus
- what success would look like by quarter end

### Phase 2: Gather Inputs

Use:

- strategy brief
- problem-opportunity map
- solution evaluations
- current constraints
- success metrics

### Phase 3: Define the Bet Structure

Group work into:

- now
- next
- later

Or if preferred:

- quarter theme 1
- quarter theme 2
- enabling work

Each bet should have a reason, not just a name.

### Phase 4: Sequence with Dependencies

For each bet, note:

- dependency
- risk
- expected learning
- expected metric effect

### Phase 5: Communicate the Tradeoffs

A useful roadmap explains:

- what is in
- what is not in
- why this order makes sense

## Examples

See `examples/sample.md`.

### Good Roadmap Logic

"This quarter prioritizes enterprise execution visibility because team-retention evidence is stronger than personal-edition expansion evidence, while personal edition work remains focused on lightweight activation improvements rather than depth."

## Common Pitfalls

- Roadmap themes that are just renamed features
- No explanation for sequencing
- No quarter-level success definition
- Treating enablers as invisible even when they dominate delivery capacity

## References

- `WPS_PROJECT_MANAGEMENT.md`
- `research/wps-project-management/01-strategy-context.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/05-success-metrics.md`
- `research/wps-project-management/08-constraints-and-assumptions.md`
- `../roadmap-planning/SKILL.md`
- `../prioritization-advisor/SKILL.md`
- `../epic-hypothesis/SKILL.md`
