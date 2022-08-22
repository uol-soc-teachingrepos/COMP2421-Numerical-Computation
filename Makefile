build:
	jupyter-book build .
	python _convert.py

linkcheck:
	jupyter-book build . --builder linkcheck

clean:
	jupyter-book clean .

build-pdf:
	jupyter-book build . --builder pdflatex

zip:
	$(MAKE) build
	zip -r comp2421.zip _build/html

LECTURES=$(shell find lec -name "*.md")
SLIDES_TARGETS=$(LECTURES:%.md=_build/slides/%.pdf)

slides: $(SLIDES_TARGETS)

_build/slides/%.pdf: %.md ./pandoc/beamer-template.tex
	mkdir -p $(@D)
	pandoc  $< \
		-t beamer \
		--table-of-contents \
		--toc-depth=1 \
		-V lang="en-GB" \
		--template ./pandoc/beamer-template.tex \
		--metadata title="num comp lecture" \
		--slide-level=3 \
		-so $@

