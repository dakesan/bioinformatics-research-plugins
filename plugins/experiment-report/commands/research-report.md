---
description: Generate integrated report from lab notebooks
---

Use the `experiment-report` skill to generate a new report.

## Pre-Generation Checklist (MANDATORY)

Before generating, verify with user:

### Step 1: Notebook Completeness
- [ ] All included notebooks have completed Results sections
- [ ] All included notebooks have completed Discussion sections
- [ ] All figures saved to `results/exp##/` directory

### Step 2: Project Alignment
- [ ] Report scope aligns with STEERING.md objectives
- [ ] Primary hypothesis/research question identified
- [ ] Notebooks collectively address the research question

### Step 3: Evidence Verification
- [ ] List all figures needed for each finding
- [ ] Verify figure paths exist: `ls ../results/exp##/`
- [ ] Identify key statistics for each claim

### Questions to Ask User
1. "Which experiments are included?" (list Exp## numbers)
2. "Is the Discussion section complete in each notebook?"
3. "What is the main research question this report addresses?"
4. "What are the 2-3 key claims you want to make?"
5. "Are all figures saved to results/exp##/ directories?"

## Workflow

After checklist passes:

1. Run `scripts/init_report.py` to generate template with claim-evidence structure
2. Fill in evidence tables for each finding
3. Verify all paths exist (notebooks, figures)
4. Complete quality gate checklists in template

## PDF Export

After report completion:
```bash
pandoc Report_*.md -o report.pdf --pdf-engine=typst --template=assets/templates/report.typ
```

See SKILL.md for detailed workflow and quality standards.
