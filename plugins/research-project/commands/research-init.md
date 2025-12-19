---
description: Initialize bioinformatics research project structure
---

Use the `research-project` skill to initialize a new research project structure. Execute the initialization script with an absolute path:

```bash
python /Users/oodakemac/ghq/github.com/dakesan/bioinformatics-research-plugins/plugins/research-project/scripts/init_project.py --path /path/to/target/project
```

This creates the standardized directory layout with STEERING.md, tasks.md, and templates for lab notebooks and reports.

**Important**: The script must be invoked using its absolute path. The `--path` argument specifies where the project structure will be created (e.g., current directory with `--path .` or a specific location).
