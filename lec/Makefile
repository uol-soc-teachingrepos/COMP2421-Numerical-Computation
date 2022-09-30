PANDOC_REVEALJS= \
  pandoc \
	-t revealjs \
	--template=../pandoc/revealjs-template.html \
	--metadata-file=../metadata.yaml \
	--mathjax \
	--embed-resources \
	--slide-level 2 \
	--standalone \
	--table-of-contents \
	--toc-depth 1 \
	-V history=true \
	-V lang="en_GB" \
	-V controls=false \
	-V progress=true \
	-V slideNumber="'c'" \
	-V overview=true \
	-V navigationMode='linear'

%.revealjs.html: %_.md
	$(PANDOC_REVEALJS) $< -o $@
