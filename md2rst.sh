#!/bin/bash

for f in *.md; do
	pandoc --from=markdown --to=rst "${f}" -o "${f%.md}".rst
done
