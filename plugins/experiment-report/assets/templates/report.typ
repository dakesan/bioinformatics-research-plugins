// Simple Scientific Report Template for pandoc + typst
// Usage: pandoc report.md -o report.pdf --pdf-engine=typst --template=report.typ

// Page settings
#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm),
)

// Text settings
#set text(
  font: ("Linux Libertine", "Hiragino Mincho ProN", "Noto Serif CJK JP"),
  size: 11pt,
  lang: "en",
)

// Paragraph settings
#set par(
  justify: true,
  leading: 0.65em,
)

// Heading settings
#set heading(numbering: "1.1")

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
  v(0.5em)
  it
  v(0.5em)
}

#show figure.caption: it => {
  set text(size: 10pt)
  it
}

// Table settings
#show table: set table(stroke: 0.5pt + gray)

// Code block settings
#show raw.where(block: true): it => {
  set text(size: 9pt)
  block(
    fill: luma(245),
    inset: 8pt,
    radius: 3pt,
    width: 100%,
    it,
  )
}

// Inline code settings
#show raw.where(block: false): it => {
  box(
    fill: luma(240),
    inset: (x: 3pt, y: 0pt),
    outset: (y: 3pt),
    radius: 2pt,
    it,
  )
}

// Link settings
#show link: it => {
  set text(fill: rgb("#0066cc"))
  it
}

// Title block
#align(center)[
  #v(2cm)
  #text(size: 20pt, weight: "bold")[$title$]
  #v(1cm)
  $if(author)$
  #text(size: 12pt)[$for(author)$$author$$sep$, $endfor$]
  #v(0.5em)
  $endif$
  $if(date)$
  #text(size: 11pt, fill: gray)[$date$]
  $endif$
  #v(1cm)
]

// Horizontal rule
#line(length: 100%, stroke: 0.5pt + gray)
#v(1em)

// Main body
$body$
