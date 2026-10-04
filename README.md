# project-relay（项目启动与接力）

> 用三个 Markdown 文件把项目状态固定在项目目录里，让任何没有历史对话的智能体（或新会话）只读文件，就能核对进度、继续工作。

A lightweight, model-agnostic project-handoff convention: three Markdown files (`AGENTS.md` / `PROJECT.md` / `STATE.md`) that let any fresh AI session pick up exactly where the last one left off — usable as a Codex CLI Skill, or as copy-paste prompts with any AI.

## 为什么需要

AI 协作项目最常见的两个断点：

- **换会话就丢上下文**：上次聊到哪、决定了什么、下一步是什么，全在对话历史里，换了工具或新开会话就归零；
- **记录不可信**：AI 说"已完成"，但产物没核过、证据没留，接手的人不敢直接用。

project-relay 用两条纪律解决：**状态落成文件**（不依赖会话历史），**完成必须附证据**（"已生成"≠"已完成验收"）。

## 三个核心文件

| 文件 | 唯一职责 |
|---|---|
| `AGENTS.md` | 项目入口：阅读顺序、文件职责、执行与更新规则 |
| `PROJECT.md` | 项目定义：目标、范围、交付物与验收标准、约束与授权、阶段方案、关键决定 |
| `STATE.md` | 当前状态：任务进度、产物与验证证据、阻塞、未决问题、下一步 |

按实际需要增加专题文件（实验记录、练习验收、架构说明等），每个必须有明确用途并从核心文件链接进入。

## 安装

**作为 Skill 使用**（推荐）：把整个目录复制到你的技能目录，例如 Codex CLI：

```bash
git clone https://github.com/<owner>/project-relay.git ~/.codex/skills/project-relay
```

任何兼容 `SKILL.md` 格式（YAML frontmatter：`name` + `description`）的智能体工具都可以用同样方式安装。

**不装 Skill 也能用**：把 `SKILL.md` 里的工作流直接贴给任何 AI 当系统提示词，或按下面的触发词人工驱动。

## 使用

装好 Skill 后，三个自然语言触发词：

| 你说 | AI 做 |
|---|---|
| "启动项目：我想做××" | 逐题澄清（最多六题、一次一题）→ 生成三文件框架 → 展示后停止，不自动开工 |
| "继续项目" / "接着上次的做" | 读入口与状态 → 核对实际产物 → 在既有授权内执行下一步 → 更新记录 |
| "准备交接" | 补齐证据、写明卡点、把下一步写成可直接执行的四要素 |

**触发词之外，维护是自动的**：完成一个可验收步骤、改变关键决定、遇到阻塞、准备交接时，AI 会主动更新 `STATE.md`，不需要你说"保存进度"。

## 接力纪律

这套约定能跨智能体生效，靠的是写进 `AGENTS.md` 的最低规则集：

- 任务只有五种状态：**待做 / 进行中 / 待验收 / 完成 / 阻塞**；
- 待验收 → 完成必须有**对应当前输入与产物的实际核验结果**（运行输出、退出码）或用户明确验收；只写命令没执行、证据过期或对不上产物的，保持待验收；
- 下一步四要素：**行动、所需输入、预期产物、完成条件**——禁止"继续完善"式空话；
- 外部动作（提交、发布、触发构建）查到回执才算完成，结果不明先查回执，不重复执行；
- 记录与实际冲突：产物只是核验对象，不自动等于正确结果——先核对或重验受影响部分，再修正记录继续；
- 记录职责可映射到已有文件（如 TODO.md 承担状态、BRIEF.md 承担定义），标准文件名只是空项目默认值，不建两套状态源；
- 已有 `AGENTS.md` 的项目局部合并，原有规则一行不改。

本节是摘要；完整规范以 [SKILL.md](SKILL.md) 与 [references/file-conventions.md](references/file-conventions.md) 为唯一来源。

详细结构规范见 [references/file-conventions.md](references/file-conventions.md)。

## 验证

验证协议、结果与证据见 [VALIDATION.md](VALIDATION.md)；可复核的夹具与输出在 [evidence/](evidence/)。时间线：

- **2026-10-04 初版**：结构校验、两类项目通用性、无历史会话接力实测、合并验证（历史记录，见 VALIDATION.md）；
- **2026-10-04 外部审查**：第三方以受控子智能体复核，正常启动/接力路径通过，同时指出 4 项规则缺口（完成证据条件、部分记录接入、用户陈述误标事实、验证结论不可追溯），脱敏转载见 [evidence/external-review-2026-10-04.md](evidence/external-review-2026-10-04.md)；
- **2026-10-04 v1.1**：修正 4 项缺口并重验受影响场景（结构校验、合并、接力、部分记录补齐、事实标注），结果与证据见 VALIDATION.md；
- **2026-10-04 v1.2**：二次外部审查指出 3 项收尾问题（README 残留旧规则、主入口固定文件名与职责映射不一致、部分记录证据缺件），已统一规则措辞、补全 after 快照、新增映射服从行为实测——见 VALIDATION.md。

边界：维护依靠智能体遵守入口规则，不保证突发中断前的每一步都已保存，也不承诺消除上下文限制；结构检查与行为实测分别报告，未实测的工具不宣称兼容。

## 设计来源

方法论提炼自三个开源项目，未引入其框架代码：

- [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) — 一次一题澄清意图
- [planning-with-files](https://github.com/OthmanAdi/planning-with-files) — 文件保存状态、恢复先核对
- [advise-project-approach](https://github.com/AaravKashyap12/advise-project-approach) — 按实际约束选方案

版本与提交哈希记录见 [references/sources.md](references/sources.md)。

## License

未附开源许可证，默认保留所有权利。
