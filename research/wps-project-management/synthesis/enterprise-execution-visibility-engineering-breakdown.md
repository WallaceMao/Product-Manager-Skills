# 企业版执行跟进与风险可见性 Engineering Breakdown

这份文档是 [`enterprise-execution-visibility-prd.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-prd.md) 的工程化补充。

它的目标不是替代 PRD，而是帮助产品、研发、测试更快进入实现协同，重点回答：

- MVP 到底做什么，不做什么
- 需要哪些对象、字段、状态和规则
- 前后端大致如何拆
- 事件和埋点应该落在哪里
- 哪些风险需要提前规避

---

## 1. Implementation Goal

第一阶段上线一个 **规则型项目健康摘要 + 风险任务清单 + 基础跟进行动入口** 的 MVP。

核心原则：

- 先解决“负责人看不见风险”的问题
- 先保证规则清晰、可解释
- 不在第一阶段引入复杂 AI 评分或跨项目大盘

---

## 2. MVP Scope

### In Scope

#### 项目健康摘要

- 在进行中项目详情页展示健康摘要
- 输出项目健康状态：
  - 正常
  - 关注中
  - 风险中
- 输出核心风险统计：
  - 逾期任务数
  - 被阻塞任务数
  - 无负责人任务数
  - 无截止时间任务数

#### 风险任务清单

- 展示风险任务列表
- 支持查看风险原因
- 支持按默认优先级排序

#### 基础跟进行动

- 发送提醒
- 修改负责人
- 修改截止时间
- 进入任务详情

#### 角色权限控制

- 项目 Owner：可查看 + 可操作
- 成员：仅查看与自己有关内容
- 管理者 / 观察者：只读摘要

#### 埋点

- 健康摘要曝光
- 风险清单点击
- 跟进行动触发

### Out of Scope

- AI 风险评分
- 跨项目健康驾驶舱
- 项目趋势分析
- 管理层全局大盘
- 自动批量催办策略
- 复杂规则配置中心

---

## 3. Functional Decomposition

### Module A: Health Summary Engine

职责：

- 读取项目和任务数据
- 根据规则计算项目健康状态
- 聚合核心风险统计

输出：

- `health_status`
- `risk_counts`
- `risk_reasons_summary`

### Module B: Risk Task List

职责：

- 拉取当前项目中的风险任务
- 为每个风险任务生成风险原因
- 返回排序后的风险列表

输出：

- 风险任务列表
- 每条任务的风险标签和风险原因

### Module C: Follow-up Actions

职责：

- 对风险任务执行负责人调整、截止时间调整、提醒动作
- 保证动作后状态可刷新

输出：

- 动作结果
- 更新后的任务状态
- 操作事件日志

### Module D: Permission Gate

职责：

- 根据用户角色判断可见内容和可执行动作

输出：

- 字段级或动作级权限结果

### Module E: Analytics / Event Tracking

职责：

- 记录健康视图相关关键行为

输出：

- 事件日志
- 用于后续产品验证的数据

---

## 4. Suggested Data Model Impact

这里不是最终数据库设计，而是产品实现所需的最小对象和字段清单。

### Project

关键字段建议：

- `project_id`
- `project_status`
- `project_owner_id`
- `project_health_status`
- `project_health_updated_at`

说明：

- `project_health_status` 第一阶段可以是计算结果，不一定要作为持久化字段保存
- 如果需要性能优化，可以考虑缓存或异步更新

### Task

关键字段建议：

- `task_id`
- `project_id`
- `task_status`
- `assignee_id`
- `due_at`
- `priority`
- `is_blocked`
- `blocked_reason`
- `completed_at`
- `archived_flag`

说明：

- 第一阶段健康判断高度依赖任务状态、负责人、截止时间
- 如果这些字段历史上不稳定，必须先做数据质量评估

### Reminder / Follow-up Action

关键字段建议：

- `action_id`
- `task_id`
- `action_type`
  - `notify`
  - `reassign`
  - `change_due_date`
- `operator_id`
- `target_user_id`
- `created_at`

### Permission Context

关键字段建议：

- `viewer_user_id`
- `viewer_role_in_project`
- `can_view_health_summary`
- `can_trigger_followup_action`

---

## 5. Health Rule Set v1

第一阶段建议用可解释规则，不做复杂打分。

### Rule Group A: Task-Level Risk Detection

#### Risk Type 1: Overdue

触发条件：

- 任务未完成
- 当前时间晚于 `due_at`

输出：

- `risk_type = overdue`

#### Risk Type 2: Blocked

触发条件：

- `is_blocked = true`

输出：

- `risk_type = blocked`

#### Risk Type 3: Missing Assignee

触发条件：

- `assignee_id` 为空

输出：

- `risk_type = missing_assignee`

#### Risk Type 4: Missing Due Date

触发条件：

- `due_at` 为空

输出：

- `risk_type = missing_due_date`

#### Risk Type 5: Near Deadline

触发条件建议：

- 未完成
- 距 `due_at` 少于约定阈值，例如 24 小时 / 48 小时 / 3 天

输出：

- `risk_type = near_deadline`

### Rule Group B: Project-Level Health State

第一阶段建议采用简单聚合逻辑：

- **正常**
  - 无高风险项，或仅少量低风险项
- **关注中**
  - 存在一定数量的风险任务，但尚未到严重程度
- **风险中**
  - 存在逾期、阻塞或关键风险任务达到阈值

注意：

- 阈值需要产品和研发联合定义
- 第一阶段不要追求过度精细
- 最重要的是让用户理解为什么是这个状态

---

## 6. Suggested API / Service Shape

这里不绑定具体技术栈，只定义能力边界。

### Read APIs

#### 1. 获取项目健康摘要

建议能力：

- 输入：`project_id`, `viewer_user_id`
- 输出：
  - 项目健康状态
  - 风险统计
  - 风险原因摘要

#### 2. 获取风险任务清单

建议能力：

- 输入：`project_id`, `viewer_user_id`, `filter`, `sort`
- 输出：
  - 风险任务列表
  - 每条任务的风险原因
  - 可执行动作列表

### Write APIs

#### 3. 对风险任务发起提醒

- 输入：`task_id`, `operator_id`
- 输出：动作执行结果

#### 4. 修改负责人

- 输入：`task_id`, `new_assignee_id`, `operator_id`
- 输出：任务更新结果

#### 5. 修改截止时间

- 输入：`task_id`, `new_due_at`, `operator_id`
- 输出：任务更新结果

### Internal Services

建议至少拆出：

- 健康计算服务
- 风险任务筛选服务
- 权限校验服务
- 埋点记录服务

---

## 7. Frontend Breakdown

### Page Placement

第一阶段建议直接落在项目详情页，不新增独立全局页面。

### UI Blocks

#### Block 1: Health Summary Card

展示：

- 当前健康状态
- 风险概览
- 风险数量

#### Block 2: Risk Task List

展示：

- 风险任务
- 风险原因
- 截止时间
- 负责人
- 快捷操作

#### Block 3: Follow-up Action Feedback

展示：

- 动作结果提示
- 成功 / 失败反馈

### Frontend Interaction Notes

- 负责人进入项目后应尽快看到健康信息
- 不要把风险视图藏得太深
- 风险项操作后应局部刷新，而不是整页重载

---

## 8. Event and Analytics Breakdown

建议事件：

- `project_health_view_opened`
  - 用户打开项目健康摘要
- `risk_task_list_viewed`
  - 用户查看风险任务列表
- `risk_signal_clicked`
  - 用户点击具体风险原因或风险任务
- `followup_action_triggered`
  - 用户执行跟进动作
- `followup_action_succeeded`
  - 跟进行动成功
- `followup_action_failed`
  - 跟进行动失败

建议事件属性：

- `project_id`
- `task_id`（如果适用）
- `viewer_role`
- `risk_type`
- `action_type`
- `health_status_before`
- `health_status_after`（后续如可获取）

---

## 9. Delivery Slices

### Slice 1: Read-Only MVP

内容：

- 项目健康摘要
- 风险任务列表
- 风险原因展示

价值：

- 先验证“负责人是否愿意看、是否觉得有用”

### Slice 2: Actionable MVP

内容：

- 在 Slice 1 基础上增加跟进行动：
  - 提醒
  - 改负责人
  - 改截止时间

价值：

- 验证“看见风险后，是否会立刻动作”

### Slice 3: Signal Optimization

内容：

- 调整规则阈值
- 优化风险排序
- 补更多风险原因解释

价值：

- 提升准确性和信任度

---

## 10. Engineering Risks

### Risk 1: Task Data Quality Is Not Reliable

影响：

- 健康摘要失真
- 用户快速失去信任

建议：

- 上线前先抽样检查任务字段完整性
- 先只使用最稳定字段做规则判断

### Risk 2: Permission Model Is Incomplete

影响：

- 管理者和成员可能看到不该看到的信息
- 跟进行动可能越权

建议：

- 第一阶段先严格收敛角色能力
- 不清楚的权限场景先默认保守

### Risk 3: Follow-up Action Coupling Too Deep

影响：

- 前端体验卡顿
- 改一个动作牵动多个旧接口

建议：

- 动作能力先收敛在少数几个高价值动作
- 动作后刷新逻辑尽量局部化

### Risk 4: Product Tries to Solve Too Much at Once

影响：

- 范围膨胀
- 交付延迟
- 验证失焦

建议：

- 坚持先做项目内可解释 MVP
- 驾驶舱、AI 评分、跨项目管理全部放后面

---

## 11. Suggested Engineering Questions for Review

- 当前任务对象是否已经稳定支持逾期、阻塞、负责人缺失、截止时间缺失等判断？
- 项目详情页现有架构是否适合增加健康摘要与风险列表？
- 跟进行动是否可以走现有任务编辑能力，还是需要新接口封装？
- 风险计算更适合实时计算、缓存计算，还是异步聚合？
- 现有权限模型是否能稳定区分 Owner、成员、观察者？

---

## 12. Recommended Next Step

如果要继续推进到研发评审，下一步建议补两样内容：

1. 一份更细的字段 / 状态 / 阈值定义表
2. 一组可以直接进入开发排期的 user stories 与测试用例

这样这条能力就能从产品判断，继续收敛到实现排期层。
