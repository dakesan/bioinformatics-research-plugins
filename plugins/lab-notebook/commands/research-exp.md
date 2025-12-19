---
description: Create a new experiment with lab notebook (Jupyter or Markdown)
---

Use the `lab-notebook` skill to create a new experiment notebook. This command initiates an **interactive dialogue** to ensure high-quality, narrative documentation of the experiment.

## Workflow

### Step 1: Basic Information
1. Determine next experiment number (check existing `notebook/labnote/` files)
2. Ask user for:
   - Experiment title/description
   - Format preference (Jupyter vs Markdown)

### Step 2: Core Questions Dialog (MANDATORY)

**CRITICAL**: Do NOT simply copy the template with placeholders. Ask ALL of the following questions to build high-quality narrative content.

#### 2.1 Purpose & Motivation
Ask the user:
- "What problem or question does this experiment address?"
- "Why is this important to the broader research goal?"
- "What motivated you to run this experiment now?"

#### 2.2 Prior Work & Context
- Check `STEERING.md` and previous notebooks for related experiments
- Ask the user:
  - "What prior experiments led to this? (e.g., Exp01 showed X, so now we test Y)"
  - "What literature findings inform this experiment?"
  - "How does this fit into the overall research narrative?"

#### 2.3 Hypothesis & Expected Outcome
Ask the user:
- "What is your testable prediction?"
- "What specific outcome do you expect?"
- Refine together:
  - Is it specific enough? (variables, relationships, expected magnitude)
  - Is it testable with available data/methods?

#### 2.4 Success Criteria & Effect Size
Ask the user:
- "What quantitative change would confirm success?" (e.g., fold-change > 2, p < 0.05, AUC > 0.8)
- "What is the minimum effect size you consider biologically meaningful?"
- "How will you know if the experiment 'worked'?"

#### 2.5 Primary Endpoints
Ask the user:
- "What are the main measurements or variables?"
- "Which endpoint is most critical to the hypothesis?"

#### 2.6 Controls & Replication
Ask the user:
- "What are the control conditions (positive/negative controls)?"
- "How many replicates will you run?"
- "What normalization or baseline comparisons will you use?"

#### 2.7 Anticipated Risks & Rescue Plans
Ask the user:
- "What could go wrong with this approach?"
- "What alternative methods exist if the primary approach fails?"
- "What confounding factors might affect interpretation?"

### Step 3: Synthesize Narrative Content

Use dialog answers to write **coherent prose paragraphs** (not bullet lists) for:

1. **Purpose & Motivation section**: 1 paragraph summarizing why this experiment matters
2. **Background & Prior Work section**: Narrative connecting to prior experiments and literature
3. **Hypothesis section**: Testable prediction with success criteria and expected effect size
4. **Materials and Methods section**: Data sources, environment, procedure with parameters

### Step 4: Template Customization
1. Copy appropriate template:
   - Jupyter: `assets/templates/labnote-template.ipynb` → `notebook/labnote/Exp##_[title].ipynb`
   - Markdown: `assets/templates/labnote-template.md` → `notebook/labnote/Exp##_[title].md`
2. **Replace placeholders** with the narrative content created through dialogue
3. Ensure all sections contain **narrative text**, not just TODO comments

### Step 5: Post-Creation
1. Update `notebook/tasks.md` with new experiment entry
2. Inform user about:
   - Next steps (filling in results after execution)
   - Quality standards to maintain
   - When to return for discussion section completion

## After Experiment Execution

### Post-Execution Checklist (MANDATORY)

When the user returns after running the experiment, ask ALL of these questions:

**Observation Questions**:
1. "What are the 3 most important observations from this experiment?"
2. "Were there any unexpected or surprising results?"
3. "Did anything differ from your initial expectations?"

**Data & Artifact Questions**:
4. "What figures/tables were generated? Please list with file paths."
5. "Where are the output files saved? (expected: `results/exp##_*.{png,csv,etc}`)"
6. "What intermediate files should be preserved?"

**Quality Control Questions**:
7. "What QC checks were performed? (e.g., normalization, outlier detection)"
8. "Were there any anomalies, warnings, or errors during execution?"
9. "Did all samples/replicates pass QC?"

**Deviation Questions**:
10. "Did you deviate from the planned procedure? If so, document the changes."
11. "Were any parameters changed from the original plan?"
12. "Any failed attempts or troubleshooting steps to document?"

**Forward-Looking Questions**:
13. "Based on these results, what is the most logical next step?"
14. "Does this confirm, refute, or modify the original hypothesis?"

### Completing Results Section

After the checklist, engage in dialogue to:
1. Document observations as factual statements (no interpretation)
2. Record quantitative results with statistics (CI, p-values)
3. Document QC outcomes and any anomalies
4. Catalog all figures/tables with paths

### Completing Discussion Section

**CRITICAL**: Create through **interactive dialogue**, not generic text.

1. **Interpretation**: Discuss what the results mean biologically
2. **Hypothesis Evaluation**: Evaluate against success criteria defined earlier
3. **Alternative Interpretations**: Consider other explanations
4. **Limitations**: Discuss constraints and caveats
5. **Next Steps**: Identify specific follow-up experiments

## Key Principles

1. **Complete Question Set**: Ask ALL core questions in Step 2 - do not skip any
2. **Narrative Content**: Write actual prose, not placeholders or bullet lists
3. **Success Criteria First**: Define quantitative success criteria BEFORE running experiment
4. **Post-Execution Dialog**: Use the 14-question checklist to capture complete results
5. **Traceability**: Ensure every claim links to data/figure with path
