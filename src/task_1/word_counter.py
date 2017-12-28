#!/bin/python

import sys
import os
import logging
sys.path.append(os.getcwd())
from src.task_1.WordCounter import WordCounter

if len(sys.argv) < 2:
    logging.error('No file given. I need a file.')
    exit(-1)

if len(sys.argv) > 2:
    logging.warning("Extra parameters given. I'll ignore %s", sys.argv[2:])

print('Parsing {}...'.format(sys.argv[1]))
word_counter = WordCounter(sys.argv[1])
print(
"""
Total number of words in text file:
{}

Ten most common words and number of occurrences for each
{}
""".format(word_counter.count, word_counter.get_top_n_words(10))
)

