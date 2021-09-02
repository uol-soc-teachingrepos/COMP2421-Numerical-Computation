MAKEFLAGS += --no-builtin-rules

# custom variables
BUILDDIR=public
LECTURES=$(shell find lec -name "*.md")
HANDOUTS=$(shell find handouts -name "*.md")
CODE=$(shell find code -name "*.py")
STATIC=$(shell find css img js static -type f)

# conversion rules
PANDOC_REVEALJS= \
  pandoc \
    --template=./pandoc/revealjs-template.html \
    -t revealjs \
    --mathjax \
    --no-highlight \
    --slide-level 2 \
    --standalone \
    --table-of-contents \
    --toc-depth=1 \
    -V history=true \

PANDOC_REVEALJS_INDEX= \
  $(PANDOC_REVEALJS) \
  -V controls=true \
  -V controlsTutorial=true \
  -V slideNumber="'c'" \
  -V menu=true \
  -V basename=".."

PANDOC_REVEALJS_SELF_CONTAINED= \
  $(PANDOC_REVEALJS) \
    --self-contained \
    -V controls=false \
    -V slideNumber="'c'" \
    -V basename="$(BUILDDIR)"

# targets
REVEALJS_INDEX_TARGETS=$(LECTURES:%.md=%.html)
REVEALJS_SELF_CONTAINED_TARGETS=$(LECTURES:%.md=%.full.html)
CODE_INDEX_TARGETS=$(CODE:%.py=%.html)
HANDOUTS_DOCX_TARGETS=$(HANDOUTS:%.md=%.docx)

TARGETS= \
  $(REVEALJS_INDEX_TARGETS) \
  $(CODE_INDEX_TARGETS) \
  $(HANDOUTS_DOCX_TARGETS)

RAW=$(LECTURES) $(CODE)
BUILD_TARGETS= \
  $(BUILDDIR)/index.html \
  $(TARGETS:%=$(BUILDDIR)/%) \
  $(RAW:%=$(BUILDDIR)/%) \
  $(STATIC:%=$(BUILDDIR)/%) \
  $(REVEALJS_SELF_CONTAINED_TARGETS) \
  $(REVEALJS_SELF_CONTAINED_TARGETS:%=$(BUILDDIR)/%) 

# global rules
all: $(TARGETS)
build: $(BUILD_TARGETS)

# implicit rules
%.html: %.md ./pandoc/revealjs-template.html
	$(PANDOC_REVEALJS_INDEX) $< -o $@

%.full.html: %.md ./pandoc/revealjs-template.html
	$(PANDOC_REVEALJS_SELF_CONTAINED) $< -o $@

%.html: %.py ./pandoc/make-code-index.py ./pandoc/html-template.html
	python ./pandoc/make-code-index.py $@ $<

%.docx: %.md
	pandoc $< -o $@

# build rules
${BUILDDIR}/%: %
	mkdir -p $(@D)
	cp -r $< $@

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
	rm -f $(BUILD_TARGETS)
	rm -rf $(BUILDDIR)
