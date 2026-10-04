# 设计来源（2026-10-04 检索）

本 Skill 只提炼方法，不安装上游框架、不引入其审批流/钩子/软件开发专用流程。以下链接与版本是设计时的参考依据，日常使用本技能不需要联网。

| 来源 | 版本（检索时） | 提炼要点 | 未采纳 |
|---|---|---|---|
| [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | superpowers v6.4.1，main@5bf4e78（2026-09-19，skills/brainstorming/SKILL.md 路径最新提交） | 一次一题澄清意图；需求转设计；信息充分即停止提问 | 其完整头脑风暴阶段流程与审批环节 |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | v3.22.0，main@dab9d16（2026-10-01） | 用文件持久化项目状态；恢复后先重新核对实际进度再继续 | 其面向软件开发的计划文件模板 |
| [advise-project-approach](https://github.com/AaravKashyap12/advise-project-approach) | v0.7.2，main@abdde26（2026-08-30） | 方案选择基于实际约束；明确区分证据与不确定性 | 其建议式问答的输出结构 |

## 第一版范围决定

只覆盖：通用项目、同一本地目录、顺序接力、核心文件（AGENTS.md/PROJECT.md/STATE.md）+ 按需专题扩展。

明确不做：多项目路由、跨目录接力、并行任务协调、自动化钩子、联网检索（启动每个项目时不强制搜索）。

维护方式：第一版依靠智能体遵守项目入口里的规则完成更新，不保证突发中断前的每一步都已保存，也不承诺消除上下文限制。
