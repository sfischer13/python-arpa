from abc import ABCMeta, abstractmethod

UNK = '<unk>'
SOS = '<s>'
EOS = '</s>'


class ARPAModel(metaclass=ABCMeta):
    def __init__(self, unk=UNK):
        self._base = 10
        self._unk = unk

    def __contains__(self, word):
        self._check_word(word)
        return word in self.vocabulary()

    def __len__(self):
        return len(self.vocabulary())

    @abstractmethod
    def add_count(self, order, count):  # pragma: no cover
        pass

    @abstractmethod
    def add_entry(self, ngram, p, bo=None, order=None):  # pragma: no cover
        pass

    def log_p(self, ngram):
        words = self._check_input(ngram)
        if self._unk:
            words = self._replace_unks(words)
        return self.log_p_raw(words)

    def log_p_raw(self, ngram):
        try:
            return self._log_p(ngram)
        except KeyError:
            if len(ngram) == 1:
                raise KeyError
            else:
                try:
                    log_bo = self._log_bo(ngram[:-1])
                except KeyError:
                    log_bo = 0
                return log_bo + self.log_p_raw(ngram[1:])

    def log_s(self, sentence, sos=SOS, eos=EOS):
        words = self._check_input(sentence)
        if self._unk:
            words = self._replace_unks(words)
        if sos:
            words = (sos, ) + words
        if eos:
            words = words + (eos, )
        result = sum(self.log_p_raw(words[:i]) for i in range(1, len(words) + 1))
        if sos:
            result = result - self.log_p_raw(words[:1])
        return result

    def p(self, ngram):
        return self._base**self.log_p(ngram)

    def s(self, sentence):
        return self._base**self.log_s(sentence)

    @abstractmethod
    def counts(self):  # pragma: no cover
        pass

    @abstractmethod
    def order(self):  # pragma: no cover
        pass

    @abstractmethod
    def vocabulary(self, sort=True):  # pragma: no cover
        pass

    def write(self, fp):
        fp.write('\n\\data\\\n')
        for order, count in self.counts():
            fp.write('ngram {}={}\n'.format(order, count))
        fp.write('\n')
        for order, _ in self.counts():
            fp.write('\\{}-grams:\n'.format(order))
            for e in self._entries(order):
                prob = e[0]
                ngram = ' '.join(e[1])
                if len(e) == 2:
                    fp.write('{}\t{}\n'.format(prob, ngram))
                elif len(e) == 3:
                    backoff = e[2]
                    fp.write('{}\t{}\t{}\n'.format(prob, ngram, backoff))
                else:
                    raise ValueError
            fp.write('\n')
        fp.write('\\end\\\n')

    @abstractmethod
    def _entries(self, order):  # pragma: no cover
        pass

    @abstractmethod
    def _log_bo(self, ngram):  # pragma: no cover
        pass

    @abstractmethod
    def _log_p(self, ngram):  # pragma: no cover
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
            return tuple(input.strip().split(' '))
        else:
            raise ValueError

    @staticmethod
    def _check_word(input):
        if not isinstance(input, str):
            raise ValueError
        if ' ' in input:
            raise ValueError

    def _replace_unks(self, words):
        return tuple((w if w in self else self._unk) for w in words)
