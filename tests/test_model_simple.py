from arpa.models.simple import ARPAModelSimple


def test_new_model_counts():
    lm = ARPAModelSimple()
    assert lm.counts() == []

def test_new_model_len():
    lm = ARPAModelSimple()
    assert len(lm) == 0
