.PHONY: all build test clean

all: test clean build

build:
	@echo "Creating distribution tarball"
	@python setup.py sdist -q --formats=bztar

clean:
	@echo "Cleaning *.pyc files"
	@find . -name "*.pyc" -exec rm -f {} \;

test:
	@python setup.py test
