# Sample: WPS Project Management PRD

```markdown
# Project Health View PRD

## 2. Edition and Scenario Context
- Edition: Enterprise
- Primary role: Team lead
- Collaborating roles: team members, manager
- Core scenario: active project execution

## 3. Problem Statement
Team leads cannot see execution risk early enough without manually chasing updates across chat, meetings, and project pages.

## 6. Roles, Permissions, and Object Model
- Roles involved: team lead, member, manager
- Permission rules:
  - team lead can update project-level health settings
  - manager can view summary but not edit task assignments
- Affected objects: project, task, task status, reminder signal
- State transitions:
  - task becomes overdue
  - project health becomes at risk

## 9. Metrics and Instrumentation
- Primary metric: weekly active projects with health-view usage
- Guardrail metric: additional workflow time per project owner
- Events to track:
  - health_view_opened
  - risk_signal_clicked
  - followup_action_taken
```
