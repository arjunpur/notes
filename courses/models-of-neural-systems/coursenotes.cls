\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{coursenotes}[2026/05/12 AAND-style lecture notes compatibility template]

% This class is a compatibility bridge for older courses that still use
% \documentclass{coursenotes} and chapter-style source files. New courses should
% use the article preamble in templates/aand-article/main.tex directly.

\LoadClass[11pt]{article}

% ---------- Typography and layout ----------
\RequirePackage[margin=1in]{geometry}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern}
\RequirePackage{microtype}
\RequirePackage{amsmath,amssymb,mathtools}
\RequirePackage{amsthm}
\RequirePackage{booktabs}
\RequirePackage{graphicx}
\RequirePackage{hyperref}
\hypersetup{hidelinks}
\RequirePackage{parskip}
\RequirePackage{enumitem}
\RequirePackage{longtable}
\RequirePackage{tabularx}
\RequirePackage{xcolor}
\RequirePackage[most]{tcolorbox}
\RequirePackage{listings}
\RequirePackage{url}
\RequirePackage{xparse}

% ---------- Diagrams ----------
\RequirePackage{tikz}
\RequirePackage{pgfplots}
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
\pgfplotsset{compat=1.18}

% ---------- Cross-references ----------
\RequirePackage[capitalise,noabbrev]{cleveref}
\crefname{chapter}{lecture}{lectures}
\Crefname{chapter}{Lecture}{Lectures}

% ---------- Defaults ----------
\setcounter{tocdepth}{3}
\setlist{itemsep=0.25em, topsep=0.35em}
\urlstyle{same}
\lstset{
  basicstyle=\small\ttfamily,
  breaklines=true,
  frame=single,
  framerule=0.2pt,
  columns=fullflexible,
  keepspaces=true,
  showstringspaces=false
}

% Older course files may write chapter entries into the ToC. Article does not
% define that level, so map it to the same visual level as sections.
\makeatletter
\providecommand*\l@chapter{\@dottedtocline{1}{1.5em}{2.3em}}
\makeatother

% ---------- Legacy book-command compatibility ----------
\providecommand{\frontmatter}{}
\providecommand{\mainmatter}{}
\providecommand{\backmatter}{}
\providecommand{\chaptermark}[1]{}
\providecommand{\sectionmark}[1]{}
\providecommand{\index}[1]{}

\newcounter{chapter}
\renewcommand{\thechapter}{\arabic{chapter}}

\let\CourseNotesSection\section
\let\CourseNotesSubsection\subsection
\let\CourseNotesSubsubsection\subsubsection

\RenewDocumentCommand{\part}{s m}{%
  \par\bigskip
  \IfBooleanTF{#1}{%
    \CourseNotesSection*{#2}%
  }{%
    \CourseNotesSection*{#2}%
    \addcontentsline{toc}{section}{#2}%
  }%
  \par\medskip
}

\NewDocumentCommand{\chapter}{s m}{%
  \IfBooleanTF{#1}{%
    \CourseNotesSection*{#2}%
  }{%
    \refstepcounter{chapter}%
    \CourseNotesSection{Lecture \thechapter: #2}%
  }%
}

\RenewDocumentCommand{\section}{s m}{%
  \IfBooleanTF{#1}{%
    \CourseNotesSubsection*{#2}%
  }{%
    \CourseNotesSubsection{#2}%
  }%
}

\RenewDocumentCommand{\subsection}{s m}{%
  \IfBooleanTF{#1}{%
    \CourseNotesSubsubsection*{#2}%
  }{%
    \CourseNotesSubsubsection{#2}%
  }%
}

\endinput
