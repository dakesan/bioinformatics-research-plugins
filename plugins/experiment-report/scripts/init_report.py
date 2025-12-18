#!/usr/bin/env python3
"""
Report Initializer - Creates report template from lab notebooks

Usage:
    init_report.py --labnote <path1> [path2 ...] --output <output_dir> [--title <title>]

Examples:
    init_report.py --labnote notebook/labnote/Exp01_rnaseq.ipynb --output notebook/report/
    init_report.py --labnote Exp01*.ipynb Exp02*.md --output notebook/report/ --title "RNA-seq Analysis"
"""

import sys
from pathlib import Path
from datetime import datetime


REPORT_TEMPLATE = """# {title}

**Date**: {date}
**Report Type**: Integrated Analysis Report

---

## Executive Summary

[TODO: 3-5 sentences capturing key findings and implications]

{executive_summary_placeholder}

## Background

### Research Question

{research_question_placeholder}

### Context

{background_placeholder}

## Materials and Methods

{methods_placeholder}

## Findings

{findings_placeholder}

## Synthesis

{synthesis_placeholder}

## Limitations

{limitations_placeholder}

## Future Directions

{future_directions_placeholder}

## Conclusion

[TODO: Final synthesis and key takeaways]

## References

1. [TODO: Add references]

---

## Appendix

### Lab Notebooks

{notebooks_list}

### Supplementary Information

[TODO: Add supplementary materials]
"""


def extract_notebook_metadata(notebook_path):
    """
    Extract basic metadata from a notebook file.

    Args:
        notebook_path: Path to notebook file

    Returns:
        dict with metadata
    """
    path = Path(notebook_path)

    metadata = {
        'path': str(path),
        'name': path.name,
        'exists': path.exists()
    }

    if not path.exists():
        print(f"⚠️  Warning: Notebook not found: {notebook_path}")
        return metadata

    # Try to extract title from filename
    # Format: Exp##_description.ext
    filename = path.stem
    if filename.startswith('Exp'):
        parts = filename.split('_', 1)
        if len(parts) > 1:
            metadata['experiment_number'] = parts[0]
            metadata['description'] = parts[1].replace('-', ' ').replace('_', ' ')

    return metadata


def generate_placeholders(notebooks_metadata):
    """
    Generate placeholder content based on notebook metadata.

    Args:
        notebooks_metadata: List of metadata dicts

    Returns:
        dict of placeholder strings
    """
    placeholders = {}

    # Notebooks list for appendix
    notebooks_list = []
    for meta in notebooks_metadata:
        if meta['exists']:
            notebooks_list.append(f"- `{meta['name']}`")
    placeholders['notebooks_list'] = '\n'.join(notebooks_list) if notebooks_list else "- [No notebooks specified]"

    # Generate section placeholders based on number of notebooks
    num_notebooks = len([m for m in notebooks_metadata if m['exists']])

    if num_notebooks == 0:
        placeholders['executive_summary_placeholder'] = "\n[No notebooks provided - please add content manually]"
        placeholders['research_question_placeholder'] = "[TODO: Define research question]"
        placeholders['background_placeholder'] = "[TODO: Provide context and rationale]"
        placeholders['methods_placeholder'] = "[TODO: Summarize methods]"
        placeholders['findings_placeholder'] = "[TODO: Describe findings]"
        placeholders['synthesis_placeholder'] = "[TODO: Synthesize interpretations]"
        placeholders['limitations_placeholder'] = "[TODO: Acknowledge limitations]"
        placeholders['future_directions_placeholder'] = "[TODO: Outline next steps]"
    else:
        # Provide guidance for content extraction
        placeholders['executive_summary_placeholder'] = f"\n<!-- Extract key conclusions from {num_notebooks} notebook(s) -->"
        placeholders['research_question_placeholder'] = "<!-- Extract from notebook Hypothesis sections -->"
        placeholders['background_placeholder'] = "<!-- Extract from notebook Background sections -->"
        placeholders['methods_placeholder'] = f"<!-- Consolidate methods from {num_notebooks} notebook(s) -->"

        # Generate finding placeholders based on notebooks
        findings = []
        for i, meta in enumerate(notebooks_metadata, 1):
            if not meta['exists']:
                continue
            desc = meta.get('description', f'Finding {i}')
            findings.append(f"""### Finding {i}: {desc}

**Observation**: <!-- Extract from Results section of {meta['name']} -->

**Evidence**:
- Lab notebook: `{meta['name']}`
- Figures: [TODO]

**Interpretation**: <!-- Extract from Discussion section -->
""")

        placeholders['findings_placeholder'] = '\n'.join(findings) if findings else "[TODO: Add findings]"
        placeholders['synthesis_placeholder'] = f"<!-- Integrate interpretations from {num_notebooks} notebook(s) -->"
        placeholders['limitations_placeholder'] = "<!-- Consolidate limitations from all notebooks -->"
        placeholders['future_directions_placeholder'] = "<!-- Prioritize next steps from all notebooks -->"

    return placeholders


def init_report(labnote_paths, output_dir, title=None):
    """
    Initialize report from lab notebooks.

    Args:
        labnote_paths: List of paths to lab notebooks
        output_dir: Directory where report should be created
        title: Optional custom title

    Returns:
        Path to created report, or None if error
    """
    output_path = Path(output_dir).resolve()

    print(f"🚀 Initializing report from {len(labnote_paths)} notebook(s)")
    print(f"   Output directory: {output_path}")
    print()

    # Create output directory if needed
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created output directory: {output_path}")

    # Extract metadata from notebooks
    notebooks_metadata = []
    for notebook_path in labnote_paths:
        metadata = extract_notebook_metadata(notebook_path)
        notebooks_metadata.append(metadata)
        if metadata['exists']:
            print(f"✅ Found notebook: {metadata['name']}")
        else:
            print(f"⚠️  Notebook not found: {notebook_path}")

    print()

    # Determine report title
    if title is None:
        # Generate title from notebooks
        if len(notebooks_metadata) == 1:
            meta = notebooks_metadata[0]
            title = f"Report_{meta.get('experiment_number', 'Exp00')}_{meta.get('description', 'analysis')}"
        else:
            # Multiple notebooks
            exp_numbers = [m.get('experiment_number', '') for m in notebooks_metadata if m.get('experiment_number')]
            if exp_numbers:
                title = f"Report_{exp_numbers[0]}-{exp_numbers[-1]}_integrated_analysis"
            else:
                title = f"Report_integrated_analysis_{datetime.now().strftime('%Y%m%d')}"

    # Sanitize title for filename
    safe_title = title.replace(' ', '_').replace('/', '_')
    report_path = output_path / f"{safe_title}.md"

    # Check if report already exists
    if report_path.exists():
        print(f"⚠️  Warning: Report already exists: {report_path}")
        response = input("Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("❌ Cancelled")
            return None

    # Generate placeholders
    placeholders = generate_placeholders(notebooks_metadata)

    # Generate report content
    report_content = REPORT_TEMPLATE.format(
        title=title.replace('_', ' ').title(),
        date=datetime.now().strftime('%Y-%m-%d'),
        **placeholders
    )

    # Write report
    report_path.write_text(report_content)
    print(f"✅ Created report: {report_path}")
    print()

    # Next steps
    print("📋 Next steps:")
    print("1. Review the generated report template")
    print("2. Extract content from lab notebooks to fill in placeholders")
    print("3. Synthesize findings across experiments")
    print("4. Use /research-refine to improve report quality")
    print()
    print("💡 Tip: Look for <!-- comments --> for extraction guidance")

    return report_path


def main():
    if len(sys.argv) < 5:
        print("Usage: init_report.py --labnote <path1> [path2 ...] --output <output_dir> [--title <title>]")
        print()
        print("Examples:")
        print("  init_report.py --labnote notebook/labnote/Exp01_rnaseq.ipynb --output notebook/report/")
        print("  init_report.py --labnote Exp01*.ipynb Exp02*.md --output notebook/report/ --title 'RNA-seq Analysis'")
        sys.exit(1)

    # Parse arguments
    args = sys.argv[1:]

    labnote_paths = []
    output_dir = None
    title = None

    i = 0
    while i < len(args):
        if args[i] == '--labnote':
            i += 1
            # Collect all paths until next flag
            while i < len(args) and not args[i].startswith('--'):
                labnote_paths.append(args[i])
                i += 1
        elif args[i] == '--output':
            i += 1
            if i < len(args):
                output_dir = args[i]
                i += 1
        elif args[i] == '--title':
            i += 1
            if i < len(args):
                title = args[i]
                i += 1
        else:
            i += 1

    # Validate arguments
    if not labnote_paths:
        print("❌ Error: No lab notebooks specified (use --labnote)")
        sys.exit(1)

    if not output_dir:
        print("❌ Error: No output directory specified (use --output)")
        sys.exit(1)

    # Initialize report
    result = init_report(labnote_paths, output_dir, title)

    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
