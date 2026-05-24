DOC := main
COURSE_SLUG := foundations-clustered-spiking-networks-chaos
LATEXMK := latexmk
LATEXMKRC := $(CURDIR)/latexmkrc
LATEX_CACHE := $(CURDIR)/.tex-cache
LATEXMK_FLAGS := -norc -r $(LATEXMKRC) -lualatex
ENV := TEXMFCACHE="$(LATEX_CACHE)" TEXMFVAR="$(LATEX_CACHE)" \
       TEXMFCONFIG="$(LATEX_CACHE)" LUAOTFLOAD_CACHE="$(LATEX_CACHE)" \
       LUAOTFLOADCACHE="$(LATEX_CACHE)"

.PHONY: all pdf clean distclean

all: pdf

pdf:
	@mkdir -p $(LATEX_CACHE) build
	$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) $(DOC).tex
	cp build/$(DOC).pdf $(DOC).pdf
	cp build/$(DOC).pdf $(COURSE_SLUG)-lecture-notes.pdf

clean:
	@mkdir -p $(LATEX_CACHE)
	$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) -c $(DOC).tex

distclean:
	rm -rf build .tex-cache main.pdf $(COURSE_SLUG)-lecture-notes.pdf
