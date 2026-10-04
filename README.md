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
- 待验收 → 完成必须附证据（产物路径 + 验证命令或输出，或用户确认）；
- 下一步四要素：**行动、所需输入、预期产物、完成条件**——禁止"继续完善"式空话；
- 外部动作（提交、发布、触发构建）查到回执才算完成，结果不明先查回执，不重复执行；
- 记录与实际冲突：以实际为准，先修正记录再继续；
- 已有 `AGENTS.md` 的项目局部合并，原有规则一行不改。

详细结构规范见 [references/file-conventions.md](references/file-conventions.md)。

## 验证

2026-10 完成的验证（结构与接力实测分别报告）：

- **结构检查**：frontmatter、触发词、链接、占位符、行数全部通过；
- **通用性**：科研项目（可复现实验验收）与软件项目（依赖约束验收）各生成一套框架，内容随目标分化，无虚构信息；
- **独立接力实测**：让一个没有历史对话的智能体只凭项目文件接手半成品项目，成功识别记录与实际的冲突（记录称测试通过、实际失败）、补齐证据、不越过阻塞任务、对外部动作先查回执不重复执行、更新后的下一步含四要素；
- **合并验证**：在已有规则的仓库生成新框架，原有规则零删除零改写。

边界：维护依靠智能体遵守入口规则，不保证突发中断前的每一步都已保存，也不承诺消除上下文限制。

## 设计来源

方法论提炼自三个开源项目，未引入其框架代码：

- [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) — 一次一题澄清意图
- [planning-with-files](https://github.com/OthmanAdi/planning-with-files) — 文件保存状态、恢复先核对
- [advise-project-approach](https://github.com/AaravKashyap12/advise-project-approach) — 按实际约束选方案

版本与提交哈希记录见 [references/sources.md](references/sources.md)。

## License

未附开源许可证，默认保留所有权利。
