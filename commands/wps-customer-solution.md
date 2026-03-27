---
name: wps-customer-solution
description: Turn a WPS Project Management product capability into a customer-facing solution story for sales, marketing, and customer success.
argument-hint: "<WPS capability, target customer, and scenario>"
uses:
  - wps-project-management-strategy
  - wps-feature-design
  - customer-solution-narrative
outputs:
  - Customer-facing solution narrative
  - Best-fit customer and scenario framing
  - Adoption, rollout, and objection-handling story
---

# /wps-customer-solution

Translate WPS Project Management product work into a reusable customer solution story.

## Invocation

```text
/wps-customer-solution Enterprise execution visibility for team leads who struggle to spot project risk before weekly reviews
```

## Workflow

1. Confirm the edition, target segment, and scenario with `wps-project-management-strategy`.
2. Clarify the product capability shape and workflow impact with `wps-feature-design`.
3. Turn the internal product truth into customer-facing value communication with `customer-solution-narrative`.

## Checkpoints

- Do not reuse PRD language without translating it into customer language.
- Anchor the story to a real buyer, user, and scenario instead of generic "efficiency" claims.
- Make fit boundaries explicit so sales and customer success do not oversell.
- End with value, rollout guidance, and likely objections, not just feature bullets.

## Next Steps

- Pair this output with `/wps-write-prd` if internal product and external customer narratives need to stay aligned.
- Convert the narrative into a one-pager, sales deck section, or customer enablement brief.
