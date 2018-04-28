from arpa.models.base import ARPAModel
from arpa.models.simple import ARPAModelSimple
from arpa.parsers.quick import ARPAParserQuick

from test_arpa import TEST_ARPA


def test_parse():
    with open(TEST_ARPA, 'rt') as fp:
        result = ARPAParserQuick(ARPAModelSimple).parse(fp)[0]
        assert isinstance(result, ARPAModel)
