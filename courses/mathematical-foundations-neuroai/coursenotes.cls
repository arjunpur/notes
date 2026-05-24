\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{coursenotes}[2026/04/17 Generic course notes template extracted from Models of Neural Systems]

% ---------- Base class ----------
\LoadClass[
  12pt,
  twoside,
  openright,
  headings=normal,
  chapterprefix=true,
  numbers=noenddot
]{scrbook}

% ---------- Typography ----------
\RequirePackage{fontspec}
\RequirePackage{mathtools}  % Load before unicode-math
\RequirePackage{unicode-math}
\RequirePackage{microtype}

\defaultfontfeatures{Ligatures=TeX}
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}[Scale=MatchLowercase]
\setmonofont{Latin Modern Mono}[Scale=MatchLowercase]
\setmathfont{TeX Gyre Pagella Math}

% ---------- Layout ----------
\RequirePackage{geometry}
\geometry{
  papersize={8.5in, 11in},
  textheight=8.5in,
  inner=0.9in,
  outer=0.9in,
  top=0.85in
}

\setlength{\parskip}{0pt}
\setlength{\parindent}{1.5em}
\linespread{1.15}

% ---------- Colours ----------
\RequirePackage{xcolor}

% Only what we actually use
\definecolor{courseRule}{RGB}{0, 0, 0}     % black rules

% ---------- Core packages ----------
\RequirePackage{graphicx}
\RequirePackage{amsmath}
\RequirePackage{booktabs}
\RequirePackage{enumitem}
\RequirePackage[most]{tcolorbox}
\RequirePackage{tabularx}

% ---------- Diagrams ----------
\RequirePackage{tikz}
\RequirePackage{pgfplots}
\pgfplotsset{compat=1.18}
\RequirePackage[european, straightvoltages]{circuitikz}

\usetikzlibrary{
  arrows.meta,
  calc,
  decorations.pathmorphing,
  decorations.markings,
  positioning,
  shapes.geometric,
  patterns,
  backgrounds
}

% ---------- Cross-references ----------
\RequirePackage{hyperref}
\makeatletter
\AtBeginDocument{%
  \hypersetup{%
    colorlinks=true,
    linkcolor=black!70,
    citecolor=black!60,
    urlcolor=black!60,
    pdfauthor={\@author},
    pdftitle={\@title}
  }%
}
\makeatother
\RequirePackage[capitalise, noabbrev]{cleveref}

% ---------- Bibliography ----------
\RequirePackage{csquotes}

% ---------- Headers and footers (KOMA-Script) ----------
\RequirePackage{scrlayer-scrpage}
\pagestyle{scrheadings}
\clearpairofpagestyles
\ofoot[\pagemark]{\pagemark}
\ihead{\leftmark}
\ohead{\rightmark}

% Chapter on left page header, section on right
\automark[section]{chapter}

% ---------- Chapter heading style ----------
\addtokomafont{chapter}{\sffamily\color{black}}
\addtokomafont{section}{\sffamily\color{black}}
\addtokomafont{subsection}{\sffamily\color{black}}
\addtokomafont{chapterprefix}{\sffamily\large}
\renewcommand*{\raggedchapter}{\raggedright}

% Rule under chapter title
\renewcommand*{\chapterformat}{%
  \mbox{\scalebox{2.2}{\thechapter\autodot\enskip}}%
}
\RedeclareSectionCommand[
  afterskip=1.5em,
  beforeskip=0pt
]{chapter}
\renewcommand{\chapterlineswithprefixformat}[3]{%
  #2#3%
  \par\nobreak\vskip 4pt%
  {\rule{\textwidth}{0.6pt}}%
}

% ---------- Part heading style ----------
\addtokomafont{part}{\sffamily\color{black}}
\addtokomafont{partprefix}{\sffamily\large}

\endinput
