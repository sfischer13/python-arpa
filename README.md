Python ARPA Package
===================

Python library for reading ARPA n-gram models.  

-   [Documentation](https://arpa.readthedocs.io/en/latest/) is available.
-   [Changes](https://github.com/sfischer13/python-arpa/blob/master/HISTORY.md) between releases are documented.
-   [Bugs](https://github.com/sfischer13/python-arpa/issues) can be reported on the issue tracker.
-   [Questions](mailto:sfischer13@ymail.com) can be asked via e-mail.
-   [Source code](https://github.com/sfischer13/python-arpa) is tracked on GitHub.

Setup
-----

### Python 3.4+

[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/arpa.svg)](https://pypi.python.org/pypi/arpa) [![PyPI Version](https://img.shields.io/pypi/v/arpa.svg)](https://pypi.python.org/pypi/arpa)

In order to install the Python 3 version:

    $ pip install --user -U arpa

### Python 2.7

[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/arpa-backport.svg)](https://pypi.python.org/pypi/arpa-backport) [![PyPI Version](https://img.shields.io/pypi/v/arpa-backport.svg)](https://pypi.python.org/pypi/arpa-backport)

In order to install the Python 2.7 version:

    $ pip install --user -U arpa-backport

Usage
-----

The package may be imported directly:

    import arpa  # Python 3.4+
    # OR
    import arpa_backport as arpa  # Python 2.7

    models = arpa.loadf("foo.arpa")
    lm = models[0]  # ARPA files may contain several models.

    # probability p(end|in, the)
    lm.p("in the end")
    lm.log_p("in the end")

    # sentence score w/ sentence markers
    lm.s("This is the end .")
    lm.log_s("This is the end .")

    # sentence score w/o sentence markers
    lm.s("This is the end .", sos=False, eos=False)
    lm.log_s("This is the end .", sos=False, eos=False)

Development
-----------

[![Travis](https://img.shields.io/travis/sfischer13/python-arpa.svg)](https://travis-ci.org/sfischer13/python-arpa) [![Documentation Status](https://readthedocs.org/projects/arpa/badge/?version=latest)](https://arpa.readthedocs.io/en/latest/?badge=latest) [![Coverage Status](https://coveralls.io/repos/sfischer13/python-arpa/badge.svg?branch=master&service=github)](https://coveralls.io/github/sfischer13/python-arpa?branch=master)

*Contributions are welcome!*  
Write a bug report or send a pull request.  
Other [contributors](https://github.com/sfischer13/python-arpa/graphs/contributors) have done so before.

License
-------

Copyright (c) 2015-2018 Stefan Fischer  
The source code is available under the **MIT License**.  
See [LICENSE](https://github.com/sfischer13/python-arpa/blob/master/LICENSE) for further details.
