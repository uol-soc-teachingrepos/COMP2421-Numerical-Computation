# conversion rules
PANDOC_REVEALJS= \
  pandoc \
    --template=../pandoc/revealjs-template.html \
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
  -V starttime="no"

PANDOC_REVEALJS_SELF_CONTAINED= \
  $(PANDOC_REVEALJS) \
    --self-contained \
    -V controls=false \
    -V slideNumber="'c'" \
    -V basename=".."

PANDOC_BEAMER = \
  pandoc \
    --template ../pandoc/beamer-template.tex \
    -t beamer \
    --table-of-contents \
    --toc-depth=1 \
    --slide-level 2

# implicit rules
%.html: %.md ../pandoc/revealjs-template.html
	$(PANDOC_REVEALJS_INDEX) $< -o $@

%.full.html: %.md ../pandoc/revealjs-template.html
	$(PANDOC_REVEALJS_SELF_CONTAINED) $< -o $@

%.pdf: %.md ../pandoc/beamer-template.tex
	$(PANDOC_BEAMER) $< -o $@

