#!/usr/bin/env python3

from setuptools import find_packages, setup

import arpa

readme = open("README.rst").read()
authors = open("AUTHORS.rst").read()
changelog = open("CHANGELOG.rst").read()

setup(
    name="arpa",
    version=arpa.__version__,
    author=arpa.__author__,
    author_email=arpa.__author_email__,
    url=arpa.__url__,
    license=arpa.__license__,
    description=arpa.__doc__.strip().split("\n")[0],
    long_description=("\n\n".join([readme, authors, changelog])),
    keywords="ARPA n-gram ngram language model LM language technology LT "
    "natural language processing NLP",
    install_requires=[],
    packages=find_packages("arpa"),
    package_dir={"": "arpa"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic"
    ],
    zip_safe=False)
