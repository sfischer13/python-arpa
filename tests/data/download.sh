#!/usr/bin/env bash

wget https://raw.githubusercontent.com/kpu/kenlm/master/lm/test.arpa

gzip -k test.arpa
