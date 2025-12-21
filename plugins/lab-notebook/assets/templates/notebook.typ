// Lab Notebook Template for pandoc + typst
// Usage: pandoc notebook.md -o notebook.pdf --pdf-engine=typst --template=notebook.typ
// Optimized for Jupyter notebook output with code blocks and figures

// Page settings
#set page(
  paper: "a4",
  margin: (top: 2cm, bottom: 2cm, left: 2cm, right: 2cm),
)

// Text settings
#set text(
  font: ("Linux Libertine", "Hiragino Mincho ProN", "Noto Serif CJK JP"),
  size: 10pt,
  lang: "en",
)

// Paragraph settings
#set par(
  justify: true,
  leading: 0.6em,
)

// Heading settings (no numbering for notebooks)
#set heading(numbering: none)

#show heading.where(level: 1): it => {
  set text(size: 14pt, weight: "bold")
  v(1.2em)
  it
  v(0.4em)
}

#show heading.where(level: 2): it => {
  set text(size: 12pt, weight: "bold")
  v(0.8em)
  it
  v(0.3em)
}

#show heading.where(level: 3): it => {
  set text(size: 10pt, weight: "bold")
  v(0.6em)
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
  set text(size: 9pt)
  it
}

// Table settings
#show table: set table(stroke: 0.5pt + gray)

// Code block settings (larger for notebooks)
#show raw.where(block: true): it => {
  set text(size: 8pt, font: "Menlo")
  block(
    fill: luma(248),
    inset: 6pt,
    radius: 2pt,
    width: 100%,
    it,
  )
}

// Inline code settings
#show raw.where(block: false): it => {
  set text(font: "Menlo")
  box(
    fill: luma(240),
    inset: (x: 2pt, y: 0pt),
    outset: (y: 2pt),
    radius: 2pt,
    it,
  )
}

// Link settings
#show link: it => {
  set text(fill: rgb("#0066cc"))
  it
}

// Title block (compact for notebooks)
#align(center)[
  #v(1cm)
  #text(size: 18pt, weight: "bold")[$title$]
  #v(0.5cm)
$if(author)$
  #text(size: 11pt)[$for(author)$$author$$sep$, $endfor$]
  #v(0.3em)
$endif$
$if(date)$
  #text(size: 10pt, fill: gray)[$date$]
$endif$
  #v(0.5cm)
]

// Horizontal rule
#line(length: 100%, stroke: 0.5pt + gray)
#v(0.8em)

// Main body
$body$
