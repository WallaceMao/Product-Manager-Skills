**改造蓝图**

目标不是把这个仓库改成“日事清资料库”，而是把它升级成一个 **面向 WPS 项目管理产品团队的 PM 操作系统**：既能沉淀产品知识，也能驱动战略、方案、PRD、路线图这些具体工作产出。

建议按“两层架构”改造：

- **底层通用 PM 引擎**：保留现有通用 skill，不动它们的定位。
- **上层 WPS 项目管理领域层**：新增产品域知识、专属 skill、专属 command、模板和样例。

---

**一、改造目标**

你要支持的核心工作有三类：

1. **产品战略规划**
   例如目标市场、用户分层、产品定位、季度重点、竞争策略。
2. **产品功能设计**
   例如场景拆解、任务流、信息结构、协同关系、边界条件。
3. **产品解决方案生成**
   例如多方案对比、推荐方案、MVP 范围、PRD 初稿、路线图建议。

所以仓库也应该围绕这三类产出设计。

---

**二、推荐目录结构**

建议新增这些目录与文件：

```text
research/wps-project-management/
  00-product-overview.md
  01-strategy-context.md
  02-user-segments.md
  03-core-scenarios.md
  04-competitive-landscape.md
  05-success-metrics.md
  06-feature-history.md
  07-domain-terminology.md
  08-constraints-and-assumptions.md

skills/wps-project-management-strategy/
  SKILL.md
  template.md
  examples/sample.md

skills/wps-problem-opportunity-map/
  SKILL.md
  template.md
  examples/sample.md

skills/wps-feature-design/
  SKILL.md
  template.md
  examples/sample.md

skills/wps-solution-evaluation/
  SKILL.md
  template.md
  examples/sample.md

skills/wps-project-management-prd/
  SKILL.md
  template.md
  examples/sample.md

skills/wps-quarter-roadmap/
  SKILL.md
  template.md
  examples/sample.md

commands/wps-strategy.md
commands/wps-design-solution.md
commands/wps-write-prd.md
commands/wps-quarter-planning.md

docs/WPS PM Operating Guide.md
docs/WPS Skill Map.md
```

---

**三、仓库分层设计**

**1. `research/`：沉淀事实，不做推理**
这里放“产品上下文源材料”，供 skill 调用。

建议拆成这些主题：

- `00-product-overview.md`
  内容：日事清在 WPS 产品体系中的定位、服务对象、核心价值、与其他 WPS 产品的关系。
- `01-strategy-context.md`
  内容：当前阶段、公司目标、商业模式、增长压力、平台协同方向。
- `02-user-segments.md`
  内容：用户分层。
  例如：项目经理、团队负责人、普通协作者、管理层、企业采购方。
- `03-core-scenarios.md`
  内容：高频场景。
  例如：项目立项、任务分工、进度跟踪、跨部门协作、周报复盘、模板复用。
- `04-competitive-landscape.md`
  内容：竞品格局。
  例如：飞书项目、Teambition、钉钉项目、Jira、Asana、Monday。
- `05-success-metrics.md`
  内容：北极星和关键指标。
  例如：项目创建率、任务活跃率、多人协作率、周留存、企业渗透率、付费转化。
- `06-feature-history.md`
  内容：已有功能、已做过的尝试、历史结论、踩过的坑。
- `07-domain-terminology.md`
  内容：统一术语。
  例如：项目、任务、子任务、里程碑、视图、模板、成员、负责人、评论、提醒。
- `08-constraints-and-assumptions.md`
  内容：平台、技术、组织、商业约束。

原则：
- `research/` 只讲“事实、历史、定义、数据、假设”。
- 不要在这里写一堆指导语；指导语属于 `skills/`。

---

**2. `skills/`：沉淀方法和判断**
每个 skill 解决一种稳定、可重复的 PM 问题。

建议优先做这 6 个。

**A. `wps-project-management-strategy`**
用途：做产品战略框定。  
适合场景：季度规划、年度方向、业务调整、竞争压力上升时。

输出建议：
- 产品使命 / 战略意图
- 目标用户与重点细分
- 核心场景
- 差异化定位
- 增长飞轮或 adoption 路径
- 本阶段“不做什么”

关键概念建议：
- 平台型产品 vs 单点工具
- 协作深度 vs 功能广度
- 采用成本
- 组织渗透率
- 用户链路连续性

反模式必须写：
- 把功能清单当战略
- 把竞品对标当定位
- 只服务老板口头需求，不服务真实使用场景

---

**B. `wps-problem-opportunity-map`**
用途：把零散需求整理成问题空间与机会池。  
适合场景：收集了很多需求，但不知道先做什么。

输出建议：
- 用户角色
- 问题陈述
- 影响链条
- 频率 / 痛感 / 商业价值
- 机会分级
- 待验证假设

关键概念建议：
- 症状 vs 根因
- 机会空间
- 高价值问题的判断标准
- 用户说想要的 vs 真正阻碍 adoption 的

反模式：
- 直接收敛到某个功能
- 单看反馈数量，不看价值密度
- 用大客户诉求替代市场判断

---

**C. `wps-feature-design`**
用途：把一个功能机会做成完整的设计方案骨架。  
适合场景：进入方案设计和 PRD 前期。

输出建议：
- 功能目标
- 目标用户
- 核心使用场景
- 任务流 / 决策流
- 状态与规则
- 权限与协作关系
- 异常路径
- 埋点与验收点

关键概念建议：
- 主路径 vs 边界路径
- 单人效率工具 vs 多人协同工具
- 可配置性 vs 可理解性
- 入口设计与 adoption friction

反模式：
- 只写页面，不写用户任务
- 只写 happy path，不写状态切换
- 只看单人操作，不看协作对象

---

**D. `wps-solution-evaluation`**
用途：对多个方案做结构化比较并给出推荐。  
适合场景：产品、设计、研发在几种方案之间摇摆。

输出建议：
- 方案列表
- 每个方案的适用前提
- 用户价值
- 战略一致性
- 实施复杂度
- 风险与依赖
- 数据验证路径
- 推荐方案与原因

固定评估维度建议：
- 用户价值
- 战略贴合度
- 复杂度
- 协同成本
- 风险
- 上线路径
- 可验证性

反模式：
- “谁声音大选谁”
- “谁做得快选谁”
- 不明确方案适用边界

---

**E. `wps-project-management-prd`**
用途：生成日事清专属 PRD。  
做法：不要从零造，直接基于现有 [`prd-development`](/Users/sihuo/workspace/Product-Manager-Skills/skills/prd-development/SKILL.md) 扩展。

需要补的专属章节：
- 场景适用边界
- 协作对象与权限关系
- 项目/任务/里程碑等对象模型
- 和 WPS 其他产品的连接点
- adoption 设计
- 关键行为埋点
- 风险发布策略

反模式：
- 把页面说明当 PRD
- 没有对象模型和状态规则
- 没有发布后验证计划

---

**F. `wps-quarter-roadmap`**
用途：把战略和机会池转成季度路线图。  
适合场景：季度 OKR、版本规划、资源分配。

输出建议：
- 目标
- 战略主题
- 候选机会池
- 优先级
- 版本节奏
- 风险和依赖
- 明确不做项

反模式：
- 路线图等于需求清单
- 所有方向都重要
- 没有“为什么现在做”

---

**3. `commands/`：把多个 skill 串成工作流**
这是你最值得投入的地方，因为它最接近日常工作。

建议先做 4 个 command。

**`commands/wps-strategy.md`**
用途：从业务背景到战略建议。  
推荐串联：
- `wps-project-management-strategy`
- `problem-statement`
- `positioning-statement`
- `roadmap-planning`

输出：
- 战略摘要
- 用户与场景优先级
- 差异化方向
- 季度战略建议

**`commands/wps-design-solution.md`**
用途：从问题到方案。  
推荐串联：
- `wps-problem-opportunity-map`
- `wps-feature-design`
- `wps-solution-evaluation`

输出：
- 问题定义
- 候选方案
- 推荐方案
- MVP 范围
- 下一步验证建议

**`commands/wps-write-prd.md`**
用途：从解决方案到 PRD 草稿。  
推荐串联：
- `wps-feature-design`
- `wps-project-management-prd`
- `user-story`
- `epic-hypothesis`

输出：
- PRD 初稿
- 用户故事
- 验收条件
- 风险与待确认项

**`commands/wps-quarter-planning.md`**
用途：做季度规划。  
推荐串联：
- `wps-project-management-strategy`
- `wps-problem-opportunity-map`
- `wps-solution-evaluation`
- `wps-quarter-roadmap`

输出：
- 季度主题
- Top 机会池
- 投资建议
- roadmap 草案

---

**四、建议新增的“产品专属字段”**

为了让输出更像“日事清产品工作”，你可以在相关 skill/template 里统一加入这些字段：

- `目标用户角色`
- `核心协作场景`
- `触发入口`
- `主要任务流`
- `涉及对象`
  例如项目、任务、子任务、里程碑、模板、视图
- `角色与权限`
- `跨端/跨产品关系`
- `关键状态变化`
- `用户反馈机制`
- `埋点与验证指标`
- `风险发布策略`
- `不做什么`

这组字段会显著减少“空泛方案”。

---

**五、建议复用而不是重写的现有 skill**

这些现有 skill 可以直接作为底座：

- [`product-strategy-session`](/Users/sihuo/workspace/Product-Manager-Skills/skills/product-strategy-session/SKILL.md)
- [`prd-development`](/Users/sihuo/workspace/Product-Manager-Skills/skills/prd-development/SKILL.md)
- [`problem-statement`](/Users/sihuo/workspace/Product-Manager-Skills/skills/problem-statement/SKILL.md)
- [`opportunity-solution-tree`](/Users/sihuo/workspace/Product-Manager-Skills/skills/opportunity-solution-tree/SKILL.md)
- [`recommendation-canvas`](/Users/sihuo/workspace/Product-Manager-Skills/skills/recommendation-canvas/SKILL.md)
- [`positioning-statement`](/Users/sihuo/workspace/Product-Manager-Skills/skills/positioning-statement/SKILL.md)
- [`roadmap-planning`](/Users/sihuo/workspace/Product-Manager-Skills/skills/roadmap-planning/SKILL.md)
- [`user-story`](/Users/sihuo/workspace/Product-Manager-Skills/skills/user-story/SKILL.md)

原则：
- 通用方法论不动。
- WPS 专属 skill 只补“产品域判断”和“上下文约束”。

---

**六、第一阶段最小可用版本**

先不要做全套。建议 2 周内先做 MVP：

**第 1 周：沉淀上下文**
- `research/wps-project-management/00-product-overview.md`
- `research/wps-project-management/02-user-segments.md`
- `research/wps-project-management/03-core-scenarios.md`
- `research/wps-project-management/04-competitive-landscape.md`
- `research/wps-project-management/05-success-metrics.md`

**第 2 周：补最关键工作流**
- `skills/wps-project-management-strategy/SKILL.md`
- `skills/wps-feature-design/SKILL.md`
- `skills/wps-solution-evaluation/SKILL.md`
- `commands/wps-design-solution.md`
- `docs/WPS PM Operating Guide.md`

这样你就已经能支撑：
- 战略讨论
- 单个需求方案产出
- 方案评审
- PRD 前置工作

---

**七、推荐的使用方式**

未来团队可以这样用：

1. 先在 `research/` 里维护事实和背景。
2. 开战略会时跑 `commands/wps-strategy.md`。
3. 有需求要做时跑 `commands/wps-design-solution.md`。
4. 方案定了以后跑 `commands/wps-write-prd.md`。
5. 季度规划时跑 `commands/wps-quarter-planning.md`。

这样仓库会形成闭环：
`事实沉淀 -> 框架判断 -> 方案产出 -> 文档输出 -> 复盘再沉淀`

---

**八、最重要的三条原则**

- **不要把业务知识直接塞进通用 skill。**
  通用 skill 继续通用，业务知识放 `research/` 和 WPS 专属 skill。
- **不要让 skill 只会产出文档，要让它会教判断。**
  这个仓库本身就强调 pedagogic-first。
- **不要跳过反模式。**
  对“项目管理产品”来说，反模式尤其重要，因为它很容易沦为功能堆砌。

---

**九、你下一步最值得做的事**

建议直接从这三件开始：

1. 建 `research/wps-project-management/` 的 5 个基础文档。
2. 起草 `skills/wps-project-management-strategy/SKILL.md`。
3. 起草 `commands/wps-design-solution.md`。

如果你要，我下一步可以直接继续给你其中一个：
- 一份 **目录+文件清单的脚手架**，你可以直接照着建。
- 一份 **`wps-project-management-strategy/SKILL.md` 初稿**。
- 一份 **`commands/wps-design-solution.md` 初稿**。