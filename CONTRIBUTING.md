Contributing
============

Contributions are welcome!

Dependencies
------------

```sh
pipenv --rm
pipenv sync
pipenv sync --dev

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

-   `arpa/__init__.py`
    -   `__date__`
    -   `__version__`
-   `docs/conf.py`
    -   `release`
    -   `version`
-   `setup.py`
    -   `version`
-   `AUTHORS.md`
-   `HISTORY.md`

Format
------

```sh
pipenv run yapf -e docs/conf.py -i -r .
```

```sh
pipenv run flake8 .
```

Documentation
-------------

```sh
cd docs
pipenv run make html
```

```sh
cd docs
pipenv run sphinx-build -nWT -b html -d _build/doctrees . _build/html
```

Packaging
---------

```sh
git clean -dxn
git clean -dxf
```

```sh
pipenv run check-manifest -v
```

```sh
pipenv run pyroma .
```

Tests
-----

```sh
pipenv run python setup.py test
```

Release
-------

```sh
pipenv run python setup.py check

pipenv run python setup.py sdist
pipenv run python setup.py bdist_wheel

pipenv run twine check dist/*

pipenv run twine upload dist/*
```
