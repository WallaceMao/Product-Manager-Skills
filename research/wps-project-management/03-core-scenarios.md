# Core Scenarios

## Purpose

这份文档用于定义“产品最值得服务的核心场景”。场景比功能更重要，因为项目管理产品很容易被需求清单牵着走，最后变成功能很多、价值模糊。

这份文档要回答：

- 用户在什么情境下会真正需要这个产品
- 哪些场景最值得产品优先服务
- 每个场景的任务流、协作关系、成功标准是什么

---

## Scenario Selection Principles

### 本次场景梳理的判断标准
- 是否直接决定用户留存（是否持续使用）
- 是否能够形成 Aha Moment（首次价值感知）
- 是否具备团队扩散潜力（PLG）
- 是否可以被 AI 显著优化（而不是仅做记录）

### 哪些看起来热闹但不算核心场景
- 复杂流程审批（偏企业场景）
- 纯数据统计与报表（低频、结果导向）
- 高度定制化项目管理（非标准化）
- 单人任务清单（过于轻量，难形成留存）

---

## Scenario Inventory

先盘全量候选场景。

| Scenario | 触发事件 | 主要角色 | 任务复杂度 | 协作复杂度 | 当前痛点强度 | 产品机会 | 优先级 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI生成项目计划 | 有新项目/想法 | 负责人 | 中 | 低 | 高 | 非常高 | P0 |
| 项目拆解与分工 | 项目启动 | 负责人 | 中 | 中 | 高 | 高 | P0 |
| 项目执行跟进 | 项目进行中 | 负责人 + 成员 | 中 | 中 | 非常高 | 非常高 | P0 |
| 会议纪要转任务 | 开完会 | 负责人 | 低 | 中 | 高 | 高 | P1 |
| 多项目优先级管理 | 同时多个项目 | 负责人 | 高 | 中 | 中 | 中 | P2 |
| 项目复盘沉淀 | 项目结束 | 负责人 | 低 | 低 | 中 | 中 | P2 |

---

## Core Scenario 1（最关键）

### Scenario：AI 生成项目计划

#### Scenario Summary
- 用户有一个想法或任务，需要转化为项目
- 发生在项目起点（最关键入口）
- 决定用户是否产生 Aha Moment

#### Trigger
- 写完一个文档
- 有一个新想法
- 接到一个任务

#### Actors
- 主要角色：项目负责人
- 协作角色：暂无
- 决策角色：本人

#### Goal
- 快速把想法变成结构化、可执行的项目

#### Current Workflow
1. 用脑子想 → Excel/文档列任务
2. 手动拆解
3. 容易遗漏或结构混乱

#### Pain Points
- 不知道怎么拆任务
- 很耗时间
- 容易漏关键步骤

#### Collaboration Complexity
- 单人或轻协作
- 无跨部门
- 强依赖脑力

#### Product Opportunity
- AI 自动生成任务结构
- 自动补全逻辑
- 提供模板化能力
- 不该解决: 复杂项目建模

#### Success Signals
- 生成后直接开始使用
- 不修改或少修改

#### Risks
- AI 生成质量不够 → 直接流失

#### Related Features / Objects
- 项目 / 任务 / 模板 / AI生成

## Core Scenario 2（留存核心）

### Scenario：项目拆解与分工

#### Scenario Summary
- 项目从“想法”进入“执行”
- 决定团队是否开始协作

#### Trigger
- 项目创建完成

#### Actors
- 负责人
- 团队成员

#### Goal
- 明确谁做什么、什么时候完成

#### Current Workflow
- 群里分配
- 口头说
- Excel记录

#### Pain Points
- 分工不清
- 责任不明确
- 信息分散

#### Collaboration Complexity
- 多人协作
- 同团队

#### Product Opportunity
- AI辅助分工
- 快速指派任务
- 明确责任人

#### Success Signals
- 所有任务都有负责人
- 成员理解清晰

#### Risks
- 分配复杂 → 用户放弃使用

#### Related Features
- 任务 / 负责人 / 截止时间

## Core Scenario 3（最核心价值）

### Scenario：项目执行跟进（⭐最重要）

#### Scenario Summary
- 项目进行中
- 负责人需要持续推进
- 决定产品是否成为“执行系统”

#### Trigger
- 项目启动后

#### Actors
- 负责人（核心）
- 成员

#### Goal
- 确保项目按时推进

#### Current Workflow
1. 问人进度
2. 开会同步
3. 手动记录

#### Pain Points
- 需要不断催
- 信息滞后
- 状态不透明

#### Collaboration Complexity
- 多人
- 跨时间

#### Product Opportunity
- 自动提醒
- 状态可视化
- AI跟进未完成任务

👉 核心价值点：
👉 “不用盯人也能推进”

#### Success Signals
- 减少沟通
- 项目按时完成

#### Risks
- AI无法真正推动执行 → 变工具

#### Related Features
- 状态 / 评论 / 提醒 / AI跟进

## Core Scenario 4（WPS差异化）

### Scenario：会议纪要 → 自动任务

#### Scenario Summary
- 会后产生待办
- 高价值入口（WPS优势）

#### Trigger
- 会议结束

#### Actors
- 负责人

#### Goal
- 不遗漏任务

#### Pain Points
- 会后没人跟进
- 任务丢失

#### Product Opportunity
- AI提取任务
- 自动生成项目

#### Success Signals
- 会后直接进入执行

---

## User Journey Across Scenarios

### Journey Flow
1. AI生成项目（入口）
2. 拆解与分工
3. 执行跟进（核心留存）
4. 风险暴露与处理
5. 汇报与复盘

### 关键洞察
- 最容易流失：步骤1（AI不好用）
- 最关键突破：步骤3（执行跟进）
- 最大差异点：步骤1 + WPS入口

---

## Scenario Prioritization

### Tier 1: Must Win Scenarios

- AI生成项目计划
- 项目执行跟进

原因：
- 决定激活 + 留存

### Tier 2: Important but Secondary

- 拆解与分工
- 会议转任务

### Tier 3: Watchlist

- 多项目管理
- 项目复盘

---

## Anti-Patterns to Watch

- 把“甘特图”等功能当核心场景
- 过早做复杂流程
- 忽略执行阶段（只做生成）

---

## Evidence Base

- 用户访谈：小团队负责人
- 需求数据：项目管理需求库
- 竞品：飞书、Notion

---

## Open Questions

- AI能否真正替代“催人”行为？
- 用户是否会形成“以项目为中心”的工作习惯？
- 执行阶段AI如何持续提供价值？

---

## Change Log

- **日期：** 2026-03-26
- **修改人：** 毛文强
- **变更内容：** 初始版本
