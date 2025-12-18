# Inbox Classification Rules

## Overview

This document defines rules for classifying and routing unstructured input files from the `inbox/` directory into appropriate locations within the research workflow.

---

## Classification Categories

### 1. Meeting Notes

**Indicators**:
- Contains discussion, decisions, action items
- Dated content (mentions specific meeting date)
- Multiple speakers or discussion format
- Agenda or topics listed

**Content patterns**:
- "Discussed...", "Decided...", "Action items"
- Names with attributions (John: "...")
- Dates and times
- TODO lists

**Destination**: `notebook/knowledge/meeting_YYYY-MM-DD.md`

**Example**:
```markdown
# Team Meeting 2025-01-15

## Attendees
- John, Jane, Bob

## Decisions
- Approved Exp04 (ATAC-seq analysis)
- Will use bulk RNA-seq instead of three-prime

## Action Items
- [ ] John: Design qPCR primers by Friday
- [ ] Jane: Share ChIP-seq data next week
```

**Actions**:
1. Move to `notebook/knowledge/` with standardized name
2. Extract action items → Add to `notebook/tasks.md`
3. Extract decisions → Update `STEERING.md` if relevant

---

### 2. Protocols

**Indicators**:
- Step-by-step procedures
- Materials/reagents lists
- Specific concentrations, volumes, times
- "Protocol", "SOP", "Procedure" in title

**Content patterns**:
- Numbered steps (1. 2. 3.)
- "Materials:", "Reagents:", "Equipment:"
- Measurements (10 μL, 37°C, 2 hours)
- Safety notes or warnings

**Destination**: `notebook/knowledge/protocol_[name].md`

**Example**:
```markdown
# RNA Extraction Protocol

## Materials
- TRIzol reagent
- Chloroform
- Isopropanol

## Procedure
1. Add 1 mL TRIzol to sample
2. Incubate 5 min at RT
3. Add 200 μL chloroform
...
```

**Actions**:
1. Move to `notebook/knowledge/` with descriptive name
2. Note availability in project documentation
3. Reference in future experiments

---

### 3. Experiment Ideas

**Indicators**:
- Hypothesis or research question
- Proposed experimental approach
- Exploratory or brainstorming tone
- "What if...", "Could we...", "Idea:"

**Content patterns**:
- Hypothesis statements
- Experimental design sketch
- Expected outcomes
- Questions to answer

**Destination**: Create new lab notebook via `/research-exp`

**Example**:
```markdown
# Idea: Test Gene X knockout effect on migration

## Hypothesis
Knockout of Gene X will reduce cell migration by >50%

## Approach
- CRISPR knockout in MDA-MB-231 cells
- Transwell migration assay
- Compare to wild-type and scramble control

## Expected outcome
Reduced migration if Gene X promotes motility
```

**Actions**:
1. Use `/research-exp` to create Exp##_gene-x-knockout.ipynb
2. Transfer content to new notebook
3. Refine hypothesis with `hypothesis-driven` skill
4. Add to `notebook/tasks.md` as planned experiment

---

### 4. Raw Data Files

**Indicators**:
- File extensions: .csv, .tsv, .fastq, .bam, .txt (data)
- Numeric content
- Tabular structure
- Large file size

**Content patterns**:
- Headers with column names
- Rows of measurements
- Sequence data
- Binary data files

**Destination**: `data/raw/[filename]`

**Example files**:
- `counts.csv` → `data/raw/counts.csv`
- `sample1.fastq.gz` → `data/raw/sample1.fastq.gz`

**Actions**:
1. Move to `data/raw/` preserving filename
2. Note in relevant lab notebook or STEERING.md
3. Ensure .gitignore excludes from version control
4. Document data provenance

---

### 5. Literature/Reading Notes

**Indicators**:
- Paper citations
- Summary of findings
- Notes on methods
- Relevance to current work

**Content patterns**:
- Author names and years
- Journal names
- "Key findings:", "Methods:", "Relevance:"
- DOI or PubMed ID

**Destination**: `notebook/knowledge/literature_[topic].md`

**Example**:
```markdown
# Literature Notes: Cell Cycle in Cancer

## Smith et al. 2024 (Nature)

**Key findings**:
- CDK4/6 inhibitors effective in ER+ breast cancer
- Resistance mechanisms identified

**Methods**:
- RNA-seq of resistant cell lines
- Proteomics validation

**Relevance**:
- Supports our cell cycle pathway findings
- Potential comparison dataset
```

**Actions**:
1. Move to `notebook/knowledge/` grouped by topic
2. Add citations to relevant reports/notebooks
3. Note in STEERING.md if highly relevant

---

### 6. Administrative/Grant Content

**Indicators**:
- Budget information
- Timeline/milestones
- Reporting requirements
- Institutional correspondence

**Content patterns**:
- Dollar amounts
- Grant numbers
- Deadline dates
- Formal language

**Destination**: Keep in `inbox/` or move to `inbox/archive/`

**Example**:
```markdown
# Grant Progress Report - Due Feb 1

Budget utilization: $45,000 / $100,000
...
```

**Actions**:
1. Usually keep in `inbox/` for administrative reference
2. Optionally create `inbox/admin/` subdirectory
3. Not integrated into research workflow
4. May extract milestones to STEERING.md

---

### 7. Miscellaneous/Unclear

**Indicators**:
- Mixed content types
- Unclear purpose
- Fragmentary notes
- Personal reminders

**Content patterns**:
- Short, incomplete thoughts
- Multiple unrelated topics
- To-do lists without context
- Brainstorming without structure

**Destination**: Review with user, may need manual classification

**Actions**:
1. Present content to user
2. Ask for clarification on intent
3. May split into multiple categories
4. May need manual filing

---

## Classification Decision Tree

```
Is file in inbox/?
├─ Yes → Read content
│  │
│  ├─ Contains step-by-step procedures?
│  │  └─ Yes → Protocol (knowledge/protocol_*.md)
│  │
│  ├─ Contains hypothesis + experimental plan?
│  │  └─ Yes → Experiment Idea (create new lab notebook)
│  │
│  ├─ Contains meeting discussion, decisions, action items?
│  │  └─ Yes → Meeting Notes (knowledge/meeting_*.md)
│  │
│  ├─ Contains paper citations and summaries?
│  │  └─ Yes → Literature (knowledge/literature_*.md)
│  │
│  ├─ Is tabular/sequence data file?
│  │  └─ Yes → Raw Data (data/raw/)
│  │
│  ├─ Contains budget, grants, admin info?
│  │  └─ Yes → Administrative (keep in inbox/ or inbox/admin/)
│  │
│  └─ Unclear or mixed?
│     └─ Miscellaneous (ask user for classification)
│
└─ No → Not an inbox processing task
```

---

## Extraction Rules

### Meeting Notes Extraction

**What to extract**:
1. **Decisions**: Concrete choices made
   - Format: "Decided: [decision]"

2. **Action Items**: Tasks with assignee
   - Format: "[ ] [Person]: [Task] (by [deadline])"

3. **Discussion Points**: Key topics
   - Format: "Discussed: [topic]"

**Example**:

From raw notes:
```
John suggested we try ATAC-seq. Jane agreed it's better than ChIP. We decided
to go with ATAC-seq. John will order kit by Friday. Bob asked about controls.
```

Extracted:
```markdown
**Decision**: Use ATAC-seq instead of ChIP-seq

**Action Items**:
- [ ] John: Order ATAC-seq kit (by Friday 2025-01-18)

**Discussion**:
- Compared ATAC-seq vs ChIP-seq approaches
- Discussed control design (Bob's question - follow-up needed)
```

### Protocol Extraction

**What to extract**:
1. **Title**: Protocol name
2. **Materials**: Required items with specs
3. **Steps**: Numbered procedure
4. **Notes**: Warnings, tips, troubleshooting
5. **Citations**: Source of protocol

**Standardize format**:
```markdown
# [Protocol Name]

**Source**: [Citation or lab]
**Last updated**: YYYY-MM-DD

## Materials
- Item 1 (specifications)
- Item 2 (specifications)

## Procedure
1. Step 1 (with details: volumes, times, temperatures)
2. Step 2
...

## Notes
- Important tip or warning
- Troubleshooting advice
```

### Idea Extraction

**What to extract**:
1. **Hypothesis**: Testable statement
2. **Background**: Why this idea emerged
3. **Approach**: Experimental plan
4. **Expected outcome**: Predictions

**Transform to lab notebook format**:
```markdown
# Exp##_[descriptive-name]

## Hypothesis
[Extracted and refined hypothesis]

## Background
[Context from idea + additional research]

## Materials and Methods
[Planned approach from idea]

...
```

### Literature Extraction

**What to extract**:
1. **Citation**: Full reference
2. **Key findings**: Main results (3-5 bullets)
3. **Methods**: Relevant techniques
4. **Relevance**: How it relates to current work

**Format**:
```markdown
# Literature: [Topic]

## [Author et al., Year] - [Journal]

**DOI**: [doi]

**Key Findings**:
- Finding 1
- Finding 2

**Methods**:
- Method 1
- Method 2

**Relevance**:
[How this relates to our work]

**Notes**:
[Additional thoughts, questions]
```

---

## Integration Actions

After classification and extraction, take appropriate actions:

### For Meeting Notes

1. **Move file**:
   ```bash
   mv inbox/meeting.md notebook/knowledge/meeting_2025-01-15.md
   ```

2. **Extract action items to tasks.md**:
   ```markdown
   ## From Meeting 2025-01-15
   - [ ] John: Order ATAC-seq kit (by 2025-01-18)
   - [ ] Jane: Share ChIP-seq data (by 2025-01-22)
   ```

3. **Update STEERING.md** (if major decisions):
   ```markdown
   **Recent Decisions** (2025-01-15):
   - Approved Exp04 (ATAC-seq chromatin accessibility)
   - Prioritize cell cycle validation experiments
   ```

### For Protocols

1. **Move file**:
   ```bash
   mv inbox/rna_extraction.txt notebook/knowledge/protocol_rna-extraction.md
   ```

2. **Document availability**:
   - Mention in STEERING.md or knowledge/ README if significant
   - Reference when planning experiments

### For Experiment Ideas

1. **Create new lab notebook**:
   ```
   /research-exp
   → Title: Gene X knockout migration assay
   → Format: Jupyter
   ```

2. **Transfer content**:
   - Copy hypothesis, background, approach from idea
   - Expand with full lab notebook structure

3. **Update tasks.md**:
   ```markdown
   ## Planned Experiments
   - [ ] Exp06: Test Gene X knockout effect on migration
   ```

### For Raw Data

1. **Move file**:
   ```bash
   mv inbox/counts.csv data/raw/counts_2025-01-15.csv
   ```

2. **Document in notebook**:
   ```markdown
   ## Data
   - Source: Collaborator Jane Doe
   - File: data/raw/counts_2025-01-15.csv
   - Date received: 2025-01-15
   - Description: RNA-seq counts for 30 samples
   ```

### For Literature

1. **Move file**:
   ```bash
   mv inbox/smith_2024_notes.md notebook/knowledge/literature_cell-cycle.md
   ```

2. **Add citation to relevant notebooks**:
   ```markdown
   ## References
   1. Smith et al. 2024. Cell cycle dysregulation in cancer. Nature. DOI: xxx
   ```

---

## Quality Checks

Before finalizing classification, verify:

- [ ] Content accurately classified
- [ ] Destination appropriate
- [ ] Key information extracted
- [ ] File renamed with clear, consistent naming
- [ ] Integrated into relevant workflow files (tasks.md, STEERING.md)
- [ ] No information lost
- [ ] User consulted on ambiguous cases

---

## Common Patterns

### Pattern: Mixed Meeting Notes + Ideas

**Input**: Meeting notes that include new experiment ideas

**Action**:
1. Save meeting notes → `knowledge/meeting_*.md`
2. Extract experiment idea → Create new lab notebook
3. Link between files

**Example**:
```markdown
# meeting_2025-01-15.md
...
**New experiment proposed**: Test Gene X knockout (→ see Exp06)

# Exp06_gene-x-knockout.ipynb
Hypothesis: [from meeting discussion]
Background: Emerged from team meeting 2025-01-15 (see knowledge/meeting_2025-01-15.md)
...
```

### Pattern: Protocol + Data

**Input**: Protocol with example data file

**Action**:
1. Save protocol → `knowledge/protocol_*.md`
2. Move data → `data/raw/protocol-example-data.csv`
3. Reference data in protocol

### Pattern: Literature Notes Relevant to Active Experiment

**Input**: Paper notes that inform ongoing experiment

**Action**:
1. Save literature notes → `knowledge/literature_*.md`
2. Add citation to relevant lab notebook
3. Update experiment background or discussion

---

## Edge Cases

### Case: Incomplete or Fragmentary Content

**Example**: "Try ATAC-seq next?"

**Action**:
1. Ask user for context
2. If experiment idea: Prompt for hypothesis, approach
3. If meeting note: Ask for meeting context
4. If just thought: Keep in inbox/ for later development

### Case: Multiple File Types in Batch

**Example**: Process inbox/ with 10 mixed files

**Action**:
1. Classify each independently
2. Group by category in summary
3. Ask user for confirmation before bulk actions
4. Present organized list of proposed moves

### Case: Conflicting Classifications

**Example**: Notes that could be meeting or literature

**Action**:
1. Present both possibilities to user
2. Let user decide primary classification
3. Can create cross-references if needed

---

## Automation Guidelines

While processing can be partially automated:

**Do NOT automatically**:
- Move files without user confirmation (especially data files)
- Delete anything from inbox/
- Modify file contents (except formatting)

**Safe to automate** (with user approval):
- Classification and suggestion
- Information extraction
- Destination recommendation
- Batch processing with confirmation

**Always confirm**:
- Before moving files
- Before creating new notebooks
- Before modifying workflow files (tasks.md, STEERING.md)
- For ambiguous classifications

---

## References

Classification supports:
- Organized knowledge management
- Reduced inbox clutter
- Efficient information retrieval
- Integration into research workflow
