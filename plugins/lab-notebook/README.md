# lab-notebook Plugin

Lab notebook creation and management for individual bioinformatics experiments.

## Overview

The `lab-notebook` plugin provides structured templates and guidelines for creating and managing experiment notebooks. Supports both Jupyter notebooks (.ipynb) for Python-based experiments and Markdown (.md) for non-Python experiments.

## Features

- **Template-based creation**: Pre-structured notebook templates with standard sections
- **Dual format support**: Jupyter for Python experiments, Markdown for others
- **Quality guidelines**: Comprehensive documentation standards
- **Integration**: Works seamlessly with research-project and experiment-report plugins

## Commands

### /research-exp

Create a new experiment notebook with standardized structure.

**Workflow**:
1. Determines next experiment number
2. Asks for experiment title and format preference
3. Copies appropriate template with customization
4. Updates `notebook/tasks.md` with new experiment entry

**Output**:
- Jupyter: `notebook/labnote/Exp##_[title].ipynb`
- Markdown: `notebook/labnote/Exp##_[title].md`

Usage:
```
/research-exp
```

## Notebook Structure

Standard sections in all notebooks:

1. **Header**: Title, date, experimenter
2. **Hypothesis**: Testable prediction
3. **Background**: Context and rationale
4. **Materials and Methods**: Data, tools, procedure
5. **Results**: Observations and outputs (factual only)
6. **Discussion**: Interpretation, hypothesis evaluation, limitations, next steps

## Files

### Templates

- `assets/templates/labnote-template.ipynb` - Jupyter notebook template
- `assets/templates/labnote-template.md` - Markdown template

### Commands

- `commands/research-exp.md` - New experiment creation command

### References

- `references/notebook-guidelines.md` - Comprehensive section-by-section guidelines

## Format Selection

**Use Jupyter (.ipynb) when**:
- Experiment involves Python code
- Need inline visualization
- Require iterative analysis

**Use Markdown (.md) when**:
- Experiment uses non-Python tools (R, command-line)
- Documentation-heavy with minimal code
- Prefer plain text format

## Quality Standards

Follows scientific rigor principles:
- **Facts first**: Results section contains observations only
- **Separate interpretation**: Discussion section contains analysis
- **Complete documentation**: Methods are fully reproducible
- **Version control**: Regular commits with meaningful messages

See `references/notebook-guidelines.md` for detailed standards.

## Best Practices

### Naming Convention

```
Exp##_[brief-description].ext

Examples:
Exp01_rnaseq-differential-expression.ipynb
Exp02_protein-quantification.md
```

### Workflow

1. Create notebook: `/research-exp`
2. Fill in hypothesis and background
3. Execute experiment and document results
4. Write discussion and next steps
5. Update `notebook/tasks.md`
6. Commit regularly

### Quality Checklist

Before finalizing:
- [ ] Hypothesis clearly stated
- [ ] Methods reproducible
- [ ] Results are factual (no interpretation)
- [ ] Discussion separates facts from interpretation
- [ ] Limitations acknowledged
- [ ] Next steps identified

## Installation

```bash
/plugin install lab-notebook@bioinformatics-research
```

## Integration

Works with:
- `research-project` - Project initialization and status tracking
- `hypothesis-driven` - Hypothesis refinement
- `experiment-report` - Report generation from notebooks

## License

MIT
