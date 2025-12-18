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
    "\\n",
    "# Configuration\\n",
    "DATA_DIR = Path(\\"../data/raw\\")\\n",
    "RESULTS_DIR = Path(\\"../results\\")"
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
    "# Analysis code here"
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

GITIGNORE_TEMPLATE = """# Data
data/raw/*
!data/raw/.gitkeep

# Results
results/*
!results/.gitkeep

# Python
__pycache__/
*.py[cod]
*$py.class
.ipynb_checkpoints/

# Environment
.env
.venv
env/
venv/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
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

    # Create directory structure
    directories = [
        project_dir,
        project_dir / "notebook" / "labnote",
        project_dir / "notebook" / "report",
        project_dir / "notebook" / "knowledge",
        project_dir / "inbox",
        project_dir / "data" / "raw",
        project_dir / "results",
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
        project_dir / "notebook" / "tasks.md": TASKS_TEMPLATE,
        project_dir / "notebook" / "labnote" / "Exp00_TEMPLATE_labnote.ipynb": LABNOTE_JUPYTER_TEMPLATE,
        project_dir / "notebook" / "labnote" / "Exp00_TEMPLATE_labnote.md": LABNOTE_MD_TEMPLATE,
        project_dir / "notebook" / "report" / "Exp00_TEMPLATE_report.md": REPORT_TEMPLATE,
        project_dir / ".gitignore": GITIGNORE_TEMPLATE,
        project_dir / "data" / "raw" / ".gitkeep": "",
        project_dir / "results" / ".gitkeep": "",
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
