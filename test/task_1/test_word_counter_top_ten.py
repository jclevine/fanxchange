from unittest import TestCase
from os.path import relpath, join, abspath
import os
from src.task_1.WordCounter import WordCounter


class WordCounterTopTenTest(TestCase):

    def test_top_ten_in_empty_file(self):
        word_counter = WordCounter(abspath(relpath(join(os.getcwd(), 'test', 'task_1', 'data', 'empty_file.txt'))))
        actual = word_counter.get_top_n_words(10)
        self.assertEqual([], actual)

    def test_top_ten_in_one_word_file(self):
        word_counter = WordCounter(abspath(relpath(join(os.getcwd(), 'test', 'task_1', 'data', 'one_word.txt'))))
        actual = word_counter.get_top_n_words(10)
        self.assertEqual([('hello', 1)], actual)

    def test_top_ten_in_two_words_blank_two_words_file(self):
        word_counter = WordCounter(abspath(relpath(join(os.getcwd(), 'test', 'task_1', 'data', 'two_words_blank_two_words.txt'))))
        actual = word_counter.get_top_n_words(10)
        self.assertEqual([('two', 2), ('with', 1), ('words', 1)], actual)

    def test_top_three_in_file_with_counts_that_cut_off_least_popular_word_file(self):
        word_counter = WordCounter(abspath(relpath(join(os.getcwd(), 'test', 'task_1', 'data', 'top_three.txt'))))
        actual = word_counter.get_top_n_words(3)
        self.assertEqual([('happy', 4), ('joy', 3), ('smiles', 2)], actual)
