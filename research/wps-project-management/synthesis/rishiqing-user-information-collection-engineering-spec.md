# 日事清用户信息采集 Engineering Spec

这份文档用于把 [`rishiqing-user-information-collection-prd.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/rishiqing-user-information-collection-prd.md) 下沉为研发、前端、测试、数据可执行的实现口径。

它不是最终数据库设计稿，也不是最终接口契约文档；它的目标是先在字段、接口、埋点、状态机四层达成统一理解，避免“PRD 看懂了，但每个团队实现成不同东西”。

---

## 1. Scope

本文件覆盖：

- 用户画像主对象和历史对象字段
- onboarding 采集接口
- AI 追问接口
- 模板触发采集接口
- 标签计算结果字段
- 埋点事件表
- 采集状态机

本文件不覆盖：

- 底层数据库分表策略
- 缓存、消息队列和异步任务实现
- AI 提示词具体文案
- CRM 侧完整同步协议

---

## 2. Entity Field Definitions

### 2.1 User Context Profile

用于保存当前“生效中的”用户上下文结果。一个用户只有一份主画像。

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `user_id` | string | yes | 用户唯一 ID | 主键之一 |
| `account_id` | string | no | 企业/团队账号 ID | 企业版可用 |
| `edition` | enum | yes | 产品版本 | `personal`, `enterprise` |
| `profile_status` | enum | yes | 当前画像完成状态 | `empty`, `basic_profiled`, `scenario_profiled`, `pain_profiled`, `enriched` |
| `company_size_band` | enum | no | 公司规模段 | `1`, `2_10`, `11_50`, `51_200`, `200_plus` |
| `team_size_band` | enum | no | 当前团队规模段 | `1`, `2_5`, `6_10`, `11_30`, `30_plus` |
| `industry` | enum | no | 所属行业 | 见行业枚举 |
| `role` | enum | no | 当前角色 | 见角色枚举 |
| `primary_scenario` | enum | no | 一级主场景 | 见场景枚举 |
| `secondary_scenarios` | string[] | no | 二级场景列表 | 二期支持 |
| `problem_types` | string[] | no | 当前主要痛点 | 见痛点枚举 |
| `current_tools` | string[] | no | 当前在用工具 | 见工具枚举 |
| `pain_detail_text` | string | no | 补充痛点文本 | 可空，最长建议 500 |
| `urgency_level` | enum | no | 紧急度 | `low`, `medium`, `high` |
| `management_maturity_level` | enum | no | 管理成熟度 | `manual`, `excel`, `saas`, `advanced` |
| `has_existing_process` | boolean | no | 是否已有流程 | 可空 |
| `source_summary` | object | yes | 各字段来源摘要 | key 为字段名，value 为来源对象 |
| `profile_confidence` | number | yes | 整体画像置信度 | 0-1 |
| `last_confirmed_at` | datetime | no | 最近一次用户明确确认时间 | |
| `last_updated_at` | datetime | yes | 最近更新时间 | |
| `created_at` | datetime | yes | 创建时间 | |

#### `source_summary` 建议结构

```json
{
  "primary_scenario": {
    "source": "onboarding",
    "confidence": 1.0,
    "updated_at": "2026-03-30T10:00:00Z"
  },
  "industry": {
    "source": "ai_chat",
    "confidence": 0.9,
    "updated_at": "2026-04-02T09:30:00Z"
  }
}
```

### 2.2 User Context Answer History

用于保留历史答案，支持冲突追踪、审计和冷却判断。

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `answer_id` | string | yes | 答案记录 ID | 主键 |
| `user_id` | string | yes | 用户 ID | 外键 |
| `session_id` | string | no | 采集会话 ID | onboarding / AI 会话 / 模板会话 |
| `field_name` | string | yes | 字段名 | 例如 `role` |
| `answer_value` | json | yes | 原始答案值 | 支持单选 / 多选 / 文本 |
| `answer_display_text` | string | no | 展示文案 | 便于回显 |
| `source` | enum | yes | 来源入口 | `onboarding`, `ai_chat`, `template_trigger`, `sales_cs`, `behavior_inferred`, `system_default` |
| `confidence` | number | yes | 当前答案置信度 | 0-1 |
| `is_effective` | boolean | yes | 是否为当前生效答案 | 允许仅一条 true |
| `question_id` | string | no | 问题 ID | 追溯问题文案版本 |
| `trigger_context` | object | no | 触发上下文 | 模板类目、意图、页面等 |
| `answered_at` | datetime | yes | 回答时间 | |

### 2.3 User Tag

用于下游消费，不要求下游自己再做规则判断。

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `tag_id` | string | yes | 标签记录 ID | 主键 |
| `user_id` | string | yes | 用户 ID | 外键 |
| `tag_name` | string | yes | 标签名 | 例如 `segment_small_team_lead` |
| `tag_value` | string | no | 标签值 | 可选 |
| `tag_level` | enum | yes | 标签级别 | `segment`, `scenario`, `pain`, `commercial`, `maturity` |
| `reason` | string | yes | 标签命中原因 | 便于调试和运营理解 |
| `valid_from` | datetime | yes | 生效时间 | |
| `valid_to` | datetime | no | 失效时间 | |
| `is_active` | boolean | yes | 是否当前生效 | |

### 2.4 Context Collection Task

用于管理“系统是否应该问、问过没有、最近是否应冷却”。

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `task_id` | string | yes | 采集任务 ID | 主键 |
| `user_id` | string | yes | 用户 ID | 外键 |
| `field_name` | string | yes | 目标字段 | |
| `entry_surface` | enum | yes | 触发入口 | `onboarding`, `ai_chat`, `template_trigger`, `sales_cs` |
| `task_status` | enum | yes | 任务状态 | `eligible`, `asked`, `answered`, `skipped`, `dismissed`, `cooldown` |
| `priority` | integer | yes | 优先级 | 数值越大越高 |
| `cooldown_until` | datetime | no | 冷却截止时间 | |
| `last_asked_at` | datetime | no | 最近一次提问时间 | |
| `ask_count_7d` | integer | yes | 最近 7 天提问次数 | |
| `skip_count_7d` | integer | yes | 最近 7 天跳过次数 | |
| `created_at` | datetime | yes | 创建时间 | |
| `updated_at` | datetime | yes | 更新时间 | |

---

## 3. Enum Suggestions

### 3.1 `role`

| Value | Meaning |
| --- | --- |
| `boss` | 老板 / 业务负责人 |
| `project_manager` | 项目经理 |
| `team_lead` | 团队负责人 |
| `executor` | 执行者 |
| `operations` | 运营 |
| `other` | 其他 |

### 3.2 `primary_scenario`

| Value | Meaning |
| --- | --- |
| `project_management` | 项目管理 |
| `team_task_management` | 团队任务管理 |
| `workflow_approval` | 流程审批 |
| `customer_management` | 客户管理 |
| `okr_goal_management` | OKR / 目标管理 |
| `other` | 其他 |

### 3.3 `problem_type`

| Value | Meaning |
| --- | --- |
| `progress_not_visible` | 项目进度不可控 |
| `tasks_delayed` | 任务经常拖延 |
| `communication_chaotic` | 沟通混乱 |
| `ownership_unclear` | 不清楚谁在负责 |
| `dont_know_how_to_start` | 不知道从哪开始 |
| `template_hard_to_build` | 模板不会搭 |

### 3.4 `industry`

建议先收敛为一级大类：

| Value | Meaning |
| --- | --- |
| `internet` | 互联网 |
| `manufacturing` | 制造 |
| `ecommerce` | 电商 |
| `education` | 教培 |
| `professional_service` | 专业服务 |
| `other` | 其他 |

### 3.5 `current_tool`

| Value | Meaning |
| --- | --- |
| `excel` | Excel |
| `feishu` | 飞书 |
| `wecom` | 企业微信 |
| `dingtalk` | 钉钉 |
| `manual` | 手工 / 口头 |
| `other` | 其他 |

### 3.6 `profile_status`

| Value | Meaning |
| --- | --- |
| `empty` | 尚无有效画像 |
| `basic_profiled` | 已完成基础画像 |
| `scenario_profiled` | 已明确主场景 |
| `pain_profiled` | 已明确主要痛点 |
| `enriched` | 已补充成熟度 / 工具等增强字段 |

---

## 4. API Suggestions

### 4.1 API 1: 获取当前用户画像

#### Purpose

用于首页、AI、模板中心读取当前用户上下文。

#### Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `user_id` | string | yes | 用户 ID |

#### Output

```json
{
  "user_id": "u_123",
  "edition": "personal",
  "profile_status": "scenario_profiled",
  "company_size_band": "2_10",
  "role": "team_lead",
  "primary_scenario": "project_management",
  "problem_types": ["progress_not_visible"],
  "profile_confidence": 0.92,
  "last_confirmed_at": "2026-03-30T10:00:00Z",
  "tags": [
    "segment_small_team_lead",
    "scenario_project_management",
    "pain_progress_visibility"
  ]
}
```

#### Notes

- 若用户尚无画像，应返回 `profile_status=empty`
- tags 建议由服务端直接返回，减少前端再次判断

---

### 4.2 API 2: 提交 onboarding 回答

#### Purpose

用于首次注册后的 3 题 onboarding 提交。

#### Input

```json
{
  "user_id": "u_123",
  "session_id": "onb_001",
  "answers": [
    {
      "question_id": "onb_q1_v1",
      "field_name": "primary_scenario",
      "answer_value": "project_management"
    },
    {
      "question_id": "onb_q2_v1",
      "field_name": "problem_types",
      "answer_value": ["progress_not_visible"]
    },
    {
      "question_id": "onb_q3_v1",
      "field_name": "role",
      "answer_value": "team_lead"
    }
  ],
  "entry_surface": "register_success"
}
```

#### Output

```json
{
  "success": true,
  "profile_status": "pain_profiled",
  "updated_fields": ["primary_scenario", "problem_types", "role"],
  "assigned_tags": [
    "scenario_project_management",
    "pain_progress_visibility"
  ],
  "next_recommendations": {
    "recommended_templates": [
      {
        "template_id": "tpl_001",
        "template_name": "项目执行模板"
      }
    ],
    "recommended_ai_agent": {
      "agent_id": "agent_pm",
      "agent_name": "项目拆解助手"
    }
  }
}
```

#### Validation rules

- `answers` 至少包含 1 个有效字段
- `field_name` 必须在允许的 onboarding 字段白名单中
- 同一 `field_name` 在同一请求中只允许出现一次

---

### 4.3 API 3: 获取 AI 追问建议

#### Purpose

用于 AI 在收到用户意图后，判断是否需要追问及追问什么。

#### Input

```json
{
  "user_id": "u_123",
  "conversation_id": "c_1001",
  "intent_type": "project_create",
  "user_message": "我想管理一个市场活动项目",
  "entry_surface": "ai_chat"
}
```

#### Output

```json
{
  "should_ask_followup": true,
  "question": {
    "question_id": "ai_industry_v1",
    "field_name": "industry",
    "question_text": "你这个项目更偏哪个行业或业务场景？",
    "answer_type": "single_select",
    "options": [
      {"label": "互联网", "value": "internet"},
      {"label": "电商", "value": "ecommerce"},
      {"label": "制造", "value": "manufacturing"},
      {"label": "其他", "value": "other"}
    ]
  },
  "reason": "industry_missing_and_high_impact",
  "cooldown_applied": false
}
```

#### Notes

- AI 层不应自行硬编码追问规则，建议统一从服务端拿
- 若 `should_ask_followup=false`，AI 直接继续主任务

---

### 4.4 API 4: 提交 AI 追问答案

#### Purpose

用于 AI 对话补采完成后写回画像。

#### Input

```json
{
  "user_id": "u_123",
  "conversation_id": "c_1001",
  "question_id": "ai_industry_v1",
  "field_name": "industry",
  "answer_value": "ecommerce",
  "entry_surface": "ai_chat"
}
```

#### Output

```json
{
  "success": true,
  "updated_fields": ["industry"],
  "profile_status": "enriched",
  "assigned_tags": ["industry_ecommerce"],
  "generation_context": {
    "role": "team_lead",
    "primary_scenario": "project_management",
    "industry": "ecommerce",
    "problem_types": ["progress_not_visible"]
  }
}
```

---

### 4.5 API 5: 模板触发采集提交

#### Purpose

用于用户点击模板或 AI 生成入口时收集强意图场景信息。

#### Input

```json
{
  "user_id": "u_123",
  "session_id": "tmp_001",
  "template_category": "project_template",
  "question_id": "tmp_project_type_v1",
  "field_name": "secondary_scenarios",
  "answer_value": ["marketing_campaign"],
  "entry_surface": "template_center"
}
```

#### Output

```json
{
  "success": true,
  "updated_fields": ["secondary_scenarios"],
  "refreshed_recommendations": [
    {
      "template_id": "tpl_618",
      "template_name": "618 活动执行模板"
    }
  ]
}
```

---

### 4.6 API 6: 销售/客成补录画像

#### Purpose

用于企业客户由销售或客户成功补充组织信息。

#### Input

```json
{
  "operator_id": "sales_001",
  "user_id": "u_123",
  "account_id": "acc_009",
  "updates": [
    {
      "field_name": "management_maturity_level",
      "answer_value": "excel"
    },
    {
      "field_name": "company_size_band",
      "answer_value": "51_200"
    }
  ],
  "entry_surface": "sales_console"
}
```

#### Output

```json
{
  "success": true,
  "updated_fields": [
    "management_maturity_level",
    "company_size_band"
  ],
  "assigned_tags": [
    "high_value_enterprise_lead",
    "maturity_low_manual"
  ]
}
```

#### Permission notes

- 只有授权的销售/客成角色可调用
- 销售更新应保留历史，不得覆盖掉原用户回答记录

---

## 5. Tag Rule Suggestions

| Tag Name | Trigger Logic | Use Case |
| --- | --- | --- |
| `segment_individual_user` | `company_size_band=1` and `role=executor` | 个人版首页 |
| `segment_small_team_lead` | `company_size_band in [2_10, 11_50]` and `role in [boss, project_manager, team_lead]` | 团队项目推荐 |
| `scenario_project_management` | `primary_scenario=project_management` | 模板推荐 |
| `scenario_customer_management` | `primary_scenario=customer_management` | CRM 模板推荐 |
| `pain_progress_visibility` | `problem_types contains progress_not_visible` | AI 话术、首页文案 |
| `pain_ownership_unclear` | `problem_types contains ownership_unclear` | 看板/责任分工推荐 |
| `high_value_enterprise_lead` | `edition=enterprise` and `company_size_band in [51_200, 200_plus]` | 销售跟进 |
| `maturity_low_manual` | `management_maturity_level in [manual, excel]` | 导入/迁移引导 |

---

## 6. 埋点表

### 6.1 事件定义表

| Event Name | Trigger | Required Properties | Optional Properties | Success Criteria |
| --- | --- | --- | --- | --- |
| `profile_onboarding_exposed` | onboarding 首次曝光 | `user_id`, `edition`, `entry_surface`, `session_id` | `experiment_id` | 曝光成功即发 |
| `profile_question_answered` | 任一采集题回答 | `user_id`, `field_name`, `answer_value`, `source`, `session_id`, `question_id` | `step_index`, `duration_ms` | 回答提交成功后发 |
| `profile_question_skipped` | 用户跳过题目 | `user_id`, `field_name`, `source`, `session_id`, `question_id` | `step_index` | 跳过动作成功后发 |
| `profile_onboarding_completed` | onboarding 完成 | `user_id`, `session_id`, `question_count`, `answered_fields`, `duration_ms` | `recommended_template_ids` | 返回成功页后发 |
| `profile_ai_followup_triggered` | AI 决定追问 | `user_id`, `conversation_id`, `field_name`, `intent_type` | `reason`, `cooldown_applied` | 追问文案展示时发 |
| `profile_ai_followup_answered` | AI 追问被回答 | `user_id`, `conversation_id`, `field_name`, `answer_value`, `question_id` | `duration_ms` | 回答提交后发 |
| `profile_template_probe_triggered` | 模板触发采集曝光 | `user_id`, `template_category`, `field_name`, `session_id` | `template_id` | 触发提问时发 |
| `profile_template_probe_answered` | 模板触发题回答 | `user_id`, `template_category`, `field_name`, `answer_value`, `session_id` | `template_id` | 回答成功后发 |
| `profile_field_updated` | 主画像字段变化 | `user_id`, `field_name`, `old_value`, `new_value`, `source`, `confidence` | `is_conflict_resolved` | 主表写成功后发 |
| `profile_tag_assigned` | 标签分配 | `user_id`, `tag_name`, `reason` | `tag_level` | 标签写入成功后发 |
| `profile_personalization_rendered` | 个性化内容渲染 | `user_id`, `surface`, `tags`, `scenario` | `template_ids`, `agent_ids` | 页面渲染完成后发 |
| `profile_personalization_clicked` | 点击个性化内容 | `user_id`, `surface`, `content_type`, `content_id` | `position_index` | 点击后发 |
| `sales_context_updated` | 销售补录提交 | `user_id`, `account_id`, `operator_id`, `field_name`, `answer_value` | `operator_role` | 补录成功后发 |

### 6.2 公共属性要求

所有事件必须携带：

| Property | Type | Required | Notes |
| --- | --- | --- | --- |
| `user_id` | string | yes | 用户 ID |
| `account_id` | string | no | 企业账号 ID |
| `edition` | string | yes | `personal` / `enterprise` |
| `source` | string | yes | 入口来源 |
| `entry_surface` | string | yes | 页面或模块 |
| `timestamp` | datetime | yes | 事件时间 |
| `client_type` | string | yes | `web`, `pc`, `mobile` |
| `app_version` | string | no | 客户端版本 |

### 6.3 关键埋点口径说明

#### `profiled_activation_rate`

- 分子：
  完成最小画像采集且在 24 小时内完成关键激活动作的用户数
- 分母：
  进入 onboarding 的新用户数

#### `field_coverage_rate`

- 分子：
  至少拥有该字段有效值的用户数
- 分母：
  进入对应入口的用户数

#### `personalization_ctr`

- 分子：
  点击个性化模板 / AI 推荐的用户数
- 分母：
  看到个性化内容的用户数

#### `followup_answer_rate`

- 分子：
  AI 追问后给出有效答案的会话数
- 分母：
  AI 追问被触发的会话数

---

## 7. 状态机

### 7.1 全局画像状态机

用于描述主画像对象的整体完整度。

| Current State | Trigger | Next State | Notes |
| --- | --- | --- | --- |
| `empty` | 任一基础字段写入成功 | `basic_profiled` | 至少有一个基础字段 |
| `basic_profiled` | `primary_scenario` 有效 | `scenario_profiled` | 主场景明确 |
| `scenario_profiled` | `problem_types` 有效 | `pain_profiled` | 痛点明确 |
| `pain_profiled` | 任一增强字段有效，如 `industry` / `current_tools` / `management_maturity_level` | `enriched` | 进入增强画像 |
| `enriched` | 字段被清空或失效 | 视情况回退到 `pain_profiled` / `scenario_profiled` / `basic_profiled` | 必须允许回退 |

#### 判定建议

- 一期建议不把 `industry` 作为进入 `enriched` 的唯一条件，避免状态过早膨胀
- `problem_types` 为空时，不应标记为 `pain_profiled`

### 7.2 单字段状态机

用于描述单个字段的可靠性和来源层级。

| Current State | Trigger | Next State | Notes |
| --- | --- | --- | --- |
| `unknown` | 系统给默认值 | `inferred` | 置信度低 |
| `unknown` | 用户明确回答 | `confirmed` | 置信度高 |
| `inferred` | 用户明确回答 | `confirmed` | 用户回答优先 |
| `confirmed` | 用户再次修改 | `updated` | 记录历史 |
| `updated` | 用户再次确认同值 | `confirmed` | 可重新确认为稳定值 |

#### 状态说明

- `unknown`：无值
- `inferred`：系统推断或默认
- `confirmed`：用户明确给出
- `updated`：用户在旧答案基础上修改过

### 7.3 采集任务状态机

用于控制“该不该问”和“最近问过没有”。

| Current State | Trigger | Next State | Notes |
| --- | --- | --- | --- |
| `eligible` | 前端展示问题 | `asked` | 仅展示一次 |
| `asked` | 用户回答 | `answered` | 写入画像 |
| `asked` | 用户点击跳过 | `skipped` | 进入冷却判断 |
| `asked` | 用户关闭弹窗/离开页面 | `dismissed` | 可再次触发 |
| `skipped` | 达到冷却规则 | `cooldown` | 一段时间内不再问 |
| `cooldown` | 冷却时间到期且字段仍缺失 | `eligible` | 可再次进入候选 |
| `answered` | 字段过期或失效 | `eligible` | 支持重新确认 |

#### 冷却规则建议

- 同字段 7 天内跳过 >=2 次：进入 `cooldown`
- `cooldown_until` 默认建议为 7 天后
- onboarding 场景可比 AI 追问更保守，避免反复弹出

### 7.4 AI 追问决策状态机

这不是前端状态，而是服务端判断链路。

| Step | Condition | Result |
| --- | --- | --- |
| 1 | 当前意图是否需要某字段 | 否则不追问 |
| 2 | 该字段是否缺失或低置信度 | 否则不追问 |
| 3 | 最近是否问过且被跳过 | 若是则进入冷却，不追问 |
| 4 | 本轮会话是否已追问过主问题 | 若是则不追问 |
| 5 | 追问是否会阻断主任务超过一步 | 若是则不追问 |
| 6 | 满足以上条件 | 返回追问问题 |

---

## 8. Frontend Rendering Rules

### 8.1 onboarding

- 首次曝光后立即发 `profile_onboarding_exposed`
- 每题提交成功后发 `profile_question_answered`
- 若用户点击跳过，发 `profile_question_skipped`
- 完成后必须展示推荐内容，再发 `profile_onboarding_completed`

### 8.2 AI 追问

- 只有收到 `should_ask_followup=true` 才展示追问
- 同一轮会话最多展示 1 个主追问
- 用户不回答时，AI 继续主任务，不等待第二次确认

### 8.3 模板触发

- 若服务端返回需补采，仅允许在用户主动作链路中插入 1 步
- 回答后必须刷新推荐结果或默认模板

---

## 9. Suggested Implementation Order

### Phase 1

- `User Context Profile`
- `User Context Answer History`
- onboarding 读写接口
- 标签基础规则
- 基础埋点

### Phase 2

- `Context Collection Task`
- AI 追问判断接口
- 模板触发采集接口
- 个性化推荐读接口

### Phase 3

- 销售/客成补录接口
- 字段过期与重问逻辑
- 更多标签和商业化规则

---

## 10. Risks and Implementation Notes

- 如果没有 `Answer History`，后续几乎无法解释字段为什么变了，也无法做冷却和冲突处理。
- 如果标签不由服务端统一计算，前端、AI、销售后台会出现多套口径。
- 如果 AI 自己在客户端硬编码追问规则，会很快和产品策略脱节。
- 如果 `profile_field_updated` 埋点没有在主表写成功后触发，数据分析会出现“看见事件但查不到结果”的假象。

---

## 11. References

- [rishiqing-user-information-collection-prd.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/rishiqing-user-information-collection-prd.md)
- [enterprise-execution-visibility-api-field-spec.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-api-field-spec.md)
- [analysis-field-spec.md](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/analysis-field-spec.md)
