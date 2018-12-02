from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod


class ARPAParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, model):  # pragma: no cover
        pass

    @abstractmethod
    def parse(self, fp):  # pragma: no cover
        pass
