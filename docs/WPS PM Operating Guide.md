# WPS PM Operating Guide

这份指南告诉 `WPS 项目管理 / 日事清` 产品团队，如何使用本仓库中的 WPS 专属 `skills` 和 `commands` 来支撑日常产品工作。

目标不是“多一个模板库”，而是形成一套稳定的工作方式：

- 先沉淀事实
- 再做判断
- 再出方案
- 再写 PRD
- 再做季度规划

如果你想看一条真实跑通过的完整路径，从原始需求分析一直走到方案、PRD、工程拆解和评审包，请直接看：

- [`WPS Demand-to-Decision Workflow.md`](/Users/sihuo/workspace/Product-Manager-Skills/docs/WPS%20Demand-to-Decision%20Workflow.md)
- [`WPS Skill Map.md`](/Users/sihuo/workspace/Product-Manager-Skills/docs/WPS%20Skill%20Map.md)

---

## 这套体系解决什么问题

团队在做产品工作时，最常见的混乱通常不是“不会写文档”，而是下面这些：

- 研究资料很多，但没人知道哪些是真的有用
- 需求很多，但没有清晰的问题地图
- 方案很多，但比较方式不一致
- PRD 能写出来，但经常缺上下文、缺边界、缺验证计划
- 路线图总在收需求，而不是在表达战略

这套 WPS PM skill/command 体系，就是为了解决这些问题。

一句话说：

**`research/` 沉淀事实，`skills/` 沉淀方法，`commands/` 负责把工作流串起来。**

---

## 先理解三层结构

### 1. `research/`

这是产品上下文底座，放的是事实，不是结论。

当前重点目录：

- [`research/wps-project-management/00-product-overview.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/00-product-overview.md)
- [`research/wps-project-management/01-strategy-context.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/01-strategy-context.md)
- [`research/wps-project-management/02-user-segments.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/02-user-segments.md)
- [`research/wps-project-management/03-core-scenarios.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/03-core-scenarios.md)
- [`research/wps-project-management/04-competitive-landscape.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/04-competitive-landscape.md)
- [`research/wps-project-management/05-success-metrics.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/05-success-metrics.md)
- [`research/wps-project-management/06-feature-history.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/06-feature-history.md)
- [`research/wps-project-management/07-domain-terminology.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/07-domain-terminology.md)
- [`research/wps-project-management/08-constraints-and-assumptions.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/08-constraints-and-assumptions.md)

规则很简单：

- 这里写事实、历史、数据、定义、假设
- 不在这里写“应该做什么”

### 2. `skills/`

这是单项能力层，用来解决一种稳定、可重复的 PM 问题。

WPS 专属 skill：

- [`wps-project-management-strategy`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-strategy/SKILL.md)
- [`wps-problem-opportunity-map`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-problem-opportunity-map/SKILL.md)
- [`wps-feature-design`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-feature-design/SKILL.md)
- [`wps-solution-evaluation`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-solution-evaluation/SKILL.md)
- [`wps-project-management-prd`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-prd/SKILL.md)
- [`wps-quarter-roadmap`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-quarter-roadmap/SKILL.md)

### 3. `commands/`

这是工作流层，用来把多个 skill 串起来。

WPS 专属 command：

- [`wps-strategy`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-strategy.md)
- [`wps-design-solution`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-design-solution.md)
- [`wps-write-prd`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-write-prd.md)
- [`wps-quarter-planning`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-quarter-planning.md)

---

## 什么时候用 skill，什么时候用 command

简单规则：

- **你已经知道自己要产出什么单一文档或判断**：用 `skill`
- **你要跑完一段完整工作流**：用 `command`

例子：

- “我要写一份 WPS 项目管理 PRD”  
  用 [`wps-project-management-prd`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-prd/SKILL.md)

- “我现在有一堆需求，想从问题到方案再到推荐方向”  
  用 [`wps-design-solution`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-design-solution.md)

- “我们要做下季度方向规划”  
  用 [`wps-quarter-planning`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-quarter-planning.md)

---

## 团队默认工作流

这是建议团队默认采用的工作顺序。

### 场景 1：做战略判断

适合问题：

- 个人版和企业版这季度到底先做谁
- 我们当前要打哪些场景
- WPS 项目管理到底要占据 WPS 生态中的哪一层价值

推荐流程：

1. 先更新研究底稿
   - `00-product-overview`
   - `01-strategy-context`
   - `02-user-segments`
   - `03-core-scenarios`
2. 跑 [`wps-strategy`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-strategy.md)
3. 输出：
   - 战略问题定义
   - 当前阶段主战场
   - 差异化方向
   - 非目标

### 场景 2：做需求梳理和方案设计

适合问题：

- 我们收到了很多用户需求，到底该做什么
- 某个场景要怎么设计
- 多个方案之间怎么选

推荐流程：

1. 把需求清单、访谈、反馈先整理进 `research/`
2. 跑 [`wps-design-solution`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-design-solution.md)
3. 输出：
   - 问题/机会地图
   - 设计骨架
   - 方案对比
   - 推荐方向

### 场景 3：写 PRD

适合问题：

- 方案已经基本定了，要进入研发协同
- 需要明确角色、状态、对象模型和指标

推荐流程：

1. 确认前置输入已经有：
   - 问题定义
   - 目标用户
   - 场景边界
   - 方案方向
2. 跑 [`wps-write-prd`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-write-prd.md)
3. 输出：
   - WPS 专属 PRD
   - 用户故事
   - Epic 假设
   - 指标和发布风险

### 场景 4：做季度规划

适合问题：

- 下季度做什么
- 哪些 bet 现在做，哪些下季度再做
- 个人版和企业版怎么分配重心

推荐流程：

1. 先确认当前战略没有明显失真
2. 汇总机会地图和方案评估
3. 跑 [`wps-quarter-planning`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-quarter-planning.md)
4. 输出：
   - quarter thesis
   - now / next / later
   - 关键依赖和风险
   - 成功定义

---

## 每个 WPS skill 是干什么的

### `wps-project-management-strategy`

用途：

- 做战略框定
- 明确个人版 / 企业版关系
- 明确 must-win 场景
- 明确差异化和非目标

不要用它做什么：

- 不要拿它直接写 feature PRD
- 不要拿它做需求优先级打分

### `wps-problem-opportunity-map`

用途：

- 把需求清单和反馈整理成问题空间
- 找出重复问题和机会簇
- 区分症状和根因

不要用它做什么：

- 不要直接输出功能列表
- 不要把需求数量当优先级结论

### `wps-feature-design`

用途：

- 设计一个功能的结构骨架
- 明确任务流、角色、状态、规则、边界条件

不要用它做什么：

- 不要把它当视觉稿说明
- 不要只写页面，不写用户任务和状态变化

### `wps-solution-evaluation`

用途：

- 比较多个方案
- 说明为什么推荐 A 而不是 B

不要用它做什么：

- 不要拿它给“还没定义清楚的问题”强行选方案
- 不要让“谁声音大”替代比较框架

### `wps-project-management-prd`

用途：

- 写 WPS 场景下的 PRD
- 特别适合需要写清 edition、角色、对象模型、WPS 集成点的功能

不要用它做什么：

- 不要拿它写一句话级的小需求
- 不要在没有问题定义时直接开始

### `wps-quarter-roadmap`

用途：

- 产出季度路线图
- 把战略和机会池变成 bet sequencing

不要用它做什么：

- 不要把它变成 backlog dump
- 不要没有 quarter thesis 就开始排项目

---

## 每个 WPS command 是怎么用的

### `/wps-strategy`

适合：

- 战略澄清
- 版型关系判断
- must-win 场景和方向选择

示例：

```text
Run commands/wps-strategy.md for this request:
We need to decide whether WPS Project Management should prioritize enterprise execution depth or personal edition activation in the next quarter.
```

### `/wps-design-solution`

适合：

- 从问题到方案
- 从需求清单到推荐方向

示例：

```text
Run commands/wps-design-solution.md for this request:
Enterprise team leads cannot quickly identify project risk without manually chasing updates.
```

### `/wps-write-prd`

适合：

- 方案已定，进入 PRD 阶段

示例：

```text
Run commands/wps-write-prd.md for this request:
Write a PRD for an enterprise project health view for team leads in active execution scenarios.
```

### `/wps-quarter-planning`

适合：

- 季度规划
- 路线图排序

示例：

```text
Run commands/wps-quarter-planning.md for this request:
Plan Q3 for WPS Project Management with enterprise execution visibility as the main bet and personal edition activation as a secondary bet.
```

---

## 推荐的最小团队协作方式

如果团队刚开始使用这套体系，建议先按下面的简单分工来跑：

### PM

- 维护 `research/` 事实底稿
- 发起 `command`
- 对最终判断负责

### 设计

- 参与 `wps-feature-design`
- 补充任务流、状态、边界条件

### 研发

- 参与 `wps-solution-evaluation`
- 补充复杂度、依赖、风险
- 审阅 `wps-project-management-prd` 中的对象模型和状态逻辑

### 数据 / 分析

- 补充 `05-success-metrics.md`
- 校对 PRD 中的指标和埋点定义

---

## 工作前的输入要求

不要在研究底稿为空时，就直接让 AI “写战略”“写 PRD”。

每次开始前，至少准备下面 4 类输入中的 2-3 类：

- 用户需求或反馈
- 用户角色和场景
- 当前业务目标或战略问题
- 已知约束 / 历史经验

如果输入太空，AI 输出通常会变得看似完整、实则空泛。

---

## 推荐的提示词模式

如果你在 Codex 或其他代码工作区里使用，推荐用这种提示方式：

```text
Using commands/wps-design-solution.md:
1. Ask up to 3 clarifying questions if needed.
2. Use the linked WPS skills in order.
3. Keep the output in Chinese.
4. End with risks, assumptions, and next steps.
```

如果只调用单个 skill：

```text
Using skills/wps-feature-design/SKILL.md:
1. Follow the skill sections exactly.
2. Use WPS Project Management context from research/wps-project-management/.
3. Keep the output in Chinese.
```

---

## 常见误用

- 把 `research/` 写成结论区
- 在没有问题地图时直接开始方案设计
- 在没有明确 edition 的情况下写 PRD
- 把路线图写成功能清单
- 让 AI 直接给答案，却不要求它显式写出假设、边界和风险

---

## 团队默认原则

这套体系建议遵循 4 条默认原则：

1. **先研究，后判断。**
   没有研究底稿，就不要假装有清晰结论。

2. **先问题，后方案。**
   先搞清楚机会空间，再讨论功能形态。

3. **先边界，后扩张。**
   尤其是个人版和企业版，不要默认天然共用同一前台策略。

4. **先可验证，后完美。**
   输出不仅要看起来完整，还要能被验证、被执行、被复盘。

---

## 建议的下一步

如果团队刚开始用这套体系，建议先做这三件事：

1. 补齐 `research/wps-project-management/` 的核心内容
2. 用一份真实需求清单跑一遍 [`wps-design-solution`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-design-solution.md)
3. 再把跑出来的推荐方案写成一份 [`wps-project-management-prd`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-prd/SKILL.md) 的示范件

这样团队会最快形成统一用法，而不是把这些文件放在仓库里却没人真正使用。
