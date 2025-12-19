# research-project Plugin

Project steering management for bioinformatics research.

## Overview

The `research-project` plugin provides comprehensive project management capabilities for bioinformatics research projects. It handles initialization, phase tracking, status monitoring, and best practices guidance.

## Features

- **Project Initialization**: Create standardized directory structure with templates
- **Phase Management**: Track research phases from planning through publication
- **Status Monitoring**: Check project progress and next actions
- **Best Practices**: Access research guidelines and quality standards

## Commands

### /research-init

Initialize a new research project structure.

Creates:
- `STEERING.md` - Project progress tracker
- `notebook/tasks.md` - Task management
- `notebook/labnote/` - Lab notebook templates
- `notebook/report/` - Report template
- `notebook/knowledge/` - Reusable procedures
- `inbox/` - User input files
- `data/raw/` - Raw data directory
- `results/` - Output directory

Usage:
```
/research-init
```

### /research-status

Check current project status and recommended next actions.

Reads:
- `STEERING.md` - Current phase and priorities
- `notebook/tasks.md` - Experiment progress

Displays:
- Current phase
- Active experiments
- Completed milestones
- Next recommended actions

Usage:
```
/research-status
```

## Files

### Scripts

- `scripts/init_project.py` - Project initialization script (executable)

  **Usage**:
  ```bash
  python /Users/oodakemac/ghq/github.com/dakesan/bioinformatics-research-plugins/plugins/research-project/scripts/init_project.py --path /path/to/target/project
  ```

  **Important**: Execute with absolute path. The `--path` argument specifies the target project directory.

### References

- `references/phases.md` - Research phase definitions and transition criteria
- `references/best-practices.md` - Hypothesis-driven research guidelines
- `references/quality-standards.md` - Scientific quality standards

## Installation

```bash
/plugin install research-project@bioinformatics-research
```

## Usage Example

1. **Initialize project**:
   ```
   /research-init
   ```

2. **Check status**:
   ```
   /research-status
   ```

3. **Update STEERING.md** with research question and priorities

4. **Create first experiment** with `/research-exp` (requires `lab-notebook` plugin)

## Integration

Works with:
- `lab-notebook` - Create and manage lab notebooks
- `experiment-report` - Generate integrated reports
- `hypothesis-driven` - Refine hypotheses

## License

MIT
