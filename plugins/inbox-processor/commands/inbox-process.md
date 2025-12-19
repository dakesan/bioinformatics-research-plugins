---
description: Process and classify files in the inbox/ directory
---

## Workflow

1. List files in the `inbox/` directory of the current project
2. For each file, classify into categories:
   - Meeting Notes → `notebook/knowledge/meeting_YYYY-MM-DD.md`
   - Protocols → `notebook/knowledge/protocol_[name].md`
   - Ideas → Create experiment with `/research-exp`
   - Data → `data/raw/`
   - Literature → `notebook/knowledge/literature_[topic].md`
3. Extract actionable information (decisions, action items, key points)
4. Suggest destination and actions
5. With user approval, move/process files and update tasks.md or STEERING.md

## Example

```bash
ls inbox/
```

Then read and classify each file, present summary to user, and ask for approval before moving.

**Note**: Processed files should be moved to `inbox/archive/` after integration.
