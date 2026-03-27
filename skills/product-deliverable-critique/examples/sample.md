# Sample: Product Deliverable Critique

```markdown
# Product Deliverable Critique

## 1. Artifact Context
- Artifact name: Enterprise Execution Visibility PRD v0.1
- Artifact type: PRD
- Intended job: Align product, design, and engineering on MVP scope and validation path
- Audience: PM, design lead, engineering lead, QA
- Decision or next step this artifact is meant to support: Internal review and sprint planning

## 2. Review Scope
- Most relevant review dimensions:
  - evidence quality
  - logic continuity
  - scope and non-goals
  - object / state / permission clarity
  - execution readiness

## 3. Core Claims
1. Enterprise team leads need risk visibility inside the project context.
2. A health summary plus risk list is the right MVP shape.
3. The proposed scope is implementable in one release cycle.

## 4. Findings

### P1
- Problem: The PRD states that "team leads need project health at a glance" but does not show which evidence proves in-project visibility is better than a separate dashboard.
- Why it matters: The recommendation may still be right, but the reasoning chain is incomplete.
- Consequence: Stakeholders can reopen the solution debate late because the document does not clearly show why the chosen shape wins.
- Fix: Add a short option comparison summary or link to the solution-direction document in the PRD context section.

### P1
- Problem: The requirement mentions "risk tasks" but does not define when a task becomes a risk item versus remaining a normal task with a warning signal.
- Why it matters: This is an object-model ambiguity, not a wording issue.
- Consequence: Product, engineering, and QA may implement different interpretations and produce inconsistent behavior.
- Fix: Add a rule table that distinguishes signal-only tasks from explicit risk items, including who can create, dismiss, and resolve them.

### P2
- Problem: The rollout section says the feature will help execution follow-up, but the guardrail metrics are not specific enough to detect alert fatigue or low action quality.
- Why it matters: This weakens post-launch learning.
- Consequence: The team may ship the MVP, see activity increase, and still not know whether the behavior is genuinely useful.
- Fix: Add guardrails such as ignored-risk rate, follow-up completion rate, and reopened-risk rate.

## 5. Open Questions
- Will enterprise viewers outside the project team have read-only access to the health summary?
- Should the MVP support manual risk creation, automatic rule-based risk creation, or both?
- What existing WPS notification surfaces can carry follow-up actions without creating duplicate reminders?

## 6. Verdict
- Revise and Re-review
- Short rationale: The PRD is directionally strong, but it still has meaningful evidence and behavior-definition gaps that should be fixed before planning.
```
