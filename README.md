# Bioinformatics Research Plugins

AI-first hypothesis-driven workflow plugins for reproducible bioinformatics research.

## Overview

This is a Claude Code plugin marketplace that provides a complete workflow for bioinformatics research projects. The plugins work together to enable:

- **Hypothesis-driven research**: AI-guided hypothesis refinement and validation
- **Reproducible experiments**: Structured lab notebooks with Jupyter/Markdown templates
- **Integrated reporting**: Automatic report generation from experimental results
- **Project steering**: Phase management and best practices guidance

## Plugins

### 1. research-project

Project initialization and steering management.

**Commands**: `/research-init`, `/research-status`

**Use cases**:
- Initialize new research project structure
- Check current project phase and next actions
- Get guidance on research best practices

### 2. lab-notebook

Lab notebook creation and management for individual experiments.

**Commands**: `/research-exp`

**Use cases**:
- Create new Jupyter/Markdown lab notebook from template
- Document experimental procedures and observations
- Record raw results and data

### 3. hypothesis-driven

Hypothesis refinement and validation after experiment execution.

**Use cases**:
- Refine initial hypotheses based on experimental results
- Validate hypothesis quality (testability, specificity)
- Separate facts from interpretation

### 4. experiment-report

Integrated report generation and improvement from lab notebook results.

**Commands**: `/research-report`, `/research-refine`

**Use cases**:
- Generate integrated reports from multiple lab notebooks
- Improve existing reports for scientific accuracy and clarity
- Map experimental results to report structure

### 5. inbox-processor

Classification and processing of user input files.

**Use cases**:
- Process meeting notes and memos from `inbox/`
- Extract actionable items and decisions
- Route information to appropriate destinations

## Installation

### Add marketplace

```bash
/plugin marketplace add dakesan/bioinformatics-research-plugins
```

### Install all plugins

```bash
/plugin install research-project@bioinformatics-research
/plugin install lab-notebook@bioinformatics-research
/plugin install hypothesis-driven@bioinformatics-research
/plugin install experiment-report@bioinformatics-research
/plugin install inbox-processor@bioinformatics-research
```

## Quick Start

1. **Initialize project**:
   ```
   /research-init
   ```

2. **Create lab notebooks** (for each experiment):
   ```
   /research-exp  # Create Exp01
   # Run experiment, save figures to results/
   /research-exp  # Create Exp02
   # Run experiment, save figures to results/
   /research-exp  # Create Exp03
   # Run experiment, save figures to results/
   ```

3. **Generate integrated report** (after all experiments complete):
   ```
   /research-report  # Synthesize Exp01-03 into one report
   ```

4. **Refine report**:
   ```
   /research-refine
   ```

**Key principle**: Reports integrate findings across **multiple completed experiments**, referencing all saved figures from `results/` directory.

## Project Structure

After initialization, your project will have this structure:

```
your-project/
├── STEERING.md       # Current status & navigation (dynamic)
├── notebook/
│   ├── tasks.md      # Experiment progress tracking
│   ├── knowledge/    # Reusable procedures
│   ├── labnote/      # Exp##_*.md or *.ipynb
│   └── report/       # Exp##_*.md (integrated reports)
├── results/          # Output files (gitignored)
├── data/raw/         # Raw data (gitignored)
└── inbox/            # User input files (memos, meeting notes)
```

## Development

This marketplace is designed to work with [BItemplate](https://github.com/dakesan/BItemplate), a bioinformatics analysis template repository.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Issues and pull requests are welcome at https://github.com/dakesan/bioinformatics-research-plugins
