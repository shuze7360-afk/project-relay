import unittest

from wordcount import count_words, top_words


class TestCountWords(unittest.TestCase):
    def test_basic_count(self):
        self.assertEqual(count_words("apple banana apple"), {"apple": 2, "banana": 1})

    def test_repeated_words(self):
        self.assertEqual(count_words("Hello, hello WORLD"), {"hello": 3, "world": 1})
