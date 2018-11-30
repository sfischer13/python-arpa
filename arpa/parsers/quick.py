from enum import Enum, unique
import re

from .base import ARPAParser
from ..exceptions import ParseException


class ARPAParserQuick(ARPAParser):
    @unique
    class State(Enum):
        DATA = 1
        COUNT = 2
        HEADER = 3
        ENTRY = 4

    re_count = re.compile(r'^ngram (\d+)=(\d+)$')
    re_header = re.compile(r'^\\(\d+)-grams:$')
    re_entry = re.compile('^(-?\\d+(\\.\\d+)?([eE]-?\\d+)?)'
                          '\t'
                          '(\\S+( \\S+)*)'
                          '(\t(-?\\d+(\\.\\d+)?)([eE]-?\\d+)?)?$')

    def __init__(self, model):
        self.ModelClass = model

    def parse(self, fp):
        self._result = []
        self._state = self.State.DATA
        self._tmp_model = None
        self._tmp_order = None
        for line in fp:
            line = line.strip()
            if self._state == self.State.DATA:
                self._data(line)
            elif self._state == self.State.COUNT:
                self._count(line)
            elif self._state == self.State.HEADER:
                self._header(line)
            elif self._state == self.State.ENTRY:
                self._entry(line)
        if self._state != self.State.DATA:
            raise ParseException(line)
        return self._result

    def _data(self, line):
        if line == '\\data\\':
            self._state = self.State.COUNT
            self._tmp_model = self.ModelClass()
        else:
            pass  # skip comment line

    def _count(self, line):
        match = self.re_count.match(line)
        if match:
            order = match.group(1)
            count = match.group(2)
            self._tmp_model.add_count(int(order), int(count))
        elif not line:
            self._state = self.State.HEADER  # there are no counts
        else:
            raise ParseException(line)

    def _header(self, line):
        match = self.re_header.match(line)
        if match:
            self._state = self.State.ENTRY
            self._tmp_order = match.group(1)
        elif line == '\\end\\':
            self._result.append(self._tmp_model)
            self._state = self.State.DATA
            self._tmp_model = None
            self._tmp_order = None
        elif not line:
            pass  # skip empty line
        else:
            raise ParseException(line)

    def _entry(self, line):
        match = self.re_entry.match(line)
        if match:
            p = self._float_or_int(match.group(1))
            ngram = tuple(match.group(4).split(' '))
            bo = match.group(7)
            bo = self._float_or_int(bo) if bo else None
            self._tmp_model.add_entry(ngram, p, bo, self._tmp_order)
        elif not line:
            self._state = self.State.HEADER  # last entry
        else:
            raise ParseException(line)

    @staticmethod
    def _float_or_int(s):
        f = float(s)
        i = int(f)
        if str(i) == s:  # don't drop trailing ".0"
            return i
        else:
            return f
