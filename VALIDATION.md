# VALIDATION — 验证记录

本文件的唯一目的：让 README 里的每一条验证结论都可追溯到输入、方法、输出与限制，并且可复跑。证据文件在 [evidence/](evidence/)，脱敏说明见 [evidence/README.md](evidence/README.md)。

## 如何复跑

| 验证 | 复跑方法 |
|---|---|
| 结构校验 | `python evidence/check-format.py <仓库根目录>`；SKILL 官方校验工具亦通过（2026-10-04，输出 `Skill is valid!`，退出码 0） |
| 通用性 | 对比 `evidence/generality-learning/` 与 `evidence/generality-software/` 的三文件：结构同构、内容随目标分化 |
| 合并 | 对比 `evidence/merge/before-AGENTS.md` 与 `after-AGENTS.md`：原有规则零删除（见 `merge/` 与 diff 断言） |
| 接力 | 把 `evidence/relay/fixture-before/` 复制到空目录，将 `evidence/relay/prompt.txt` 交给任意无历史对话的智能体，应复现 `result-diff.txt` 所示行为 |
| 部分记录 | 同法使用 `evidence/partial-records/`（夹具 = 仅有 AGENTS.md + TODO.md + 业务文件；`after/` 保存完整结果快照） |
| 映射服从 | 把 `evidence/mapped-records/fixture-before/`（状态=TODO.md、定义=BRIEF.md，含过期证据）复制到空目录，将 `prompt.txt` 交给任意智能体：应只按映射更新 TODO.md（任务降级并附实际核验结果），不新建 STATE.md/PROJECT.md、不动业务文件 |
| 事实标注 | 将 `evidence/fact-labeling/prompt.txt` 交给任意智能体，检查生成 PROJECT.md 的信息分级 |

行为实测统一条件：Codex CLI 0.153.4，`codex exec --sandbox workspace-write`（审批关闭），模型 `gpt-5.6-sol`（reasoning effort high），夹具目录互相隔离，被测智能体无历史对话、不加载本仓库以外的提示。

## 结果（v1.1，2026-10-04）

| # | 验证 | 关键断言 | 结果 | 证据 |
|---|---|---|---|---|
| 1 | 结构校验 | 官方校验与自有检查（frontmatter / 触发词 / 链接 / 占位符 / 行数）全部通过 | 通过 | `check-format.py`；quick_validate 输出 `Skill is valid!` |
| 2 | 合并 | 已有 AGENTS.md 局部合并：原 4 条规则零删除零改写（diff 内容删除行 = 0，由 6 行增至 33 行，新增 27 行，原 6 行规则为完整前缀）；NOTES.md 仅链接引用、原文未动 | 通过 | `merge/` |
| 3 | 接力（收紧规则后） | 接棒者发现"记录称测试已通过、实际仅 2 用例且 1 失败"；修正并补用例；完成条目附实际执行结果（`Ran 4 tests`、`OK`、退出码 0），并对 README 示例实际运行留证；阻塞任务（PyPI 发布）未触碰；无编号的外部 CI 动作不重复执行、查不到回执如实记录 | 通过 | `relay/` |
| 4 | 部分记录补齐 | 目录仅有 AGENTS.md + TODO.md 时：不执行业务（`build/` 未产生、业务代码与数据未动）；TODO.md 按实际用途映射为唯一状态源（未新建重复 STATE.md，映射写入 AGENTS.md）；原 `[x]` 勾选因无运行证据降级为"待验收"；下一步四要素齐全 | 通过 | `partial-records/`（fixture-before + 完整 after 快照，result-diff 含新建 PROJECT.md 全文） |
| 5 | 事实标注 | 用户转述的"快排一定比冒泡快得多"标为【用户提供·未核实】并改写为待验证主张；方案保留两种算法公平对比，用户偏好记录为【用户要求】；未编造数据；只建三文件框架 | 通过 | `fact-labeling/` |
| 6 | 映射服从（含过期证据反例） | 状态=TODO.md、定义=BRIEF.md 的项目：接棒者按映射读取三个记录；实跑 `python verify.py` 得 `expected=60 actual=30`、退出码 1，据此把标记"完成"的任务降级为未通过并附本次实际结果与业务文件 SHA-256 前后比对；**仅更新 TODO.md**，未新建 STATE.md/PROJECT.md，未动 data.csv/report.txt/verify.py；新下一步四要素且以"取得修改业务文件授权"为前提 | 通过 | `mapped-records/`（fixture-before + after + result-diff + last-message） |

## 历史记录（v1.0，2026-10-04）

初版验证（结构、通用性、接力、合并）由仓库作者完成；其中结构、合并、接力已被上表 v1.1 重验覆盖；通用性的两套框架夹具随包提供（`generality-*`），当时的生成过程未随包保存运行日志，该条按"夹具可复核"对待。

## 外部审查：第一轮（2026-10-04）

第三方以三个子智能体（静态复核、启动、冷启动接力）完成受控验证：正常启动与接力路径通过（含产物独立复算）；同时指出 4 项缺口。处置映射：

| 审查缺口 | 修正 | 重验落点 |
|---|---|---|
| P1 完成证据允许"验证命令"充当已验证结果；冲突处理过度相信现有产物 | 完成 = 实际执行结果或用户明确验收，且对应当前版本的输入、产物与验收条件；"实际产物不会撒谎"改为"产物是核验对象，不自动等于正确结果" | 上表 #3、#4（`[x]` 无证据降级） |
| P2 只有部分记录时无可执行的复用/补齐路径 | 启动区分空目录 / 三件套齐全 / 部分记录三种情况；部分记录按实际用途映射职责并写入入口，是否执行业务由用户当前请求决定 | 上表 #4 |
| P2 用户陈述直接标为事实，固化未验证前提 | 信息四分类：【用户要求】/【用户提供·未核实】/【已验证】/【假设】；阶段方案由目标、已验证事实、硬约束、待验证假设推导，用户实现路径非硬约束时列为候选 | 上表 #5 |
| P2 README 既有实测结论无可追溯证据 | 新增本文件与 `evidence/`，README 验证章节改为指向本文件 | 本文件 |

审查报告脱敏转载：[evidence/external-review-2026-10-04.md](evidence/external-review-2026-10-04.md)。

## 外部审查：第二轮（2026-10-04）

对象为提交 720c0cd（v1.1）。结论：核心修复有效，指出 3 项收尾问题。处置：

| 二轮问题 | 修正 | 复验落点 |
|---|---|---|
| P2 README 仍传达已废止的验收规则（"验证命令或输出"充当证据、"以实际为准"） | 接力纪律两条改为现行规则摘要，声明 SKILL.md/file-conventions.md 为唯一规范来源；check-format.py 新增规范一致性回归检查（废弃措辞不得再现） | 上表 #1 |
| P2 主入口固定"三文件"措辞与职责映射不一致（可能重建第二份状态/定义文件） | 启动步骤改为"创建或更新承担三职责的记录，只补缺失职责"；维护/恢复/授权各步骤统一按入口映射读写；标准名仅为空项目默认值 | 上表 #6（映射服从行为实测） |
| P2 部分记录证据缺件（新建 PROJECT.md 只有 "Only in" 行）；合并新增行数说明不准（22 → 实为 27） | 补交完整 after 快照；result-diff 改用 `diff -ruN` 含新建文件全文；行数说明修正；新增 MANIFEST.sha256 与版本/调用条件 | 上表 #4、#2 |

审查方本轮独立验证：映射项目组合反例（状态=TODO.md、定义=BRIEF.md、输入变化导致旧证据过期）通过——执行者实跑校验得 expected=60 actual=30、退出码 1，任务退回待验收，未双写状态文件。仓库作者在 v1.2 规则文本上复现同场景，结果一致（上表 #6）。报告脱敏转载：[evidence/external-review-2-2026-10-04.md](evidence/external-review-2-2026-10-04.md)。

## 版本与调用条件

规范文件 SHA-256（v1.2 工作区文件，对应 git 历史中的 v1.2 提交）：

```
339e94d26364de878b29ab03dcc83e0e318cdfad41ce3ffdbb5ecd9c5c991db0  SKILL.md
773be939beef20c2d136b2733a1800a8d2334eb44f76a9b453d74b5c11441724  README.md
ea3bf63b4d5d0d54638823c14bedce0a3b2a6e2962986db53a50c0427463760a  references/file-conventions.md
93e7741486fe4055381d688e5bc3a30480cb2e13ae841671806f6a177b483b99  references/sources.md
```

行为验证的版本与调用条件：

| 验证 | 被测规则版本 | 夹具来源 | 调用 |
|---|---|---|---|
| #3 接力 | v1.1 规则文本（内容 = 提交 720c0cd 的 SKILL/references） | 仓库作者生成（wordcount 工程化，四类陷阱） | codex exec，gpt-5.6-sol / high |
| #4 部分记录 | v1.1 规则文本 | 仓库作者生成（仅 AGENTS.md + TODO.md） | 同上 |
| #5 事实标注 | v1.1 规则文本 | 仓库作者生成（空目录 + 含未核实说法的启动请求） | 同上 |
| #6 映射服从 | v1.2 规则文本（上列哈希） | 复用二次外部审查的 mapped-before 夹具（审查方设计，含过期证据反例） | 同上 |

证据完整性：每个行为验证目录的文件哈希见 [evidence/MANIFEST.sha256](evidence/MANIFEST.sha256)。已由外部复核的条目：#3 的修复后测试产物（第三方在独立目录应用 result-diff 并复跑 unittest，4 用例通过）；#4 曾因缺件被指出，本轮补全。

## 未验证 / 边界

- 未实测：真实 ZCode 等其他智能体工具的加载与遵守情况、突发中断恢复、跨目录/并行接力、外部提交超时与回执恢复、旧记录完整迁移闭环（本次仅验证补齐路径）。
- 行为实测基于 `gpt-5.6-sol`（high）及作者会话内的自测，不构成对所有模型、所有工具的兼容性认证。
- 第一版维护依靠智能体遵守项目入口规则：不保证突发中断前的每一步都已保存，不承诺消除上下文限制。
