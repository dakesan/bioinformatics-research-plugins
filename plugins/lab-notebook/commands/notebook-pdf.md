---
description: Export Jupyter notebook or Markdown to PDF using pandoc + typst
---

Export a Jupyter notebook (.ipynb) or Markdown file (.md) to PDF format.

## Workflow

- **For .ipynb files**: Uses nbconvert → pandoc → typst pipeline
- **For .md files**: Uses pandoc → typst pipeline directly

## Usage

```bash
"${CLAUDE_PLUGIN_ROOT}/scripts/notebook_to_pdf.sh" <input.ipynb|input.md> [output.pdf]
```

## User Workflow

1. User specifies the file to export (notebook or markdown)
2. Run the export script with appropriate options
3. Report the result and output location

## Options

| Option | Description |
|--------|-------------|
| `--keep-md` | Keep intermediate markdown file (for .ipynb only) |
| `--no-input` | Exclude code cells from output (for .ipynb only, results only) |

## Examples

### Export Jupyter notebook

```bash
# Export with same basename
notebook_to_pdf.sh notebook/labnote/Exp01_analysis.ipynb

# Export with custom output path
notebook_to_pdf.sh notebook/labnote/Exp01_analysis.ipynb reports/Exp01_report.pdf
```

### Export Markdown file

```bash
# Export markdown directly to PDF
notebook_to_pdf.sh notebook/labnote/Exp01_labnote.md

# Export with custom output path
notebook_to_pdf.sh notebook/labnote/Exp01_labnote.md reports/Exp01_report.pdf
```

### Export without code cells (notebook only)

```bash
# Clean report without source code
notebook_to_pdf.sh --no-input notebook/labnote/Exp01_analysis.ipynb
```

## Prerequisites

The script requires the following tools:

- **nbconvert**: `uv pip install nbconvert` (only needed for .ipynb files)
- **pandoc**: `brew install pandoc` (required for all formats)
- **typst**: `brew install typst` (required for all formats)

## Template

The export uses a custom typst template located at:
`assets/templates/notebook.typ`

This template provides consistent styling for lab notebook PDFs and works with both notebook and markdown inputs.

## Post-Export

After successful export:
1. Inform user of the output location and file size
2. If within a research project, suggest updating `STEERING.md` to track the PDF

## Notes

- For `.md` files, the script skips nbconvert and goes directly to pandoc
- The `--keep-md` and `--no-input` options are only applicable to `.ipynb` files
- Both input formats use the same typst template for consistent output styling
