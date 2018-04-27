Python ARPA Package
===================

|PyPI Version| |Travis| |Coverage Status| |Dependency
Status|

| This is a library for reading ARPA n-gram models.
| Python 3.3+ and Wheels are supported.
| It was initiated by Stefan Fischer and is developed and maintained by
  many others.

-  `Questions <mailto:sfischer13@ymail.com>`__ can be asked via e-mail.
-  `Source code <http://github.com/sfischer13/python-arpa>`__ is tracked
   on GitHub.
-  `Changes <https://github.com/sfischer13/python-arpa/blob/master/CHANGELOG.rst>`__
   between releases are documented.
-  `Bugs <https://github.com/sfischer13/python-arpa/issues>`__ can be
   reported on the issue tracker.

Install
-------

|PyPI Python Versions|

The package is available on
`PyPI <https://pypi.python.org/pypi/arpa>`__:

::

    $ pip install arpa

Use
---

The package may be imported directly:

::

    import arpa
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

Contribute
----------

| Write a bug report or send a pull request.
| Other
  `contributors <https://github.com/sfischer13/python-arpa/graphs/contributors>`__
  have done so before.

-  `Roadmap <https://github.com/sfischer13/python-arpa/blob/master/TODO.rst>`__
   of planned improvements
-  `Issues <https://github.com/sfischer13/python-arpa/issues>`__ that
   have been reported

License
-------

| Copyright (c) 2015-2018 Stefan Fischer
| The source code is available under the **MIT License**.
| See
  `LICENSE <https://github.com/sfischer13/python-arpa/blob/master/LICENSE>`__
  for further details.

.. |PyPI Version| image:: https://img.shields.io/pypi/v/arpa.svg
   :target: https://pypi.python.org/pypi/arpa
.. |Travis| image:: https://img.shields.io/travis/sfischer13/python-arpa.svg
   :target: https://travis-ci.org/sfischer13/python-arpa
.. |Coverage Status| image:: https://coveralls.io/repos/sfischer13/python-arpa/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/sfischer13/python-arpa?branch=master
.. |Dependency Status| image:: https://www.versioneye.com/user/projects/55c5d4fa6537620017003629/badge.svg?style=flat
   :target: https://www.versioneye.com/user/projects/55c5d4fa6537620017003629
.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/arpa.svg
   :target: https://pypi.python.org/pypi/arpa
