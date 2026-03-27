---
name: product-deliverable-critique
description: Critically review product artifacts for evidence gaps, logic jumps, scope creep, and execution ambiguity. Use when a deliverable looks polished but may be weak.
intent: >-
  Pressure-test product work with disciplined critique. Use this when you need
  to review an insight summary, opportunity map, solution direction, PRD,
  engineering breakdown, roadmap, or review pack and identify what is missing,
  weak, overstated, or not executable.
type: component
best_for:
  - "Reviewing product artifacts before stakeholder or engineering review"
  - "Finding logic gaps in polished-looking PM deliverables"
  - "Separating supported conclusions from plausible but unproven claims"
scenarios:
  - "Critique this PRD before I send it to design and engineering"
  - "Review this insights summary and tell me where the evidence is weak"
estimated_time: "20-45 min"
---

## Purpose

Use this skill to review product deliverables with critical thinking, not copyediting instincts.

This skill exists because many weak deliverables fail in the same deceptive way:

- they look structured
- they sound confident
- they contain some true facts
- but the reasoning chain is incomplete, overstated, or not actionable

The goal is not to make a document look smarter. The goal is to decide whether the artifact can support product decisions, alignment, or execution.

## Key Concepts

### Critique Is Not Negativity

Good critique does not mean being combative, cynical, or vague.

It means asking:

- what claim is being made
- what evidence supports it
- what reasoning connects the two
- what would make the claim false or weaker

### Review the Artifact at Its Intended Job

Different deliverables exist to do different work.

- An insight summary should clarify signal, not propose implementation detail.
- A PRD should make scope, roles, rules, and validation explicit.
- A roadmap should help sequencing and tradeoff decisions, not just list asks.

Critique should be tied to the artifact's purpose. Otherwise the review becomes noise.

### Polished Does Not Mean Decision-Ready

Many PM artifacts are over-trusted because they are well formatted or use familiar language.

Common false signals:

- clean headings
- precise-looking but unsupported statements
- feature vocabulary that hides a fuzzy problem
- long requirement lists without object, state, or permission clarity

### Evidence Gaps Matter More Than Stylistic Gaps

Prioritize issues that could distort a decision or break execution:

- unsupported conclusions
- edition, role, or scenario confusion
- problem/solution mixing
- scope creep
- unclear validation path
- ambiguous ownership or behavior rules

Do not waste the review on cosmetic edits unless they block understanding.

### Severity Levels

Use severity to help the team act.

- **P0** — Decision-breaking flaw. The artifact should not be used as-is.
- **P1** — High-priority weakness. The artifact may be usable after revision.
- **P2** — Medium issue. Important, but not immediately blocking.

### Why This Works

- raises the quality bar for PM deliverables
- prevents false confidence from polished artifacts
- teaches the team how to distinguish evidence from inference
- creates reusable review discipline instead of ad hoc opinion

### Anti-Patterns

- **Nitpick theater** — spending all review energy on wording instead of logic
- **Vibe review** — "this feels off" without naming the defect
- **Harsh without help** — identifying a problem but not the consequence or fix path
- **Everything-is-critical review** — no severity distinction, so nothing is actionable
- **Solution policing too early** — criticizing design detail when the actual problem statement is still broken

### When to Use This

- Before circulating a major product artifact
- Before stakeholder review
- Before design or engineering commitment
- After AI-generated outputs that look plausible but may be weak

### When NOT to Use This

- When the artifact is still just raw notes
- When you need editing or rewriting rather than review
- When the real blocker is missing source material, not document quality

## Application

Use `template.md` for the final review output.

### Step 1: Identify the Artifact Type and Its Job

State what you are reviewing:

- insight summary
- opportunity map
- solution direction
- PRD
- engineering breakdown
- roadmap
- review pack

Then name the artifact's intended job in one sentence.

Example:

"This is a PRD. Its job is to align product, design, and engineering on scope, rules, responsibilities, and validation before implementation."

Without this step, critique often becomes generic and unfair.

### Step 2: Extract the Core Claims

List the main claims the document is making.

Examples:

- this is the right problem to solve
- this is the right target user
- this opportunity is strategically important
- this solution is better than alternatives
- this scope is implementable in one release

If you cannot identify the core claims, the artifact may be too vague already.

### Step 3: Pressure-Test Across Review Dimensions

Review against the dimensions that most often break PM deliverables:

- evidence quality
- logic continuity
- problem/solution separation
- edition, role, and scenario fit
- scope and non-goals
- object, state, and permission clarity
- measurement and validation path
- execution readiness

Not every artifact needs equal emphasis on every dimension, but you should explicitly say which dimensions were most relevant.

### Step 4: Write Findings in a Structured Way

Each finding should include:

- **Problem** — what is wrong
- **Why it matters** — why this weakens the artifact
- **Consequence** — what decision or execution risk it creates
- **Fix** — how to repair it

This is the minimum bar for useful critique.

### Step 5: Separate Findings from Open Questions

Findings are defects you can point to.

Open questions are unresolved issues where more information is needed before judging.

Do not blur them together. Otherwise readers cannot tell what is broken versus what is merely unknown.

### Step 6: End with a Verdict

Use one of three verdicts:

- **Pass** — no major defects; usable with minor edits
- **Revise and Re-review** — promising, but important weaknesses remain
- **Do Not Use Yet** — decision quality is too weak to proceed

The verdict should match the findings. Do not write a mild conclusion after listing severe flaws.

## Examples

See `examples/sample.md`.

### Example of a Good Finding

> **P1 — The insight summary treats "dashboard" as the problem instead of a proposed solution.**
>
> **Why it matters:** This hides whether users actually need executive visibility, faster follow-up, or lower reporting effort.
>
> **Consequence:** The team may converge on a dashboard build without validating the underlying job.
>
> **Fix:** Rewrite the insight in problem language first, then compare dashboard versus in-context visibility versus proactive follow-up options.

Why this works:

- it names the defect precisely
- it explains the product consequence
- it does not confuse critique with rewriting
- it gives a concrete repair path

## Common Pitfalls

- Reviewing style before reviewing logic
- Calling evidence "weak" without saying what evidence is missing
- Treating every open question as a defect
- Forgetting to judge whether the artifact can support its intended next decision
- Writing a "balanced" verdict that ignores the actual severity of findings

## References

- `docs/WPS Demand-to-Decision Workflow.md`
- `docs/WPS PM Operating Guide.md`
- `../problem-statement/SKILL.md`
- `../recommendation-canvas/SKILL.md`
- `../wps-problem-opportunity-map/SKILL.md`
- `../wps-solution-evaluation/SKILL.md`
- `../prd-development/SKILL.md`
