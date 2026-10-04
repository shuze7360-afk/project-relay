# wordcount

统计文本中单词出现频次的极简工具。

## 简介
`wordcount.py` 提供两个函数：`count_words(text)` 按空白切分统计频次（忽略大小写与首尾标点），`top_words(counts, n)` 返回频次最高的前 n 项。

## 安装
无需安装第三方依赖（纯标准库）。将 `wordcount.py` 放入你的项目或 PYTHONPATH 即可；打包版可用 `pip install .` 安装。

## 用法示例
```python
from wordcount import count_words, top_words

counts = count_words("apple banana apple")
print(counts)            # {'apple': 2, 'banana': 1}
print(top_words(counts)) # [('apple', 2), ('banana', 1)]
```
