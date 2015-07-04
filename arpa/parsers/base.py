from abc import ABCMeta, abstractmethod


class ARPAParser(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, model):
        pass

    @abstractmethod
    def parse(self, fp):
        pass
