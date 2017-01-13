default: all

clean: clean-readmes clean-fulls

clean-fulls:
	rm -R */*-full.yaml

clean-readmes:
	rm -R */README.md
	rm README.md

clean-shaders:
	rm -R */*.frag

all:
	python setup.py