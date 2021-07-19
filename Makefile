HTML_TARGETS=index.html
ALL_HTML_TARGETS=index.html index.full.html index.embed.html

TARGETS=${HTML_TARGETS}

BUILDDIR=public

all: ${TARGETS}

%.html: %.md pandoc/video-filter.py pandoc/revealjs-template.html bib/library.bibtex
	pandoc  \
	--mathjax \
	--template=./pandoc/revealjs-template.html \
	-t revealjs \
	--no-highlight \
	--slide-level 2 \
	-V controls=true \
	-V controlsTutorial=true \
	-V slideNumber="'c'" \
	-s $< -o $@

%.embed.html: %.md
	pandoc --citeproc \
	--filter ./pandoc/video-filter.py \
	--mathjax \
	--template=./pandoc/revealjs-template.html \
	-t revealjs \
	--no-highlight \
	-V controls=true \
	-V controlsTutorial=true \
	-V slideNumber=false \
	--slide-level 2 \
	-V embedded="true" \
	-V print-pdf=false \
	-s $< -o $@

%.full.html: %.md
	pandoc --citeproc \
	--filter ./pandoc/video-filter.py \
	--self-contained \
	--mathjax \
	--template=./pandoc/revealjs-template.html \
	-t revealjs \
	--no-highlight \
	--slide-level 2 \
	-V controls=false \
	-V slideNumber="'c'" \
	-s $< -o $@

build: ${ALL_HTML_TARGETS}
	mkdir -p ${BUILDDIR}
	cp ${ALL_HTML_TARGETS} ${BUILDDIR}/.
	cp -r css ${BUILDDIR}/css
	cp -r img ${BUILDDIR}/img
	cp -r js ${BUILDDIR}/js
	cp -r video ${BUILDDIR}/video

.PHONY: build

clean:
	rm -f ${TARGETS}
	rm -rf ${BUILDDIR}
