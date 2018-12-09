"""Exceptions raised by this package."""


class ARPAException(Exception):
    """Common base class for all package exceptions."""

    pass


class FatalException(ARPAException):
    """This should not have happened."""

    pass


class FrozenException(ARPAException):
    """Language model is frozen."""

    pass


class ParseException(ARPAException):
    """ARPA file could not be parsed."""

    pass
