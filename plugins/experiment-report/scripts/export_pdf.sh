#!/usr/bin/env bash
# export_pdf.sh - Export markdown report to PDF using pandoc + typst
#
# Usage:
#   export_pdf.sh <input.md> [output.pdf]
#
# Examples:
#   export_pdf.sh Report_Exp01-02_analysis.md
#   export_pdf.sh Report_Exp01-02_analysis.md custom_output.pdf
#
# Prerequisites:
#   - pandoc (https://pandoc.org/)
#   - typst (https://typst.app/)
#
# Installation:
#   brew install pandoc typst

set -euo pipefail

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory (for finding template)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_PATH="${SCRIPT_DIR}/../assets/templates/report.typ"

# Usage function
usage() {
    echo "Usage: $(basename "$0") <input.md> [output.pdf]"
    echo ""
    echo "Export markdown report to PDF using pandoc + typst"
    echo ""
    echo "Arguments:"
    echo "  input.md    Path to the markdown report file"
    echo "  output.pdf  Optional: Output PDF path (default: same name as input)"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") Report_Exp01-02_analysis.md"
    echo "  $(basename "$0") Report_Exp01-02_analysis.md custom_output.pdf"
    exit 1
}

# Check prerequisites
check_prerequisites() {
    local missing=()

    if ! command -v pandoc &> /dev/null; then
        missing+=("pandoc")
    fi

    if ! command -v typst &> /dev/null; then
        missing+=("typst")
    fi

    if [ ${#missing[@]} -ne 0 ]; then
        echo -e "${RED}Error: Missing required tools: ${missing[*]}${NC}"
        echo ""
        echo "Install with:"
        echo "  brew install ${missing[*]}"
        exit 1
    fi
}

# Main function
main() {
    # Check arguments
    if [ $# -lt 1 ]; then
        usage
    fi

    local input_file="$1"
    local output_file="${2:-}"

    # Validate input file
    if [ ! -f "$input_file" ]; then
        echo -e "${RED}Error: Input file not found: ${input_file}${NC}"
        exit 1
    fi

    # Determine output filename
    if [ -z "$output_file" ]; then
        output_file="${input_file%.md}.pdf"
    fi

    # Check template exists
    if [ ! -f "$TEMPLATE_PATH" ]; then
        echo -e "${YELLOW}Warning: Template not found at ${TEMPLATE_PATH}${NC}"
        echo "Using default pandoc + typst rendering"
        TEMPLATE_PATH=""
    fi

    # Check prerequisites
    check_prerequisites

    # Build pandoc command
    echo -e "${GREEN}Exporting PDF...${NC}"
    echo "  Input:    ${input_file}"
    echo "  Output:   ${output_file}"
    if [ -n "$TEMPLATE_PATH" ]; then
        echo "  Template: ${TEMPLATE_PATH}"
    fi
    echo ""

    # Run pandoc with typst engine
    if [ -n "$TEMPLATE_PATH" ]; then
        pandoc "$input_file" \
            -o "$output_file" \
            --pdf-engine=typst \
            --template="$TEMPLATE_PATH"
    else
        pandoc "$input_file" \
            -o "$output_file" \
            --pdf-engine=typst
    fi

    # Check result
    if [ -f "$output_file" ]; then
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
