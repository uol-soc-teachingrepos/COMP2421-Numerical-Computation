# custom variables
BUILDDIR=public
LECTURES=$(shell find lec -name "*.md")
CODE=$(shell find code -name "*.py")
STATIC=$(shell find {css,img,js,static} -type f)

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
  -V basename=".." \

# targets
REVEALJS_INDEX_TARGETS=$(LECTURES:%.md=%.html)
CODE_INDEX_TARGETS=$(CODE:%.py=%.html)

TARGETS=$(REVEALJS_INDEX_TARGETS) $(CODE_INDEX_TARGETS)
RAW=$(LECTURES) $(CODE)
BUILD_TARGETS= \
  $(BUILDDIR)/index.html \
  $(TARGETS:%=$(BUILDDIR)/%) \
  $(RAW:%=$(BUILDDIR)/%) \
  $(STATIC:%=$(BUILDDIR)/%) \

# global rules
all: $(TARGETS)
build: $(BUILD_TARGETS)

# implicit rules
%.html: %.md ./pandoc/revealjs-template.html
	$(PANDOC_REVEALJS_INDEX) $< -o $@

%.html: %.py
	python ./pandoc/make-code-index.py $@ $<

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

# ${BUILDDIR}/lec%/presenter.html: lec/lec%.md pandoc/revealjs-template.html
# 	pandoc \
# 	--self-contained \
# 	--mathjax \
# 	--template=./pandoc/revealjs-template.html \
# 	-t revealjs \
# 	--no-highlight \
# 	--slide-level 2 \
# 	--table-of-contents \
# 	-V controls=false \
# 	-V slideNumber="'c'" \
# 	-V history=true \
# 	-V basename="public" \
# 	$< -so $@

dist: $(BUILD_TARGETS)
	tar -cvzf slides.tar.gz ${BUILDDIR}

clean:
	rm -f $(TARGETS)
	rm -rf ${BUILDDIR}
