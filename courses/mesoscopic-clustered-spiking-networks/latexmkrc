$pdf_mode = 1;
$pdflatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 %O %S';
$bibtex = 'biber %O %S';
$recorder = 1;

$aux_dir = 'build';
$out_dir = 'build';

# Extra files to clean with `latexmk -c`
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
@clean_ext = qw(acn acr alg glg glo gls glsdefs ist run.xml idx ilg ind);
