# Constraints and Assumptions

## Purpose

这份文档用于明确产品工作中默认成立的前提和已经存在的约束，避免后续在战略、方案和 PRD 里反复出现这些问题：

- 方案看起来很好，但依赖的前提其实不成立
- 团队默认某个能力可用，实际上当前做不到
- 讨论时把“愿望”当“现实”

一个成熟的产品团队，不只是会提方案，也会把约束显性化。

---

## Working Principles

- 区分“约束”和“假设”
- 区分“当前已确认”和“待验证”
- 区分“短期不可变”和“中期可争取”

定义建议：

- **Constraint：** 当前客观存在、短期不能忽略的边界
- **Assumption：** 当前用于推进判断的前提，但还需要证据验证

---

## Constraint Categories

建议从以下维度梳理。

### Business Constraints

- 商业模式限制
- 收费能力限制
- 客户类型限制
- 销售策略限制

### Organizational Constraints

- 团队人数
- 研发带宽
- 跨团队协同难度
- 决策链路

### Technical Constraints

- 现有架构
- 平台能力
- 兼容性
- 数据可用性
- 性能与稳定性边界

### Product Constraints

- 历史交互包袱
- 已有对象模型
- 已上线用户习惯
- 多端一致性要求

### Legal / Compliance Constraints

- 数据安全
- 权限边界
- 企业客户合规要求

---

## Constraint Template

```md
### Constraint Name
- 类型：
- 描述：
- 为什么它存在：
- 会限制哪些产品决策：
- 严重程度：
  - 高 / 中 / 低
- 预计持续时间：
- 是否可缓解：
- 缓解方式：
```

---

## Key Assumptions

写当前产品判断所依赖的关键前提。

```md
### Assumption Name
- 假设内容：
- 为什么现在先这样假设：
- 若成立，意味着：
- 若不成立，意味着：
- 当前证据：
- 需要怎样验证：
- 验证优先级：
```

---

## Assumption Register

```md
| Assumption | Category | Current Evidence | Risk if Wrong | Validation Plan | Priority |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
```

---

## Non-Negotiables

明确当前阶段绝对不能突破的边界。

- **不可突破边界 1：**
- **不可突破边界 2：**
- **不可突破边界 3：**

例如：

- 不破坏现有核心协作链路
- 不引入高培训成本的复杂能力
- 不在未解决权限模型前上线跨组织协作能力

---

## Flexible Constraints

写那些“目前受限，但如果价值足够可以争取”的点。

- **可争取项 1：**
- **可争取项 2：**
- **可争取项 3：**

---

## Decision Impact Summary

总结这些约束和假设会如何影响产品策略与功能设计。

- 对战略范围的影响：
- 对功能优先级的影响：
- 对上线节奏的影响：
- 对验证方式的影响：

---

## Signals That Assumptions Are Breaking

- **信号 1：**
- **信号 2：**
- **信号 3：**

这部分很有用，因为它能帮助团队尽早发现“原来我们的前提已经失效了”。

---

## Sources

- 管理层输入：
- 技术评估：
- 架构文档：
- 客户反馈：
- 商业化要求：
- 法务 / 安全要求：

---

## Open Questions

- **约束待确认问题 1：**
- **约束待确认问题 2：**
- **约束待确认问题 3：**

---

## Change Log

- **日期：**
- **修改人：**
- **变更内容：**
