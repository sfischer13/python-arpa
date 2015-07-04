from io import StringIO

from .models.simple import ARPAModelSimple
from .parsers.quick import ARPAParserQuick


def dump(obj, fp):
    raise NotImplementedError
    # TODO: obj.write(fp)


def dumpf(obj, path, mode="wt", encoding=None):
    with open(path, mode=mode, encoding=encoding) as f:
        dump(obj, f)


def dumps(obj):
    with StringIO() as f:
        dump(obj, f)
        return f.getvalue()


def load(fp, model=None, parser=None):
    if not model:
        model = "simple"
    if not parser:
        parser = "quick"

    if model not in ["simple"]:
        raise ValueError
    if parser not in ["quick"]:
        raise ValueError

    if model == "simple" and parser == "quick":
        return ARPAParserQuick(ARPAModelSimple).parse(fp)
    else:
        raise ValueError


def loadf(path, mode="rt", encoding=None, model=None, parser=None):
    with open(path, mode=mode, encoding=encoding) as f:
        return load(f, model, parser)


def loads(s, model=None, parser=None):
    with StringIO(s) as f:
        return load(f, model, parser)
