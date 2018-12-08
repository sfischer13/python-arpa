import filecmp
import os
import os.path
import tempfile

import arpa

import pytest

PARSERS = [None, 'quick']
TEST_ARPA = os.path.join(os.path.dirname(__file__), 'data/test.arpa')
TEST_ARPA_GZ = os.path.join(os.path.dirname(__file__), 'data/test.arpa.gz')


def test_load_option_model():
    with pytest.raises(ValueError):
        arpa.load(None, model='foo')


def test_load_option_parser():
    with pytest.raises(ValueError):
        arpa.load(None, parser='foo')


def test_load_dump():
    with open(TEST_ARPA, 'rt') as fp:
        lm = arpa.load(fp)[0]
        fp.seek(0)
        with tempfile.TemporaryFile(mode='w+t') as gp:
            arpa.dump(lm, gp)
            gp.seek(0)
            assert fp.read() == gp.read()


def test_loadf_dumpf_read():
    for p in PARSERS:
        for src in [TEST_ARPA, TEST_ARPA_GZ]:
            # read
            lm = arpa.loadf(src, parser=p)[0]
            # write
            out = tempfile.NamedTemporaryFile(mode='w+t', suffix='.arpa', delete=False)
            arpa.dumpf(lm, out.name)
            out.close()
            # compare
            assert filecmp.cmp(TEST_ARPA, out.name, shallow=False)
            os.unlink(out.name)


def test_loadf_dumpf_write():
    for p in PARSERS:
        for suf in ['.arpa', '.gz']:
            # read
            lm1 = arpa.loadf(TEST_ARPA, parser=p)[0]
            # write
            out1 = tempfile.NamedTemporaryFile(mode='w+t', suffix=suf, delete=False)
            arpa.dumpf(lm1, out1.name)
            out1.close()
            # read again
            lm2 = arpa.loadf(out1.name, parser=p)[0]
            # write again
            out2 = tempfile.NamedTemporaryFile(mode='w+t', suffix='.arpa', delete=False)
            arpa.dumpf(lm2, out2.name)
            out2.close()
            # compare
            assert filecmp.cmp(TEST_ARPA, out2.name, shallow=False)
            os.unlink(out2.name)


def test_loads_dumps():
    with open(TEST_ARPA, 'rt') as fp:
        txt = fp.read()
        lm = arpa.loads(txt)[0]
        out = arpa.dumps(lm)
        assert txt == out
