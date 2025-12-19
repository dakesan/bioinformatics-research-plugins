# bioinformatics-research-plugins Project Context

## Version Management

### research-project plugin - v0.2.0

**Release Date**: Dec 19, 2025

**Changes**:
- Fixed `init_project.py` execution path issue by clarifying absolute path requirements in documentation
- Updated SKILL.md with concrete execution path example
- Updated commands/research-init.md with explicit path specification
- Updated README.md with usage section and path requirements

**Breaking Changes**: None - Documentation fix only

**Notes**:
- When specifying script execution paths in documentation, use absolute paths instead of relative paths
- The `--path` argument specifies the target project directory where structure will be created
- Example: `python /Users/oodakemac/ghq/github.com/dakesan/bioinformatics-research-plugins/plugins/research-project/scripts/init_project.py --path /path/to/target/project`

### experiment-report plugin - v0.2.0

Previous release with similar path execution fixes.

## Coding Rules

### Version Management

**Rule**: After editing files, you MUST bump the plugin version in `plugin.json`.

- Increment version according to semantic versioning:
  - Patch (0.0.x): Bug fixes and documentation clarifications
  - Minor (0.x.0): New features or significant improvements
  - Major (x.0.0): Breaking changes

- Update keywords in `plugin.json` to reflect changes made
- Always commit version changes together with the changes that prompted them
- Include version bump in the commit message

## Important Guidelines

- Always specify absolute paths when referencing plugin scripts in documentation
- Keep this file updated with version changes and important fixes
- Version bumps are required when documentation clarifications affect user-facing behavior
