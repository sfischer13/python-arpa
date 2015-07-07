"""Exceptions raised by this package."""


class ARPAException(Exception):
    """Common base class for all package exceptions."""
    pass


class ParseException(ARPAException):
    """ARPA file could not be parsed."""
    pass
