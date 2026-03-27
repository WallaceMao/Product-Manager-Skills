---
name: customer-solution-narrative
description: Turn product capabilities into a customer-facing solution story for sales, marketing, and customer success. Use when internal product thinking must become external value communication.
intent: >-
  Create a customer-facing solution narrative that translates product strategy,
  problem understanding, and feature capabilities into business-language value
  for prospects and customers. Use this when product work must be packaged into
  a clear solution story that sales, marketing, customer success, or partners
  can reuse without relying on internal product jargon.
type: component
best_for:
  - "Turning internal product thinking into sales-ready solution messaging"
  - "Creating customer-facing value narratives from a PRD or feature direction"
  - "Helping GTM teams explain who a solution is for, why it matters, and how it lands"
scenarios:
  - "We have the product plan, now help me write the customer solution story"
  - "Sales needs a clear solution narrative for this new SaaS capability"
  - "Turn this feature direction into a customer-facing value proposition and rollout story"
estimated_time: "30-60 min"
---

## Purpose

Create a customer-facing solution narrative that explains:

- who this solution is for
- what business problem it addresses
- how it helps in the customer's real workflow
- why it is better than the customer's current approach
- what outcomes the customer should expect

This is not a PRD, a launch checklist, or a feature inventory. It is a translation layer between internal product understanding and external customer value communication.

## Key Concepts

### Product Solution vs Customer Solution

Internal product work answers:

- what are we building
- how does it behave
- what are the rules, states, and edge cases

Customer-facing solution work answers:

- what business problem is solved
- which customer should care
- what changes for them operationally
- what value they should expect
- how adoption and rollout should happen

Do not confuse these two artifacts. A strong PRD can still be useless to sales if it does not explain customer value in customer language.

### A Customer Solution Is Scenario-Based

Customers do not buy "task status signal aggregation" or "rule-based project health logic."

They buy outcomes like:

- fewer missed deadlines
- faster handoff across teams
- better visibility into execution risk
- lower coordination overhead

The solution story should stay anchored to scenarios, roles, and jobs-to-be-done.

### Value Must Be Specific, Not Puffy

Customer-facing solution writing often collapses into empty claims:

- "improve efficiency"
- "empower collaboration"
- "unlock productivity"

These are not yet value propositions. They are placeholders.

Translate value into operational or business consequences:

- reduce manual follow-up for team leads
- shorten project startup time for distributed teams
- make execution risk visible before weekly status meetings

### The GTM Audience Is Indirect

Often the first reader is not the buyer. It is:

- a sales rep
- a marketing manager
- a customer success manager
- a partner

So the artifact must be reusable. It should help non-product teams explain the solution consistently without needing the PM in every call.

### Good Solution Narratives Have Boundaries

A useful customer solution story says:

- who this is good for
- who it is not yet for
- what scope it covers
- what assumptions matter for success

Without boundaries, the narrative becomes overselling material instead of trustworthy positioning.

### Why This Works

- makes product value legible outside the product team
- helps GTM teams sell scenarios, not feature lists
- reduces internal/external message drift
- creates a reusable base for decks, one-pagers, enablement, and case studies

### Anti-Patterns

- **Feature brochure disguised as solution** — lists capabilities but no scenario or business value
- **Internal jargon leak** — uses PM or engineering language customers would never say
- **Everyone customer** — no clarity on segment, role, or readiness
- **Value inflation** — promises transformation without showing mechanism
- **No implementation reality** — sounds good, but gives GTM teams nothing on rollout, adoption, or fit

### When to Use This

- After a product direction is clear enough to explain externally
- When sales or marketing needs messaging for a new capability
- When customer success needs rollout framing or adoption guidance
- When a feature should be packaged as part of a bigger SaaS solution story

### When NOT to Use This

- Before the underlying problem is understood
- Before the product direction is stable enough to describe honestly
- As a substitute for detailed PRD or technical specification

## Application

Use `template.md` for the final artifact.

### Step 1: Start from Internal Product Truth

Gather the internal inputs first:

- problem statement
- target segment or persona
- product strategy
- feature design or solution direction
- PRD or capability outline
- known constraints and non-goals

If the internal material is still fuzzy, the customer solution narrative will become fluffy or misleading.

### Step 2: Define the Customer and Scenario

State clearly:

- which customer segment this is for
- which role feels the pain most
- what scenario triggers the need
- what current workaround or alternative exists today

This is where many "solution" docs fail. They jump to product description before the customer context is concrete.

### Step 3: Write the Problem in Customer Language

Do not copy the PRD wording blindly.

Translate into business-language pain:

- what slows the customer down
- what creates risk or waste
- what is hard to see, control, or scale

Ask: would a salesperson or customer success manager feel comfortable saying this aloud to a customer?

### Step 4: Translate Capability into Value Mechanism

Explain how the product helps, but do it through the customer's workflow:

- what changes in their day-to-day operation
- where friction is reduced
- where visibility improves
- where coordination becomes easier

Use feature detail only when it clarifies the mechanism of value.

### Step 5: Define Business Outcomes and Adoption Path

State:

- expected customer outcomes
- success indicators
- rollout or adoption path
- what conditions make this solution a good fit

This is what makes the document usable by GTM and customer-facing teams instead of merely inspirational.

### Step 6: Add Fit Boundaries and Objection Handling

Include:

- who is a strong fit
- who is not yet a fit
- likely objections or confusion points
- concise answers grounded in product reality

This protects the organization from overselling.

## Examples

See `examples/sample.md`.

### Example of a Good Solution Statement

"For growing cross-functional teams that struggle to spot execution risk before status meetings, this solution gives team leads in-context project health visibility so they can act earlier, reduce manual chasing, and keep execution moving without adding a separate reporting ritual."

Why this works:

- names the customer and scenario
- focuses on a real operational pain
- explains the value in workflow terms
- avoids pretending the feature solves every project-management problem

## Common Pitfalls

- Reusing PRD language without translating it for customers
- Leading with features before the business problem is clear
- Promising ROI without any believable mechanism
- Hiding fit limitations to make the message sound bigger
- Creating a narrative so generic that sales still cannot qualify customers

## References

- `../positioning-statement/SKILL.md`
- `../problem-statement/SKILL.md`
- `../jobs-to-be-done/SKILL.md`
- `../recommendation-canvas/SKILL.md`
- `../prd-development/SKILL.md`
- `../wps-feature-design/SKILL.md`
- `../wps-solution-evaluation/SKILL.md`
- `../wps-project-management-strategy/SKILL.md`
