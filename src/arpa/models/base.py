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
        ngram = self._check_input(ngram)
        try:
            return self._log10_p(ngram)
        except KeyError:
            try:
                log10_bo = self._log10_bo(ngram[:-1])
            except KeyError:
                log10_bo = 0
            return log10_bo + self.log10_p(ngram[1:])

    def log10_s(self, sentence):
        words = self._check_input(sentence)
        return sum(self.log10_p(words[:i]) for i in range(1, len(words) + 1))

    def p(self, ngram):
        return 10 ** self.log10_p(ngram)

    def s(self, sentence):
        return 10 ** self.log10_s(sentence)

    @abstractmethod
    def _log10_bo(self, ngram):
        pass

    @abstractmethod
    def _log10_p(self, ngram):
        pass

    @staticmethod
    def _check_input(input):
        if not input:
            raise ValueError
        elif isinstance(input, tuple):
            return input
        elif isinstance(input, list):
            return tuple(input)
        elif isinstance(input, str):
            return tuple(input.strip().split(" "))
        else:
            raise ValueError
