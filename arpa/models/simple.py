from collections import OrderedDict

from .base import ARPAModel
from .base import UNK


class ARPAModelSimple(ARPAModel):
    def __init__(self, unk=UNK):
        super().__init__(unk=unk)
        self._counts = OrderedDict()
        self._ps = OrderedDict()
        self._bos = OrderedDict()

    def add_count(self, order, count):
        self._counts[order] = count

    def add_entry(self, ngram, p, bo=None, order=None):
        key = tuple(ngram)
        self._ps[key] = p
        if bo is not None:
            self._bos[key] = bo

    def counts(self):
        return sorted(self._counts.items())

    def order(self):
        try:
            return max(self._counts.keys())
        except ValueError:  # max([], default=None) is Python 3.4+ only
            return None

    def vocabulary(self):
        return sorted(set(word for ngram in self._ps.keys() for word in ngram))

    def _entries(self, order):
        return (self._entry(k) for k in self._ps.keys() if len(k) == order)

    def _entry(self, ngram):
        if ngram in self._bos:
            return self._ps[ngram], ngram, self._bos[ngram]
        else:
            return self._ps[ngram], ngram

    def _log_bo(self, ngram):
        return self._bos[ngram]

    def _log_p(self, ngram):
        return self._ps[ngram]
