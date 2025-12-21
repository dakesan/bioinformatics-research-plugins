---
description: Export Jupyter notebook to PDF using pandoc + typst
---

Export a Jupyter notebook (.ipynb) to PDF format. Uses nbconvert → pandoc → typst pipeline for high-quality PDF output.

## Usage

```bash
/Users/oodakemac/ghq/github.com/dakesan/bioinformatics-research-plugins/plugins/lab-notebook/scripts/notebook_to_pdf.sh <input.ipynb> [output.pdf]
```

## Workflow

1. User specifies the notebook to export (or Claude finds it from context)
2. Run the export script with appropriate options
3. Report the result and output location

## Options

| Option | Description |
|--------|-------------|
| `--keep-md` | Keep intermediate markdown file |
| `--no-input` | Exclude code cells from output (results only) |

## Examples

### Basic export

```bash
# Export with same basename
notebook_to_pdf.sh notebook/labnote/Exp01_analysis.ipynb

# Export with custom output path
notebook_to_pdf.sh notebook/labnote/Exp01_analysis.ipynb reports/Exp01_report.pdf
```

### Export without code cells

```bash
# Clean report without source code
notebook_to_pdf.sh --no-input notebook/labnote/Exp01_analysis.ipynb
```

## Prerequisites

The script requires the following tools:

- **nbconvert**: `uv pip install nbconvert`
- **pandoc**: `brew install pandoc`
- **typst**: `brew install typst`

## Template

The export uses a custom typst template located at:
`assets/templates/notebook.typ`

This template provides consistent styling for lab notebook PDFs.

## Post-Export

After successful export:
1. Inform user of the output location and file size
2. If within a research project, suggest updating `STEERING.md` to track the PDF
