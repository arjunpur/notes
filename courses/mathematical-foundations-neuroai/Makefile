DOC := main
COURSE_SLUG := mathematical-foundations-neuroai
LATEXMK := latexmk
LATEXMKRC := $(CURDIR)/latexmkrc
LATEX_CACHE := $(CURDIR)/.tex-cache
LATEXMK_FLAGS := -norc -r $(LATEXMKRC) -lualatex
ENV := TEXMFCACHE="$(LATEX_CACHE)" TEXMFVAR="$(LATEX_CACHE)" \
       TEXMFCONFIG="$(LATEX_CACHE)" LUAOTFLOAD_CACHE="$(LATEX_CACHE)" \
       LUAOTFLOADCACHE="$(LATEX_CACHE)"
PYTHON ?= python3

.PHONY: all source pdf clean distclean

all: pdf

source:
	$(PYTHON) scripts/generate_course.py

pdf: source
	@mkdir -p $(LATEX_CACHE) build
	@rm -f build/$(DOC).aux build/$(DOC).bcf build/$(DOC).bbl build/$(DOC).blg build/$(DOC).run.xml build/$(DOC).fdb_latexmk build/$(DOC).fls
	$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) $(DOC).tex
	cp build/$(DOC).pdf $(DOC).pdf
	cp build/$(DOC).pdf $(COURSE_SLUG)-lecture-notes.pdf

clean:
	@mkdir -p $(LATEX_CACHE)
	$(ENV) $(LATEXMK) $(LATEXMK_FLAGS) -c $(DOC).tex

distclean:
	rm -rf build .tex-cache main.pdf $(COURSE_SLUG)-lecture-notes.pdf
