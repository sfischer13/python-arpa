"""Exceptions raised by this package."""


class ARPAException(Exception):
    """Base exception that is never raised."""
    pass


class ParseException(ARPAException):
    pass
