%.docx: %.md
	pandoc $< -o $@

%.html: %.md
	pandoc --template ../pandoc/html-template.html $< -o $@

%.pdf: %.md
	pandoc $< -o $@
