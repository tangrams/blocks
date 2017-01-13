default: all

clean: clean-docs clean-standalones clean-benchmarks

clean-standalones:
	rm -R */*-full.yaml

clean-docs:
	rm -R */README.md
	rm README.md

clean-benchmarks:
	rm -R */*.frag

standalones:
	python setup.py standalones

benchmarks:
	python setup.py benchmarks

docs:
	python setup.py docs

all:
	python setup.py