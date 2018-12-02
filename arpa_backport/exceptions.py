from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
"""Exceptions raised by this package."""


class ARPAException(Exception):
    """Common base class for all package exceptions."""

    pass


class FrozenException(ARPAException):
    """Language model is frozen."""

    pass


class ParseException(ARPAException):
    """ARPA file could not be parsed."""

    pass
