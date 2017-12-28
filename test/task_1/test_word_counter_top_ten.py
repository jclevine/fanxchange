from unittest import TestCase
from os.path import relpath, join
from src.task_1.WordCounter import WordCounter


class WordCounterTopTenTest(TestCase):

    def test_top_ten_in_empty_file(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'empty_file.txt')))
        actual = word_counter.get_top_n_words(10)
        self.assertEqual([], actual)

    def test_top_ten_in_one_word_file(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'one_word.txt')))
        actual = word_counter.get_top_n_words(10)
        self.assertEqual([('hello', 1)], actual)
