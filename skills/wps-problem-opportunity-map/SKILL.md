---
name: wps-problem-opportunity-map
description: Turn WPS Project Management demand lists into a structured problem and opportunity map. Use when many requests exist but priority and value are unclear.
intent: >-
  Convert raw WPS Project Management inputs such as demand lists, user feedback,
  and stakeholder requests into a structured problem-opportunity map. Use this
  to distinguish symptoms from root problems, cluster demand into scenario-level
  opportunities, and identify which opportunities deserve validation or product
  investment.
type: component
best_for:
  - "Making sense of large demand backlogs"
  - "Clustering user requests into problem spaces"
  - "Finding which opportunities deserve strategy or design work"
scenarios:
  - "I have two long user demand lists and need to understand what problems they point to"
  - "Help me turn scattered requests into opportunity areas for WPS Project Management"
estimated_time: "45-90 min"
---

## Purpose

Create a structured problem-opportunity map for WPS Project Management from messy demand inputs.

This skill is for the moment when the team has a lot of requests but not enough judgment. It helps answer:

- What problem is actually underneath the request?
- Which requests are duplicates in disguise?
- Which opportunities matter by scenario, not just by count?
- What should be validated before solution design starts?

This is not a prioritization scorecard. It is the bridge between raw demand and product sense.

## Key Concepts

### Demand Is Not the Same as Opportunity

A request like "add more views" is a demand. The opportunity might actually be "team leads cannot understand project status fast enough."

### Cluster by Scenario, Not by Surface Feature

Good clustering groups requests into shared user goals, constraints, and breakdown points. Bad clustering groups them by menu label.

### Opportunity Quality Matters

The strongest opportunities tend to have:

- clear user role
- recurring scenario
- meaningful pain
- visible business relevance
- a plausible path to validation

### Why This Works

- Reduces duplicate or noisy requests
- Prevents teams from jumping straight to feature design
- Helps separate strategic opportunities from one-off asks
- Gives later skills cleaner inputs

### Anti-Patterns

- **Counting requests as truth** — volume alone is not priority
- **Feature-first clustering** — grouping by capability label instead of user problem
- **Big customer override** — one loud enterprise ask becomes the roadmap
- **Premature solutioning** — deciding the feature before understanding the failure mode

### When to Use This

- After collecting demand lists
- Before prioritization or roadmap planning
- Before a major design sprint
- When research and requests feel noisy or contradictory

### When NOT to Use This

- When the problem space is already clean and validated
- For tiny tactical bugs
- When you need final prioritization math rather than opportunity framing

## Application

Use `template.md` for the final artifact.

### Step 1: Gather Inputs

Typical sources:

- raw demand lists
- sales and support feedback
- research notes
- stakeholder asks
- historical feature requests

Preserve original wording where useful. User language often reveals the real failure mode.

### Step 2: Normalize the Requests

For each request, capture:

- source
- user type
- edition context
- scenario context
- request wording
- implied problem

If you do not know the scenario, mark it unknown rather than guessing.

### Step 3: Cluster by Problem Space

Group requests into recurring problem areas such as:

- project setup friction
- assignment clarity
- progress visibility
- management visibility
- cross-role coordination

Each cluster should answer: "What repeatedly breaks for this user in this scenario?"

### Step 4: Name the Opportunity

Write the opportunity as a user-value statement, not a feature statement.

Bad:

- Better dashboard

Better:

- Team leads need to see project health quickly without manually chasing every member

### Step 5: Assess Opportunity Strength

For each opportunity, estimate:

- frequency
- pain intensity
- affected role breadth
- business relevance
- fit with current strategy
- evidence quality

If evidence is weak, say so. Weak evidence should lead to validation, not invented confidence.

### Step 6: Recommend the Next Action

Each opportunity should end in one of these recommendations:

- validate now
- move to feature design
- defer and monitor
- reject as off-strategy

## Examples

See `examples/sample.md`.

### Example Opportunity Reframe

Raw requests:

- "Need calendar view"
- "Need better reminders"
- "Need overdue tasks visible"

Opportunity:

> Team leads cannot reliably detect execution risk early enough, so work slips until a meeting exposes it.

Why this works:

- combines multiple surface asks
- identifies the shared breakdown
- gives design a real problem to solve

## Common Pitfalls

- Treating every request as equally important
- Ignoring edition context
- Mixing personal and enterprise asks in the same cluster without checking if they share a failure mode
- Writing opportunity labels that are actually feature names
- Forgetting to state what evidence is still missing

## References

- `WPS_PROJECT_MANAGEMENT.md`
- `research/wps-project-management/02-user-segments.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/05-success-metrics.md`
- `research/wps-project-management/06-feature-history.md`
- `../problem-statement/SKILL.md`
- `../opportunity-solution-tree/SKILL.md`
- `../recommendation-canvas/SKILL.md`
