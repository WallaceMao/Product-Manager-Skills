---
name: wps-project-management-strategy
description: Frame product strategy for WPS Project Management across editions, target users, scenarios, and differentiation. Use when aligning direction before roadmap or solution work.
intent: >-
  Create a WPS Project Management strategy brief that connects edition structure
  (personal vs enterprise), target users, core scenarios, differentiation,
  adoption path, and non-goals into one strategic view. Use this before roadmap,
  major feature bets, or product repositioning so the team does not confuse
  feature inventory with actual strategy.
type: component
best_for:
  - "Framing the next quarter or half-year strategy for WPS Project Management"
  - "Clarifying personal edition vs enterprise edition priorities"
  - "Aligning product, design, engineering, and leadership on strategic direction"
scenarios:
  - "We need a strategy brief before deciding what WPS Project Management should build next"
  - "Help me define who WPS Project Management is really for and what we should not do"
  - "I need a product strategy artifact that goes beyond competitor feature comparison"
estimated_time: "45-75 min"
---

## Purpose

Create a strategy brief for `WPS Project Management` that makes the core strategic choices explicit:

1. Which users matter most now
2. Which scenarios are must-win
3. How personal edition and enterprise edition relate
4. What differentiation is defensible inside the WPS ecosystem
5. What not to build in this phase

This is not a vision slogan deck. It is a working strategy artifact for deciding where to invest and where to refuse work.

## Key Concepts

### Strategy Is Choice, Not Coverage

If the strategy can accommodate every request, it is not a strategy. WPS Project Management needs explicit choices about editions, user environments, and scenario priority.

### Edition Structure Matters

WPS Project Management is not one flat product context. At minimum it has:

- **Personal edition** — Individual WPS Office users, lower setup friction, lighter execution jobs
- **Enterprise edition** — WPS 365 / Jinshan Collaboration / WPS Collaboration customers, team rollout, multi-role collaboration, stronger management needs

If you blur these together, you will get vague strategy and noisy prioritization.

### Differentiation Should Fit the Ecosystem

The strategy should use WPS-native advantages where possible:

- document-to-execution flow
- meeting-to-task flow
- AI-native work intake
- collaboration inside a broader office suite

Competing feature-for-feature with every project tool is an anti-strategy.

### Why This Works

- Forces clarity on who the product serves now
- Turns research into explicit strategic choices
- Prevents roadmap discussions from collapsing into request triage
- Makes edition conflicts visible before they distort execution

### Anti-Patterns

- **Feature list as strategy** — "We need gantt, dashboards, SSO, approvals, templates"
- **Competitor mimicry as positioning** — "Feishu has it, so we need it"
- **Stakeholder demand as truth** — executive or sales requests without user/scenario grounding
- **Edition blur** — pretending personal and enterprise share the same success definition

### When to Use This

- Quarterly or semi-annual planning
- Product repositioning
- Before creating a major roadmap
- When team debates keep circling around "who is this for?"

### When NOT to Use This

- For a minor feature tweak
- When you need implementation detail rather than direction
- When the product context documents are still empty

## Application

Use `template.md` for the final artifact.

### Step 1: Read the Current Context

Pull from:

- `research/wps-project-management/00-product-overview.md`
- `research/wps-project-management/01-strategy-context.md`
- `research/wps-project-management/02-user-segments.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/04-competitive-landscape.md`
- `research/wps-project-management/05-success-metrics.md`

If those are incomplete, say what is missing instead of pretending certainty.

### Step 2: State the Strategic Problem

Answer:

- What strategic ambiguity exists right now?
- Why does it matter now?
- What decision pressure is forcing clarity?

Example:

> WPS Project Management must decide whether the near-term product is primarily a personal AI execution entry point or a team collaboration system anchored in WPS 365. That choice affects scenarios, metrics, adoption design, and roadmap shape.

### Step 3: Choose the Strategic Focus

Define:

- primary user environment
- primary segment
- must-win scenarios
- strategic value layer in the WPS ecosystem

Do not say "both" unless you can prove both share the same value path.

### Step 4: Define Differentiation

Write the product's strategic angle in plain language:

- what users get here that they do not get elsewhere
- why WPS is a better home for that value
- what level of product depth is actually required

### Step 5: Define Adoption Path

Explain how users reach value:

- entry point
- aha moment
- repeat loop
- expansion or collaboration path

This is critical for edition design. Personal and enterprise often have different adoption paths.

### Step 6: Name Non-Goals

List what the product will not optimize for in this phase.

Strong non-goals are a sign that the strategy is doing real work.

## Examples

See `examples/sample.md`.

### Example of a Good Strategic Choice

"For the next two quarters, WPS Project Management will prioritize enterprise edition team execution scenarios where a team lead needs to turn WPS-native content into shared execution, while keeping personal edition focused on lightweight intake rather than full project management depth."

Why this works:

- picks a primary value layer
- still gives personal edition a role
- avoids pretending both editions need equal depth immediately

### Anti-Pattern Example

"Our strategy is to become the best AI project management platform for everyone, from solo users to large enterprises."

Why this fails:

- no user choice
- no scenario choice
- no edition tradeoff
- impossible to operationalize in roadmap decisions

## Common Pitfalls

- Skipping the edition question and writing one generic strategy
- Treating "AI" as differentiation without showing user value
- Confusing top-of-funnel traffic with a product strategy
- Writing goals without naming what gets deprioritized
- Using competitor grids instead of scenario evidence

## References

- `WPS_PROJECT_MANAGEMENT.md`
- `research/wps-project-management/00-product-overview.md`
- `research/wps-project-management/01-strategy-context.md`
- `research/wps-project-management/02-user-segments.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/04-competitive-landscape.md`
- `research/wps-project-management/05-success-metrics.md`
- `../product-strategy-session/SKILL.md`
- `../positioning-statement/SKILL.md`
- `../roadmap-planning/SKILL.md`
