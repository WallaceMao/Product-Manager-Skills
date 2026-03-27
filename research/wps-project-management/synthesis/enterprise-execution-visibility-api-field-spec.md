# 企业版执行跟进与风险可见性 API / 字段定义表

这份文档用于帮助产品、后端、前端、测试在接口和字段层面对齐。

它不是最终技术设计稿，而是一份面向跨团队协同的“实现口径文件”。

---

## 1. Scope

本文件覆盖：

- 健康摘要读取接口
- 风险任务清单读取接口
- 跟进行动写接口
- 关键对象字段
- 关键事件字段

不覆盖：

- 底层数据库结构
- 中间缓存设计
- 内部服务调用细节

---

## 2. Entity Field Definitions

### Project

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `project_id` | string | yes | 项目唯一 ID | 主键 |
| `project_name` | string | yes | 项目名称 | 前端展示 |
| `project_status` | enum | yes | 项目状态 | 建议值：`not_started`, `active`, `completed`, `archived` |
| `project_owner_id` | string | yes | 项目负责人 ID | 用于权限和角色判断 |
| `project_health_status` | enum | no | 项目健康状态 | 建议值：`normal`, `attention`, `at_risk` |
| `project_health_updated_at` | datetime | no | 最近一次健康状态计算时间 | 用于展示和调试 |

### Task

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `task_id` | string | yes | 任务唯一 ID | 主键 |
| `project_id` | string | yes | 所属项目 ID | 外键 |
| `task_name` | string | yes | 任务名称 | 前端展示 |
| `task_status` | enum | yes | 任务状态 | 建议值：`not_started`, `in_progress`, `blocked`, `done` |
| `assignee_id` | string | no | 当前负责人 ID | 为空时可触发风险 |
| `due_at` | datetime | no | 截止时间 | 为空时可触发风险 |
| `priority` | enum | no | 优先级 | 可选：`low`, `medium`, `high`, `critical` |
| `is_blocked` | boolean | no | 是否阻塞 | 可与 `task_status=blocked` 口径统一 |
| `blocked_reason` | string | no | 阻塞原因 | 用于风险解释 |
| `completed_at` | datetime | no | 完成时间 | 已完成任务过滤 |
| `archived_flag` | boolean | yes | 是否归档 | 归档任务不进入当前风险判断 |

### Risk Item

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `task_id` | string | yes | 对应任务 ID | 关联任务 |
| `risk_types` | string[] | yes | 风险类型列表 | 一个任务可命中多个风险 |
| `risk_reason_texts` | string[] | yes | 风险原因文案 | 面向用户展示 |
| `severity` | enum | yes | 风险严重程度 | 建议值：`low`, `medium`, `high` |
| `rank_score` | number | no | 排序分值 | 用于内部排序，不要求前端展示 |

### Follow-up Action

| Field | Type | Required | Description | Notes |
| --- | --- | --- | --- | --- |
| `action_id` | string | yes | 动作唯一 ID | 主键 |
| `task_id` | string | yes | 对应任务 ID | |
| `action_type` | enum | yes | 动作类型 | 建议值：`notify`, `reassign`, `change_due_date` |
| `operator_id` | string | yes | 操作人 ID | 当前一般为项目负责人 |
| `target_user_id` | string | no | 目标用户 ID | 提醒 / 重分配时使用 |
| `created_at` | datetime | yes | 动作创建时间 | |
| `result_status` | enum | yes | 动作结果 | 建议值：`success`, `failed` |

---

## 3. Enum Suggestions

### `project_health_status`

| Value | Meaning |
| --- | --- |
| `normal` | 当前无明显执行风险 |
| `attention` | 存在需要关注的问题，但未达到高风险 |
| `at_risk` | 存在明显执行风险，建议尽快跟进 |

### `risk_type`

| Value | Meaning |
| --- | --- |
| `overdue` | 任务逾期 |
| `blocked` | 任务阻塞 |
| `missing_assignee` | 无负责人 |
| `missing_due_date` | 无截止时间 |
| `near_deadline` | 临近关键节点 |

### `viewer_role`

| Value | Meaning |
| --- | --- |
| `project_owner` | 项目负责人 |
| `member` | 项目成员 |
| `manager` | 管理者 / 观察者 |

---

## 4. Read API Suggestions

### API 1: 获取项目健康摘要

#### Purpose

用于项目详情页加载健康摘要。

#### Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | 项目 ID |
| `viewer_user_id` | string | yes | 当前查看用户 ID |

#### Output

```json
{
  "project_id": "p_123",
  "project_health_status": "attention",
  "project_health_updated_at": "2026-03-27T10:00:00Z",
  "risk_counts": {
    "overdue": 3,
    "blocked": 1,
    "missing_assignee": 2,
    "missing_due_date": 4,
    "near_deadline": 2
  },
  "risk_reason_summary": [
    "3 个任务已逾期",
    "1 个任务被标记为阻塞"
  ],
  "viewer_role": "project_owner",
  "can_trigger_followup_action": true
}
```

#### Notes

- 若用户无查看权限，应返回权限错误或受限结果
- 若项目非进行中，可返回空摘要或不展示标记

---

### API 2: 获取风险任务清单

#### Purpose

用于项目详情页中的风险任务列表。

#### Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | 项目 ID |
| `viewer_user_id` | string | yes | 当前查看用户 ID |
| `risk_type_filter` | string[] | no | 风险类型过滤 |
| `sort_by` | string | no | 排序方式 |

#### Output

```json
{
  "project_id": "p_123",
  "items": [
    {
      "task_id": "t_001",
      "task_name": "确认供应商交付计划",
      "task_status": "in_progress",
      "assignee_id": "u_009",
      "assignee_name": "张三",
      "due_at": "2026-03-28T18:00:00Z",
      "risk_types": ["near_deadline", "blocked"],
      "risk_reason_texts": [
        "任务临近截止时间",
        "任务已被标记为阻塞"
      ],
      "severity": "high",
      "allowed_actions": ["notify", "change_due_date", "open_task_detail"]
    }
  ]
}
```

#### Notes

- 一个任务允许有多个风险原因
- 返回结果中建议包含 `allowed_actions`，方便前端控制按钮展示

---

## 5. Write API Suggestions

### API 3: 发送提醒

#### Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `task_id` | string | yes | 风险任务 ID |
| `operator_id` | string | yes | 当前操作人 |

#### Output

```json
{
  "action_id": "a_001",
  "action_type": "notify",
  "result_status": "success"
}
```

#### Error notes

- 若任务无负责人，应返回业务错误，提示先设置负责人
- 若操作人无权限，应返回权限错误

---

### API 4: 修改负责人

#### Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `task_id` | string | yes | 任务 ID |
| `operator_id` | string | yes | 当前操作人 |
| `new_assignee_id` | string | yes | 新负责人 ID |

#### Output

```json
{
  "action_id": "a_002",
  "action_type": "reassign",
  "result_status": "success",
  "task_id": "t_001",
  "new_assignee_id": "u_011"
}
```

---

### API 5: 修改截止时间

#### Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `task_id` | string | yes | 任务 ID |
| `operator_id` | string | yes | 当前操作人 |
| `new_due_at` | datetime | yes | 新截止时间 |

#### Output

```json
{
  "action_id": "a_003",
  "action_type": "change_due_date",
  "result_status": "success",
  "task_id": "t_001",
  "new_due_at": "2026-03-29T18:00:00Z"
}
```

---

## 6. Frontend Field Mapping Suggestions

### Health Summary Card

| UI Element | Field |
| --- | --- |
| 健康状态文案 | `project_health_status` |
| 最近更新时间 | `project_health_updated_at` |
| 逾期任务数 | `risk_counts.overdue` |
| 阻塞任务数 | `risk_counts.blocked` |
| 无负责人任务数 | `risk_counts.missing_assignee` |
| 无截止时间任务数 | `risk_counts.missing_due_date` |

### Risk Task List

| UI Element | Field |
| --- | --- |
| 任务名称 | `task_name` |
| 负责人 | `assignee_name` / `assignee_id` |
| 截止时间 | `due_at` |
| 风险标签 | `risk_types` |
| 风险原因说明 | `risk_reason_texts` |
| 操作按钮 | `allowed_actions` |

---

## 7. Event Field Suggestions

### Event: `project_health_view_opened`

| Field | Type | Required |
| --- | --- | --- |
| `project_id` | string | yes |
| `viewer_user_id` | string | yes |
| `viewer_role` | string | yes |
| `project_health_status` | string | yes |

### Event: `risk_signal_clicked`

| Field | Type | Required |
| --- | --- | --- |
| `project_id` | string | yes |
| `task_id` | string | yes |
| `viewer_user_id` | string | yes |
| `viewer_role` | string | yes |
| `risk_type` | string | yes |

### Event: `followup_action_triggered`

| Field | Type | Required |
| --- | --- | --- |
| `project_id` | string | yes |
| `task_id` | string | yes |
| `operator_id` | string | yes |
| `viewer_role` | string | yes |
| `action_type` | string | yes |
| `result_status` | string | yes |

---

## 8. Open Alignment Questions

- `project_health_status` 是否实时计算，还是需要缓存字段？
- `near_deadline` 的阈值由谁配置，产品固定还是后台可调？
- `viewer_role` 是否可直接复用现有项目角色体系？
- 风险原因文案由后端直接返回，还是前端根据 `risk_type` 组装？
- 跟进行动写接口是否复用现有任务接口，还是新增封装层？

---

## 9. Suggested Next Step

如果继续推进，建议下一步补：

- 风险规则阈值表
- 测试数据样例集
- 前后端联调字段检查单
