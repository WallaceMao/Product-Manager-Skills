# WPS Demand Analysis Workflow

这个目录用于承接 `raw-input/` 下两份原始需求文件的结构化整理、分析和洞察输出。

目标不是只做“需求统计”，而是把原始需求转成可以用于产品决策的分析资产。

---

## 推荐工作顺序

### 1. 原始数据结构化

先把 markdown 表转成 CSV：

```bash
python3 scripts/wps-demand-markdown-to-csv.py
```

输出目录：

- `data/wps-demand-personal.csv`
- `data/wps-demand-enterprise.csv`
- `data/wps-demand-master.csv`

---

### 2. 数据清洗

对 `wps-demand-master.csv` 做以下处理：

- 删除无效值
- 标记脏数据
- 统一类目
- 去重
- 补充分析字段

字段说明见：

- [`analysis-field-spec.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/analysis-field-spec.md)

---

### 3. 先分版分析，再合并比较

不要一开始把个人版和企业版混在一起。

先分别回答：

- 个人版用户最集中卡在哪些问题上
- 企业版用户最集中卡在哪些协作和管理问题上

再回答：

- 哪些问题是共性底座
- 哪些问题是版本特有

---

### 4. 产出 3 份核心分析文档

- [`demand-taxonomy.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/demand-taxonomy.md)
- [`demand-insights-summary.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/demand-insights-summary.md)
- [`top-opportunities.md`](/Users/sihuo/workspace/Product-Manager-Skills/research/wps-project-management/synthesis/top-opportunities.md)

---

### 5. 把分析结果送入产品工作流

建议使用顺序：

1. `top-opportunities.md` -> [`wps-problem-opportunity-map`](/Users/sihuo/workspace/Product-Manager-Skills/skills/wps-problem-opportunity-map/SKILL.md)
2. 进入 [`wps-design-solution`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-design-solution.md)
3. 进入 [`wps-write-prd`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-write-prd.md)
4. 最后进入 [`wps-quarter-planning`](/Users/sihuo/workspace/Product-Manager-Skills/commands/wps-quarter-planning.md)

---

## 判断原则

- 高频不等于高价值
- 大客户表达不等于普遍场景
- 功能词不等于问题空间
- 需求分析的目标不是“列功能”，而是“识别问题与机会”

---

## 当前目录建议

```text
synthesis/
  README.md
  analysis-field-spec.md
  demand-taxonomy.md
  demand-insights-summary.md
  top-opportunities.md
  data/
    wps-demand-master.csv
    wps-demand-personal.csv
    wps-demand-enterprise.csv
```
