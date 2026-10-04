# evidence — 验证证据

本目录存放验证过程的夹具与输出，已脱敏（本机路径统一替换为 `<local>`）。复跑方法见上级 [VALIDATION.md](../VALIDATION.md)。

| 条目 | 内容 |
|---|---|
| `check-format.py` | 结构检查脚本（用法：`python evidence/check-format.py <仓库根目录>`） |
| `generality-learning/` | 科研项目启动框架产物（仅三核心文件） |
| `generality-software/` | 软件项目启动框架产物（仅三核心文件） |
| `merge/` | 已有规则仓库的局部合并：before / after / NOTES.md（diff 显示原规则零删除） |
| `relay/` | 接力实测：`fixture-before/`（预埋过时记录、缺证据、阻塞任务、外部动作结果不明四类陷阱）、`result-diff.txt`、`last-message.md`、`prompt.txt` |
| `partial-records/` | 部分记录（仅有 AGENTS.md + TODO.md）补齐路径实测 |
| `fact-labeling/` | 用户未核实说法的信息分级实测 |
| `external-review-2026-10-04.md` | 第三方审查报告脱敏转载 |

行为实测统一条件：Codex CLI 0.153.4，`codex exec --sandbox workspace-write`，模型 `gpt-5.6-sol`（reasoning effort high），夹具目录互相隔离，被测智能体无历史对话。
