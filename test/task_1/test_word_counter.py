from unittest import TestCase
from os.path import relpath, join
from src.task_1.WordCounter import WordCounter


class WordCounterTest(TestCase):
    def test_file_not_found(self):
        self.assertRaisesRegexp(IOError, '.*No such file', WordCounter, relpath(join('task_1', 'dne.txt')))

    def test_counting(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'empty_file.txt')))
        actual = word_counter.count
        self.assertEqual(0, actual)

    def test_one_word_on_one_line(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'one_word.txt')))
        actual = word_counter.count
        self.assertEqual(1, actual)

    def test_one_word_on_one_line_with_extra_spaces_pre_and_postpended(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'one_word_with_spaces.txt')))
        actual = word_counter.count
        self.assertEqual(1, actual)

    def test_two_words_on_one_line(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'two_words.txt')))
        actual = word_counter.count
        self.assertEqual(2, actual)

    def test_two_words_on_one_line_with_extra_spaces_pre_and_postpended(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'two_words_with_spaces.txt')))
        actual = word_counter.count
        self.assertEqual(2, actual)

    def test_two_words_on_one_line_with_extra_spaces_pre_and_postpended(self):
        word_counter = WordCounter(relpath(join('task_1', 'data', 'two_words_with_spaces.txt')))
        actual = word_counter.count
        self.assertEqual(2, actual)
