import pytest

import arpa
from arpa.models.base import ARPAModel
from arpa.models.simple import ARPAModelSimple

from test_arpa import TEST_ARPA


def test_manual_log_p_unk():
    lm = arpa.loadf(TEST_ARPA)[0]
    assert lm.log_p("UnladenSwallow") == -1.995635


def test_manual_p():
    lm = arpa.loadf(TEST_ARPA)[0]
    assert round(lm.p("<s>"), 4) == 0


def test_manual_contains():
    lm = arpa.loadf(TEST_ARPA)[0]
    assert "foo" in lm


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


def test_log_s_int():
    lm = ARPAModelSimple()
    with pytest.raises(ValueError):
        lm.log_s(1)


def test_check_input_list():
    lm = ARPAModelSimple()
    result = ARPAModel._check_input(["foo", "bar"])
    assert isinstance(result, tuple)


def test_check_input_string_word():
    lm = ARPAModelSimple()
    result = ARPAModel._check_input("foo")
    assert isinstance(result, tuple) and len(result) == 1


def test_check_input_string_words():
    lm = ARPAModelSimple()
    result = ARPAModel._check_input("foo bar")
    assert isinstance(result, tuple) and len(result) == 2
