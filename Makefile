HTML_TARGETS=index.html

TARGETS=${HTML_TARGETS}

BUILDDIR=public

all: ${TARGETS}

%.html: %.md pandoc/video-filter.py pandoc/revealjs-template.html bib/library.bibtex
	pandoc --citeproc \
	--filter ./pandoc/video-filter.py \
	--mathjax \
	--template=./pandoc/revealjs-template.html \
	-t revealjs \
	--slide-level 2 \
	-V controls=true \
	-V controlsTutorial=true \
	-V slideNumber="'c'" \
	-s $< -o $@

%.embed.html: %.md
	pandoc --filter pandoc-citeproc \
	--filter ./pandoc/video-filter.py \
	--mathjax \
	--template=./pandoc/revealjs-template.html \
	-t revealjs \
	-V controls=true \
	-V controlsTutorial=true \
	-V slideNumber=false \
	--slide-level 2 \
	-V embedded="true" \
	-s $< -o $@

%.full.html: %.md
	pandoc --filter pandoc-citeproc \
	--filter ./pandoc/video-filter.py \
	--self-contained \
	--mathjax \
	--template=./pandoc/revealjs-template.html \
	-t revealjs \
	--slide-level 2 \
	-V controls=false \
	-V slideNumber="'c'" \
	-s $< -o $@

build: ${HTML_TARGETS}
	mkdir -p ${BUILDDIR}
	cp ${HTML_TARGETS} ${BUILDDIR}/.
	cp -r css ${BUILDDIR}/css
	cp -r img ${BUILDDIR}/img
	cp -r js ${BUILDDIR}/js
	cp -r video ${BUILDDIR}/video

clean:
	rm -f ${TARGETS}
	rm -rf ${BUILDDIR}
