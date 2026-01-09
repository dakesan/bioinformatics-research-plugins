#!/usr/bin/env bash
# notebook_to_pdf.sh - Export Jupyter notebook or Markdown to PDF using pandoc + typst
#
# Workflow:
#   .ipynb → (nbconvert) → .md → (pandoc) → .pdf
#   .md → (pandoc) → .pdf
#
# Usage:
#   notebook_to_pdf.sh <input.ipynb|input.md> [output.pdf]
#
# Examples:
#   notebook_to_pdf.sh Exp01_analysis.ipynb
#   notebook_to_pdf.sh Exp01_analysis.md
#   notebook_to_pdf.sh Exp01_analysis.ipynb custom_output.pdf
#
# Prerequisites:
#   - jupyter/nbconvert (pip install nbconvert) - only for .ipynb files
#   - pandoc (https://pandoc.org/)
#   - typst (https://typst.app/)
#
# Installation:
#   uv pip install nbconvert  # only needed for .ipynb files
#   brew install pandoc typst

set -euo pipefail

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory (for finding template)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_PATH="${SCRIPT_DIR}/../assets/templates/notebook.typ"

# Usage function
usage() {
    echo "Usage: $(basename "$0") <input.ipynb|input.md> [output.pdf]"
    echo ""
    echo "Export Jupyter notebook or Markdown to PDF using pandoc + typst"
    echo ""
    echo "Workflow:"
    echo "  .ipynb → .md → .pdf"
    echo "  .md → .pdf"
    echo ""
    echo "Arguments:"
    echo "  input.ipynb|.md  Path to the Jupyter notebook or Markdown file"
    echo "  output.pdf       Optional: Output PDF path (default: same name as input)"
    echo ""
    echo "Options:"
    echo "  --keep-md    Keep intermediate markdown file (for .ipynb only)"
    echo "  --no-input   Exclude code cells from output (for .ipynb only)"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") Exp01_analysis.ipynb"
    echo "  $(basename "$0") Exp01_labnote.md"
    echo "  $(basename "$0") Exp01_analysis.ipynb report.pdf"
    echo "  $(basename "$0") --no-input Exp01_analysis.ipynb"
    exit 1
}

# Check prerequisites
check_prerequisites() {
    local input_file="$1"
    local missing=()

    # nbconvert is only needed for .ipynb files
    if [[ "$input_file" =~ \.ipynb$ ]]; then
        if ! command -v jupyter &> /dev/null && ! command -v jupyter-nbconvert &> /dev/null; then
            missing+=("nbconvert (uv pip install nbconvert)")
        fi
    fi

    if ! command -v pandoc &> /dev/null; then
        missing+=("pandoc")
    fi

    if ! command -v typst &> /dev/null; then
        missing+=("typst")
    fi

    if [ ${#missing[@]} -ne 0 ]; then
        echo -e "${RED}Error: Missing required tools:${NC}"
        for tool in "${missing[@]}"; do
            echo "  - $tool"
        done
        echo ""
        echo "Install with:"
        if [[ "$input_file" =~ \.ipynb$ ]]; then
            echo "  uv pip install nbconvert"
        fi
        echo "  brew install pandoc typst"
        exit 1
    fi
}

# Main function
main() {
    local keep_md=false
    local no_input=false
    local input_file=""
    local output_file=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --keep-md)
                keep_md=true
                shift
                ;;
            --no-input)
                no_input=true
                shift
                ;;
            -h|--help)
                usage
                ;;
            -*)
                echo -e "${RED}Error: Unknown option: $1${NC}"
                usage
                ;;
            *)
                if [ -z "$input_file" ]; then
                    input_file="$1"
                elif [ -z "$output_file" ]; then
                    output_file="$1"
                else
                    echo -e "${RED}Error: Too many arguments${NC}"
                    usage
                fi
                shift
                ;;
        esac
    done

    # Check arguments
    if [ -z "$input_file" ]; then
        usage
    fi

    # Validate input file
    if [ ! -f "$input_file" ]; then
        echo -e "${RED}Error: Input file not found: ${input_file}${NC}"
        exit 1
    fi

    # Check file extension
    local is_notebook=false
    if [[ "$input_file" =~ \.ipynb$ ]]; then
        is_notebook=true
    elif [[ "$input_file" =~ \.md$ ]]; then
        is_notebook=false
    else
        echo -e "${RED}Error: Input file must be a .ipynb or .md file${NC}"
        exit 1
    fi

    # Determine output filename and intermediate markdown file
    local basename
    local md_file
    if $is_notebook; then
        basename="${input_file%.ipynb}"
        md_file="${basename}.md"
    else
        basename="${input_file%.md}"
        md_file="$input_file"
    fi

    if [ -z "$output_file" ]; then
        output_file="${basename}.pdf"
    fi

    # Check template exists
    local use_template=true
    if [ ! -f "$TEMPLATE_PATH" ]; then
        echo -e "${YELLOW}Warning: Template not found at ${TEMPLATE_PATH}${NC}"
        echo "Using default pandoc + typst rendering"
        use_template=false
    fi

    # Check prerequisites
    check_prerequisites "$input_file"

    echo -e "${GREEN}Converting to PDF...${NC}"
    echo "  Input:  ${input_file}"
    echo "  Output: ${output_file}"
    echo ""

    # Step 1: Convert notebook to markdown (only for .ipynb files)
    if $is_notebook; then
        echo -e "${BLUE}Step 1/2: Converting notebook to markdown...${NC}"

        local nbconvert_opts=("--to" "markdown" "--output" "$(basename "$md_file" .md)")
        if $no_input; then
            nbconvert_opts+=("--no-input")
        fi

        if command -v jupyter-nbconvert &> /dev/null; then
            jupyter-nbconvert "${nbconvert_opts[@]}" "$input_file"
        else
            jupyter nbconvert "${nbconvert_opts[@]}" "$input_file"
        fi

        if [ ! -f "$md_file" ]; then
            echo -e "${RED}Error: Markdown conversion failed${NC}"
            exit 1
        fi
        echo "  → Created: ${md_file}"

        # Step 2: Convert markdown to PDF
        echo -e "${BLUE}Step 2/2: Converting markdown to PDF...${NC}"
    else
        # For .md files, skip nbconvert and go directly to pandoc
        echo -e "${BLUE}Converting markdown to PDF...${NC}"
    fi

    # Note: -f markdown-grid_tables disables grid_tables to avoid typst conversion errors
    if $use_template; then
        pandoc "$md_file" \
            -f markdown-grid_tables \
            -o "$output_file" \
            --pdf-engine=typst \
            --template="$TEMPLATE_PATH"
    else
        pandoc "$md_file" \
            -f markdown-grid_tables \
            -o "$output_file" \
            --pdf-engine=typst
    fi

    # Cleanup intermediate file (only for .ipynb files)
    if $is_notebook && ! $keep_md; then
        rm -f "$md_file"
        # Also remove generated image directory if exists
        local img_dir="${basename}_files"
        if [ -d "$img_dir" ]; then
            rm -rf "$img_dir"
        fi
    elif $is_notebook && $keep_md; then
        echo "  → Kept: ${md_file}"
    fi

    # Check result
    if [ -f "$output_file" ]; then
        echo ""
        echo -e "${GREEN}✓ PDF exported successfully: ${output_file}${NC}"

        # Show file size
        local size
        size=$(du -h "$output_file" | cut -f1)
        echo "  Size: ${size}"
    else
        echo -e "${RED}✗ PDF export failed${NC}"
        exit 1
    fi
}

main "$@"
