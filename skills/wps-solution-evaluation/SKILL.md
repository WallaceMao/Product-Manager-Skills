---
name: wps-solution-evaluation
description: Compare WPS Project Management solution options by user value, strategic fit, complexity, risk, and validation path. Use when multiple approaches compete.
intent: >-
  Evaluate competing WPS Project Management solution options in a structured
  way. Use this when product, design, and engineering have multiple possible
  approaches and need a defensible recommendation that balances user value,
  edition fit, strategic alignment, complexity, risk, and measurability.
type: component
best_for:
  - "Comparing multiple product solution options"
  - "Recommending one approach without hand-wavy reasoning"
  - "Making tradeoffs visible before PRD lock-in"
scenarios:
  - "We have three ways to solve project progress visibility and need a recommendation"
  - "Help me compare WPS Project Management solution directions before we commit"
estimated_time: "45-75 min"
---

## Purpose

Create a structured comparison of competing WPS Project Management solutions and recommend one.

This skill exists because teams often compare options poorly:

- the loudest stakeholder wins
- the quickest implementation wins
- every option gets described at a different level of detail

The output should make the recommendation explainable, not merely intuitive.

## Key Concepts

### Compare at the Same Altitude

Do not compare a narrow UI tweak against a broad platform investment as if they were equivalent options. Normalize the level of abstraction first.

### A Good Option Is Contextual

The best solution depends on:

- edition
- user role
- scenario
- strategy
- delivery constraints

There is no "best" option outside that context.

### Validation Path Matters

An option that looks attractive but cannot be validated quickly may be weaker than a simpler option with cleaner proof-of-life.

### Why This Works

- makes tradeoffs explicit
- prevents vague "I like this one more" debates
- keeps recommendation tied to strategy and scenario
- creates a documented rationale for later review

### Anti-Patterns

- **Speed-only choice** — "this one is faster so we should do it"
- **Voice-power choice** — "leadership likes it"
- **Unbounded optioning** — options are too vaguely defined to compare
- **No fit check** — option ignores edition or scenario reality

### When to Use This

- When there are 2-4 serious options
- During solution exploration
- Before PRD lock-in
- During cross-functional debate on approach

### When NOT to Use This

- When only one viable option exists
- When the underlying problem is still unclear
- When you need portfolio prioritization across many initiatives

## Application

Use `template.md` for the final artifact.

### Step 1: Frame the Comparison Context

State:

- problem being solved
- edition
- user role
- scenario
- decision to be made

Without this, the evaluation will drift into generic product talk.

### Step 2: Define the Options Cleanly

For each option, describe:

- what it is
- how it works at a high level
- what assumptions it depends on
- what it does not try to do

### Step 3: Score Against Core Dimensions

Use the same dimensions for every option:

- user value
- strategic fit
- complexity
- collaboration cost
- risk
- validation path
- time-to-learning

Scores are useful, but the explanation matters more than the number.

### Step 4: Recommend with Conditions

Give:

- recommended option
- why it wins
- what conditions could change the recommendation
- what should be validated next

## Examples

See `examples/sample.md`.

### Example of a Good Recommendation

"Recommend Option B because it gives enterprise team leads earlier risk visibility with lower workflow change than Option C, while still producing measurable proof within one release cycle."

Why this works:

- names the winner
- names the user and value
- acknowledges tradeoff
- ties to validation speed

## Common Pitfalls

- Comparing solution shapes at different levels of scope
- Ignoring rollout or collaboration cost
- Calling something "low risk" without naming what could fail
- Forgetting what evidence would overturn the recommendation

## References

- `WPS_PROJECT_MANAGEMENT.md`
- `research/wps-project-management/01-strategy-context.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/05-success-metrics.md`
- `research/wps-project-management/08-constraints-and-assumptions.md`
- `../recommendation-canvas/SKILL.md`
- `../feature-investment-advisor/SKILL.md`
- `../problem-statement/SKILL.md`
