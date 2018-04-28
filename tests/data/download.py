#!/usr/bin/env python3

import sys

import nltk


def main():
    for corpus in ['punkt', 'udhr2', 'words']:
        nltk.download(corpus)
    return 0


if __name__ == '__main__':
    sys.exit(main())
