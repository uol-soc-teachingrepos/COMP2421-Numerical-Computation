PANDOC_REVEALJS= \
  pandoc \
	-t revealjs \
	--template=../pandoc/revealjs-template.html \
	--metadata-file=../metadata.yaml \
	--mathjax \
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
	-V navigationMode='linear' \
	-V transition='none'

%.revealjs.html: %_.md
	$(PANDOC_REVEALJS) $< -o $@


%.revealjs.html: %_.ipynb
	jupyter nbconvert  \
	  --execute \
	  --TagRemovePreprocessor.remove_input_tags={\"remove-input\"} \
	  $< --to slides --output $@
	mv $@.slides.html $@
