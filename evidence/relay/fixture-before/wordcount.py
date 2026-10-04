"""wordcount — 统计文本单词频次的极简工具。"""


def count_words(text: str) -> dict:
    """按空白切分并统计单词频次，忽略大小写与首尾标点。"""
    counts = {}
    for word in text.split():
        word = word.strip(".,!?;:\"'()[]").lower()
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(counts: dict, n: int = 3) -> list:
    """返回频次最高的前 n 个 (单词, 次数)，同频按字母序。"""
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
