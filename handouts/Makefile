%.docx: %.md
	pandoc $< -o $@

%.html: %.md
	pandoc --template ../pandoc/html-template.html --standalone $< -o $@

%.pdf: %.md
	pandoc $< -o $@
