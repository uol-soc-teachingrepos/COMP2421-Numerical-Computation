build:
	jupyter-book build .
	python _convert.py

linkcheck:
	jupyter-book build . --builder linkcheck

clean:
	jupyter-book clean .

zip:
	$(MAKE) build
	zip -r comp2421.zip _build/html
