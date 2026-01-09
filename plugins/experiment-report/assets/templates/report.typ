// Scientific Report Template for pandoc + typst
// Usage: pandoc report.md -o report.pdf --pdf-engine=typst --template=report.typ
// Optimized for complex tables and multilingual content

#import "@preview/booktabs:0.0.4": *

// Define fonts
#let font-jp = "Noto Serif CJK JP"
#let font-mono = "Courier New"
#let body-size = 11pt

// Page settings
#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm),
  numbering: "1",
  number-align: center,
)

// Text settings
#set text(
  font: font-jp,
  size: body-size,
  lang: "ja",
  fill: luma(30),
)

// Paragraph settings
#set par(
  justify: true,
  leading: 0.75em,
  spacing: 1.3em,
  first-line-indent: 0em,
)

// Heading settings
#set heading(numbering: "1.1")
#show heading: set par(justify: false)

#show heading.where(level: 1): it => {
  set text(size: 14pt, weight: "bold")
  v(1.5em)
  it
  v(0.5em)
}

#show heading.where(level: 2): it => {
  set text(size: 12pt, weight: "bold")
  v(1em)
  it
  v(0.3em)
}

#show heading.where(level: 3): it => {
  set text(size: 11pt, weight: "bold")
  v(0.8em)
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

// Table settings - booktabs package style
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
  #text(size: 22pt, weight: "bold")[$title$]
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
