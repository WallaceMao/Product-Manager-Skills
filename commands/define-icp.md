---
name: define-icp
description: Define an ideal customer profile by connecting the problem, user context, customer environment, and fit signals.
argument-hint: "<product or solution, target user, and customer context>"
uses:
  - problem-statement
  - proto-persona
  - ideal-customer-profile
outputs:
  - Ideal customer profile brief
  - Strong-fit, medium-fit, and poor-fit customer definitions
  - Qualification and disqualification cues
---

# /define-icp

Define which customers are actually worth targeting, not just which users can feel the pain.

## Invocation

```text
/define-icp Enterprise execution visibility for project owners in multi-team delivery environments
```

## Workflow

1. Clarify the underlying customer problem with `problem-statement`.
2. Confirm the user-side context with `proto-persona`.
3. Build the account-level fit logic with `ideal-customer-profile`.

## Checkpoints

- Separate user role from customer environment.
- Include buying reality and implementation readiness, not just problem intensity.
- Explicitly define poor-fit customers and false-positive demand signals.
- End with qualification cues that sales, product, and customer success can all use.

## Next Steps

- Run `/strategy` if ICP choices should influence broader product focus.
- Run `/wps-customer-solution` or customer-facing solution work once the target customer is clear.
