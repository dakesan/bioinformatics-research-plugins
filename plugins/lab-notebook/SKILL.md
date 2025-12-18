---
name: lab-notebook
description: This skill should be used when creating a new experiment, starting lab notebook, recording experimental results, or documenting observations. Triggered by requests like "start experiment", "create lab notebook", "record results", or "新しい実験を始める".
---

# Lab Notebook Management

## Overview

Provides lab notebook creation and management for individual bioinformatics experiments. Supports both Jupyter notebooks (.ipynb) for Python-based experiments and Markdown (.md) for non-Python experiments.

## Core Capabilities

### 1. Create New Lab Notebook

Create a new experiment notebook using templates.

**When to use**: When starting a new experiment or analysis.

**Workflow**:
1. Determine experiment number (check existing `notebook/labnote/` files)
2. Ask user:
   - Experiment title/description
   - Format preference (Jupyter vs Markdown)
   - Initial hypothesis (if available)
3. Copy appropriate template:
   - Jupyter: `assets/templates/labnote-template.ipynb` → `notebook/labnote/Exp##_[title].ipynb`
   - Markdown: `assets/templates/labnote-template.md` → `notebook/labnote/Exp##_[title].md`
4. Customize template with user input
5. Update `notebook/tasks.md` with new experiment entry

**Naming convention**:
```
Exp##_[brief-description].ext

Examples:
Exp01_rnaseq-differential-expression.ipynb
Exp02_protein-quantification.md
Exp03_pathway-enrichment.ipynb
```

**Command**: `/research-exp`

### 2. Notebook Structure Guidance

Guide users on proper notebook structure using `references/notebook-guidelines.md`.

**Standard sections**:

1. **Header**:
   - Experiment title (Exp##_[description])
   - Date
   - Experimenter name

2. **Hypothesis**:
   - Testable statement
   - Expected outcome

3. **Background**:
   - Context and rationale
   - Related experiments
   - References

4. **Materials and Methods**:
   - Data sources and versions
   - Tools and versions
   - Step-by-step procedure
   - Parameters

5. **Results**:
   - Observations (factual)
   - Figures and tables
   - Quality control checks

6. **Discussion**:
   - Interpretation
   - Hypothesis evaluation
   - Limitations
   - Next steps

### 3. Quality Checks

Ensure notebooks maintain scientific quality standards.

**Key principles** (from `references/notebook-guidelines.md`):
- **Facts first**: Results section = observations only
- **Separate interpretation**: Discussion section = analysis and reasoning
- **Document everything**: Include failed attempts and unexpected results
- **Reproducibility**: Complete procedure for replication
- **Version control**: Track changes with meaningful commits

**Pre-finalization checklist**:
- [ ] Hypothesis clearly stated
- [ ] Methods reproducible
- [ ] All parameters documented
- [ ] Figures properly labeled
- [ ] Results are factual observations
- [ ] Discussion separates facts from interpretation
- [ ] Limitations acknowledged
- [ ] Next steps identified

### 4. Integration with Workflow

Connect lab notebooks with broader project workflow.

**Before creating notebook**:
- Check `STEERING.md` for current phase and priorities
- Review `notebook/tasks.md` for planned experiments
- Ensure hypothesis aligns with research question

**After completing experiment**:
- Update `notebook/tasks.md` with status
- Consider if results warrant report generation (`/research-report`)
- Identify if hypothesis needs refinement (`hypothesis-driven` skill)
- Update `STEERING.md` if experiment completes a milestone

## Resources

### assets/templates/

- `labnote-template.ipynb`: Jupyter notebook template for Python experiments
- `labnote-template.md`: Markdown template for non-Python experiments

### commands/

- `research-exp.md`: New experiment creation command (`/research-exp`)

### references/

- `notebook-guidelines.md`: Detailed guidelines for each notebook section

## Usage Notes

### Format Selection

**Use Jupyter (.ipynb) when**:
- Experiment involves Python code
- Need inline visualization
- Require iterative analysis
- Want to execute code cells

**Use Markdown (.md) when**:
- Experiment is non-Python (e.g., command-line tools, R, manual procedures)
- Documentation-heavy with minimal code
- Prefer plain text format
- Simple version control

### Best Practices

1. **One experiment = One notebook**
   - Don't combine multiple experiments in one file
   - Split large experiments into sub-experiments (Exp01a, Exp01b)

2. **Sequential numbering**
   - Exp01, Exp02, Exp03, ...
   - Don't reuse numbers
   - Gaps are OK (deleted experiments)

3. **Descriptive titles**
   - Good: `Exp03_tcga-survival-analysis`
   - Bad: `Exp03_analysis` or `Exp03_test`

4. **Regular commits**
   - Commit after each major step
   - Use meaningful messages
   - Don't commit huge result files (use .gitignore)

5. **Document as you go**
   - Don't wait until the end
   - Record observations immediately
   - Note unexpected findings

### Common Workflow

Typical experiment workflow:

1. **Planning**:
   ```
   /research-status  # Check current priorities
   ```

2. **Creation**:
   ```
   /research-exp  # Create new notebook
   ```

3. **Execution**:
   - Run experiment
   - Document observations
   - Save results

4. **Review**:
   - Check quality standards
   - Update tasks.md

5. **Follow-up**:
   - Refine hypothesis if needed
   - Plan next experiment
   - Generate report if ready
