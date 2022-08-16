build:
	jupyter-book build .
	python _convert.py

linkcheck:
	jupyter-book build . --builder linkcheck

clean:
	jupyter-book clean .

build-pdf:
	jupyter-book build . --builder pdflatex
