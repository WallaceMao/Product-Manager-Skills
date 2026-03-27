# Domain Terminology

## Purpose

这份文档用于统一产品领域术语，避免团队和 AI 在以下问题上各说各话：

- 同一个词指代不同东西
- 不同的人用不同词指代同一个对象
- 方案文档、PRD、埋点、设计稿里的术语不一致

术语一致不是文档洁癖，而是产品设计、研发实现、数据定义和跨团队沟通的基础。

---

## Usage Rules

- 优先记录产品内真实使用的词，而不是理论上更优雅的词
- 明确“推荐用词”和“避免混用词”
- 如需中英混用，写清标准写法
- 如果词语在不同上下文里含义不同，必须拆开说明

---

## Terminology Table

```md
| Term | Chinese Name | Working Definition | Use When | Avoid Confusing With | Notes |
| --- | --- | --- | --- | --- | --- |
| project | 项目 |  |  |  |  |
| task | 任务 |  |  |  |  |
| milestone | 里程碑 |  |  |  |  |
```

---

## Core Object Definitions

建议优先覆盖这些对象。

```md
### Object Name
- 中文名称：
- 定义：
- 在产品中的作用：
- 生命周期 / 状态：
- 与其他对象的关系：
- 常见误解：
```

优先对象示例：

- 项目
- 任务
- 子任务
- 里程碑
- 模板
- 视图
- 成员
- 负责人
- 评论
- 提醒
- 状态
- 优先级

---

## Role and Permission Terminology

如果产品涉及协作，角色和权限词汇必须统一。

- 管理员
- 创建者
- 项目负责人
- 成员
- 观察者 / 访客
- 协作者

**模板：**

```md
### Role / Permission Term
- 定义：
- 拥有哪些关键权限：
- 不具备哪些权限：
- 容易混淆的点：
```

---

## Workflow Terms

记录描述流程和状态的关键词。

- 创建
- 指派
- 开始
- 阻塞
- 完成
- 归档
- 延期
- 升级
- 汇报
- 复盘

对每个词补充：

- 是否有系统含义
- 是否对应可操作动作
- 是否对应埋点事件

---

## Product Language Guidelines

写清产品和文档里的命名约束。

- 哪些词适合给用户看
- 哪些词只用于内部研发 / 埋点 / 数据
- 哪些词不应该出现在面向用户的界面中
- 是否有固定大小写 / 中英文写法

---

## Synonyms and Forbidden Terms

```md
| Preferred Term | Avoid / Deprecated Term | Why |
| --- | --- | --- |
|  |  |  |
```

例如：

- 推荐“项目负责人”，避免混用“owner”“主责人”“管理人”
- 推荐“归档”，避免和“删除”混用

---

## Open Naming Questions

- **术语待确认问题 1：**
- **术语待确认问题 2：**
- **术语待确认问题 3：**

---

## Change Log

- **日期：**
- **修改人：**
- **变更内容：**
