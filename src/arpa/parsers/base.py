from abc import ABCMeta, abstractmethod


class ARPAParser(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, model):  # pragma: no cover
        pass

    @abstractmethod
    def parse(self, fp):  # pragma: no cover
        pass
