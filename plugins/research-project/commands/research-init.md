---
description: Initialize bioinformatics research project structure
---

## Workflow

1. Confirm the target project path with the user (default: current working directory)
2. **Execute the script directly** using Bash - do NOT search for it:
   ```bash
   python /Users/oodakemac/ghq/github.com/dakesan/bioinformatics-research-plugins/plugins/research-project/scripts/init_project.py --path <target_project_path>
   ```
3. Verify the created structure (STEERING.md, notebook/, inbox/, data/, results/)
4. Guide user to next steps: edit STEERING.md and create first experiment

## Example

For current directory:
```bash
python /Users/oodakemac/ghq/github.com/dakesan/bioinformatics-research-plugins/plugins/research-project/scripts/init_project.py --path .
```

**Critical**: The script is located at a fixed path in the plugin directory. Do NOT use Glob, Search, or any file search tools to find it. Execute directly with Bash.
