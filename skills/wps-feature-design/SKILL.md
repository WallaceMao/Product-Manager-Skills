---
name: wps-feature-design
description: Design WPS Project Management features across scenarios, flows, states, roles, and validation. Use when turning an opportunity into a solution skeleton.
intent: >-
  Create a structured feature design skeleton for WPS Project Management before
  full PRD writing. Use this to move from a validated opportunity to a coherent
  design frame that covers user goals, scenario boundaries, task flow, states,
  roles, permissions, edge cases, instrumentation, and release risks.
type: component
best_for:
  - "Designing a feature before writing the PRD"
  - "Clarifying flows, rules, and edge cases for WPS Project Management"
  - "Making sure a feature design covers roles and collaboration, not just screens"
scenarios:
  - "Help me design the solution shape for a new project progress tracking feature"
  - "I need a feature design skeleton for a WPS Project Management opportunity"
estimated_time: "60-90 min"
---

## Purpose

Turn a WPS Project Management opportunity into a design skeleton the team can reason about before full PRD work starts.

The output should make it possible to answer:

- what user goal this feature serves
- which edition and scenario it belongs to
- what the main task flow is
- which roles and states matter
- what edge cases will break trust if ignored
- how success will be observed after release

This is not a UI spec. It is the structural design frame behind the feature.

## Key Concepts

### Design the User Task, Not the Page

If the design starts with screens instead of the user's job, you will miss the real workflow and the real failure modes.

### Collaboration Changes the Design

Many project management features are not single-user actions. They involve:

- initiator
- assignee
- watcher or manager
- admin or organization context

Ignoring role interaction creates false simplicity.

### State and Rule Design Are Load-Bearing

Features like projects, tasks, reminders, or progress views depend on object state, permissions, transitions, and exceptions. If those are unclear, the UI can look finished while the product logic is broken.

### Why This Works

- Forces scenario clarity before spec writing
- Makes collaboration and object rules explicit
- Reduces later PRD churn
- Improves handoff quality to design and engineering

### Anti-Patterns

- **Page-first design** — "Page A has a button that opens Page B"
- **Happy-path-only thinking** — no error, exception, reassignment, or empty-state logic
- **Single-user bias** — forgetting how collaborators experience the same flow
- **No validation plan** — shipping without knowing what outcome should move

### When to Use This

- After opportunity framing
- Before PRD writing
- During solution exploration
- When product, design, and engineering need a shared design frame

### When NOT to Use This

- For trivial copy-only or cosmetic changes
- When the opportunity itself is still unclear
- When you already have a detailed, agreed design frame

## Application

Use `template.md` for the final artifact.

### Step 1: Define the Design Context

Capture:

- edition
- target user role
- primary scenario
- adjacent scenarios
- triggering event

If you cannot name the scenario clearly, you are not ready to design the feature.

### Step 2: Define the Core User Goal

Write one primary job the feature helps complete. Then write what success looks like from the user's point of view.

### Step 3: Map the Main Flow

Describe:

1. trigger
2. entry
3. key action sequence
4. completion state
5. follow-up behavior

Keep it at the task-flow level. Do not collapse into wireframe commentary.

### Step 4: Define Roles, Permissions, and Objects

List:

- user roles involved
- affected objects
- important state changes
- permission checks

For WPS Project Management, this is usually where weak designs are exposed.

### Step 5: Document Edge Cases

Examples:

- task has no owner
- reassignment happens mid-stream
- project is archived
- reminder fires after work is already complete
- manager has view permission but not edit permission

If the feature relies on multi-role collaboration, edge cases are mandatory.

### Step 6: Define Measurement and Release Risk

Add:

- primary success metric
- guardrail metric
- event instrumentation
- release risk
- staged rollout notes if needed

## Examples

See `examples/sample.md`.

### Example of a Good Design Statement

"This feature helps enterprise team leads detect execution risk across active tasks without manually asking every member for updates."

Why this works:

- names the user
- names the scenario
- names the job
- avoids jumping to a specific screen

## Common Pitfalls

- Designing a dashboard before defining what decision it supports
- Mixing personal-edition simplicity with enterprise-edition complexity in one flow
- Ignoring permission boundaries
- Failing to define state transitions
- Calling analytics events "nice to have"

## References

- `WPS_PROJECT_MANAGEMENT.md`
- `research/wps-project-management/02-user-segments.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/05-success-metrics.md`
- `research/wps-project-management/07-domain-terminology.md`
- `research/wps-project-management/08-constraints-and-assumptions.md`
- `../user-story/SKILL.md`
- `../epic-hypothesis/SKILL.md`
- `../problem-statement/SKILL.md`
