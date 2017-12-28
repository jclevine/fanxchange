class WordCounter(object):
    def __init__(self, filepath):
        with open(filepath) as f:
            self._count = f.read().split()

    @property
    def count(self):
        return len(self._count)

    def get_top_n_words(self, n):
        return {}
