from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from io import open

from arpa_backport.models.base import ARPAModel
from arpa_backport.models.simple import ARPAModelSimple
from arpa_backport.parsers.quick import ARPAParserQuick

from test_arpa import TEST_ARPA


def test_parse():
    with open(TEST_ARPA, 'rt') as fp:
        result = ARPAParserQuick(ARPAModelSimple).parse(fp)[0]
        assert isinstance(result, ARPAModel)
