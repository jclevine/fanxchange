from collections import Counter


class WordCounter(object):
    def __init__(self, filepath):
        with open(filepath) as f:
            self._words = f.read().split()
            self._counter = Counter(self._words)

    @property
    def count(self):
        return len(self._words)

    def get_top_n_words(self, n):
        return self._counter.most_common(n)
