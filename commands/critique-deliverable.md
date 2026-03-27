---
name: critique-deliverable
description: Critically review a product artifact and return severity-ranked findings, open questions, and a verdict.
argument-hint: "<artifact type, purpose, and content or file path>"
uses:
  - product-deliverable-critique
outputs:
  - Severity-ranked findings
  - Open questions
  - Pass / revise / do-not-use verdict
---

# /critique-deliverable

Pressure-test a product artifact before you trust it.

## Invocation

```text
/critique-deliverable Review this PRD for evidence gaps, scope creep, and execution ambiguity before engineering review
```

## Workflow

1. Identify the artifact type and the decision it is supposed to support.
2. Extract the artifact's main claims.
3. Critique the deliverable with `product-deliverable-critique`.
4. Return findings first, then open questions, then a verdict.

## Checkpoints

- Prioritize logic, evidence, and execution risk over cosmetic edits.
- Do not confuse open questions with confirmed defects.
- Use severity levels so the review can drive action.
- If the artifact is mostly sound, say so explicitly and name only the residual risks.

## Next Steps

- Revise the artifact and run `/critique-deliverable` again.
- If the critique reveals a broken problem statement, run `/discover` or the relevant problem-framing skill before refining the solution.
