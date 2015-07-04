Python ARPA Package
===================

|PyPI Version| |PyPI Downloads| |Travis|

| This is a library for reading ARPA n-gram models.
| It was initiated by Stefan Fischer and is developed and maintained by
  many others.

-  `Questions <mailto:sfischer13@ymail.com>`__ can be asked via e-mail.
-  `Source code <http://github.com/sfischer13/python-arpa>`__ is tracked
   on GitHub.
-  `Changes <CHANGELOG.md>`__ between releases are documented.
-  `Bugs <https://github.com/sfischer13/python-arpa/issues>`__ can be
   reported on the issue tracker.

Install
-------

The package is available on `PyPI <https://pypi.python.org/arpa>`__:

::

    $ pip install arpa

| Python 3.3+ is required: |PyPI Python Versions|
| Wheels are not yet supported: |PyPI Wheel|

Use
---

The package may be imported directly:

::

    import arpa
    models = arpa.loadf("foo.arpa")
    lm = models[0]  # ARPA files may contain several models.
    lm.p("in the end")  # p(end|in, the)

Contribute
----------

| Write a bug report or send a pull request.
| Other
  `contributors <https://github.com/sfischer13/python-arpa/graphs/contributors>`__
  have done so before.

-  `Roadmap <TODO.md>`__ of planned improvements
-  `Issues <https://github.com/sfischer13/python-arpa/issues>`__ that
   have been reported

License |License|
-----------------

| Copyright (c) 2015 Stefan Fischer
| The source code is available under the `MIT
  License <http://www.opensource.org/licenses/mit-license.php>`__.
| See `LICENSE <LICENSE>`__ for further details.

.. |PyPI Version| image:: https://img.shields.io/pypi/v/arpa.svg
   :target: https://pypi.python.org/arpa
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/arpa.svg
   :target: https://pypi.python.org/arpa
.. |Travis| image:: https://img.shields.io/travis/sfischer13/python-arpa.svg
   :target: https://travis-ci.org/sfischer13/python-arpa
.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/arpa.svg
   :target: https://pypi.python.org/arpa
.. |PyPI Wheel| image:: https://img.shields.io/pypi/wheel/arpa.svg
   :target: https://pypi.python.org/arpa
.. |License| image:: https://img.shields.io/github/license/sfischer13/python-arpa.svg
   :target: LICENSE
