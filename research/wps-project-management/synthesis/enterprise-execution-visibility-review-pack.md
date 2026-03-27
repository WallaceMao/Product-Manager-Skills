# 企业版执行跟进与风险可见性 Review Pack

这份文档用于内部评审会快速对齐 `企业版执行跟进与风险可见性` 这条能力。

它压缩整合了以下材料：

- [`enterprise-execution-visibility-solution-direction.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-solution-direction.md)
- [`enterprise-execution-visibility-prd.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-prd.md)
- [`enterprise-execution-visibility-engineering-breakdown.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-engineering-breakdown.md)
- [`enterprise-execution-visibility-user-stories.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-user-stories.md)
- [`enterprise-execution-visibility-test-matrix.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-test-matrix.md)
- [`enterprise-execution-visibility-api-field-spec.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-api-field-spec.md)

目标不是替代原始文档，而是给评审参与者一份可以快速阅读、快速提问、快速做决策的版本。

---

## 1. Decision Summary

### 本次要评审什么

在 Enterprise 版 `WPS 项目管理` 中，为项目负责人提供：

- 项目健康摘要
- 风险任务清单
- 基础跟进行动入口

### 本次要做的决策

1. 这条能力是否值得作为近期企业版重点 bet 推进
2. 第一阶段是否采用“项目内健康摘要 + 风险清单”的方案形态
3. 第一阶段 MVP 范围是否合理
4. 是否具备进入研发排期的前提

### 当前建议结论

- **建议推进**
- **建议采用项目内方案，而不是独立驾驶舱**
- **建议以规则型、可解释的 MVP 起步**

---

## 2. Why This Matters

### 背景问题

企业版中，项目负责人在执行阶段看不清项目是否健康，通常要靠：

- 群聊追问
- 开会同步
- 手工台账
- 反复催人

这导致：

- 风险暴露晚
- 跟进成本高
- 产品价值停留在“记录”而不是“执行推进”

### 为什么是现在

- 在需求分析中，这类问题是企业版最强机会之一
- 它比复杂行业化需求更接近产品共性底座
- 它直接关系企业版留存和团队执行价值

### 为什么不是别的方向先做

- 不是先做大报表中心
- 不是先做跨项目驾驶舱
- 不是先上复杂 AI 风险评分

因为当前第一性问题是：

**负责人能不能在项目上下文里低成本看见风险并采取行动。**

---

## 3. User and Scenario

### Primary User

- 团队负责人 / 项目 Owner

### Secondary Roles

- 项目成员
- 管理者 / 观察者

### Core Scenario

项目进入执行阶段后，负责人需要快速判断：

- 当前项目是否健康
- 哪些任务存在风险
- 哪些责任人需要跟进
- 下一步该采取什么动作

### Out of Scope

- 项目创建与启动
- 跨项目组合管理
- 复杂经营报表
- 绩效管理

---

## 4. Proposed Solution

### 方案一句话

在项目详情页中增加一套 **健康摘要 + 风险任务清单 + 快捷跟进行动** 的能力，让负责人在原工作流中完成“发现风险 -> 采取动作”。

### 方案结构

#### 模块 1：项目健康摘要

展示：

- 健康状态
- 风险统计
- 风险来源概览

#### 模块 2：风险任务清单

展示：

- 风险任务
- 风险原因
- 负责人
- 截止时间
- 快捷操作

#### 模块 3：跟进行动入口

支持：

- 发送提醒
- 修改负责人
- 修改截止时间
- 打开任务详情

### 为什么推荐这个方案

- 最贴近负责人真实任务流
- 最容易形成“看见风险 -> 动作”的闭环
- 更符合企业版执行系统定位
- 验证成本低于驾驶舱或复杂 AI 方案

---

## 5. MVP Scope

### In Scope

- 进行中项目的健康摘要
- 风险任务清单
- 规则型风险判断
- 3 个基础跟进行动
- 角色权限控制
- 基础埋点

### Out of Scope

- AI 风险评分
- 跨项目统一视图
- 高级报表
- 自动批量催办
- 复杂配置中心

### 建议切片

#### Slice 1：只读 MVP

- 健康摘要
- 风险任务清单
- 风险原因解释
- 角色可见性控制

#### Slice 2：可操作 MVP

- 提醒
- 改负责人
- 改截止时间
- 动作结果反馈

#### Slice 3：信号优化

- 风险排序优化
- 去重优化
- 阈值优化

---

## 6. Product Rules at a Glance

### 风险类型 v1

- 逾期任务
- 被阻塞任务
- 无负责人任务
- 无截止时间任务
- 临近关键节点任务

### 健康状态 v1

- `normal`
- `attention`
- `at_risk`

### 核心原则

- 状态必须可解释
- 一个任务可命中多个风险，但列表中只展示一次
- 已完成任务、归档任务不进入当前风险判断

---

## 7. Role and Permission Summary

| Role | Can View Summary | Can View Risk List | Can Trigger Action |
| --- | --- | --- | --- |
| 项目负责人 | Yes | Yes | Yes |
| 项目成员 | Limited | Limited | No |
| 管理者 / 观察者 | Yes | Summary-first / restricted | No |

需要评审确认：

- 成员到底能看到多深
- 管理者能看到摘要还是也能下钻到任务

---

## 8. Engineering Impact Summary

### 需要的主要模块

- 健康计算模块
- 风险任务筛选模块
- 跟进行动模块
- 权限校验模块
- 埋点模块

### 关键对象 / 字段

- Project
  - `project_status`
  - `project_health_status`
- Task
  - `task_status`
  - `assignee_id`
  - `due_at`
  - `is_blocked`
  - `blocked_reason`
- Risk Item
  - `risk_types`
  - `risk_reason_texts`
  - `severity`

### 工程主要风险

- 任务数据质量不稳定
- 权限模型边界不清
- 动作接口耦合过深
- 范围膨胀

---

## 9. Validation and Metrics

### Primary Metric

- 使用项目健康摘要的活跃项目数

### Guardrails

- 负责人额外状态维护成本是否上升
- 跟进行动触发率是否足够
- 用户是否认为风险判断不可信

### 关键事件

- `project_health_view_opened`
- `risk_signal_clicked`
- `followup_action_triggered`

### 本次最关键要验证什么

1. 负责人是否真的会用这个视图
2. 看见风险后是否真的会采取动作
3. 这个能力是否减少了人工追问和手工台账依赖

---

## 10. Test Focus

P0 建议重点覆盖：

- 健康摘要展示
- 风险任务识别
- 已完成 / 已归档任务过滤
- 提醒 / 改负责人 / 改截止时间
- 权限隔离
- 动作失败反馈

---

## 11. Open Questions for Review

建议评审会重点讨论下面这些问题：

### 产品问题

- 第一阶段是否只做项目内能力，不做跨项目视图？
- 管理者视角到底要到什么深度？
- “临近关键节点”在第一阶段是否必须做？

### 研发问题

- 当前任务对象是否足够支持规则判断？
- 风险计算更适合实时算还是异步聚合？
- 现有任务编辑能力能否直接支撑 3 个跟进行动？

### 测试问题

- 哪些任务状态最容易出现脏数据？
- 角色权限测试账号如何准备？
- 埋点校验如何纳入验收？

---

## 12. Recommended Decision

### 建议本次会后达成的结论

1. 立项推进这条能力
2. 采用“项目内健康摘要 + 风险任务清单”作为第一阶段形态
3. 第一阶段坚持规则型、可解释方案
4. 按 `只读 MVP -> 可操作 MVP -> 信号优化` 切片推进

### 如果不推进，最可能的代价

- 企业版继续停留在“记录工具”认知
- 团队负责人核心痛点得不到解决
- 企业版高价值执行场景缺乏清晰 bet

---

## 13. Meeting Output Template

评审会结束后，建议至少记录：

- **结论：** 通过 / 修改后通过 / 暂缓
- **范围调整：**
- **关键争议点：**
- **研发前置项：**
- **测试前置项：**
- **下一步负责人：**
- **计划时间：**
