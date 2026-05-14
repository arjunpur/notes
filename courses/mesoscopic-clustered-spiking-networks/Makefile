DOC := main
LATEXMK := latexmk
LATEXMKRC := $(CURDIR)/latexmkrc
LATEX_CACHE := $(CURDIR)/.tex-cache
LATEXMK_FLAGS := -norc -r $(LATEXMKRC) -lualatex
ENV := TEXMFCACHE="$(LATEX_CACHE)" TEXMFVAR="$(LATEX_CACHE)" \
       TEXMFCONFIG="$(LATEX_CACHE)" LUAOTFLOAD_CACHE="$(LATEX_CACHE)" \
       LUAOTFLOADCACHE="$(LATEX_CACHE)"

INCLUDE_DIRS := $(shell find chapters appendices -mindepth 1 -maxdepth 1 -type d 2>/dev/null)
BUILD_INCLUDE_DIRS := $(addprefix build/,$(INCLUDE_DIRS))

.PHONY: all watch clean distclean

all:
	@mkdir -p $(LATEX_CACHE) build $(BUILD_INCLUDE_DIRS)
	$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) $(DOC).tex
	cp build/$(DOC).pdf $(DOC).pdf
	cp build/$(DOC).pdf mesoscopic-clustered-spiking-networks-lecture-notes.pdf

watch:
	@mkdir -p $(LATEX_CACHE) build $(BUILD_INCLUDE_DIRS)
	$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) -pvc $(DOC).tex

clean:
	@mkdir -p $(LATEX_CACHE)
	$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) -c $(DOC).tex

distclean:
	rm -rf build .tex-cache main.pdf mesoscopic-clustered-spiking-networks-lecture-notes.pdf
