# inbox-processor Plugin

Classification and processing of user input files from inbox directory.

## Overview

The `inbox-processor` plugin organizes unstructured input files from `inbox/`, classifies content, extracts actionable information, and suggests appropriate integration into the research workflow.

## Features

- **Classification**: Categorize files (meeting notes, protocols, ideas, data, literature)
- **Information Extraction**: Extract decisions, action items, key findings
- **Destination Suggestions**: Recommend where content should be integrated
- **Workflow Integration**: Add to tasks.md, STEERING.md, or create new notebooks

## Usage

Triggered by requests like:
- "Process inbox"
- "Organize inbox files"
- "Classify this memo"
- "inbox を整理"

## Classification Categories

### 1. Meeting Notes

**Indicators**: Discussion, decisions, action items

**Destination**: `notebook/knowledge/meeting_YYYY-MM-DD.md`

**Extracted**:
- Decisions made
- Action items (who, what, when)
- Discussion points

### 2. Protocols

**Indicators**: Step-by-step procedures, materials lists

**Destination**: `notebook/knowledge/protocol_[name].md`

**Extracted**:
- Materials and reagents
- Procedure steps
- Safety notes

### 3. Experiment Ideas

**Indicators**: Hypothesis, experimental approach

**Destination**: Create new lab notebook via `/research-exp`

**Extracted**:
- Hypothesis
- Approach
- Expected outcome

### 4. Raw Data Files

**Indicators**: .csv, .tsv, .fastq, tabular data

**Destination**: `data/raw/[filename]`

**Actions**:
- Move to data/raw/
- Document provenance

### 5. Literature/Reading Notes

**Indicators**: Paper citations, summaries, findings

**Destination**: `notebook/knowledge/literature_[topic].md`

**Extracted**:
- Citations
- Key findings
- Relevance to work

### 6. Miscellaneous/Unclear

**Indicators**: Mixed content, unclear purpose

**Actions**:
- Ask user for clarification
- May need manual classification

## Classification Decision Tree

```
Is file in inbox/? → Yes
  ├─ Step-by-step procedures? → Protocol
  ├─ Hypothesis + plan? → Experiment Idea
  ├─ Meeting discussion? → Meeting Notes
  ├─ Paper citations? → Literature
  ├─ Tabular data? → Raw Data
  └─ Unclear? → Ask user
```

## Integration Actions

After classification:

**Meeting Notes**:
1. Move to knowledge/
2. Extract action items → tasks.md
3. Update STEERING.md (if major decisions)

**Protocols**:
1. Move to knowledge/
2. Document availability

**Experiment Ideas**:
1. Create new lab notebook (`/research-exp`)
2. Add to tasks.md
3. Refine hypothesis (hypothesis-driven skill)

**Raw Data**:
1. Move to data/raw/
2. Document in relevant notebook

**Literature**:
1. Move to knowledge/
2. Add citations to notebooks

## Files

### References

- `references/classification-rules.md` - Detailed classification criteria and extraction rules

## Workflow

### Single File Processing

```
User: "Process inbox/meeting_notes.txt"

1. Read file
2. Classify: Meeting Notes
3. Extract: Decisions, action items
4. Suggest: Move to knowledge/meeting_2025-01-15.md
5. Implement (with approval):
   - Move file
   - Add action items to tasks.md
   - Update STEERING.md
```

### Batch Processing

```
User: "Process all files in inbox/"

1. Read all files
2. Classify each
3. Present summary by category
4. Get user confirmation
5. Implement batch actions
```

## Best Practices

### Do

- Always ask user confirmation before moving files
- Extract key information systematically
- Integrate into existing workflow files
- Use consistent naming conventions
- Document data provenance

### Don't

- Delete files without permission
- Move files without confirmation
- Modify file contents (except formatting)
- Make assumptions on ambiguous content

## Safety

**Never automatically**:
- Move files (especially data files)
- Delete anything from inbox/
- Modify file contents

**Always confirm**:
- Before moving files
- Before creating new notebooks
- Before modifying tasks.md or STEERING.md
- For ambiguous classifications

## Examples

### Example 1: Meeting Notes

**Input** (`inbox/team_meeting.txt`):
```
Discussed ATAC-seq approach. John suggested it's better
than ChIP. Decided to use ATAC-seq. John will order kit
by Friday.
```

**Classification**: Meeting Notes

**Extraction**:
- Decision: Use ATAC-seq instead of ChIP-seq
- Action: [ ] John: Order ATAC-seq kit (by Friday)

**Destination**: `knowledge/meeting_2025-01-15.md`

**Integration**:
- Move file
- Add action item to tasks.md
- Update STEERING.md with decision

### Example 2: Experiment Idea

**Input** (`inbox/knockout_idea.txt`):
```
Idea: Test if Gene X knockout reduces migration

Hypothesis: Gene X knockout will reduce migration >50%

Approach:
- CRISPR knockout in MDA-MB-231
- Transwell assay
- Compare to wildtype
```

**Classification**: Experiment Idea

**Destination**: Create new lab notebook

**Integration**:
- Run `/research-exp` → Create Exp06_gene-x-knockout.ipynb
- Transfer content
- Refine hypothesis with hypothesis-driven skill
- Add to tasks.md as planned experiment

## Installation

```bash
/plugin install inbox-processor@bioinformatics-research
```

## Integration

**Works with**:
- `research-project` - Updates STEERING.md, tasks.md
- `lab-notebook` - Creates new notebooks from ideas
- `hypothesis-driven` - Refines extracted hypotheses

## License

MIT
