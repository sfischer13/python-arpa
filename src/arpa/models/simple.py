from .base import ARPAModel


class ARPAModelSimple(ARPAModel):
    def __init__(self):
        self._counts = {}
        self._ps = {}
        self._bos = {}

    def add_count(self, order, count):
        self._counts[order] = count

    def add_entry(self, ngram, p, bo=None, order=None):
        key = tuple(ngram)
        self._ps[key] = p
        if bo:
            self._bos[key] = bo

    def _log10_bo(self, ngram):
        return self._bos[ngram]

    def _log10_p(self, ngram):
        return self._ps[ngram]
