# Sample: WPS Feature Design

```markdown
# WPS Feature Design

## 1. Feature Context
- Feature name: Project health view
- Edition: Enterprise
- Primary role: Team lead
- Core scenario: Ongoing project execution
- Trigger: Team lead opens an active project and needs quick status understanding

## 2. User Goal
- Primary job: Detect which tasks or owners are creating execution risk without manual follow-up
- Success from the user's perspective: I can see where the project is slipping in under 30 seconds

## 3. Main Task Flow
1. Team lead opens project
2. System summarizes task status and risk signals
3. Lead drills into blocked or overdue work
4. Lead follows up or reassigns
5. Project health view updates over time

## 4. Roles and Collaboration
| Role | What they do | What they need to see | Permission concerns |
| --- | --- | --- | --- |
| Team lead | Monitors and acts | risk signals, owner status | edit access |
| Member | Updates own work | assigned tasks, status prompts | cannot change project rules |
| Manager | Reviews progress | summary only | may be view-only |

## 5. Objects and States
| Object | Key states | Important transitions | Notes |
| --- | --- | --- | --- |
| Task | not started, in progress, blocked, done, overdue | status updates, due date changes | blocked state needs explicit reason |
```
