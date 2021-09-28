%.docx: %.md
	pandoc $< -o $@

%.html: %.md
	pandoc \
	  --template ../pandoc/html-template.html \
	  --standalone \
	  -V basename=".." \
	  $< -o $@

%.pdf: %.md
	pandoc $< -o $@
