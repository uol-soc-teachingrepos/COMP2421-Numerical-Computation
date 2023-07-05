all: build slides

build:
	jupyter-book build .

linkcheck:
	jupyter-book build . --builder linkcheck

clean:
	jupyter-book clean .
	rm -f lec/*html

LEC=$(shell find lec -name "lec*.md")
PRES=$(shell find lec -name "lec*.ipynb")
SLIDES=$(LEC:lec/%_.md=_build/html/revealjs/%.html) $(PRES:lec/%_.ipynb=_build/html/revealjs/%.html)

slides:	$(SLIDES)

_build/html/revealjs/%.html: lec/%.revealjs.html
	@mkdir -p _build/html/revealjs
	cp $< $@

lec/%.revealjs.html: lec/%_.md
	$(MAKE) -C lec $(@:lec/%=%)
lec/%.revealjs.html: lec/%_.ipynb
	$(MAKE) -C lec $(@:lec/%=%)
