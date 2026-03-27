# WPS Demand-to-Decision Workflow

这份文档整理了本次 `WPS 项目管理` 从原始需求分析到方案、PRD、工程拆解、评审包的完整工作流。

它的用途有两个：

1. 作为你后续查阅和复用的操作说明
2. 作为团队以后处理新需求池时的标准路径

这不是理论说明文档，而是一份基于本仓库实际产物整理出来的“做过一遍之后的操作手册”。

---

## 1. 这套流程解决什么问题

面对大规模原始需求数据时，团队最常见的问题不是“没有需求”，而是：

- 需求太多，无法直接读完
- 类目很多，但不能直接支持产品决策
- 容易从“用户原话”直接跳到“功能列表”
- 做完统计后，无法自然进入方案设计和 PRD

所以这套流程的核心原则是：

**先把原始需求变成结构化数据，再把数据变成问题空间，再把问题空间变成方案、PRD 和评审材料。**

---

## 2. 整体流程总览

完整路径如下：

1. 原始需求入库
2. 结构化转换
3. 清洗与数据画像
4. 分类结构分析
5. 洞察总结
6. 提炼机会池
7. 选择高优机会
8. 产出方案方向
9. 产出 PRD
10. 产出工程拆解
11. 产出 user stories
12. 产出测试矩阵和 API / 字段定义
13. 产出评审包

换一种更简化的说法：

`raw demand -> structured data -> taxonomy -> insights -> opportunities -> solution -> PRD -> engineering -> review`

---

## 3. 本次输入材料

原始需求文件位于：

- [`research/wps-project-management/raw-input/WPS项目管理个人版需求聚类分析.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/raw-input/WPS项目管理个人版需求聚类分析.md)
- [`research/wps-project-management/raw-input/WPS项目管理企业版需求聚类分析.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/raw-input/WPS项目管理企业版需求聚类分析.md)

本次处理规模：

- 个人版：14130 条
- 企业版：4019 条
- 总计：18149 条

---

## 4. 第一步：把原始 markdown 表转成结构化数据

### 目标

把原始 markdown 表格转成可分析的 CSV 主表，而不是直接在 markdown 里做统计。

### 使用脚本

- [`scripts/wps-demand-markdown-to-csv.py`](/Users/sihuo/workspace/Product-Manager-Skills/scripts/wps-demand-markdown-to-csv.py)

### 执行命令

```bash
python3 scripts/wps-demand-markdown-to-csv.py
```

### 输出结果

- [`wps-demand-master.csv`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/data/wps-demand-master.csv)
- [`wps-demand-personal.csv`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/data/wps-demand-personal.csv)
- [`wps-demand-enterprise.csv`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/data/wps-demand-enterprise.csv)

### 关键做法

统一抽出这些基础字段：

- `edition`
- `source_file`
- `row_id`
- `team_name`
- `demand_text`
- `level_1`
- `level_2`

---

## 5. 第二步：做清洗与数据质量画像

### 目标

先判断哪些数据可直接用，哪些要谨慎使用，哪些应该排除。

### 使用脚本

- [`scripts/wps-demand-clean-and-profile.py`](/Users/sihuo/workspace/Product-Manager-Skills/scripts/wps-demand-clean-and-profile.py)

### 执行命令

```bash
python3 scripts/wps-demand-clean-and-profile.py
```

### 输出结果

- [`wps-demand-master-profiled.csv`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/data/wps-demand-master-profiled.csv)
- [`wps-demand-personal-profiled.csv`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/data/wps-demand-personal-profiled.csv)
- [`wps-demand-enterprise-profiled.csv`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/data/wps-demand-enterprise-profiled.csv)
- [`wps-demand-master-valid-only.csv`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/data/wps-demand-master-valid-only.csv)
- [`demand-cleaning-summary.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/demand-cleaning-summary.md)

### 本次清洗结果

- 总数：18149
- `valid`：13874
- `weak`：3139
- `invalid`：1136

### 当前清洗策略

- `valid`：进入主分析
- `weak`：后续人工抽样复核
- `invalid`：先不进入主分析

### 为什么这一步重要

因为如果不先清洗，就会被下面这些噪音污染：

- `无`
- 空类目
- 数字占位
- 极短且无语义文本

---

## 6. 第三步：定义分析字段规范

### 目标

把“原始需求记录”升级成“可用于产品决策的分析数据集”。

### 字段规范文件

- [`analysis-field-spec.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/analysis-field-spec.md)

### 核心分析字段

- `normalized_scenario`
- `user_role_guess`
- `problem_type`
- `request_type`
- `strategic_relevance`
- `decision_bucket`
- `data_quality`
- `notes`

### 为什么这一步重要

因为：

- 一级类目不是问题空间
- 二级类目也不等于产品机会
- 只有把需求继续提升成场景、角色、问题类型，才能自然进入产品决策

---

## 7. 第四步：做分类结构分析

### 目标

先理解需求池的结构分布，而不是马上做机会判断。

### 输出文档

- [`demand-taxonomy.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/demand-taxonomy.md)

### 这一步做了什么

- 分别看个人版和企业版的一级类目分布
- 看各类目的代表性二级类目
- 做跨版本对比
- 判断当前 taxonomy 的局限

### 本次关键发现

- 两个版本的共性底座都还是 `项目与任务管理`
- 工程、制造、研发是强行业信号
- 个人版和企业版已经出现明显分化
- 当前 taxonomy 更像“业务主题分类”，还不是“问题地图”

---

## 8. 第五步：写洞察总结

### 目标

从统计结果上升到产品判断，但还不直接跳到方案。

### 输出文档

- [`demand-insights-summary.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/demand-insights-summary.md)

### 这一步回答的问题

- 个人版最核心的问题空间是什么
- 企业版最核心的问题空间是什么
- 哪些是共性底座
- 哪些是版本特有需求
- 哪些地方最容易误判

### 本次关键结论

- 共性底座仍然是执行推进
- 企业版更像团队执行系统
- 个人版更像低门槛启动和持续推进的个人执行工具
- 不要被甘特图、看板、台账这些表面功能词带偏

---

## 9. 第六步：提炼机会池

### 目标

把洞察沉淀成可以进入方案设计的“机会空间”。

### 输出文档

- [`top-opportunities.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/top-opportunities.md)

### 本次产出的主要机会

- 企业版执行跟进与风险可见性
- 企业版任务拆解与分工协作
- 个人版项目创建与启动
- 个人版个人规划与持续推进
- 管理汇报与执行可视化
- 企业版应优先服务重执行场景团队

### 这一步的原则

- 写“问题空间”，不写“功能名”
- 写“为什么值得做”，不只写“有多少人提”

---

## 10. 第七步：选一个高优机会进入方案设计

本次选择的机会是：

- **企业版执行跟进与风险可见性**

选择它的原因：

- 企业版高价值机会
- 直接服务执行系统价值
- 问题明确
- 易于进入 MVP 验证

---

## 11. 第八步：产出方案方向

### 输出文档

- [`enterprise-execution-visibility-solution-direction.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-solution-direction.md)

### 这一步做了什么

- 写问题与机会摘要
- 写 feature design 骨架
- 比较多个方案方向
- 给出推荐方案
- 定义第一版 MVP 范围

### 本次方案结论

推荐先做：

- **项目内健康摘要 + 风险任务清单 + 基础跟进行动入口**

不建议第一阶段先做：

- 独立驾驶舱
- 复杂 AI 风险评分
- 管理大报表中心

---

## 12. 第九步：产出 PRD

### 输出文档

- [`enterprise-execution-visibility-prd.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-prd.md)

### 这一步做了什么

- 明确 edition 和场景边界
- 写清问题定义
- 写清角色、对象和状态
- 写清需求、指标、风险和 rollout 计划

### 后续又做了什么

继续把 `Requirements` 细化成：

- 更细的 user stories
- 更具体的 acceptance criteria
- 模块级验收逻辑

---

## 13. 第十步：做工程拆解

### 输出文档

- [`enterprise-execution-visibility-engineering-breakdown.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-engineering-breakdown.md)

### 这一步做了什么

- 拆 MVP 范围
- 拆功能模块
- 写建议的数据对象和字段
- 写 `Health Rule Set v1`
- 写建议 API / service 形态
- 写前端模块拆解
- 写 delivery slices
- 写工程风险

---

## 14. 第十一步：拆 user stories

### 输出文档

- [`enterprise-execution-visibility-user-stories.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-user-stories.md)

### 这一步做了什么

- 提炼 epic hypothesis
- 写 story map
- 给出 release slices
- 写 14 条 user stories
- 给每条 story 配 Gherkin acceptance criteria

---

## 15. 第十二步：补测试和 API 对齐材料

### 输出文档

- 测试矩阵  
  [`enterprise-execution-visibility-test-matrix.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-test-matrix.md)

- API / 字段定义  
  [`enterprise-execution-visibility-api-field-spec.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-api-field-spec.md)

### 这一步做了什么

- 明确测试覆盖范围
- 列核心测试矩阵
- 定义主要对象字段
- 定义接口输入输出
- 定义事件字段

---

## 16. 第十三步：整理评审包

### 输出文档

- [`enterprise-execution-visibility-review-pack.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/enterprise-execution-visibility-review-pack.md)

### 这一步做了什么

- 把上游多份材料压缩成一份评审可读版本
- 重点聚焦：
  - 为什么做
  - 做什么
  - 不做什么
  - 风险是什么
  - 本次会需要做什么决策

---

## 17. 这套流程里用了哪些 WPS skill / command

### 研究和判断层

- [`wps-problem-opportunity-map`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-problem-opportunity-map/SKILL.md)
- [`wps-project-management-strategy`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-strategy/SKILL.md)

### 方案层

- [`wps-feature-design`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-feature-design/SKILL.md)
- [`wps-solution-evaluation`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-solution-evaluation/SKILL.md)
- [`wps-design-solution`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-design-solution.md)

### PRD 和路线图层

- [`wps-project-management-prd`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-project-management-prd/SKILL.md)
- [`wps-write-prd`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-write-prd.md)
- [`wps-quarter-roadmap`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-quarter-roadmap/SKILL.md)
- [`wps-quarter-planning`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-quarter-planning.md)

---

## 18. 以后复用时的最简路径

如果你以后再处理一个新需求池，建议按这个最简顺序复用：

1. 把 raw-input 转成 CSV
2. 做清洗和数据画像
3. 更新 taxonomy 和 insights
4. 提炼 top opportunities
5. 选 1 个高优机会
6. 做 solution direction
7. 做 PRD
8. 做 engineering breakdown
9. 做 stories / test / API
10. 做 review pack

---

## 19. 常见误用

- 直接从 raw-input 跳到路线图
- 用需求数量代替产品判断
- 把类目当问题空间
- 把表面功能词当方案结论
- 没有明确 edition 就开始写 PRD
- 写完 PRD 却没有工程拆解、测试矩阵和 API 定义

---

## 20. 下一步建议

这次完整跑通了一条企业版核心机会。  
如果继续扩展，最自然的下一步有两个：

1. 用同样流程继续推进  
   `企业版任务拆解与分工协作`

2. 把当前这套流程抽象成团队标准：
   - 每次大需求分析必须先做 `taxonomy + insights + opportunities`
   - 每个高优机会必须至少有：
     - solution direction
     - PRD
     - engineering breakdown
     - review pack

如果团队能按这个标准复用，你后面做产品决策的效率和一致性会明显提升。
