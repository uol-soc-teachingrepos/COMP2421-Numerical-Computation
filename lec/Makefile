PANDOC_REVEALJS= \
  pandoc \
	-t revealjs \
	--template=../pandoc/revealjs-template.html \
	--metadata-file=../metadata.yaml \
	--mathjax \
	--embed-resources \
	--slide-level 3 \
	--standalone \
	--table-of-contents \
	--toc-depth=2 \
	-V history=true \
	-V lang="en_GB" \
	-V controls=false \
	-V progress=true \
	-V slideNumber="'c'" \
	-V overview=true \
	-V navigationMode='linear'

%.revealjs.html: %.md
	$(PANDOC_REVEALJS) $< -o $@
