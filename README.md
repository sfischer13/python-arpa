# Python ARPA Package [![PyPI Version](https://img.shields.io/pypi/v/arpa.svg)](https://pypi.python.org/arpa) [![PyPI Downloads](https://img.shields.io/pypi/dm/arpa.svg)](https://pypi.python.org/arpa) [![Travis](https://img.shields.io/travis/sfischer13/python-arpa.svg)](https://travis-ci.org/sfischer13/python-arpa)

This is a library for reading ARPA n-gram models.  
It was initiated by Stefan Fischer and is developed and maintained by many others.

* [Questions](mailto:sfischer13@ymail.com) can be asked via e-mail.
* [Changes](CHANGELOG.md) between releases are documented.
* [Bugs](https://github.com/sfischer13/python-arpa/issues) can be reported on the issue tracker.
* [Source code](http://github.com/sfischer13/python-arpa) is tracked on GitHub.

## Install

The package is available on [PyPI](https://pypi.python.org/arpa):

    $ pip install arpa

Python 3.3+ is required: [![PyPI Python Versions](https://img.shields.io/pypi/pyversions/arpa.svg)](https://pypi.python.org/arpa)  
Wheels are not yet supported: [![PyPI Wheel](https://img.shields.io/pypi/wheel/arpa.svg)](https://pypi.python.org/arpa)

## Use

The package may be imported directly:

    import arpa
    models = arpa.loadf("foo.arpa")
    lm = models[0]  # ARPA files may contain several models.
    lm.p("in the end")  # p(end|in, the)

## Contribute

Write a bug report or send a pull request.  
Other [contributors](https://github.com/sfischer13/python-arpa/graphs/contributors) have done so before.

* [Roadmap](TODO.md) of planned improvements
* [Issues](https://github.com/sfischer13/python-arpa/issues) that have been reported

## License [![License](https://img.shields.io/github/license/sfischer13/python-arpa.svg)](LICENSE)

Copyright (c) 2015 Stefan Fischer  
The source code is available under the [MIT License](http://www.opensource.org/licenses/mit-license.php).  
See [LICENSE](LICENSE) for further details.
