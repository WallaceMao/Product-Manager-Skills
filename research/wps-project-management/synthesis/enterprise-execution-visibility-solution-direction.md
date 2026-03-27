# Enterprise Execution Visibility Solution Direction

这份文档基于 [`top-opportunities.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/top-opportunities.md) 中的 `Opportunity 1：企业版执行跟进与风险可见性`，按照 `wps-design-solution` 的工作流产出第一版方案方向。

目标不是直接写 PRD，而是先把问题、方案骨架和推荐方向写清楚，方便后续进入 [`wps-project-management-prd`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-prd/SKILL.md)。

---

## 1. Problem and Opportunity Summary

### Opportunity Name

企业版执行跟进与风险可见性

### Edition

Enterprise

### Primary Role

- 团队负责人 / 项目 Owner
- 次要相关角色：项目成员、管理者 / 观察者

### Core Scenario

项目已启动并进入执行阶段，负责人需要快速知道：

- 哪些任务在按计划推进
- 哪些任务已经逾期或存在风险
- 哪些责任人需要跟进
- 当前项目整体健康度如何

### Problem Statement

团队负责人无法低成本地看见项目当前是否在按计划推进，往往需要通过开会、催问、手工更新台账等方式获取状态，导致风险暴露过晚、管理成本过高，项目状态对管理者也缺乏可见性。

### Why This Opportunity Matters

- 这是企业版最核心的执行价值之一
- 它直接决定产品是否只是“记录工具”，还是“团队执行系统”
- 它和企业版协作深度、团队留存、管理可见性高度相关

### Evidence Snapshot

- 高频一级类目：`项目与任务管理`
- 高频二级类目：
  - 项目台账管理
  - 项目进度跟踪
  - 甘特图与排期可视化
  - 项目计划管理
- 代表性需求：
  - “战略任务分解及每周跟进”
  - “项目进度、质量、安全、费用管理”
  - “项目时间节点提醒，建议是一个日历，通过日历标注项目时间节点，并设置提醒”
  - “软件公司项目进度、员工任务工作分解、员工任务完成进度考核”

### Non-Goal Reminder

这个机会的本质不是“补一个甘特图”或“加一个报表页面”，而是解决负责人在执行阶段的判断成本和跟进成本。

---

## 2. WPS Feature Design

## 1. Feature Context

- Feature name: 企业项目健康视图与风险摘要
- Edition: Enterprise
- Primary role: 团队负责人 / 项目 Owner
- Core scenario: 执行跟进
- Trigger:
  - 负责人打开一个进行中的项目
  - 负责人需要做周跟进 / 周汇报
  - 负责人想快速识别风险任务和责任人

## 2. User Goal

- Primary job:
  负责人希望在不反复问人、不手工维护复杂台账的前提下，快速判断项目当前是否健康，并知道下一步该跟进哪里。
- Success from the user's perspective:
  我能在短时间内看见项目整体状态、风险来源和待跟进对象，并据此采取行动。

## 3. Main Task Flow

1. 负责人进入进行中的项目
2. 系统展示项目健康摘要：
   - 任务完成情况
   - 逾期 / 临期风险
   - 阻塞任务
   - 无负责人任务
   - 高风险责任人或环节
3. 负责人点击风险点查看详情
4. 负责人执行跟进动作：
   - 提醒
   - 重新分配
   - 调整时间
   - 标记需要同步
5. 系统记录项目健康状态，并为后续汇报或复盘提供依据

## 4. Roles and Collaboration

| Role | What they do | What they need to see | Permission concerns |
| --- | --- | --- | --- |
| 团队负责人 / 项目 Owner | 判断项目健康并做跟进动作 | 项目整体健康、风险任务、责任人状态 | 可查看全部项目任务，可做提醒和调整 |
| 项目成员 | 更新自己负责的任务状态 | 与自己相关的任务和提醒 | 不应默认看到所有管理视图 |
| 管理者 / 观察者 | 了解项目整体状态和风险 | 汇总状态、关键风险、趋势信息 | 更多偏只读，不应直接改任务细节 |

## 5. Objects and States

| Object | Key states | Important transitions | Notes |
| --- | --- | --- | --- |
| 项目 | 正常、关注中、风险中 | 风险累积后从正常变为关注中或风险中 | 项目健康不是手工标签，应有规则支持 |
| 任务 | 未开始、进行中、已完成、已逾期、被阻塞 | 到期未完成、被标记阻塞、重新分配 | 风险判断高度依赖任务状态质量 |
| 负责人 | 正常推进、待跟进、风险聚集 | 多个任务逾期或阻塞时进入待跟进态 | 仅作为管理提示，不应演变为绩效系统 |
| 提醒 / 跟进动作 | 待触发、已触发、已处理 | 负责人发起提醒或系统生成提醒 | 需避免提醒泛滥 |

## 6. Rules and Edge Cases

- Rule 1：没有负责人或没有截止时间的任务，应被视为管理风险而非普通任务
- Rule 2：逾期任务不等于高风险任务，需结合优先级、依赖关系、项目阶段判断
- Rule 3：阻塞任务应要求记录阻塞原因，否则健康判断会失真
- Edge case 1：成员长期不更新状态，系统会误判项目健康
- Edge case 2：一个项目中存在大量低优先级历史任务，可能污染风险信号
- Edge case 3：管理者需要汇总视图，但不应默认获得编辑权限
- Edge case 4：提醒过多会让用户把系统当噪音源

## 7. Instrumentation

- Primary metric:
  - 使用企业项目健康视图的活跃项目数
- Guardrail metric:
  - 项目负责人为维护状态额外花费的操作成本
- Key events:
  - `project_health_view_opened`
  - `risk_signal_clicked`
  - `followup_action_triggered`
  - `task_blocked_marked`
  - `owner_reassigned`

## 8. Release Risk

- Main risk:
  - 风险信号质量不够高，导致负责人不信任
- Mitigation:
  - 第一阶段先从简单、可解释的规则开始，不一开始做复杂健康评分
- Rollout note:
  - 先在企业版中限定为“进行中项目 + 团队负责人可见”的 MVP 范围

---

## 3. WPS Solution Evaluation

## 1. Decision Context

- Problem:
  负责人看不清项目风险，需要高成本人工跟进
- Edition:
  Enterprise
- User role:
  团队负责人 / 项目 Owner
- Scenario:
  执行跟进
- Decision needed:
  企业版应该用什么方案形态先解决“执行可见性”问题

## 2. Options

### Option A: 独立项目驾驶舱 / 仪表盘

- Summary:
  提供一个独立的项目驾驶舱页面，集中展示项目状态、任务分布、逾期情况和关键指标
- Assumptions:
  用户愿意主动进入一个独立视图看项目状态
- Scope boundary:
  偏展示和汇总，不强调直接跟进行动

### Option B: 项目内健康摘要 + 风险清单

- Summary:
  在项目详情页内直接提供项目健康摘要、风险任务列表和可执行跟进行动，让负责人在原场景中看见风险并处理
- Assumptions:
  用户更愿意在项目上下文中完成判断和跟进，而不是跳到单独报表页
- Scope boundary:
  先聚焦单项目和负责人视角，不一开始做全局管理中心

### Option C: 主动风险提醒 / 跟进收件箱

- Summary:
  通过提醒、待办、消息或 AI 摘要主动告诉负责人哪些项目存在风险，并提供跟进入口
- Assumptions:
  主动触达比用户主动查看更能形成执行节奏
- Scope boundary:
  更强调“提醒”和“跟进入口”，弱化完整项目状态页

## 3. Comparison Table

| Option | User Value | Strategic Fit | Complexity | Collaboration Cost | Risk | Validation Path | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 中 | 中 | 中 | 低 | 中 | 中 | 容易沦为被动报表页，和“执行系统”价值距离较远 |
| B | 高 | 高 | 中 | 低 | 中 | 高 | 最贴近负责人真实任务流，也最容易与后续动作联动 |
| C | 中高 | 高 | 中高 | 中 | 高 | 中 | 很有潜力，但前提是风险判断足够准，否则容易沦为噪音提醒 |

## 4. Tradeoffs

- What Option A does better
  - 更适合做汇总展示
  - 更容易被管理者理解为“看状态的地方”
- What Option B does better
  - 最贴近负责人日常工作流
  - 更适合把“看见风险”直接转成“采取行动”
  - 更符合企业版作为执行系统的方向
- What Option C does better
  - 更有机会建立持续的执行节奏
  - 如果风险识别做得好，长期价值很强
- What each option sacrifices
  - A 牺牲行动闭环
  - B 牺牲跨项目管理视角
  - C 牺牲可解释性和前期落地稳定性

## 5. Recommendation

- Recommended option:
  **Option B：项目内健康摘要 + 风险清单**
- Why it wins:
  - 它最符合当前机会的核心问题，不是“有没有一个报表”，而是“负责人能不能低成本看见并处理风险”
  - 它嵌在项目上下文里，使用门槛更低
  - 它更容易和后续提醒、状态更新、重新分配等动作形成闭环
  - 它比独立驾驶舱更像执行工具，而不是被动可视化工具
- Conditions that would change the recommendation:
  - 如果后续发现负责人真正需要的是跨项目管理视角，Option A 需要补强
  - 如果后续验证主动提醒对留存和使用频率帮助更大，Option C 可以作为第二阶段能力

## 6. Next Validation Step

- What to test:
  - 负责人是否更愿意使用项目内的健康摘要，而不是单独报表
  - 哪些风险信号最值得优先展示：
    - 逾期任务
    - 无负责人任务
    - 被阻塞任务
    - 临期关键节点
  - 负责人看到风险后最常见的下一步动作是什么
- What evidence would confirm or reject the choice:
  - Confirm:
    - 负责人能在更短时间内识别项目风险
    - 负责人有明显后续动作（提醒、重分配、改时间）
    - 项目活跃跟进频次提升
  - Reject:
    - 负责人认为健康信号不可信
    - 负责人仍需要回到 Excel / 群聊 / 手工台账
    - 视图打开率高但跟进行动率低

---

## 4. Suggested MVP Scope

第一阶段建议只做可解释、可验证、低复杂度的 MVP。

### In Scope

- 项目内健康摘要
- 风险任务列表
- 明确的风险来源说明
- 基础跟进行动入口
  - 提醒责任人
  - 查看风险任务
  - 调整负责人 / 时间

### Out of Scope

- 复杂 AI 风险评分
- 跨项目统一驾驶舱
- 高级报表中心
- 过多自动提醒策略
- 管理层专属大屏

---

## 5. Why This Is the Right First Bet

这条方案方向有三个优点：

1. **问题贴合度高**  
   它直接瞄准“负责人看不清风险、跟进成本高”的核心问题。

2. **战略一致性强**  
   它强化的是企业版“执行系统”价值，而不是把产品带偏成报表工具。

3. **验证成本可控**  
   可以先用规则型健康信号做 MVP，不需要一开始就依赖复杂 AI 判断。

---

## 6. Next Step

如果继续推进，下一步应直接进入 [`wps-project-management-prd`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-prd/SKILL.md)，把这份方案方向收敛成正式 PRD，重点写清：

- edition 边界
- 角色和权限
- 对象模型和状态规则
- 健康信号定义
- 埋点与发布计划
