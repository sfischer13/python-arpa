#!/usr/bin/env python2

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from io import open

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if not ((2, 7) <= sys.version_info < (3, 0)):
    print('ERROR: Python 2.7 is required!')
    sys.exit(1)

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['enum34']

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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    description='Library for reading ARPA n-gram models with Python 2.7.',
    include_package_data=True,
    install_requires=requirements,
    keywords='ARPA n-gram ngram language model LM language technology LT '
    'computational linguistics CL natural language processing NLP unigram bigram trigram',
    license='MIT',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='arpa-backport',
    package_dir={'arpa_backport': 'arpa_backport'},
    packages=['arpa_backport'],
    python_requires='~=2.7',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/sfischer13/python-arpa',
    version='0.1.0b3',
    zip_safe=False,
)
