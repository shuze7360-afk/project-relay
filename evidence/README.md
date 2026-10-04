# evidence — 验证证据

本目录存放验证过程的夹具与输出，已脱敏（本机路径统一替换为 `<local>`）。复跑方法见上级 [VALIDATION.md](../VALIDATION.md)。

| 条目 | 内容 |
|---|---|
| `check-format.py` | 结构检查脚本（用法：`python evidence/check-format.py <仓库根目录>`） |
| `generality-learning/` | 科研项目启动框架产物（仅三核心文件） |
| `generality-software/` | 软件项目启动框架产物（仅三核心文件） |
| `merge/` | 已有规则仓库的局部合并：before / after / NOTES.md（diff 显示原规则零删除） |
| `relay/` | 接力实测：`fixture-before/`（预埋过时记录、缺证据、阻塞任务、外部动作结果不明四类陷阱）、`result-diff.txt`、`last-message.md`、`prompt.txt` |
| `partial-records/` | 部分记录（仅有 AGENTS.md + TODO.md）补齐路径实测：`fixture-before/`、完整 `after/` 快照、`result-diff.txt`（`-N` 模式，含新建 PROJECT.md 全文）、`last-message.md`、`prompt.txt` |
| `fact-labeling/` | 用户未核实说法的信息分级实测 |
| `mapped-records/` | 映射服从实测（状态=TODO.md、定义=BRIEF.md，含过期证据反例）：`fixture-before/`、`after/`（模型原始输出，任务状态措辞含已注明偏差）、`after-revised-TODO.md`（明确标记的人工修订示例）、`result-diff.txt`、`last-message.md`、`prompt.txt` |
| `MANIFEST.sha256` | 本目录全部文件的 SHA-256 清单（不含自身） |
| `external-review-2026-10-04.md` | 第一轮审查报告脱敏转载 |
| `external-review-2-2026-10-04.md` | 第二轮审查报告脱敏转载（v1.1 复查） |
| `external-review-3-2026-10-04.md` | 第三轮审查报告脱敏转载（v1.2 复查）；`external-review-3-checks.json` 为其 61 文件哈希校验记录 |

行为实测统一条件：Codex CLI 0.153.4，`codex exec --sandbox workspace-write`，模型 `gpt-5.6-sol`（reasoning effort high），夹具目录互相隔离，被测智能体无历史对话。
