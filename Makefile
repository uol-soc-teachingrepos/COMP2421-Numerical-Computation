build:
	jupyter-book build .

linkcheck:
	jupyter-book build . --builder linkcheck

clean:
	jupyter-book clean .

zip:
	$(MAKE) build
	zip -r comp2421.zip _build/html


LEC=$(shell find lec -name "lec*.md")
SLIDES=$(LEC:lec/%.md=_build/revealjs/%.html)
slides:	$(SLIDES)

_build/revealjs/%.html: lec/%.revealjs.html
	@mkdir -p _build/revealjs
	cp $< $@

lec/%.revealjs.html: lec/%_.md
	$(MAKE) -C lec $(@:lec/%=%)
lec/%.revealjs.html: lec/%_.ipynb
	$(MAKE) -C lec $(@:lec/%=%)
