#!/usr/bin/env python3

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if not ((3, 4) <= sys.version_info < (4, 0)):
    print('ERROR: Python 3.4+ is required!')
    sys.exit(1)

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
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
    install_requires=[],
    keywords='ARPA n-gram ngram language model LM language technology LT '
    'computational linguistics CL natural language processing NLP unigram bigram trigram',
    license='MIT',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='arpa',
    package_dir={'arpa': 'arpa'},
    packages=['arpa'],
    python_requires='~=3.4',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/sfischer13/python-arpa',
    version='0.1.0b3',
    zip_safe=False,
)
