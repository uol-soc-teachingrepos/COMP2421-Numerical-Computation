MAKEFLAGS += --no-builtin-rules

# custom variables
BUILDDIR=public
LECTURES=$(shell find lec -name "*.md")
HANDOUTS=$(shell find handouts -name "*.md")
CODE=$(shell find code -name "*.py")
STATIC=$(shell find css img js static video -type f)

# targets
REVEALJS_INDEX_TARGETS=$(LECTURES:%.md=%.html)
REVEALJS_SELF_CONTAINED_TARGETS=$(LECTURES:%.md=%.full.html)
BEAMER_TARGETS=$(LECTURES:%.md=%.pdf)
CODE_INDEX_TARGETS=$(CODE:%.py=%.html)
HANDOUTS_DOCX_TARGETS=$(HANDOUTS:%.md=%.docx)

TARGETS= \
  $(REVEALJS_INDEX_TARGETS) \
  $(REVEALJS_SELF_CONTAINED_TARGETS) \
  $(BEAMER_TARGETS) \
  $(CODE_INDEX_TARGETS) \
  $(HANDOUTS_DOCX_TARGETS) \

RAW=$(LECTURES) $(CODE)

# global rules
all: $(TARGETS)

.PHONY: build
build: $(TARGETS) $(RAW) $(STATIC)
	mkdir -p $(BUILDDIR)
	$(MAKE) $(BUILDDIR)/index.html
	cp --parents $^ $(BUILDDIR)

# implicit rules
%.html: %.md ./pandoc/revealjs-template.html
	$(MAKE) -C $(shell dirname $@) $(shell basename $@)

%.full.html: %.md ./pandoc/revealjs-template.html
	$(MAKE) -C $(shell dirname $@) $(shell basename $@)

%.pdf: %.md ./pandoc/beamer-template.tex
	$(MAKE) -C $(shell dirname $@) $(shell basename $@)

%.html: %.py ./pandoc/make-code-index.py ./pandoc/html-template.html
	python ./pandoc/make-code-index.py $@ $<

%.docx: %.md
	pandoc $< -o $@

# build rules
$(BUILDDIR)/index.html: ./pandoc/make-index.py
	mkdir -p $(@D)
	python ./pandoc/make-index.py $@ $(LECTURES)

# ${BUILDDIR}/lec%/embed.html: lec/lec%.md pandoc/revealjs-template.html
# 	mkdir -p $(shell dirname $@)
# 	pandoc \
# 	--mathjax \
# 	--template=./pandoc/revealjs-template.html \
# 	-t revealjs \
# 	--no-highlight \
# 	-V controls=true \
# 	-V controlsTutorial=true \
# 	-V slideNumber=false \
# 	--slide-level 2 \
# 	--table-of-contents \
# 	-V embedded="true" \
# 	-V history=true \
# 	-V basename=".." \
# 	-s $< -o $@


dist: $(BUILD_TARGETS)
	tar -cvzf slides.tar.gz ${BUILDDIR}

clean:
	rm -f $(TARGETS)
	rm -rf $(BUILDDIR)
