#!/usr/bin/env python3
"""
Research Project Initializer - Creates standardized bioinformatics project structure

Usage:
    init_project.py --path <path>

Examples:
    init_project.py --path .
    init_project.py --path /path/to/new/project
"""

import sys
from pathlib import Path


STEERING_TEMPLATE = """# Project Steering

## Current Status

**Phase**: Planning
**Last Updated**: [DATE]

## Research Question

[TODO: Define your main research question]

## Current Priorities

1. [TODO: Define immediate next steps]

## Active Experiments

- None yet

## Completed Milestones

- ✅ Project initialized

## Next Actions

1. Define research question and hypotheses
2. Create first experiment notebook with `/research-exp`
3. Review best practices in `references/best-practices.md`

---

## Phase History

| Phase | Start Date | End Date | Notes |
|-------|------------|----------|-------|
| Planning | [DATE] | - | Initial setup |
"""

TASKS_TEMPLATE = """# Experiment Tasks

## Active Experiments

None yet

## Planned Experiments

- [ ] Exp01: [TODO: First experiment description]

## Completed Experiments

None yet

---

## Notes

- Use `/research-exp` to create new lab notebooks
- Use `/research-report` to generate integrated reports
- Update this file as experiments progress
"""

LABNOTE_JUPYTER_TEMPLATE = """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exp00_TEMPLATE_labnote\\n",
    "\\n",
    "**Date**: YYYY-MM-DD  \\n",
    "**Experimenter**: [Your Name]\\n",
    "\\n",
    "---\\n",
    "\\n",
    "## Hypothesis\\n",
    "\\n",
    "[TODO: State your testable hypothesis]\\n",
    "\\n",
    "## Background\\n",
    "\\n",
    "[TODO: Provide context and rationale]\\n",
    "\\n",
    "## Materials and Methods\\n",
    "\\n",
    "### Data\\n",
    "\\n",
    "- Source: [TODO]\\n",
    "- Format: [TODO]\\n",
    "- Location: `data/raw/[filename]`\\n",
    "\\n",
    "### Tools\\n",
    "\\n",
    "- Python: [version]\\n",
    "- Key libraries: [list]\\n",
    "\\n",
    "### Procedure\\n",
    "\\n",
    "1. [TODO: Step-by-step procedure]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Setup\\n",
    "import pandas as pd\\n",
    "import numpy as np\\n",
    "import matplotlib.pyplot as plt\\n",
    "from pathlib import Path\\n",
    "\\n",
    "# Configuration\\n",
    "DATA_DIR = Path(\\"../data/raw\\")\\n",
    "RESULTS_DIR = Path(\\"../results\\")\\n",
    "\\n",
    "# Ensure results directory exists\\n",
    "RESULTS_DIR.mkdir(parents=True, exist_ok=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Results\\n",
    "\\n",
    "[TODO: Document observations and outputs]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Analysis code here\\n",
    "\\n",
    "# Example: Creating and saving a figure\\n",
    "# fig, ax = plt.subplots(figsize=(8, 6))\\n",
    "# ax.plot(x, y)\\n",
    "# ax.set_xlabel('X label')\\n",
    "# ax.set_ylabel('Y label')\\n",
    "# ax.set_title('Plot title')\\n",
    "# \\n",
    "# # IMPORTANT: Save figure before showing\\n",
    "# fig.savefig(RESULTS_DIR / 'exp00_example_plot.png', dpi=300, bbox_inches='tight')\\n",
    "# fig.savefig(RESULTS_DIR / 'exp00_example_plot.pdf')  # Vector format for reports\\n",
    "# plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Discussion\\n",
    "\\n",
    "### Interpretation\\n",
    "\\n",
    "[TODO: What do these results mean?]\\n",
    "\\n",
    "### Hypothesis Evaluation\\n",
    "\\n",
    "- [ ] Hypothesis supported\\n",
    "- [ ] Hypothesis rejected\\n",
    "- [ ] Inconclusive\\n",
    "\\n",
    "**Reasoning**: [TODO]\\n",
    "\\n",
    "### Next Steps\\n",
    "\\n",
    "1. [TODO: Follow-up experiments or analyses]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
"""

LABNOTE_MD_TEMPLATE = """# Exp00_TEMPLATE_labnote

**Date**: YYYY-MM-DD
**Experimenter**: [Your Name]

---

## Hypothesis

[TODO: State your testable hypothesis]

## Background

[TODO: Provide context and rationale]

## Materials and Methods

### Data

- Source: [TODO]
- Format: [TODO]
- Location: `data/raw/[filename]`

### Tools

- [TODO: List tools and versions]

### Procedure

1. [TODO: Step-by-step procedure]

## Results

[TODO: Document observations and outputs]

### Figures

![Figure 1](path/to/figure.png)

### Tables

| Column1 | Column2 |
|---------|---------|
| Data    | Data    |

## Discussion

### Interpretation

[TODO: What do these results mean?]

### Hypothesis Evaluation

- [ ] Hypothesis supported
- [ ] Hypothesis rejected
- [ ] Inconclusive

**Reasoning**: [TODO]

### Next Steps

1. [TODO: Follow-up experiments or analyses]
"""

REPORT_TEMPLATE = """# Exp00_TEMPLATE_report

**Date**: YYYY-MM-DD
**Report Type**: Integrated Analysis Report

---

## Executive Summary

[TODO: 2-3 sentence overview of key findings]

## Research Question

[TODO: Define the main research question addressed in this report]

## Background

[TODO: Provide context and rationale for the research]

## Materials and Methods

[TODO: Summarize datasets, tools, and analytical approach]

## Results

### Finding 1: [Title]

**Observation**: [Factual description]

**Interpretation**: [What it means]

**Evidence**:
- Lab notebook: `labnote/Exp##_[name].ipynb`
- Figures: [links]

### Finding 2: [Title]

[Repeat structure]

## Discussion

### Summary of Findings

[TODO: Synthesize key results]

### Biological Implications

[TODO: Discuss scientific significance]

### Limitations

[TODO: Acknowledge constraints and caveats]

### Future Directions

1. [TODO: Next research steps]

## Conclusion

[TODO: Final synthesis and key takeaways]

## References

1. [TODO: Citations]

---

## Appendix

### Lab Notebooks

- `Exp01_[name].ipynb`
- `Exp02_[name].ipynb`

### Supplementary Figures

[Links to additional figures]
"""

GITIGNORE_TEMPLATE = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.venv/
venv/
ENV/
env/

# Jupyter Notebook
.ipynb_checkpoints

# macOS
.DS_Store

# Data (exclude raw data to avoid large files)
data/raw/

# IDE
.vscode/
.idea/
"""

README_TEMPLATE = """# {project_name}

## Overview

[TODO: Describe your research project]

## Research Question

[TODO: Define your main research question]

## Structure

```
{project_name}/
├── STEERING.md       # Project status & navigation
├── notebook/
│   ├── tasks.md      # Experiment progress tracking
│   ├── analysis/     # Exploratory analysis
│   ├── labnote/      # Individual experiments (ipynb)
│   ├── report/       # Integrated reports
│   └── knowledge/    # Reusable procedures
├── src/
│   ├── {{exp_no}}/     # Non-notebook code per experiment
│   └── workflow/     # Snakemake pipelines
│       ├── Snakefile
│       ├── config.yaml
│       ├── rules/    # Modular rule files
│       └── scripts/  # Scripts called by workflow
├── data/
│   ├── raw/          # Original data (gitignored)
│   ├── processed/    # Cleaned data
│   └── experimental/ # Experiment-specific data
├── results/          # Analysis outputs
├── reports/          # Final report outputs
└── inbox/            # User input files
```

## Getting Started

1. Edit `STEERING.md` to define your research question
2. Create experiments with `/research-exp`
3. Generate reports with `/research-report`

## Dependencies

```bash
uv sync
```
"""

PYPROJECT_TEMPLATE = """[project]
name = "{project_name}"
version = "0.1.0"
description = "[TODO: Project description]"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "jupyter>=1.0.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]
"""

SNAKEFILE_TEMPLATE = """# Snakemake workflow for {project_name}
#
# Usage:
#   snakemake --cores 4
#   snakemake --cores 4 --dry-run
#
# Configuration:
#   Edit config.yaml to set parameters

configfile: "config.yaml"


rule all:
    input:
        # Define final outputs here
        expand("results/{{sample}}_result.txt", sample=config["samples"])


rule example_rule:
    input:
        "data/raw/{{sample}}.fastq"
    output:
        "results/{{sample}}_result.txt"
    params:
        param1=config.get("param1", "default")
    threads: 4
    shell:
        \"\"\"
        echo "Processing {{wildcards.sample}}" > {{output}}
        \"\"\"
"""

SNAKEMAKE_CONFIG_TEMPLATE = """# Snakemake configuration for {project_name}

# Sample list
samples:
  - sample1
  - sample2

# Parameters
param1: "default_value"

# Paths
data_dir: "data/raw"
results_dir: "results"
"""


def init_project(path):
    """
    Initialize research project directory structure.

    Args:
        path: Path where the project should be initialized

    Returns:
        True if successful, False otherwise
    """
    project_dir = Path(path).resolve()

    print(f"🚀 Initializing research project at: {project_dir}")
    print()

    # Get project name from directory
    project_name = project_dir.name

    # Create directory structure
    directories = [
        project_dir,
        project_dir / "notebook" / "analysis",
        project_dir / "notebook" / "labnote",
        project_dir / "notebook" / "report",
        project_dir / "notebook" / "knowledge",
        project_dir / "inbox",
        project_dir / "inbox" / "archive",
        project_dir / "data" / "raw",
        project_dir / "data" / "processed",
        project_dir / "data" / "experimental",
        project_dir / "results",
        project_dir / "reports",
        project_dir / "src" / "workflow" / "rules",
        project_dir / "src" / "workflow" / "scripts",
    ]

    for directory in directories:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {directory.relative_to(project_dir.parent)}")
        else:
            print(f"⏭️  Directory exists: {directory.relative_to(project_dir.parent)}")

    print()

    # Create files
    files = {
        project_dir / "STEERING.md": STEERING_TEMPLATE,
        project_dir / "README.md": README_TEMPLATE.format(project_name=project_name),
        project_dir / "pyproject.toml": PYPROJECT_TEMPLATE.format(project_name=project_name),
        project_dir / ".gitignore": GITIGNORE_TEMPLATE,
        project_dir / "notebook" / "tasks.md": TASKS_TEMPLATE,
        project_dir / "notebook" / "labnote" / "Exp00_TEMPLATE_labnote.ipynb": LABNOTE_JUPYTER_TEMPLATE,
        project_dir / "notebook" / "labnote" / "Exp00_TEMPLATE_labnote.md": LABNOTE_MD_TEMPLATE,
        project_dir / "notebook" / "report" / "Exp00_TEMPLATE_report.md": REPORT_TEMPLATE,
        project_dir / "results" / ".gitkeep": "",
        project_dir / "reports" / ".gitkeep": "",
        project_dir / "data" / "processed" / ".gitkeep": "",
        project_dir / "data" / "experimental" / ".gitkeep": "",
        project_dir / "src" / "workflow" / "Snakefile": SNAKEFILE_TEMPLATE.format(project_name=project_name),
        project_dir / "src" / "workflow" / "config.yaml": SNAKEMAKE_CONFIG_TEMPLATE.format(project_name=project_name),
        project_dir / "src" / "workflow" / "rules" / ".gitkeep": "",
        project_dir / "src" / "workflow" / "scripts" / ".gitkeep": "",
        project_dir / "src" / ".gitkeep": "",  # For future {exp_no}/ directories
    }

    for file_path, content in files.items():
        if not file_path.exists():
            file_path.write_text(content)
            print(f"✅ Created file: {file_path.relative_to(project_dir.parent)}")
        else:
            print(f"⏭️  File exists: {file_path.relative_to(project_dir.parent)}")

    print()
    print("✅ Project initialization complete!")
    print()
    print("📋 Next steps:")
    print("1. Edit STEERING.md to define your research question")
    print("2. Create your first experiment with /research-exp")
    print("3. Review templates in notebook/labnote/ and notebook/report/")

    return True


def main():
    if len(sys.argv) < 3 or sys.argv[1] != '--path':
        print("Usage: init_project.py --path <path>")
        print()
        print("Examples:")
        print("  init_project.py --path .")
        print("  init_project.py --path /path/to/new/project")
        sys.exit(1)

    path = sys.argv[2]

    success = init_project(path)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
