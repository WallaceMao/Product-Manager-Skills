# 企业版执行跟进与风险可见性 User Stories

这份文档基于以下三份上游材料整理：

- [`enterprise-execution-visibility-solution-direction.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-solution-direction.md)
- [`enterprise-execution-visibility-prd.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-prd.md)
- [`enterprise-execution-visibility-engineering-breakdown.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-engineering-breakdown.md)

目标是把这项能力拆成更适合研发排期、测试设计和项目跟踪的 stories。

---

## Epic Hypothesis

我们相信，为企业版中的项目负责人提供“项目健康摘要 + 风险任务清单 + 基础跟进行动入口”，将帮助他们更低成本地识别执行风险并采取跟进行动，因为当前他们仍高度依赖人工追问、会议同步和手工台账来掌握项目状态。

---

## Story Map View

### Backbone

1. 查看项目健康状态
2. 查看风险任务
3. 对风险任务采取行动
4. 按角色控制可见与可操作范围
5. 记录事件并支持后续验证

### Recommended Release Slices

#### Slice 1: Read-Only MVP

- US-001 项目健康摘要展示
- US-002 风险任务清单展示
- US-003 风险原因可解释性
- US-007 管理者只读查看
- US-008 成员受限查看
- US-010 健康摘要与风险视图埋点

#### Slice 2: Actionable MVP

- US-004 从风险项直接提醒负责人
- US-005 从风险项直接改负责人
- US-006 从风险项直接改截止时间
- US-009 动作结果反馈与状态刷新
- US-011 跟进行动埋点

#### Slice 3: Rule and Signal Optimization

- US-012 风险去重与排序优化
- US-013 历史任务与归档任务过滤
- US-014 健康状态阈值优化

---

## User Stories

### US-001 项目健康摘要展示

**As a** 项目负责人  
**I want** 在项目详情页直接看到项目健康摘要  
**So that** 我可以快速判断这个项目当前是否需要重点跟进

**Notes**

- 面向 Enterprise
- 仅适用于进行中项目

**Gherkin**

```gherkin
Feature: 项目健康摘要展示

  Scenario: 项目负责人进入进行中项目时看到健康摘要
    Given 我是该项目的项目负责人
    And 该项目状态为“进行中”
    When 我打开项目详情页
    Then 我应看到项目健康摘要模块
    And 我应看到项目当前健康状态
    And 我应看到逾期任务数、被阻塞任务数、无负责人任务数、无截止时间任务数

  Scenario: 项目当前无明显风险
    Given 我是该项目的项目负责人
    And 该项目状态为“进行中”
    And 该项目当前无风险任务
    When 我打开项目详情页
    Then 健康摘要应显示“正常”或等价状态
    And 不应出现空白的健康区域
```

---

### US-002 风险任务清单展示

**As a** 项目负责人  
**I want** 查看当前项目中的风险任务清单  
**So that** 我可以知道哪些任务最值得优先处理

**Gherkin**

```gherkin
Feature: 风险任务清单展示

  Scenario: 展示风险任务列表
    Given 我是该项目的项目负责人
    And 项目中存在逾期、阻塞、无负责人或无截止时间任务
    When 我查看风险任务清单
    Then 系统应展示所有符合规则的风险任务
    And 每条任务应展示任务名称、当前状态、负责人、截止时间和风险原因

  Scenario: 已完成任务不进入风险清单
    Given 某任务状态为“已完成”
    When 我查看风险任务清单
    Then 该任务不应出现在风险任务清单中
```

---

### US-003 风险原因可解释性

**As a** 项目负责人  
**I want** 看到每条风险任务被标记为风险的具体原因  
**So that** 我能理解系统判断并建立信任

**Gherkin**

```gherkin
Feature: 风险原因可解释性

  Scenario: 风险任务展示明确原因
    Given 某任务已被识别为风险任务
    When 我查看该风险任务
    Then 我应看到至少一个明确的风险原因
    And 风险原因应使用可理解的产品语言

  Scenario: 健康状态为风险中时可追溯原因
    Given 项目健康状态为“风险中”
    When 我查看健康摘要
    Then 我应能进入风险详情
    And 我应能看到造成风险状态的任务或原因类型
```

---

### US-004 从风险项直接提醒负责人

**As a** 项目负责人  
**I want** 从风险任务直接发起提醒  
**So that** 我不必切换到其他页面或工具催办

**Gherkin**

```gherkin
Feature: 从风险项直接提醒

  Scenario: 对风险任务发起提醒
    Given 我是该项目的项目负责人
    And 某任务在风险任务清单中
    When 我点击“提醒”操作
    Then 系统应向该任务负责人发起提醒
    And 系统应提示提醒发送结果

  Scenario: 无负责人任务不可提醒
    Given 某风险任务无负责人
    When 我点击“提醒”操作
    Then 系统不应直接发送提醒
    And 系统应提示先补充负责人
```

---

### US-005 从风险项直接改负责人

**As a** 项目负责人  
**I want** 从风险任务直接调整负责人  
**So that** 我可以快速修正无负责人或负责人不合适的问题

**Gherkin**

```gherkin
Feature: 从风险项直接修改负责人

  Scenario: 成功修改风险任务负责人
    Given 我是该项目的项目负责人
    And 某风险任务允许编辑负责人
    When 我为该任务选择新的负责人
    Then 系统应成功保存新的负责人
    And 任务详情应反映最新负责人
    And 风险状态应根据新数据重新计算
```

---

### US-006 从风险项直接改截止时间

**As a** 项目负责人  
**I want** 从风险任务直接调整截止时间  
**So that** 我可以及时修正明显失效或缺失的计划安排

**Gherkin**

```gherkin
Feature: 从风险项直接修改截止时间

  Scenario: 为风险任务补充截止时间
    Given 我是该项目的项目负责人
    And 某风险任务无截止时间
    When 我为该任务设置新的截止时间
    Then 系统应保存新的截止时间
    And 该任务的风险状态应重新计算

  Scenario: 调整截止时间后刷新风险状态
    Given 某任务因逾期被标记为风险
    When 我修改该任务截止时间为未来时间
    Then 系统应重新计算该任务是否仍为风险任务
```

---

### US-007 管理者只读查看

**As a** 管理者 / 观察者  
**I want** 查看项目健康摘要和关键风险  
**So that** 我可以了解项目状态但不干扰执行细节

**Gherkin**

```gherkin
Feature: 管理者只读查看

  Scenario: 管理者可查看摘要但不可操作
    Given 我是该项目的管理者或观察者
    When 我打开项目详情页
    Then 我应看到项目健康摘要
    And 我不应看到提醒、改负责人、改截止时间等可操作入口
```

---

### US-008 成员受限查看

**As a** 项目成员  
**I want** 仅查看与自己相关的风险信息  
**So that** 我可以知道需要处理什么，而不会看到超出权限范围的项目管理信息

**Gherkin**

```gherkin
Feature: 成员受限查看

  Scenario: 成员查看自己相关任务的风险原因
    Given 我是项目成员
    And 我负责至少一个风险任务
    When 我查看自己相关任务
    Then 我应看到该任务的风险原因
    And 我不应看到不属于我权限范围的全局管理动作
```

---

### US-009 动作结果反馈与状态刷新

**As a** 项目负责人  
**I want** 在执行跟进行动后立即看到反馈和刷新结果  
**So that** 我知道动作是否生效，不需要手动反复验证

**Gherkin**

```gherkin
Feature: 动作反馈与状态刷新

  Scenario: 跟进行动后展示成功反馈
    Given 我对风险任务执行了提醒、改负责人或改截止时间
    When 操作成功
    Then 系统应显示明确的成功反馈
    And 风险列表或任务信息应更新为最新状态

  Scenario: 跟进行动失败时展示失败反馈
    Given 我对风险任务执行某个操作
    When 操作失败
    Then 系统应显示明确的失败反馈
    And 不应误显示为成功
```

---

### US-010 健康摘要与风险视图埋点

**As a** 产品和数据团队  
**I want** 记录健康摘要和风险视图相关事件  
**So that** 我们可以判断这个能力是否真的被使用和信任

**Gherkin**

```gherkin
Feature: 健康视图埋点

  Scenario: 打开健康摘要时记录事件
    Given 用户进入项目详情页
    When 健康摘要模块被展示
    Then 系统应记录 project_health_view_opened 事件

  Scenario: 点击风险任务时记录事件
    Given 用户正在查看风险任务清单
    When 用户点击某个风险任务或风险原因
    Then 系统应记录 risk_signal_clicked 事件
```

---

### US-011 跟进行动埋点

**As a** 产品和数据团队  
**I want** 记录所有关键跟进行动  
**So that** 我们可以判断“看见风险”是否转化成了“实际行动”

**Gherkin**

```gherkin
Feature: 跟进行动埋点

  Scenario: 执行跟进行动时记录事件
    Given 用户在风险任务清单中执行操作
    When 操作为提醒、改负责人或改截止时间之一
    Then 系统应记录 followup_action_triggered 事件
    And 事件中应包含 action_type、project_id、task_id、viewer_role
```

---

### US-012 风险去重与排序优化

**As a** 项目负责人  
**I want** 风险任务列表去重且优先展示最重要的任务  
**So that** 我不会被重复项和低优先级项干扰

**Gherkin**

```gherkin
Feature: 风险去重与排序

  Scenario: 同一任务命中多个风险规则时只展示一次
    Given 某任务同时满足逾期和无负责人条件
    When 我查看风险任务清单
    Then 该任务只应展示一次
    And 该任务应展示多个风险原因

  Scenario: 风险任务按优先级排序
    Given 项目中存在多个风险任务
    When 我查看风险任务清单
    Then 系统应优先展示更影响执行推进的风险任务
```

---

### US-013 历史任务与归档任务过滤

**As a** 项目负责人  
**I want** 健康摘要只关注当前有效执行任务  
**So that** 历史任务和归档内容不会污染当前风险判断

**Gherkin**

```gherkin
Feature: 历史任务和归档任务过滤

  Scenario: 归档任务不参与风险计算
    Given 某任务已归档
    When 系统计算项目健康状态
    Then 该任务不应参与风险统计

  Scenario: 历史完成任务不参与当前风险判断
    Given 某任务已完成且不属于当前执行阶段
    When 系统生成风险任务清单
    Then 该任务不应出现在风险清单中
```

---

### US-014 健康状态阈值优化

**As a** 产品团队  
**I want** 后续可以优化健康状态阈值  
**So that** 健康摘要能随着真实使用反馈持续提升可信度

**Gherkin**

```gherkin
Feature: 健康状态阈值优化准备

  Scenario: 健康状态规则可追溯
    Given 系统已生成项目健康状态
    When 产品或研发回看该状态
    Then 应能追溯其规则来源和触发原因
```

---

## Priority Recommendation

如果需要进一步拆到开发排期，建议优先顺序是：

1. `US-001`
2. `US-002`
3. `US-003`
4. `US-007`
5. `US-008`
6. `US-010`
7. `US-004`
8. `US-005`
9. `US-006`
10. `US-009`
11. `US-011`
12. `US-012`
13. `US-013`
14. `US-014`

---

## Suggested Next Step

如果继续往前推进，下一步最适合补：

- 测试用例矩阵
- API 字段定义表
- 风险规则阈值表

这样就可以从 story 层继续收敛到实现和测试排期层。
