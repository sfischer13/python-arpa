# MIT License
#
# Copyright (c) 2015-2018 Stefan Fischer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Library for reading ARPA n-gram models.

The package may be imported directly::

    import arpa

Details about the ARPA n-gram format can be found here:

- `SRILM <http://www.speech.sri.com/projects/srilm/manpages/ngram-format.5.html>`_
- `ICSI Speech <https://www1.icsi.berkeley.edu/Speech/faq/grammarfmts.html>`_

The library was initiated by Stefan Fischer and is developed and maintained by many others.
"""

from .api import dump, dumpf, dumps, load, loadf, loads

__all__ = ['dump', 'dumpf', 'dumps', 'load', 'loadf', 'loads']

__author__ = 'Stefan Fischer'
__contact__ = 'Stefan Fischer <sfischer13@ymail.com>'
__copyright__ = 'Copyright (c) 2015-2018 Stefan Fischer'
__credits__ = []
__date__ = '2018-12-06'
__license__ = 'MIT'
__status__ = 'development'
__version__ = '0.1.0b3'
