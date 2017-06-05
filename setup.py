#!/usr/bin/env python

import os.path
import sys

from setuptools import find_packages
from setuptools import setup


def read(name):
    path = os.path.join(os.path.dirname(__file__), name)
    with open(path) as f:
        return f.read()


install_requires = []

if sys.version_info < (3, 4):
    install_requires += ["enum34"]

setup(
    author='Stefan Fischer',
    author_email='sfischer13@ymail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    description='Library for reading ARPA n-gram models.',
    include_package_data=True,
    install_requires=install_requires,
    keywords='ARPA n-gram ngram language model LM language technology LT '
    'computational linguistics CL natural language processing NLP unigram bigram trigram',
    license='MIT',
    long_description=read('README.rst'),
    name='arpa',
    package_dir={'arpa': 'arpa'},
    packages=['arpa'],
    python_requires='>=3.3',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/sfischer13/python-arpa',
    version='0.1.0b1',
    zip_safe=False)
