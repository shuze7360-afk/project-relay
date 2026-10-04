接力框架已补齐，未执行任何业务任务。

- [AGENTS.md](<local>\test-partial\AGENTS.md:7)：保留原规则，追加阅读顺序、文件职责、状态纪律和维护规则。
- [PROJECT.md](<local>\test-partial\PROJECT.md:1)：新建项目定义，记录范围、交付物、阶段、授权边界及待确认事项。
- [TODO.md](<local>\test-partial\TODO.md:1)：扩展为唯一状态源，映射原有任务、证据、未决问题和下一步。

现有文件映射如下：

- `AGENTS.md` → 接力入口与项目规则。
- `TODO.md` → 承担 `STATE.md` 的职责，因此没有重复新建 `STATE.md`。
- `clean.py` → 待核验业务产物，不作为状态记录。
- `data/*.csv` → 只读输入。
- 原先已勾选的“跳过空行”因没有实际运行证据，映射为“待验收”。

结构检查全部通过；没有创建 `build/`、运行脚本或修改业务代码和数据。

