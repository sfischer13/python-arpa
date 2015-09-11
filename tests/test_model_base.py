import pytest

from arpa.models.simple import ARPAModelSimple


def test_new_model_contains_not():
    lm = ARPAModelSimple()
    assert "foo" not in lm


def test_new_model_counts():
    lm = ARPAModelSimple()
    assert lm.counts() == []


def test_new_model_len():
    lm = ARPAModelSimple()
    assert len(lm) == 0


def test_log_p_raw():
    lm = ARPAModelSimple()
    with pytest.raises(KeyError):
        lm.log_p_raw("UnladenSwallow")


def test_log_p_empty_string():
    lm = ARPAModelSimple()
    with pytest.raises(ValueError):
        lm.log_p("")


def test_log_p_empty_tuple():
    lm = ARPAModelSimple()
    with pytest.raises(ValueError):
        lm.log_p(tuple())


def test_log_p_int():
    lm = ARPAModelSimple()
    with pytest.raises(ValueError):
        lm.log_p(1)
