WS_MD:=$(shell find . -name "ws0[0-9].md")
WS_IPYNB:=$(shell find . -name "ws0[0-9].ipynb")

_PDF:=$(WS_MD:%.md=%_.pdf)
_PDF+=$(WS_IPYNB:%.ipynb=%_.pdf)

all: ws.pdf

ws.pdf: $(_PDF)
	pdfjam $(sort $?) -o $@

%_.pdf: %_guide.pdf %.pdf %_implemented.pdf
	pdfjam $? -o $@
ws00_.pdf: ws00.pdf ws00_implemented.pdf
	pdfjam $? -o $@
ws01_.pdf: ws01_guide.pdf
	pdfjam $? -o $@

%.pdf: %.md
	pandoc $< -so $@
%_implemented.pdf: %_implemented.ipynb
	jupyter nbconvert --execute --inplace $<
	pandoc $< -so $@
	jupyter nbconvert \
		--ClearOutputPreprocessor.enabled=True \
		--inplace $<
%.pdf: %.ipynb
	pandoc $< -so $@
