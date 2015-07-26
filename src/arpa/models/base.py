from abc import ABCMeta, abstractmethod


class ARPAModel(metaclass=ABCMeta):
    def __init__(self):
        self._base = 10

    def __contains__(self, word):
        return word in self.vocabulary()

    def __len__(self):
        return len(self.vocabulary())

    @abstractmethod
    def add_count(self, order, count):
        pass

    @abstractmethod
    def add_entry(self, ngram, p, bo=None, order=None):
        pass

    def log_p(self, ngram):
        ngram = self._check_input(ngram)
        try:
            return self._log_p(ngram)
        except KeyError:
            try:
                log_bo = self._log_bo(ngram[:-1])
            except KeyError:
                log_bo = 0
            return log_bo + self.log_p(ngram[1:])

    def log_s(self, sentence):
        words = self._check_input(sentence)
        return sum(self.log_p(words[:i]) for i in range(1, len(words) + 1))

    def p(self, ngram):
        return self._base ** self.log_p(ngram)

    def s(self, sentence):
        return self._base ** self.log_s(sentence)

    @abstractmethod
    def counts(self):
        pass

    @abstractmethod
    def order(self):
        pass

    @abstractmethod
    def vocabulary(self):
        pass

    def write(self, fp):
        fp.write("\\data\\\n")
        for order, count in self.counts():
            fp.write("ngram {}={}\n".format(order, count))
        fp.write("\n")
        for order, _ in self.counts():
            fp.write("\\{}-grams:\n".format(order))
            for e in self._entries(order):
                fp.write("{}\t{}".format(e[0], " ".join(e[1])))
                if len(e) == 3:
                    fp.write("\t{}".format(e[2]))
                fp.write("\n")
            fp.write("\n")
        fp.write("\\end\\\n")

    @abstractmethod
    def _entries(self, order):
        pass

    @abstractmethod
    def _log_bo(self, ngram):
        pass

    @abstractmethod
    def _log_p(self, ngram):
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
