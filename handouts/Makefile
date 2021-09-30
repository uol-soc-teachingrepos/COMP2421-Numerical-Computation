%.docx: %.md
	pandoc $< -o $@

%.html: %.md
	pandoc \
	  --template ../pandoc/html-template.html \
	  --standalone \
	  -V basename=".." \
          -V lang="en"\
	  $< -o $@

%.pdf: %.md
	pandoc $< -o $@
