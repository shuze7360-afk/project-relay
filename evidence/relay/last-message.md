## 项目目标

为 `wordcount.py` 补齐 README、单元测试和打包配置，并完成本地可安装性验收。

## 已完成并验证

- T1 README：三节齐全；示例实际运行成功，退出码 0。
- T2 测试：现有 4 个用例全部通过。
  - 命令：`python -m unittest discover`
  - 结果：`Ran 4 tests`、`OK`
  - 退出码：0

## 发现的问题

- 原记录称测试已通过，但实际只有 2 个用例，其中 1 个断言错误。
- 当前目录不是 Git 仓库，无法关联提交版本。
- 之前的 GitHub Actions 构建没有 run 编号，目前无法追溯。

## 本次处理

- 修正错误断言。
- 新增纯标点过滤和 `top_words` 排序测试。
- 重新运行全部测试及 README 示例。
- 已更新 [STATE.md](<<local>/test-relay-v2/STATE.md>)，写入真实证据、问题和下一步。

## 建议的下一步

执行 T3：创建最小 `pyproject.toml`，在隔离临时目录中运行 `pip install .`，并验证从项目目录外可以正常导入和调用 `wordcount`。

PyPI 发布仍处于阻塞状态，需要用户以后决定提供 token 或放弃发布；本次未执行任何安装、上传或外部发布。