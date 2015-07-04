from abc import ABCMeta, abstractmethod


class ARPAModel(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_count(self, order, count):
        pass

    @abstractmethod
    def add_entry(self, ngram, p, bo=None, order=None):
        pass

    def log10_p(self, ngram):
        if not ngram:
            raise ValueError
        elif isinstance(ngram, str):
            ngram = self._str2tuple(ngram)
        elif isinstance(ngram, list):
            ngram = tuple(ngram)
        elif not isinstance(ngram, tuple):
            raise ValueError

        try:
            return self._log10_p(ngram)
        except KeyError:
            try:
                log10_bo = self._log10_bo(ngram[:-1])
            except KeyError:
                log10_bo = 0
            return log10_bo + self.log10_p(ngram[1:])

    def p(self, ngram):
        return 10 ** self.log10_p(ngram)

    @abstractmethod
    def _log10_bo(self, ngram):
        pass

    @abstractmethod
    def _log10_p(self, ngram):
        pass

    @staticmethod
    def _str2tuple(s):
        return tuple(s.strip().split(" "))
