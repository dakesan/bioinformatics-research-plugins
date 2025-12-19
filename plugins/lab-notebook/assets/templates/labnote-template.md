# Exp00_TEMPLATE_labnote

**Date**: YYYY-MM-DD
**Experimenter**:[Your Name]

---

## Purpose & Motivation

<!--
REQUIRED: Write a 1-paragraph narrative explaining:
- What problem or question this experiment addresses
- Why this is important to the broader research goal
- What motivated running this experiment now

Example:
"This experiment investigates whether gene X expression correlates with drug resistance
in cancer cell lines. Understanding this relationship is critical because X is a
potential therapeutic target. Previous analysis (Exp02) showed differential expression
of X, motivating this follow-up to determine functional significance."
-->

[AI-GENERATED NARRATIVE: Summarize the dialog about purpose and motivation here]

## Background & Prior Work

<!--
REQUIRED: Write a narrative connecting this experiment to prior work:
- Previous experiments in this project (reference by Exp##)
- Relevant literature findings
- How this fits into the overall research narrative

Example:
"In Exp01, we performed differential expression analysis and identified 500 DEGs.
Exp02 revealed that pathway Y was significantly enriched. Smith et al. (2023) showed
that pathway Y is associated with drug resistance in similar cell types. This experiment
tests whether our specific gene set shows the same pattern."
-->

[AI-GENERATED NARRATIVE: Synthesize the dialog about background and prior work here]

## Hypothesis

<!--
REQUIRED: State a testable hypothesis with:
- Specific prediction (what you expect to observe)
- Expected effect size or direction
- Success criteria

Example:
"We hypothesize that high expression of gene X (top quartile) is associated with
reduced sensitivity to drug Y, with an expected IC50 increase of at least 2-fold
compared to low-expression cells (bottom quartile). Success criterion: p < 0.05
and effect size > 2-fold."
-->

[AI-GENERATED NARRATIVE: Refined hypothesis based on dialog]

**Success Criteria**:
- [ ] Primary:[Quantitative threshold, e.g., "fold-change > 2, p < 0.05"]
- [ ] Secondary:[Additional criteria if applicable]

**Expected Effect Size**:[e.g., "2-fold increase", "AUC > 0.8", "correlation r > 0.5"]

---

## Materials and Methods

### Data Sources

| Data | Source | Version/Date | Location |
|------|--------|--------------|----------|
| [Dataset name] | [Source URL/repository] | [Version or download date] | `data/raw/[filename]` |

### Computational Environment

- **Environment**: See `pyproject.toml` (run `uv sync` to reproduce)
- **Random seed**:[e.g., 42]
- **Hardware**:[If relevant, e.g., GPU model for deep learning]

### Procedure

<!--
REQUIRED: Write step-by-step procedure with:
- Exact commands or code references
- All parameters explicitly stated
- Decision points and rationale

Include: deviations from planned procedure, troubleshooting steps
-->

1. **Data preparation**
   - Command: `[exact command or notebook cell reference]`
   - Parameters:[list all parameters]
   - Expected output:[what should result from this step]

2. **Analysis step**
   - Command: `[exact command]`
   - Parameters:[list all parameters]
   - Notes:[any deviations or adjustments]

3. [Continue with all steps...]

### Deviations from Plan

<!--
Document any changes from the original experimental plan
-->

| Planned | Actual | Reason |
|---------|--------|--------|
| [Original plan] | [What was actually done] | [Why the change was made] |

---

## Results

<!--
CRITICAL: This section contains ONLY factual observations (Level 1).
NO interpretation here - save that for Discussion.
-->

### Primary Observations

<!--
List the 3 most important factual observations from this experiment.
State WHAT you observed, not what it means.
-->

1. **Observation 1**:[Factual statement, e.g., "Gene X showed 3.2-fold higher expression in resistant vs. sensitive cells (p=0.003)"]
2. **Observation 2**:[Factual statement]
3. **Observation 3**:[Factual statement]

### Quantitative Results

| Metric | Value | 95% CI | p-value | Notes |
|--------|-------|--------|---------|-------|
| [Metric name] | [Value] | [CI range] | [p-value] | [Any caveats] |

### Quality Control

<!--
Document QC checks performed and their outcomes
-->

- [ ] Data completeness check:[Result]
- [ ] Outlier detection:[Method used, # outliers found/removed]
- [ ] Normalization QC:[Method, diagnostic plots]
- [ ] Replicate concordance:[Correlation or variance measure]

**QC Issues/Anomalies**:[Document any warnings, errors, or unexpected behaviors]

### Figures & Tables

<!--
REQUIRED: Save all figures to results/ directory with descriptive names
-->

| ID | Description | File Path | Key Finding |
|----|-------------|-----------|-------------|
| Fig 1 | [Description] | `results/exp00_[description].png` | [One-sentence factual finding] |
| Table 1 | [Description] | `results/exp00_[description].csv` | [One-sentence factual finding] |

![Figure 1: Description](../../results/exp00_figure1.png)
*Figure 1: [Detailed caption describing what the figure shows]*

### Unexpected Observations

<!--
Document anything unexpected, even if it seems like a "failure"
-->

[Describe any unexpected results, failed analyses, or surprising findings]

---

## Discussion

<!--
CRITICAL: This section MUST be created through interactive dialogue with AI.
Do NOT fill with generic text.
-->

### Interpretation

<!--
REQUIRED: Engage in dialogue with AI to develop interpretation:
- What do these observations mean biologically?
- How do results relate to the original hypothesis?
- What mechanistic explanations are plausible?
-->

[AI-GENERATED NARRATIVE: Interpretation synthesized from dialog]

### Hypothesis Evaluation

<!--
Select ONE option after evaluating results against success criteria.
-->

- [ ] Hypothesis **supported**
- [ ] Hypothesis **rejected**
- [ ] **Inconclusive**

**Evidence Summary**:
| Criterion | Expected | Observed | Met? |
|-----------|----------|----------|------|
| [Success criterion 1] | [Expected value] | [Observed value] | Yes/No |
| [Success criterion 2] | [Expected value] | [Observed value] | Yes/No |

**Reasoning**:[AI-GENERATED: Explain how evidence supports the evaluation]

### Alternative Interpretations

<!--
Consider other explanations for the observed results
-->

1. **Alternative 1**:[Description and why it's plausible or not]
2. **Alternative 2**:[Description and why it's plausible or not]

**Most likely interpretation**:[State which interpretation is best supported and why]

### Limitations

<!--
Acknowledge constraints honestly
-->

- **Technical limitations**:[e.g., sample size, assay sensitivity]
- **Confounding factors**:[Variables not controlled]
- **Generalizability**:[How broadly do these results apply?]

### Next Steps

<!--
REQUIRED: Specific, actionable follow-up experiments
-->

| Priority | Experiment | Question Addressed | Builds on |
|----------|------------|-------------------|-----------|
| 1 | [Next experiment title] | [What question it answers] | [Current finding it extends] |
| 2 | [Alternative experiment] | [What question it answers] | [Current finding it extends] |

**Immediate action**:[Single most important next step]

---

## Metadata

**Notebook created**:[Date]
**Last modified**:[Date]
**Status**: Draft / In Progress / Complete
**Related experiments**:[Exp##, Exp##]
**Tags**:[e.g., RNA-seq, differential expression, pathway analysis]
