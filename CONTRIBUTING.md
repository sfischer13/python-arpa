Contributing
============

Contributions are welcome!

Format code:

```sh
yapf -e docs/conf.py -i -r .
```

Check code style:

```sh
flake8 .
```

Build documentation:

```sh
cd docs
make html
```

Build and check documentation:

```sh
cd docs
sphinx-build -nWT -b html -d _build/doctrees . _build/html
```

Run tests:

```sh
python setup.py test
```

Check MANIFEST.in:

```sh
check-manifest -v
```

Run pyroma:

```sh
pyroma .
```

Bump version:

-   `__init__.py`
    -   `__version__`
-   `setup.py`
    -   `version`
-   `docs/conf.py`
    -   `version`
    -   `release`
-   `HISTORY.md`

Make release:

```sh
python setup.py check
python setup.py sdist
python setup.py bdist_wheel
twine check
twine upload dist/*
```
