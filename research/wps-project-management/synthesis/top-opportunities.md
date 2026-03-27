# Top Opportunities

这份文档记录从需求分析中提炼出的高价值机会池。

每条机会都应该是“问题空间描述”，而不是“功能名”。

---

## Opportunity Template

```md
### Opportunity Name

- Edition:
- Primary Role:
- Core Scenario:
- Problem Statement:
- Representative Signals:
  - Demand count:
  - Representative requests:
  - Related categories:
- Why It Matters:
  - User value:
  - Business value:
  - Strategic relevance:
- Recommendation:
  - move_to_feature_design / validate_first / monitor / reject
- Notes:
```

---

## Priority Opportunities

### Opportunity 1

- Edition: Enterprise
- Primary Role: 团队负责人 / 项目 Owner
- Core Scenario: 执行跟进
- Problem Statement:
  团队负责人无法低成本地看见项目当前是否在按计划推进，往往需要通过开会、催问、手工更新台账等方式获取状态，导致风险暴露过晚、管理成本过高。
- Representative Signals:
  - 一级类目：项目与任务管理（企业版第一大类，1036）
  - 高频二级类目：项目台账管理、项目进度跟踪、甘特图与排期可视化、项目计划管理
  - 代表性需求：
    - “战略任务分解及每周跟进”
    - “项目进度、质量、安全、费用管理”
    - “项目时间节点提醒，建议是一个日历，通过日历标注项目时间节点，并设置提醒”
    - “软件公司项目进度、员工任务工作分解、员工任务完成进度考核”
- Why It Matters:
  - User value：解决企业版核心用户“看不清、盯人累、风险暴露晚”的持续痛点
  - Business value：直接关联企业版协作深度、团队留存和管理层可见价值
  - Strategic relevance：高
- Recommendation:
  - move_to_feature_design
- Notes:
  - 这是企业版最像“必须赢”的核心场景之一
  - 不要把它简单理解成“做个甘特图”或“加个看板”，本质是执行可见性问题

### Opportunity 2

- Edition: Enterprise
- Primary Role: 团队负责人 / 项目 Owner / 成员
- Core Scenario: 任务拆解与分工
- Problem Statement:
  企业版用户在项目启动后，缺少一种低负担的方式把任务拆解清楚、明确负责人和节点，并让团队成员真正进入协作状态，导致分工模糊和执行启动成本过高。
- Representative Signals:
  - 一级类目：项目与任务管理、研发与产品管理
  - 高频二级类目：项目计划管理、任务分配与协同、研发项目管理、产品开发管理
  - 代表性需求：
    - “汽车项目-任务跟进”
    - “记录在进行的项目，待进行的项目的时间和主要负责人”
    - “产品开发任务和进度模板”
    - “公司项目流程跟进，简单一点”
- Why It Matters:
  - User value：帮助团队从“知道要做项目”进入“真正能协作执行”
  - Business value：决定企业版是否只停留在记录工具，还是成为团队执行入口
  - Strategic relevance：高
- Recommendation:
  - move_to_feature_design
- Notes:
  - 适合和 `执行跟进` 场景联动设计，不建议完全割裂

### Opportunity 3

- Edition: Personal
- Primary Role: 个人用户 / 轻量项目发起者
- Core Scenario: 项目创建与启动
- Problem Statement:
  个人版用户知道自己有任务或项目要做，但不擅长把一个想法快速转成结构化计划，因此常常停留在“知道要做”而不是“开始推进”。
- Representative Signals:
  - 一级类目：项目与任务管理（个人版第一大类，3170）
  - 高频二级类目：项目进度跟踪、项目台账管理、甘特图与排期可视化、项目计划管理
  - 代表性需求：
    - “任务分解、进度跟踪”
    - “项目问题反馈和解决”
    - “录入项目进度计划生成项目进图计划航道图”
    - “跟踪项目执行情况”
    - “项目管理混乱”
- Why It Matters:
  - User value：决定个人版能否形成明确的 Aha Moment
  - Business value：直接影响个人版激活和首次使用成功率
  - Strategic relevance：高
- Recommendation:
  - move_to_feature_design
- Notes:
  - 这类机会不应被简化成“提供模板”或“多几个视图”，核心是低门槛启动能力

### Opportunity 4

- Edition: Personal
- Primary Role: 个人用户
- Core Scenario: 个人规划与持续推进
- Problem Statement:
  个人版用户不仅需要记录任务，更需要把短中长期目标、日程、提醒、日报周报等内容组织成可持续推进的个人执行系统，但现有工具要么太轻、要么太复杂。
- Representative Signals:
  - 一级类目：个人规划与日程管理（个人版独有高频类目，335）
  - 高频二级类目：个人规划与日程管理
  - 代表性需求：
    - “我想制定个人的短中长期计划，以及日常工作打卡内容”
    - “根据个人工作日志，生成日报、周报并定时发送”
    - “无法合理安排工作时间，配音书籍任务过多”
    - “项目时间管理、紧急度管理”
    - “怎么更好的规划事情”
- Why It Matters:
  - User value：这是个人版最明确的独有价值信号之一
  - Business value：有机会形成高频使用和个人习惯留存
  - Strategic relevance：高，但与企业版价值路径不同
- Recommendation:
  - validate_first
- Notes:
  - 需要先验证这是不是个人版核心主战场，还是一个高频但低商业外溢的需求池

### Opportunity 5

- Edition: Both
- Primary Role: 负责人 / 管理者
- Core Scenario: 管理汇报与执行可视化
- Problem Statement:
  用户需要的不只是记录任务本身，而是能把执行过程转换成对负责人、管理者有意义的状态、统计和看板，以支持项目跟踪、经营判断和汇报。
- Representative Signals:
  - 高频一级类目：数据分析与经营看板、项目与任务管理、协同办公与流程审批
  - 高频二级类目：统计汇总与经营分析、统计汇总、可视化看板、项目进度跟踪
  - 代表性需求：
    - “表格整理分析，需要知道每个月的什么项目升降”
    - “应收总看板”
    - “大数据实时监控与异常预警分析系统”
    - “项目进度、质量、安全、费用管理”
- Why It Matters:
  - User value：让执行工具从记录层升级到决策和管理可见层
  - Business value：提高团队负责人和管理者的保留价值
  - Strategic relevance：中高
- Recommendation:
  - validate_first
- Notes:
  - 这里要特别小心，不要被“看板”和“报表”需求带偏成 BI 产品

### Opportunity 6

- Edition: Enterprise
- Primary Role: 工程 / 制造 / 研发场景负责人
- Core Scenario: 重执行行业场景下的项目推进
- Problem Statement:
  大量企业版需求来自工程、施工、制造和研发等重执行场景，这些场景对节点、责任、进度、计划和过程可视化的要求更高，说明企业版核心价值更像“执行系统”而不是泛协同工具。
- Representative Signals:
  - 工程与施工管理：417
  - 研发与产品管理：308
  - 生产与制造管理：253
  - 代表性需求：
    - “工程施工项目管理”
    - “工程项目建设全周期详细流程图”
    - “软硬件一体的研发项目管理”
    - “车间任务管理 / 生产交付协同”
- Why It Matters:
  - User value：说明高价值企业场景对项目推进、节点控制和多人协作有更强要求
  - Business value：有助于判断企业版是否应优先服务“重执行场景”的团队负责人
  - Strategic relevance：高
- Recommendation:
  - move_to_opportunity_map
- Notes:
  - 这不是“要做行业化产品”的结论，而是说明战略主战场可能更偏重执行型团队，而不是泛办公协同

---

## Working View

### 当前最值得继续推进的机会

- Opportunity 1：企业版执行跟进与风险可见性
- Opportunity 2：企业版任务拆解与分工协作
- Opportunity 3：个人版项目创建与启动

### 当前最值得先验证的机会

- Opportunity 4：个人版个人规划与持续推进
- Opportunity 5：管理汇报与执行可视化

### 当前最像战略输入而不是单点功能的机会

- Opportunity 6：企业版应优先服务重执行场景团队
