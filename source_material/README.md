# Mythical Person-Month source material

Here are some PDFs and a text file conversion of The Mythical Man-Month.

## qpdf commands

It is weird that the starting page numbers in the PDF shift from the page numbers
in the table of contents and eventually it lines up for nine of the last 10
chapters.

```ShellCommands
 1010  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages 2-6 -- ../chapters/00-front-matter.pdf
 1011  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 2-6 -- ../chapters/00-front-matter.pdf
 1013  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 8-10 -- ../chapters/01-preface-20th-anniversary.pdf
 1016  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 11-13 -- ../chapters/02-preface-first-edition.pdf
 1018  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 14 -- ../chapters/03-contents.pdf
 1024  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 15-24 -- ../chapters/04-chapter-01-the-tar-pit.pdf
 1026  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 15-23 -- ../chapters/04-chapter-01-the-tar-pit.pdf
 1027  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 24-39 -- ../chapters/05-chapter-02-the-mythical-man-month.pdf
 1028  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 40-48 -- ../chapters/06-chapter-03-the-surgical-team.pdf
 1030  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 49-60 -- ../chapters/07-chapter-04-aristocracy-democracy-and-system-design.pdf
 1033  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 61-68 -- ../chapters/08-chapter-05-the-second-system-effect.pdf
 1034  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 69-79 -- ../chapters/09-chapter-06-passing-the-word.pdf
 1035  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 80-92 -- ../chapters/10-chapter-07-why-did-the-tower-of-babel-fail.pdf
 1036  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 93-102 -- ../chapters/11-chapter-08-calling-the-shot.pdf
 1037  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 103-111 -- ../chapters/12-chapter-09-ten-pounds-in-a-five-pound-sack.pdf
 1040  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 119-127 -- ../chapters/14-chapter-11-plan-to-throw-one-away.pdf
 1041  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 127-140 -- ../chapters/15-chapter-12-sharp-tools.pdf
 1044  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 112-118 -- ../chapters/13-chapter-10-the-documentary-hypothesis.pdf
 1045  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 141-152 -- ../chapters/16-chapter-13-the-whole-and-the-parts.pdf
 1047  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 153-162 -- ../chapters/17-chapter-14-hatching-a-catastrophe.pdf
 1048  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 163-177 -- ../chapters/18-chapter-15-the-other-face.pdf
 1049  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 178-204 -- ../chapters/19-chapter-16-no-silver-bullet-essence-and-accident.pdf
 1050  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 205-226 -- ../chapters/20-chapter-17-no-silver-bullet-refired.pdf
 1051  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 227-250 -- ../chapters/21-chapter-18-propositions-true-or-false.pdf
 1052  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 251-290 -- ../chapters/22-chapter-19-after-20-years.pdf
 1053  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 291-292 -- ../chapters/23-epilogue.pdf
 1054  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 293-308 -- ../chapters/98-notes-and-references.pdf
 1055  qpdf Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.pdf --pages . 309-322 -- ../chapters/99-index.pdf
```
