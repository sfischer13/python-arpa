from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from io import open
from io import StringIO

from .models.simple import ARPAModelSimple
from .parsers.quick import ARPAParserQuick


def dump(obj, fp):
    """Serialize obj to fp (a file-like object) in ARPA format."""
    obj.write(fp)


def dumpf(obj, path, mode='wt', encoding=None):
    """Serialize obj to path in ARPA format."""
    with open(path, mode=mode, encoding=encoding) as f:
        dump(obj, f)


def dumps(obj):
    """Serialize obj to an ARPA formatted str."""
    with StringIO() as f:
        dump(obj, f)
        return f.getvalue()


def load(fp, model=None, parser=None):
    """Deserialize fp (a file-like object) to a Python object."""
    if not model:
        model = 'simple'
    if not parser:
        parser = 'quick'

    if model not in ['simple']:
        raise ValueError
    if parser not in ['quick']:
        raise ValueError

    if model == 'simple' and parser == 'quick':
        return ARPAParserQuick(ARPAModelSimple).parse(fp)
    else:
        raise ValueError


def loadf(path, mode='rt', encoding=None, model=None, parser=None):
    """Deserialize path (a text file) to a Python object."""
    with open(path, mode=mode, encoding=encoding) as f:
        return load(f, model=model, parser=parser)


def loads(s, model=None, parser=None):
    """Deserialize s (a str) to a Python object."""
    with StringIO(s) as f:
        return load(f, model=model, parser=parser)
