from arpa.models.simple import ARPAModelSimple


def test_new_model_contains_not():
    lm = ARPAModelSimple()
    assert 'foo' not in lm


def test_new_model_contains():
    lm = ARPAModelSimple()
    lm.add_entry(['foo'], 1.0)
    assert 'foo' in lm


def test_new_model_counts():
    lm = ARPAModelSimple()
    assert lm.counts() == []


def test_new_model_len():
    lm = ARPAModelSimple()
    assert len(lm) == 0


def test_new_model_order():
    lm = ARPAModelSimple()
    assert lm.order() is None


def test_new_model_vocabulary():
    lm = ARPAModelSimple()
    assert lm.vocabulary() == []
