WS_MD:=$(shell find . -name "ws0[0-9].md")
WS_IPYNB:=$(shell find . -name "ws0[0-9].ipynb")
WS_GUIDE_MD:=$(shell find . -name "ws0[0-9]_guide.md")

_PDF:=$(WS_MD:%.md=%_.pdf)
_PDF+=$(WS_IPYNB:%.ipynb=%_.pdf)

GUIDE_PDF:=$(WS_GUIDE_MD:%.md=%.pdf)

all: ws.pdf

ws.pdf: $(_PDF)
	pdfjam $(sort $?) -o $@

ws_guide.pdf: $(GUIDE_PDF)
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
