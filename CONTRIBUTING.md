Contributing
============

Contributions are welcome!

Dependencies
------------

```sh
pipenv check
pipenv update
pipenv update --dev
```

```sh
vim requirements.txt
vim requirements_dev.txt
```

Version
-------

-   `__init__.py`
    -   `__date__`
    -   `__version__`
-   `setup.py`
    -   `version`
-   `docs/conf.py`
    -   `release`
    -   `version`
-   `CONTRIBUTING.md`
    -   `__date__`
-   `HISTORY.md`

Format
------

```sh
yapf -e docs/conf.py -i -r .
```

```sh
flake8 .
```

Documentation
-------------

```sh
cd docs
make html
```

```sh
cd docs
sphinx-build -nWT -b html -d _build/doctrees . _build/html
```

Packaging
---------

```sh
check-manifest -v
```

```sh
pyroma .
```

Tests
-----

```sh
python setup.py test
```

Release
-------

```sh
python setup.py check

python setup.py sdist
python setup.py bdist_wheel

twine check
twine upload dist/*
```
