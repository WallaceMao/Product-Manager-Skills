# Demand Cleaning Summary

## Overview

- Input file: `research/wps-project-management/synthesis/data/wps-demand-master.csv`
- Total rows: 18149
- Valid rows: 13874
- Weak rows: 3139
- Invalid rows: 1136

## Quality by Edition

| Edition | Valid | Weak | Invalid |
| --- | --- | --- | --- |
| enterprise | 3081 | 642 | 296 |
| personal | 10793 | 2497 | 840 |

## Top Quality Flags

| Flag | Count |
| --- | --- |
| missing_level_1 | 3796 |
| missing_level_2 | 3796 |
| very_short_text | 1906 |
| no_chinese_text | 1262 |
| digits_only | 932 |
| invalid_literal | 926 |
| empty_text | 11 |

## Top Level-1 Categories by Edition

### personal

| Level 1 | Count |
| --- | --- |
| 项目与任务管理 | 3209 |
| 无 | 1921 |
| 工程与施工管理 | 1108 |
| (empty) | 1023 |
| 生产与制造管理 | 1012 |
| 研发与产品管理 | 912 |
| 协同办公与流程审批 | 862 |
| 客户、销售与订单 | 621 |
| 财务、合同与结算 | 593 |
| 数据分析与经营看板 | 579 |
| 人力与组织管理 | 364 |
| 质量、安全与合规 | 360 |

### enterprise

| Level 1 | Count |
| --- | --- |
| 项目与任务管理 | 1047 |
| 无 | 653 |
| 工程与施工管理 | 436 |
| 研发与产品管理 | 313 |
| 生产与制造管理 | 259 |
| 协同办公与流程审批 | 209 |
| 客户、销售与订单 | 206 |
| (empty) | 199 |
| 财务、合同与结算 | 196 |
| 数据分析与经营看板 | 144 |
| 人力与组织管理 | 128 |
| 服务、工单与运维 | 100 |

## Outputs

- `research/wps-project-management/synthesis/data/wps-demand-master-profiled.csv`
- `research/wps-project-management/synthesis/data/wps-demand-personal-profiled.csv`
- `research/wps-project-management/synthesis/data/wps-demand-enterprise-profiled.csv`
- `research/wps-project-management/synthesis/data/wps-demand-master-valid-only.csv`

## Notes

- `invalid` means the row is very likely unusable without manual recovery.
- `weak` means the row may still hold signal, but category or text quality is poor.
- `valid-only` should not be treated as the final truth set; it is a convenience cut for faster analysis.
