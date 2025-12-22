// Lab Notebook / Scientific Report Template for pandoc + typst
// Usage: pandoc notebook.md -o notebook.pdf --pdf-engine=typst --template=notebook.typ
// Optimized for Jupyter notebook output and scientific reports
// Reference: basic-report template, booktabs package (Typst Universe)

#import "@preview/booktabs:0.0.4": *

// Define fonts
#let font-jp = "Noto Serif CJK JP"
#let font-mono = "Courier New"
#let body-size = 11pt

// Page setup - generous margins for readability
#set page(
  paper: "a4",
  margin: (top: 3cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm),
  numbering: "1",
  number-align: center,
  header-ascent: 1.5em,
)

// Text setup - comfortable reading
#set text(
  font: font-jp,
  size: body-size,
  lang: "ja",
  fill: luma(30),
)

// Paragraph setup - key for readability
#set par(
  justify: true,
  leading: 0.85em,
  spacing: 1.5em,
  first-line-indent: 0em,
)

// Heading settings
#set heading(numbering: "1.1.1")
#show heading: set par(justify: false)

#show heading.where(level: 1): it => {
  v(2em, weak: true)
  set text(size: 16pt, weight: "bold")
  it
  v(0.8em)
}

#show heading.where(level: 2): it => {
  v(1.5em, weak: true)
  set text(size: 13pt, weight: "bold")
  it
  v(0.6em)
}

#show heading.where(level: 3): it => {
  v(1.2em, weak: true)
  set text(size: 11pt, weight: "bold")
  it
  v(0.4em)
}

#show heading.where(level: 4): it => {
  v(1em, weak: true)
  set text(size: 10.5pt, weight: "bold")
  it
  v(0.3em)
}

#show heading.where(level: 5): it => {
  v(0.8em, weak: true)
  set text(size: 10pt, weight: "bold")
  it
  v(0.2em)
}

// Figure settings
#show figure: it => {
  set align(center)
  v(1em)
  it
  v(1em)
}

#show figure.caption: it => {
  set text(size: 10pt)
  set par(leading: 0.65em)
  it
}

// List styling with proper spacing
#set list(
  marker: ([•], [◦], [▪]),
  indent: 1.2em,
  body-indent: 0.5em,
)

#set enum(
  indent: 1.2em,
  body-indent: 0.5em,
)

#show list: set par(spacing: 0.8em)
#show enum: set par(spacing: 0.8em)

// Table styling - booktabs package style
#show: booktabs-default-table-style

#set table(
  inset: (x: 1em, y: 0.8em),
  align: left,
)

#show table: set text(size: 10pt)
#show table: set par(leading: 0.65em)

// Code block settings
#show raw.where(block: true): it => block(
  fill: rgb("#f8f8f8"),
  inset: 1em,
  radius: 3pt,
  width: 100%,
  text(font: font-mono, size: 9pt, it),
)

// Inline code settings
#show raw.where(block: false): it => {
  box(
    fill: rgb("#f0f0f0"),
    inset: (x: 0.3em, y: 0.1em),
    radius: 2pt,
    text(font: font-mono, size: 0.9em, it),
  )
}

// Link settings
#show link: it => underline(it)

// Quote styling
#show quote: block.with(
  fill: rgb("#fafafa"),
  inset: 1.2em,
  radius: 3pt,
)

// Horizontal rule
#let horizontalrule = v(1em) + line(length: 100%, stroke: 0.5pt + luma(180)) + v(1em)

// Title block
#align(center)[
  #v(1.5cm)
  #text(size: 24pt, weight: "bold")[$title$]
  #v(1em)
$if(author)$
  #text(size: 12pt)[$for(author)$$author$$sep$, $endfor$]
  #v(0.5em)
$endif$
$if(date)$
  #text(size: 11pt, fill: luma(80))[$date$]
$endif$
  #v(1.5cm)
]

// Main body
$body$
