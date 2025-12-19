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


REPORT_TEMPLATE = '''# {title}

**Date**: {date}

**Author**: [Name]

**Experiments Covered**: {experiments_list}

**Project Goal**: [Link to STEERING.md or brief statement of overarching research objective]

---

## Executive Summary

[3-5 sentences: Research question → Approach → Key findings (with numbers) → Implications]

<!-- Quality Gate: Executive Summary
- [ ] Length: 3-5 sentences (no more)
- [ ] Contains quantitative highlight (e.g., "2,453 genes", "90% validation")
- [ ] Self-contained: understandable without reading full report
- [ ] No technical jargon or figure references
- [ ] Covers: question, approach, finding, implication
-->

---

## Background

### Research Context

{background_placeholder}

### Research Question

<!-- Extract from notebook Hypothesis sections -->

### Hypotheses Tested

| ID | Hypothesis | Source Experiment | Status |
|----|------------|-------------------|--------|
{hypotheses_rows}

---

## Methods

### Data Sources

| Dataset | Version/Date | Source | Experiments Used |
|---------|--------------|--------|------------------|
{data_sources_rows}

### Analysis Environment

| Component | Specification |
|-----------|---------------|
| OS | <!-- e.g., macOS 14.0 / Ubuntu 22.04 --> |
| Python | <!-- e.g., 3.11.5 --> |
| Key packages | <!-- e.g., pandas 2.0.3, numpy 1.24.0 --> |
| Random seed | <!-- e.g., 42 --> |
| Hardware | <!-- e.g., M2 Max, 32GB RAM --> |

### Tools and Versions

| Tool | Version | Purpose |
|------|---------|---------|
{tools_rows}

### Procedures

<!-- Consolidate methods from {num_notebooks} notebook(s) -->

<!-- Quality Gate: Methods
- [ ] All datasets have version/date
- [ ] All tools have versions
- [ ] Environment reproducible (OS, packages, seed)
- [ ] Procedures detailed enough for replication
-->

---

## Findings

<!--
IMPORTANT: Use Claim-Evidence structure for each finding.
Each finding must have:
1. Claim/Theme: What you observed
2. Observation: Factual description (Level 1)
3. Evidence: Specific references to notebooks, figures, statistics
4. Uncertainty: Confidence level and caveats
5. Alternative interpretations: Other possible explanations
-->

{findings_section}

<!-- Quality Gate: Findings
- [ ] Each finding has Claim-Evidence structure
- [ ] All evidence paths exist and are correct (verify: ../labnote/, ../results/)
- [ ] Statistics include test type, p-value, effect size
- [ ] Observations are factual (no interpretation)
- [ ] Uncertainty level stated for each finding
- [ ] Alternative interpretations considered
- [ ] Figures numbered and referenced correctly
-->

---

## Synthesis

### Integration of Findings

<!-- How do the findings connect? What story do they tell together? -->

**Claim-Evidence Summary**:

| Main Claim | Supporting Findings | Confidence | Key Evidence |
|------------|---------------------|------------|--------------|
| [Integrated claim 1] | F1, F2 | Strong/Moderate/Weak | [Key stats/figures] |
| [Integrated claim 2] | F2, F3 | Strong/Moderate/Weak | [Key stats/figures] |

### Hypothesis Evaluation

| Hypothesis | Verdict | Evidence Summary | Confidence |
|------------|---------|------------------|------------|
{hypothesis_eval_rows}

### Interpretation (Level 2)

<!-- What do these findings mean? Connect to broader biological context -->

<!-- Quality Gate: Synthesis
- [ ] Claims clearly separated from facts
- [ ] Each claim links to specific findings
- [ ] Confidence language calibrated (see refinement-guide.md)
- [ ] Alternative explanations discussed
- [ ] Hypotheses evaluated with explicit verdict
- [ ] No unsupported assertions
-->

---

## Limitations

### Methodological Constraints

| Limitation | Impact | Potential Solution |
|------------|--------|-------------------|
| <!-- Specific limitation 1 --> | <!-- How it affects conclusions --> | <!-- How to address --> |
| <!-- Specific limitation 2 --> | <!-- How it affects conclusions --> | <!-- How to address --> |

### Interpretive Caveats

<!-- Broader constraints on interpretation: correlation vs causation, generalizability, etc. -->

<!-- Quality Gate: Limitations
- [ ] Limitations are specific (not generic)
- [ ] Impact on conclusions stated
- [ ] Solutions or mitigations suggested
- [ ] Honest without being apologetic
-->

---

## Future Directions

### Immediate Next Steps

| Priority | Action | Addresses | Expected Outcome |
|----------|--------|-----------|------------------|
| 1 | <!-- Specific experiment/analysis --> | <!-- Which limitation/question --> | <!-- What we'll learn --> |
| 2 | <!-- Specific experiment/analysis --> | <!-- Which limitation/question --> | <!-- What we'll learn --> |

### Long-term Directions

<!-- Broader research directions suggested by this work -->

<!-- Quality Gate: Future Directions
- [ ] Next steps are specific and actionable
- [ ] Linked to limitations or open questions
- [ ] Prioritized by importance
- [ ] Expected outcomes stated
-->

---

## Conclusion

<!-- 1-3 paragraphs: Restate key findings → Main takeaway → Broader implications → Forward-looking statement -->

<!-- Quality Gate: Conclusion
- [ ] Length: 1-3 paragraphs
- [ ] Restates key findings briefly
- [ ] Clear main takeaway message
- [ ] No new information introduced
- [ ] Appropriate confidence level
-->

---

## References

1. [TODO: Add references]

---

## Appendix

### A. Lab Notebooks

| Experiment | Notebook Path | Status | Key Outputs |
|------------|---------------|--------|-------------|
{notebooks_table}

### B. Figure Index

| Figure | Path | Description | Used In |
|--------|------|-------------|---------|
{figures_table}

### C. Reproducibility Information

**Report Generation** (from project root):
```bash
# Generate report (adjust path to init_report.py as needed)
python path/to/init_report.py --labnote {labnote_paths_cmd} --output notebook/report/

# Export to PDF (from notebook/report/ directory)
cd notebook/report/
pandoc {report_filename} -o report.pdf --pdf-engine=typst
```

**Data Availability**:
- Raw data: [Location/repository]
- Processed data: `../results/`
- Code: [Location/repository]

### D. Supplementary Materials

[Links to additional data, code, or documentation]

---

<!--
FINAL QUALITY CHECKLIST (before submission)

Structure:
- [ ] All sections complete
- [ ] Logical flow between sections
- [ ] No redundancy

Evidence:
- [ ] All figure paths verified (exist in ../results/)
- [ ] All notebook paths verified (exist in ../labnote/)
- [ ] All statistics include test, p-value, effect size
- [ ] Evidence tables complete for each finding

Scientific Rigor:
- [ ] Facts (Observations) separated from interpretation (Synthesis)
- [ ] Confidence language calibrated throughout
- [ ] Alternative explanations considered
- [ ] Limitations honestly acknowledged

Writing:
- [ ] Concise and clear
- [ ] Consistent terminology
- [ ] Figures referenced in text
- [ ] References properly formatted

See references/refinement-guide.md for detailed criteria.
-->
'''

FINDING_TEMPLATE = '''### Finding {num}: {title}

**Claim**: <!-- One sentence stating the main observation -->

**Observation** (Level 1 - Facts only):

<!-- Extract from Results section of {notebook_name} -->

**Evidence Table**:

| Evidence Type | Location | Value/Description |
|---------------|----------|-------------------|
| Lab Notebook | `{notebook_path}` | <!-- Section reference --> |
| Figure | `{results_path}/fig##_*.png` | <!-- Brief description --> |
| Statistic | <!-- Source --> | <!-- e.g., p < 0.001, FC = 2.3 --> |
| Raw Data | `{results_path}/*.csv` | <!-- Description --> |

**Uncertainty & Confidence**:
- Confidence level: <!-- Strong/Moderate/Weak -->
- Key caveats: <!-- List limitations specific to this finding -->

**Alternative Interpretations**:
- <!-- Alternative explanation 1 -->
- <!-- Alternative explanation 2 -->

---

'''


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
        'exists': path.exists(),
        'relative_path': f'../labnote/{path.name}',
        'results_path': None
    }

    if not path.exists():
        print(f"⚠️  Warning: Notebook not found: {notebook_path}")
        return metadata

    # Try to extract experiment info from filename
    # Format: Exp##_description.ext
    filename = path.stem
    if filename.startswith('Exp'):
        parts = filename.split('_', 1)
        if len(parts) > 1:
            metadata['experiment_number'] = parts[0]
            metadata['description'] = parts[1].replace('-', ' ').replace('_', ' ')
            # Infer results path
            exp_lower = parts[0].lower()
            metadata['results_path'] = f'../results/{exp_lower}'

    return metadata


def generate_findings_section(notebooks_metadata):
    """
    Generate findings section with claim-evidence structure.

    Args:
        notebooks_metadata: List of metadata dicts

    Returns:
        String containing findings section
    """
    findings = []

    for i, meta in enumerate(notebooks_metadata, 1):
        if not meta['exists']:
            continue

        title = meta.get('description', f'Finding from {meta["name"]}')
        title = title.title()

        results_path = meta.get('results_path', '../results/exp##')

        finding = FINDING_TEMPLATE.format(
            num=i,
            title=title,
            notebook_name=meta['name'],
            notebook_path=meta['relative_path'],
            results_path=results_path
        )
        findings.append(finding)

    if not findings:
        return "<!-- No notebooks provided - add findings manually -->"

    return '\n'.join(findings)


def generate_placeholders(notebooks_metadata):
    """
    Generate placeholder content based on notebook metadata.

    Args:
        notebooks_metadata: List of metadata dicts

    Returns:
        dict of placeholder strings
    """
    placeholders = {}
    num_notebooks = len([m for m in notebooks_metadata if m['exists']])

    placeholders['num_notebooks'] = num_notebooks

    # Experiments list
    exp_names = []
    for meta in notebooks_metadata:
        if meta['exists']:
            exp_num = meta.get('experiment_number', meta['name'])
            exp_names.append(exp_num)
    placeholders['experiments_list'] = ', '.join(exp_names) if exp_names else '[Exp##, Exp##, ...]'

    # Background placeholder
    if num_notebooks == 0:
        placeholders['background_placeholder'] = '<!-- No notebooks provided - add background manually -->'
    else:
        placeholders['background_placeholder'] = f'<!-- Synthesize background from {num_notebooks} notebook(s) -->'

    # Hypotheses rows
    hyp_rows = []
    for i, meta in enumerate(notebooks_metadata, 1):
        if meta['exists']:
            exp_num = meta.get('experiment_number', f'Exp{i:02d}')
            hyp_rows.append(f'| H{i} | <!-- Extract from {meta["name"]} --> | {exp_num} | Supported/Rejected/Inconclusive |')
    placeholders['hypotheses_rows'] = '\n'.join(hyp_rows) if hyp_rows else '| H1 | [Testable statement] | Exp## | Supported/Rejected/Inconclusive |'

    # Data sources rows
    data_rows = []
    for meta in notebooks_metadata:
        if meta['exists']:
            exp_num = meta.get('experiment_number', 'Exp##')
            data_rows.append(f'| <!-- Dataset --> | <!-- Version/Date --> | <!-- Source --> | {exp_num} |')
    placeholders['data_sources_rows'] = '\n'.join(data_rows) if data_rows else '| [Name] | [v1.0 / 2025-01-15] | [URL/path] | Exp## |'

    # Tools rows
    placeholders['tools_rows'] = '| <!-- Tool name --> | <!-- Version --> | <!-- Brief purpose --> |'

    # Findings section
    placeholders['findings_section'] = generate_findings_section(notebooks_metadata)

    # Hypothesis evaluation rows
    eval_rows = []
    for i, meta in enumerate(notebooks_metadata, 1):
        if meta['exists']:
            eval_rows.append(f'| H{i}: <!-- Statement --> | Supported/Rejected/Inconclusive | <!-- Brief evidence --> | Strong/Moderate/Weak |')
    placeholders['hypothesis_eval_rows'] = '\n'.join(eval_rows) if eval_rows else '| H1: [Statement] | Supported/Rejected/Inconclusive | [Brief evidence] | Strong/Moderate/Weak |'

    # Notebooks table for appendix
    nb_rows = []
    for meta in notebooks_metadata:
        if meta['exists']:
            exp_num = meta.get('experiment_number', 'Exp##')
            nb_rows.append(f'| {exp_num} | `{meta["relative_path"]}` | Complete | <!-- List figures/tables --> |')
    placeholders['notebooks_table'] = '\n'.join(nb_rows) if nb_rows else '| Exp## | `../labnote/Exp##_*.ipynb` | Complete | [List figures/tables] |'

    # Figures table for appendix
    fig_rows = []
    for i, meta in enumerate(notebooks_metadata, 1):
        if meta['exists']:
            results_path = meta.get('results_path', f'../results/exp{i:02d}')
            fig_rows.append(f'| Fig {i} | `{results_path}/fig01_*.png` | <!-- Description --> | Finding {i} |')
    placeholders['figures_table'] = '\n'.join(fig_rows) if fig_rows else '| Fig 1 | `../results/exp##/fig01_*.png` | [Description] | Finding 1 |'

    # Command line paths
    labnote_paths = ' '.join([meta['relative_path'] for meta in notebooks_metadata if meta['exists']])
    placeholders['labnote_paths_cmd'] = labnote_paths if labnote_paths else '../labnote/Exp*.ipynb'

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
    placeholders['report_filename'] = report_path.name

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
    print("2. Fill in claim-evidence tables for each finding")
    print("3. Verify all evidence paths exist (../labnote/, ../results/)")
    print("4. Complete quality gate checklists in each section")
    print("5. Use /research-refine to improve report quality")
    print()
    print("💡 Tip: Look for <!-- comments --> for extraction guidance")
    print("💡 Tip: Check quality gate checklists before finalizing")

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
