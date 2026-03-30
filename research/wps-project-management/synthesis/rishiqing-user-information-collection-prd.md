# 日事清用户信息采集(User Information Collection) PRD

## 1. Executive Summary

- **Problem**
  当前新用户进入日事清/WPS 项目管理后，系统对“他是谁、要解决什么问题、当前用什么方式工作、最痛的点是什么”缺少结构化理解，导致 onboarding 泛化、模板推荐失准、AI 回答缺乏上下文、销售无法高效跟进，最终影响激活、留存和转化。

- **Solution**
  构建一层“用户理解层（User Context Layer）”，通过注册后 onboarding、AI 对话追问、模板/功能触发采集、销售/客户成功补录四类入口，逐步采集并维护用户画像、使用场景、痛点与成熟度数据；同时将这些数据直接用于首页个性化、模板推荐、AI 输出增强、销售标签与跟进。

- **Expected impact**
  预期提升新用户首周激活率、模板命中率、AI 采纳率与团队协作转化率，并为后续“AI 执行系统”构建统一的用户上下文基础。

---

## 2. Edition and Scenario Context

- **Edition：**
  个人版优先落地，企业版同步预留字段与内部补录能力。

- **Primary role：**
  新注册用户 / 首次进入产品的负责人类用户。

- **Collaborating roles：**
  - AI 助手
  - 模板系统
  - 销售
  - 客户成功
  - 数据分析

- **Core scenario：**
  用户首次注册或首次进入关键功能时，系统以低打扰方式理解用户背景与目标，并把采集结果用于后续体验分流与 AI 增强。

- **Out-of-scenario boundary：**
  - 不在一期做超长开放式问卷
  - 不在一期做完整企业知识图谱
  - 不要求一次性收齐所有字段
  - 不在一期覆盖复杂 CRM 主数据治理

---

## 3. Problem Statement

### Who has the problem

- 新用户：进入产品后看见的是统一体验，缺少“这就是给我准备的”感受。
- AI：缺少用户背景，回答容易停留在通用建议，难以直接生成高可用项目、模板和任务拆解。
- 增长与销售团队：无法快速区分高价值用户、重点场景和高紧急度痛点，导致转化动作粗放。

### What breaks today

- 新用户 onboarding 只承接注册，不承接“理解用户”。
- 产品无法区分个人执行者、小团队负责人、企业管理者等关键角色。
- 模板推荐和首页默认内容没有稳定分流依据。
- AI 无法根据行业、团队规模、场景、痛点输出更贴近上下文的结果。
- 销售/客成对用户背景理解依赖人工询问，信息分散，无法沉淀为长期资产。

### Why it matters now

- 当前产品处于 `PLG + AI + WPS 生态导流` 的探索阶段，首周激活和 Aha Moment 的质量直接决定增长模型是否成立。
- 产品目标不是只做“项目管理工具”，而是成为“执行系统”；执行系统的前提不是功能更多，而是系统更理解用户。
- 如果不尽快建立结构化上下文层，AI 价值会停留在“会生成”，而难以进入“懂你、能推进”。

### Evidence

- 本仓库战略上下文明确指出当前重点是验证激活、Aha Moment、留存与 PLG 路径，而不是继续堆叠工具功能。
- 用户分层与核心场景文档显示：团队规模、协作复杂度、角色与核心场景，是更高价值的分流维度。
- 成功指标文档明确指出：应优先衡量推进执行、AI 采纳和协作扩散，而不是单纯点击量。

相关参考：
- [01-strategy-context.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/01-strategy-context.md)
- [02-user-segments.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/02-user-segments.md)
- [03-core-scenarios.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/03-core-scenarios.md)
- [05-success-metrics.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/05-success-metrics.md)

---

## 4. Strategic Context

- **Strategic fit**
  该能力直接服务产品从“工具”走向“AI 执行系统”的升级，是首页个性化、模板推荐、AI 上下文增强、销售提效的共同底座。

- **Related product goals**
  - 提升新用户激活率与 Aha 触达率
  - 提升 AI 采纳率与模板使用率
  - 提升团队协作扩散与高价值用户识别效率
  - 为个人版到企业版的升级链路沉淀上下文资产

- **Why now**
  - 当前是从 SLG 向 PLG 过渡阶段，缺少用户理解层会让增长漏斗前半段长期失真。
  - WPS 生态带来更多低意图流量，越需要产品快速判断“这个人是谁、下一步该给什么”。
  - AI 能力已经可用，但若没有上下文，只能提供低差异化生成。

---

## 5. Solution Overview

### Summary

构建一套渐进式用户信息采集系统，而不是单次问卷。

系统由四部分组成：

1. **采集入口层**
   注册后 onboarding、AI 对话追问、模板/功能触发采集、销售/客成补录。
2. **结构化数据层**
   统一维护用户画像、场景、痛点、成熟度、来源、置信度和更新时间。
3. **决策逻辑层**
   决定何时问、问什么、跳过什么、如何去重、冲突时信谁。
4. **消费应用层**
   首页个性化、模板推荐、AI 提示增强、销售打标与跟进。

### Main flow

1. 用户完成注册并首次进入产品
2. 系统触发 3 题 onboarding，采集最低必要上下文
3. 系统生成基础标签并驱动首页/模板初次分流
4. 用户进入 AI、模板或关键功能时，按缺失字段与高价值字段继续渐进式补采
5. 销售/客成在企业线索场景补录组织与成熟度信息
6. 系统统一维护用户上下文，并供 AI、推荐、转化链路调用

### Key user actions

- 完成 onboarding 单选题
- 在 AI 对话中回答补充问题
- 在模板/功能触发时选择场景类型
- 查看基于上下文个性化后的首页和推荐内容

### MVP shape

MVP 一期只要求做到：

- onboarding 3 题
- 统一结构化存储
- 首页/模板基础分流
- AI 对话中的缺失字段追问
- 基础标签与埋点

二期再扩展：

- 模板触发采集
- 销售/客成后台补录
- 个性化首页进一步差异化

三期再扩展：

- AI 基于上下文直接生成场景化项目与任务结构
- 跨端、跨入口上下文统一
- 企业级用户知识图谱雏形

---

## 6. Roles, Permissions, and Object Model

### Roles involved

- **终端用户**
  提供自身背景与当前目标，接受个性化体验。

- **AI 助手**
  在对话中执行渐进式采集，并消费上下文生成更贴合的结果。

- **增长系统**
  读取标签做首页、模板、推荐和运营分流。

- **销售 / 客户成功**
  在企业线索或成单后补充组织信息与成熟度。

- **分析团队**
  使用埋点与结构化字段评估激活、采集效果与下游价值。

### Permission rules

- 终端用户只能查看和修改自身填写的信息。
- 销售/客成仅可编辑被授权客户的企业补充字段。
- AI 可读取用户上下文，但不得绕过权限读取其他企业或用户信息。
- 分析侧默认使用脱敏后的行为数据和标签聚合数据。

### Affected objects

- `user_profile`
- `use_case_profile`
- `pain_point_profile`
- `maturity_profile`
- `user_tag`
- `context_event`
- `context_answer_history`

### State transitions

- 用户上下文状态：`empty` -> `basic_profiled` -> `scenario_profiled` -> `pain_profiled` -> `enriched`
- 单字段状态：`unknown` -> `inferred` / `collected` -> `confirmed` -> `updated`
- 采集任务状态：`eligible` -> `asked` -> `answered` / `skipped` / `dismissed`

### Object logic notes

- 上下文是可演进对象，不是注册时一次性静态表单。
- 必须保存字段来源和更新时间，否则后续无法判断数据是否过期。
- 同一字段可能来自多个入口，系统必须支持冲突解决和置信度排序。

---

## 7. WPS Integration Points

- **WPS 应用市场 / 注册入口**
  承接首次 onboarding 触发。

- **AI 助手 / 数字员工**
  承接渐进式追问与上下文消费，是未来最关键入口。

- **模板中心**
  以用户点击模板、AI 员工或解决方案入口作为高意图采集触点。

- **首页 / 工作台**
  消费标签，动态调整默认模块、推荐模板、默认引导文案。

- **组织 / 通讯录**
  企业线索场景下辅助补录组织规模、角色、部门信息。

- **CRM / 销售工作台**
  将高价值标签、痛点与成熟度同步给销售/客成。

---

## 8. Requirements

### 8.1 字段模型

#### 核心设计原则

- 先采集“会影响体验分流与 AI 输出”的字段，再采集 nice to have 信息。
- 优先单选/多选结构化字段，开放题只作为补充，不作为一期核心。
- 每个字段都要回答“采了之后系统会做什么”，否则不采。

#### 字段清单

| 字段组 | 字段名 | 类型 | 必填阶段 | 示例值 | 用途 |
| --- | --- | --- | --- | --- | --- |
| UserProfile | `edition` | enum | 系统自动 | personal / enterprise | 区分版本逻辑 |
| UserProfile | `company_size_band` | enum | onboarding | 1 / 2-10 / 11-50 / 51-200 / 200+ | 首页分流、销售打标 |
| UserProfile | `team_size_band` | enum | AI或模板触发 | 1 / 2-5 / 6-10 / 11-30 / 30+ | 场景复杂度判断 |
| UserProfile | `industry` | enum | onboarding | 互联网 / 制造 / 电商 / 教培 / 其他 | 模板与 AI 场景适配 |
| UserProfile | `role` | enum | onboarding | 老板 / 项目经理 / 团队负责人 / 执行者 / 运营 / 其他 | 首页与推荐分流 |
| UseCase | `primary_scenario` | enum | onboarding | 项目管理 / 团队任务 / 流程审批 / 客户管理 / OKR目标管理 / 其他 | 模板推荐、首页分流 |
| UseCase | `secondary_scenario` | enum[] | 二期 | 项目复盘 / 会议纪要转任务 / 活动执行 / 研发管理 | 后续推荐增强 |
| PainPoints | `problem_type` | enum[] | onboarding | 进度不可控 / 任务拖延 / 沟通混乱 / 不清楚谁负责 / 模板不会搭 | AI 话术与销售话术 |
| PainPoints | `current_tool` | enum[] | AI追问 | Excel / 飞书 / 企业微信 / 钉钉 / 手工 / 其他 | 替代迁移策略 |
| PainPoints | `pain_detail_text` | text | AI补充 | 自由文本 | 训练语料、销售上下文 |
| PainPoints | `urgency_level` | enum | 二期 | low / medium / high | 销售优先级 |
| Maturity | `management_maturity_level` | enum | AI或销售补录 | manual / excel / SaaS / advanced | 方案深度与销售分层 |
| Maturity | `has_existing_process` | boolean | 二期 | true / false | 决定导入/迁移提示 |
| System | `profile_source` | enum | 系统自动 | onboarding / ai_chat / template_trigger / sales_cs | 溯源 |
| System | `profile_confidence` | number | 系统自动 | 0-1 | 冲突解决 |
| System | `last_confirmed_at` | datetime | 系统自动 | 时间戳 | 数据新鲜度 |

#### 一期最低必要字段

- `company_size_band`
- `role`
- `primary_scenario`
- `problem_type`
- `edition`
- `profile_source`
- `last_confirmed_at`

#### 标签派生规则

系统基于字段自动生成标签，供下游直接使用。

示例：

- `segment_small_team_lead`
  条件：`company_size_band=2-10` 且 `role in [项目经理, 团队负责人, 老板]`
- `scenario_project_management`
  条件：`primary_scenario=项目管理`
- `pain_progress_visibility`
  条件：`problem_type` 包含 `进度不可控`
- `high_value_enterprise_lead`
  条件：`edition=enterprise` 且 `company_size_band in [51-200, 200+]`
- `maturity_low_manual`
  条件：`management_maturity_level in [manual, excel]`

### 8.2 页面与触点要求

#### 页面 1：注册后 onboarding

- **目标：**
  在 10 秒内采集最小必要上下文，建立第一层分流基础。

- **页面形式：**
  全屏轻引导或弹层式 3 步问答，默认单选，可跳过。

- **问题设计：**
  1. 你希望用日事清解决什么问题？
     选项：项目管理 / 团队任务 / 流程审批 / 客户管理 / OKR目标管理 / 其他
  2. 你当前最大的困扰是什么？
     选项：项目进度不可控 / 任务经常拖延 / 沟通混乱 / 不清楚谁在负责 / 不知道从哪开始
  3. 你目前更接近哪种角色？
     选项：老板 / 项目经理 / 团队负责人 / 执行者 / 其他

- **可选第四题：**
  你的团队规模大约是？
  选项：1人 / 2-10人 / 11-50人 / 51人以上

- **交互要求：**
  - 每题单屏呈现，减少压迫感
  - 支持 `跳过`
  - 完成后立即给出个性化结果页，而不是只关闭弹窗

- **结果页：**
  展示“为你准备的推荐模板 / AI 员工 / 首个动作”，让用户感知采集是有回报的

#### 页面 2：AI 对话补采

- **目标：**
  在高意图对话中逐步补齐缺失字段，提升上下文真实性与 AI 输出质量。

- **触发条件：**
  - 用户主动发起“我要管理项目”“帮我建一个客户跟进流程”等高意图请求
  - 当前上下文字段缺失且该字段会明显影响 AI 输出

- **问题设计原则：**
  - 一次只追问 1 个关键问题
  - 先问高价值字段，再问 nice to have
  - 问题必须解释其价值，避免像审问

- **示例：**
  用户说“我想管理项目”
  AI 追问：
  - 你是做什么行业的？
  - 团队大概多少人？
  - 你现在主要用什么工具跟进项目？

- **交互要求：**
  - 用户回答后，AI 直接消费该信息继续生成，不让用户感觉“白答了”
  - 如用户拒答，AI 用默认假设继续，但标记低置信度

#### 页面 3：模板/功能触发采集

- **目标：**
  在高意图行为节点获取更准确的强意图数据。

- **触发场景：**
  - 点击项目模板
  - 点击“AI 生成项目”
  - 点击流程审批模板
  - 点击客户管理模板

- **示例问题：**
  “你这个项目更接近哪一类？”
  选项：软件开发 / 市场活动 / 客户交付 / 内部协作 / 其他

- **交互要求：**
  - 问题插在用户动作链路里，但不阻断主任务超过一步
  - 选择后立即刷新模板推荐或 AI 输出

#### 页面 4：销售/客户成功补录页

- **目标：**
  为企业客户建立更完整组织上下文，支撑转化和续费。

- **字段建议：**
  - 行业
  - 部门结构
  - 管理方式
  - 当前工具栈
  - 成熟度判断
  - 当前重点场景
  - 核心痛点摘要

- **交互要求：**
  - 默认带出用户自填信息
  - 销售可补充，不应重复录入已有字段
  - 明确区分用户自填 vs 销售判断

### 8.3 采集与消费逻辑

#### 逻辑 1：渐进式 profiling

- 不要求一次采全。
- 首次只采影响首页和推荐的最低必要字段。
- 后续按用户行为与高价值场景逐步补齐。

#### 逻辑 2：高价值字段优先级

字段优先级从高到低：

1. `primary_scenario`
2. `problem_type`
3. `role`
4. `company_size_band`
5. `industry`
6. `current_tool`
7. `management_maturity_level`

判断原则：
如果某字段不影响当前推荐、AI 输出或销售动作，就不应优先追问。

#### 逻辑 3：入口去重

- 已确认字段在 30 天内不重复问。
- 同一会话内，同一字段只问一次。
- 若已有高置信度答案，低置信度入口不覆盖。
- 若用户主动修改，以最新用户主动输入为准。

#### 逻辑 4：冲突解决

默认优先级：

1. 用户主动最新回答
2. 用户历史明确回答
3. 销售/客成补录
4. 行为推断
5. 系统默认值

当字段冲突时：

- 保留历史记录，不直接覆盖原值
- 当前生效值写入主表
- 历史值写入 `context_answer_history`

#### 逻辑 5：缺失字段追问判定

只有满足以下条件才允许追问：

- 当前任务对该字段高度敏感
- 当前会话未问过该字段
- 用户在最近 7 天未跳过该字段超过 2 次
- 提问不会显著阻断主任务

#### 逻辑 6：结果消费

采集结果必须至少驱动一项行为：

- 首页模块排序
- 模板推荐列表
- AI 系统提示词增强
- 销售标签与线索分配
- 新手任务/引导路径变化

如果采集后的数据没有被消费，视为无效采集。

### 8.4 用户故事

#### Story 1

作为首次注册用户，我希望系统快速理解我最想解决的问题，并立即给我相应模板或 AI 帮助，这样我就不会看到一个和我无关的空产品。

**Acceptance criteria**

- 新用户首次进入时触发 onboarding
- onboarding 默认不超过 3 题，平均完成时长不超过 10 秒
- 用户完成 onboarding 后，首页或结果页必须展示与答案相关的推荐内容
- 若用户跳过 onboarding，系统仍允许继续使用，但降低个性化程度

#### Story 2

作为使用 AI 的用户，我希望 AI 在必要时只问少量关键问题，并基于我的回答直接生成更贴近场景的结果，而不是机械收集信息。

**Acceptance criteria**

- AI 只在字段缺失且会影响当前输出时追问
- 同一轮对话中 AI 最多追问 1 个主问题
- 用户回答后，AI 生成结果必须显式反映这些信息
- 用户拒答时，AI 不能卡死在收集流程中

#### Story 3

作为点击模板或关键功能的用户，我希望系统通过少量附加问题更准确理解我的场景，并立刻优化推荐结果。

**Acceptance criteria**

- 模板触发采集仅在高意图入口触发
- 补采问题不得超过 1 步阻断
- 选择答案后，模板列表或 AI 输出必须即时刷新

#### Story 4

作为销售或客户成功，我希望看到结构化的用户背景、场景和痛点，并能补充企业信息，这样我能更高效地判断价值、制定跟进话术。

**Acceptance criteria**

- 销售页可查看用户自填字段、来源和更新时间
- 销售可补录企业字段并标记来源
- 高价值标签可用于分配和筛选

### 8.5 Edge cases

- 用户连续跳过 2 次以上时，7 天内不再主动弹出同字段问题
- 用户在个人版回答“51人以上团队”时，提示团队版/企业能力，但不强制跳转
- 用户选择“其他”时，允许自由输入，但系统仍需保留结构化 fallback
- 多设备登录时，以服务端最新确认值为准
- 企业管理员代员工开通时，允许销售/管理员预填字段，但员工首次进入后可重新确认
- 当 AI 无法确定字段是否必要时，优先继续完成主任务，而不是过度追问

---

## 9. Metrics and Instrumentation

### Primary metric

- `profiled_activation_rate`
  新用户中，完成最小画像采集且在 24 小时内完成关键激活动作的比例。

建议一期关键激活动作定义为以下任一：

- 创建项目
- 使用模板创建项目
- 发起一次 AI 生成
- 邀请至少 1 名成员

### Guardrail metrics

- onboarding 完成率上升，但首个核心动作完成率下降
- AI 追问触发率上升，但 AI 会话完成率下降
- 模板推荐点击率上升，但模板创建后的 7 日活跃率下降
- 采集字段数量上升，但字段有效消费率不升反降

### Diagnostic metrics

- onboarding 曝光率
- onboarding 完成率
- onboarding 跳过率
- 各题完成率与流失率
- AI 追问回答率
- 模板触发采集回答率
- 字段覆盖率
- 标签命中率
- 个性化首页点击率
- 模板推荐点击率
- AI 采纳率
- 高价值线索识别率

### Event list

| 事件名 | 触发时机 | 核心属性 |
| --- | --- | --- |
| `profile_onboarding_exposed` | onboarding 首次曝光 | `edition`, `entry_page`, `user_id` |
| `profile_question_answered` | 任一采集题提交 | `question_id`, `field_name`, `answer_value`, `source`, `step_index` |
| `profile_question_skipped` | 用户跳过题目 | `question_id`, `field_name`, `source` |
| `profile_onboarding_completed` | onboarding 完成 | `question_count`, `duration_ms`, `answered_fields` |
| `profile_ai_followup_triggered` | AI 决定追问 | `missing_field`, `intent_type`, `conversation_id` |
| `profile_ai_followup_answered` | AI 追问完成 | `field_name`, `answer_value`, `conversation_id` |
| `profile_template_probe_triggered` | 模板触发采集曝光 | `template_category`, `missing_field` |
| `profile_template_probe_answered` | 模板触发采集完成 | `template_category`, `field_name`, `answer_value` |
| `profile_field_updated` | 主画像字段变更 | `field_name`, `old_value`, `new_value`, `source`, `confidence` |
| `profile_tag_assigned` | 标签写入 | `tag_name`, `reason` |
| `profile_personalization_rendered` | 首页/推荐完成个性化渲染 | `surface`, `tags`, `scenario` |
| `profile_personalization_clicked` | 用户点击个性化内容 | `surface`, `content_type`, `content_id` |
| `sales_context_updated` | 销售/客成补录完成 | `field_name`, `account_id`, `operator_role` |

### Event property requirements

所有采集事件至少需要带以下公共属性：

- `user_id`
- `account_id`（如有）
- `edition`
- `source`
- `entry_surface`
- `field_name`
- `answer_value`
- `timestamp`
- `is_first_answer`
- `confidence`

### Measurement notes

- 不要只看采集完成率，必须联动看对激活、模板使用和 AI 采纳的影响。
- `profile_personalization_rendered` 到 `profile_personalization_clicked` 应形成闭环，否则无法评估“采了是否有用”。
- AI 追问效果评估应同时看回答率和会话完成率，避免把体验做成问卷机器人。

---

## 10. Dependencies, Risks, and Rollout

### Dependencies

- 用户画像主表和历史表的数据结构支持
- AI 对话层支持按字段缺失动态追问
- 首页和模板中心支持按标签渲染
- 数据埋点与分析看板建设
- 销售/客成后台支持补录企业字段

### Risks

- **过度采集风险**
  问题太多会伤害激活，系统容易退化成表单产品。

- **只采不消费风险**
  如果推荐、AI、首页不明显变好，用户不会继续配合填写。

- **字段设计失真风险**
  若字段粒度与后续动作不匹配，会得到很多“看起来完整、实际上没用”的信息。

- **冲突与陈旧风险**
  用户角色、团队规模和场景会变化，静态值会迅速失效。

### Mitigations

- 一期坚持最小必要字段
- 所有字段必须绑定消费场景
- 保存来源、置信度和更新时间
- 设置重问冷却期和陈旧更新机制

### Rollout plan

#### Phase 1（2 周）

- 上线 onboarding 3 题
- 建立结构化字段表与标签规则
- 接入首页/模板基础分流
- 打通基础埋点

#### Phase 2（1 个月）

- AI 对话补采
- 模板触发采集
- 首页差异化模块排序
- 销售后台查看画像

#### Phase 3（2-3 个月）

- AI 基于画像生成更完整场景方案
- 企业字段与 CRM/客成打通
- 形成初步“用户知识图谱”

---

## 11. Out of Scope

- 一期不做长问卷式企业调研
- 一期不做行业级复杂方案库自动匹配
- 一期不做完整组织架构建模
- 一期不做用户隐式行为推断替代显式采集
- 一期不做跨产品线统一主数据平台

---

## 12. Open Questions

- onboarding 的第三题是否优先问 `role` 还是 `team_size_band`，对激活影响更优？
- “当前最大困扰”是否应允许多选，还是单选更利于首屏完成率？
- AI 追问的最佳频率阈值是什么，既不打断又能显著提升采纳率？
- 个人版与企业版是否应共享同一套标签体系，还是需要从一期就区分？
- 哪些标签应同步给销售系统，哪些只用于产品内体验？

---

## 13. Anti-Patterns and Design Principles

### Anti-Patterns

- **把信息采集当弹窗任务**
  只追求“收集到了”，不追求“收集后体验更好”。

- **把开放题当主输入**
  看起来更懂用户，实际上完成率和可结构化程度都很差。

- **把所有字段都堆到首登**
  会直接牺牲激活，尤其不适合 PLG 新用户。

- **只服务销售，不服务产品体验**
  用户感受不到回报，就不会持续配合。

### Design Principles

- 采集必须服务于个性化体验，而不是单纯补数据库。
- 高价值字段优先，低价值字段延后。
- 系统要像“理解用户”而不是“审问用户”。
- 先做会被消费的数据，再做看起来完整的数据。

---

## 14. References

- [00-product-overview.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/00-product-overview.md)
- [01-strategy-context.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/01-strategy-context.md)
- [02-user-segments.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/02-user-segments.md)
- [03-core-scenarios.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/03-core-scenarios.md)
- [05-success-metrics.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/05-success-metrics.md)
- [wps-project-management-prd/SKILL.md](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-prd/SKILL.md)
- [prd-development/SKILL.md](/Users/sihuo/workspace/Product-Manager-Skills/skills/prd-development/SKILL.md)
- [wps-feature-design/SKILL.md](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-feature-design/SKILL.md)
