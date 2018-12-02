#!/usr/bin/env python2

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

import nltk


def main():
    for corpus in ['punkt', 'udhr2', 'words']:
        nltk.download(corpus)
    return 0


if __name__ == '__main__':
    sys.exit(main())
