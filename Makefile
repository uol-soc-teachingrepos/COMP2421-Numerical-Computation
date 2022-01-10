build:
	npx honkit build

# MAKEFLAGS += --no-builtin-rules

# # custom variables
# BUILDDIR=public
# LECTURES=$(shell find lec -name "*.md")
# HANDOUTS=$(shell find handouts -name "*.md")
# CODE=$(shell find code -name "*.py")
# STATIC=$(shell find css img js static video -type f)

# # targets
# REVEALJS_INDEX_TARGETS=$(LECTURES:%.md=%.html)
# REVEALJS_SELF_CONTAINED_TARGETS=$(LECTURES:%.md=%.full.html)
# BEAMER_TARGETS=$(LECTURES:%.md=%.pdf)
# CODE_INDEX_TARGETS=$(CODE:%.py=%.html)
# HANDOUTS_DOCX_TARGETS=$(HANDOUTS:%.md=%.docx)
# HANDOUTS_HTML_TARGETS=$(HANDOUTS:%.md=%.html)
# HANDOUTS_PDF_TARGETS=$(HANDOUTS:%.md=%.pdf)

# TARGETS= \
#   $(REVEALJS_INDEX_TARGETS) \
#   $(REVEALJS_SELF_CONTAINED_TARGETS) \
#   $(BEAMER_TARGETS) \
#   $(CODE_INDEX_TARGETS) \
#   $(HANDOUTS_DOCX_TARGETS) \
#   $(HANDOUTS_HTML_TARGETS) \
#   $(HANDOUTS_PDF_TARGETS) \

# RAW=$(LECTURES) $(CODE) $(HANDOUTS)

# # global rules
# all: $(TARGETS)

# .PHONY: build
# build: $(TARGETS) $(RAW) $(STATIC)
# 	mkdir -p $(BUILDDIR)
# 	$(MAKE) $(BUILDDIR)/index.html
# 	cp --parents $^ $(BUILDDIR)

# # implicit rules
# %.html: %.md ./pandoc/revealjs-template.html
# 	$(MAKE) -C $(shell dirname $@) $(shell basename $@)

# %.full.html: %.md ./pandoc/revealjs-template.html
# 	$(MAKE) -C $(shell dirname $@) $(shell basename $@)

# %.pdf: %.md ./pandoc/beamer-template.tex
# 	$(MAKE) -C $(shell dirname $@) $(shell basename $@)

# %.html: %.py ./pandoc/make-code-index.py ./pandoc/html-template.html
# 	python ./pandoc/make-code-index.py $@ $<

# %.docx: %.md
# 	pandoc $< -o $@

# # build rules
# $(BUILDDIR)/index.html: ./pandoc/make-index.py
# 	mkdir -p $(@D)
# 	python ./pandoc/make-index.py $@ $(LECTURES)

# # ${BUILDDIR}/lec%/embed.html: lec/lec%.md pandoc/revealjs-template.html
# # 	mkdir -p $(shell dirname $@)
# # 	pandoc \
# # 	--mathjax \
# # 	--template=./pandoc/revealjs-template.html \
# # 	-t revealjs \
# # 	--no-highlight \
# # 	-V controls=true \
# # 	-V controlsTutorial=true \
# # 	-V slideNumber=false \
# # 	--slide-level 2 \
# # 	--table-of-contents \
# # 	-V embedded="true" \
# # 	-V history=true \
# # 	-V basename=".." \
# # 	-s $< -o $@


# dist: $(BUILD_TARGETS)
# 	zip -r code/linear-systems.zip \
# 		code/matrixSolve.py \
# 		code/lec05 code/lec06 code/lec07 \
# 		code/lec10 code/lec19
# 	@cp code/linear-systems.zip $(BUILDDIR)/code

# 	zip -r code/timestepSolve.zip \
# 		code/timestepSolve.py \
# 		code/lec11 code/lec12 code/lec13 \
# 		code/lec14
# 	@cp code/timestepSolve.zip $(BUILDDIR)/code

# 	zip -r code/nonlinearSolve.zip \
# 		code/nonlinearSolve.py \
# 		code/nonlinear_functions.py \
# 		code/lec15 code/lec16 code/lec17 \
# 		code/lec18
# 	@cp code/nonlinearSolve.zip $(BUILDDIR)/code

# 	zip -r slides.zip ${BUILDDIR}

# clean:
# 	rm -f $(TARGETS)
# 	rm -rf $(BUILDDIR)

# test:
# 	find . -type f -name "*.py" -not -path $(BUILDDIR) -exec black --check {} +
# 	find . -type f -name "*.py" -not -path $(BUILDDIR) -exec isort --profile black --check {} +
# 	find . -type f -name "*.py" -not -path $(BUILDDIR) -execdir python {} +

# 	find . -typef -name "*.md" -not -path $(BUILDDIR) -exec bash ./pandoc/md-format.sh {} +
