#!/usr/bin/env python3

import os.path
from setuptools import find_packages
from setuptools import setup


def read(name):
    path = os.path.join(os.path.dirname(__file__), name)
    with open(path) as f:
        return f.read()


setup(
    name="arpa",
    version="0.1.0a2",
    author="Stefan Fischer",
    author_email="sfischer13@ymail.com",
    url="https://github.com/sfischer13/python-arpa/",
    license="MIT",
    description="This is a library for reading ARPA n-gram models.",
    long_description=read("README.rst"),
    keywords="ARPA n-gram ngram language model LM language technology LT "
    "natural language processing NLP",
    install_requires=["enum34"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic"
    ],
    test_suite="nose.collector",
    zip_safe=True)
