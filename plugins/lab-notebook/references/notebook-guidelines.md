# Lab Notebook Guidelines

## Overview

Lab notebooks are the primary documentation of individual experiments. They should contain complete information for reproducibility, maintain scientific rigor, and clearly separate observations from interpretation.

---

## Section-by-Section Guide

### Header

**Purpose**: Identify the experiment clearly

**Required information**:
- Experiment title following naming convention: `Exp##_[brief-description]`
- Date (YYYY-MM-DD format)
- Experimenter name

**Example**:
```markdown
# Exp03_tcga-survival-analysis

**Date**: 2025-01-15
**Experimenter**: Jane Doe
```

**Tips**:
- Use descriptive but concise titles
- Increment experiment numbers sequentially
- Don't reuse numbers from deleted experiments

---

### Hypothesis

**Purpose**: State the testable prediction being evaluated

**Good hypotheses are**:
- **Specific**: Clearly defined variables and relationships
- **Testable**: Can be evaluated with available data/methods
- **Falsifiable**: Can be proven wrong
- **Quantitative**: Include expected magnitude when possible

**Examples**:

❌ Bad:
- "Gene X is important"
- "Treatment will work"
- "There will be a difference"

✅ Good:
- "Knockout of gene X will reduce cell proliferation by >30% in HeLa cells"
- "Drug A will improve survival by at least 20% compared to control"
- "Patients with high expression of marker Y will have significantly worse prognosis (HR > 2.0, p < 0.05)"

**Format**:
```markdown
## Hypothesis

[State your testable hypothesis]

**Expected outcome**: [What you predict will happen]
```

---

### Background

**Purpose**: Provide context and rationale for the experiment

**Include**:
- Why this experiment is being performed
- Relevant prior findings (from literature or previous experiments)
- How this fits into the broader research question
- Key references

**Structure**:
```markdown
## Background

### Context
[Broader research question and how this experiment addresses it]

### Prior Work
[Relevant findings from literature or previous experiments]

### Rationale
[Why this specific experimental approach]

### References
1. [Citation 1]
2. [Citation 2]
```

**Tips**:
- Keep focused (not a comprehensive literature review)
- Link to related experiments: "Building on Exp02_..."
- Explain deviations from standard methods

---

### Materials and Methods

**Purpose**: Document complete procedure for reproducibility

**Critical principle**: Someone else should be able to replicate exactly what you did.

**Required information**:

#### Data
- Source (where obtained, with version/date)
- Format (FASTQ, BAM, CSV, etc.)
- Location (file paths)
- Size/scope (number of samples, features, etc.)
- Preprocessing applied (if any)

**Example**:
```markdown
### Data

- **Source**: TCGA-BRCA RNA-seq data (GDC portal, downloaded 2025-01-15)
- **Format**: HTSeq counts (normalized)
- **Location**: `data/raw/tcga_brca_counts.tsv`
- **Samples**: 1,100 tumor samples, 113 normal samples
- **Features**: 20,530 genes
- **Preprocessing**: None (using raw downloaded files)
```

#### Tools
- Software names and versions
- Key libraries/packages and versions
- Hardware used (if relevant for computational experiments)

**Example**:
```markdown
### Tools

- Python: 3.10.8
- pandas: 1.5.2
- scikit-learn: 1.2.0
- DESeq2: 1.38.0 (R 4.2.2)
- Hardware: 32GB RAM, 8 cores
```

#### Procedure
- Step-by-step protocol
- All parameters and settings
- Decision points and criteria
- Commands executed (can be in code cells for Jupyter)

**Example**:
```markdown
### Procedure

1. Load count data from `data/raw/tcga_brca_counts.tsv`
2. Filter genes with <10 counts in >90% of samples
3. Normalize using DESeq2 size factors
4. Perform differential expression testing:
   - Comparison: Tumor vs Normal
   - Model: ~condition (no covariates)
   - Adjusted p-value threshold: 0.05 (Benjamini-Hochberg)
5. Extract significantly differentially expressed genes
6. Perform pathway enrichment analysis (Reactome database)
```

**Tips**:
- Be specific about parameters (don't write "standard settings")
- Include random seeds for reproducibility
- Note any deviations from original plan
- For Jupyter notebooks, code cells can serve as procedure documentation

---

### Results

**Purpose**: Document factual observations without interpretation

**Critical principle**: Results section should contain ONLY observations (Level 1 facts from quality-standards.md).

**Include**:
- Summary statistics
- Key numbers and metrics
- Figures and tables
- Quality control checks
- Unexpected observations

**Avoid**:
- Interpretation (save for Discussion)
- Biological significance (save for Discussion)
- Causal language (e.g., "X caused Y" → "X correlated with Y")

**Good practices**:

✅ Factual observations:
- "2,453 genes showed differential expression (adjusted p < 0.05)"
- "Median fold-change was 1.8 (range: 0.1-12.4)"
- "Positive controls showed expected results (Figure 1A)"

❌ Interpretation (belongs in Discussion):
- "The pathway is activated" (interpretation)
- "This suggests gene X regulates Y" (interpretation)
- "These genes are important for cancer" (conclusion)

**Figure/Table guidelines**:
- Every figure/table must have a descriptive caption
- Axes must be labeled with units
- Include error bars/confidence intervals where appropriate
- Define abbreviations in captions
- Reference figures in text: "Differential expression results are shown in Figure 1"

**Figure saving best practices** (critical for Jupyter notebooks):
- **Always save figures to `results/` directory** before displaying
- **Use descriptive filenames**: `exp##_[description].png` (e.g., `exp03_volcano_plot.png`)
- **Save in multiple formats**: PNG (300 dpi) for notebooks, PDF/SVG for reports
- **Reference saved figures** in markdown cells for future report generation
- **Example code**:
  ```python
  # Create figure
  fig, ax = plt.subplots(figsize=(8, 6))
  ax.scatter(log2fc, -np.log10(pval))
  ax.set_xlabel('Log2 Fold Change')
  ax.set_ylabel('-Log10 P-value')

  # Save before showing (critical for report generation)
  fig.savefig('results/exp03_volcano_plot.png', dpi=300, bbox_inches='tight')
  fig.savefig('results/exp03_volcano_plot.pdf')  # Vector format for publications
  plt.show()
  ```
- **Then reference in markdown cell**:
  ```markdown
  ![Figure 1: Volcano plot](../../results/exp03_volcano_plot.png)
  *Figure 1: Volcano plot of differential expression. Red points: adjusted p < 0.05.*
  ```

**Quality control**:
Always include QC checks:
- Sample size at each filtering step
- Distribution plots (before/after normalization)
- Control results (positive/negative controls)
- Outlier detection
- Validation metrics

**Example**:
```markdown
## Results

### Data Quality

- Initial: 1,213 samples, 20,530 genes
- After filtering: 1,213 samples, 15,423 genes (removed 5,107 low-count genes)
- Sample clustering showed expected separation by tissue type (Figure 1A)

### Differential Expression

- 2,453 genes significantly differentially expressed (adjusted p < 0.05)
  - 1,342 upregulated in tumor
  - 1,111 downregulated in tumor
- Median log2 fold-change: 1.2 (range: -4.8 to 5.3)
- Top hit: GENE-X (log2FC = 5.3, adj.p = 1.2e-45)

![Figure 1: Volcano plot](../../results/exp03_volcano.png)
*Figure 1: Volcano plot of differential expression. Points in red: adjusted p < 0.05.*

### Quality Controls

- Positive control gene (ACTB) showed no differential expression (as expected)
- Technical replicate correlation: r = 0.98
- PCA showed expected separation by condition (Figure 2)
```

---

### Discussion

**Purpose**: Interpret results and evaluate hypothesis

**Structure**:

#### Interpretation
Connect observations to biological meaning (Level 2 statements from quality-standards.md).

**Include**:
- What the results mean biologically
- How results relate to hypothesis
- Connection to literature
- Mechanistic explanations (with caveats)

**Example**:
```markdown
### Interpretation

The 2,453 differentially expressed genes (Results) represent substantial transcriptional
reprogramming in breast cancer. The enrichment of cell cycle genes among upregulated
transcripts (Table 1) suggests enhanced proliferation, consistent with the known biology
of cancer cells (Smith et al. 2024).

The top hit, GENE-X (5.3-fold upregulated, adj.p = 1.2e-45), has been previously
implicated in cell migration (Jones et al. 2023), suggesting a possible role in
metastasis. However, correlation does not establish causation, and functional studies
would be needed to confirm a causal relationship.
```

#### Hypothesis Evaluation
Explicitly evaluate the original hypothesis.

**Format**:
```markdown
### Hypothesis Evaluation

**Original hypothesis**: Knockout of gene X will reduce cell proliferation by >30%

**Result**:
- [ ] Hypothesis supported
- [x] Hypothesis rejected
- [ ] Inconclusive

**Reasoning**:
Gene X knockout reduced proliferation by only 12% (95% CI: 8-16%), which is below
the 30% threshold specified in the hypothesis. This suggests Gene X has a modest
effect on proliferation, contrary to our prediction of a major role.
```

#### Limitations
Acknowledge constraints and caveats.

**Common limitations**:
- Sample size
- Model system limitations (cell lines ≠ tumors)
- Technical limitations (resolution, sensitivity)
- Confounding variables not controlled
- Generalizability

**Example**:
```markdown
### Limitations

1. **Sample heterogeneity**: TCGA samples come from different institutions with
   varying collection protocols, introducing potential batch effects.

2. **Cross-sectional design**: Cannot infer temporal dynamics or causality from
   single-timepoint expression data.

3. **Bulk RNA-seq**: Cannot distinguish cell-type-specific effects; results
   represent average across cell populations.

4. **No validation cohort**: Results should be validated in independent dataset.
```

#### Next Steps
Identify follow-up experiments or analyses.

**Be specific**:
- What exact experiment would you do next?
- What question does it address?
- How does it build on current findings?

**Example**:
```markdown
### Next Steps

1. **Validate top hits**: Perform qPCR validation of top 10 differentially
   expressed genes in independent sample set (Exp04)

2. **Functional testing**: Design knockdown experiments for GENE-X to test
   causal role in migration (Exp05)

3. **Single-cell analysis**: Examine cell-type-specific expression patterns
   using scRNA-seq data to address bulk tissue limitation (Exp06)

4. **Survival analysis**: Test prognostic value of identified gene signature
   in clinical outcome data (Exp07)
```

---

## Quality Checklist

Before finalizing a lab notebook, verify:

### Completeness
- [ ] All required sections present
- [ ] Methods reproducible (someone else could replicate)
- [ ] All parameters documented
- [ ] Figures/tables properly labeled
- [ ] References cited

### Scientific Rigor
- [ ] Hypothesis clearly stated
- [ ] Facts separated from interpretation
- [ ] Results are observational (no interpretation)
- [ ] Discussion includes reasoning
- [ ] Limitations acknowledged
- [ ] Alternative explanations considered

### Reproducibility
- [ ] Data sources specified with versions
- [ ] Software versions documented
- [ ] Random seeds set (if applicable)
- [ ] File paths provided
- [ ] Code is executable (for Jupyter notebooks)

### Documentation
- [ ] Unexpected findings documented
- [ ] Failed approaches noted
- [ ] Decisions explained
- [ ] Next steps identified
- [ ] Quality control included

---

## Common Mistakes

### 1. Interpretation in Results

❌ Bad:
```markdown
## Results
Gene X is upregulated, indicating pathway activation.
```

✅ Good:
```markdown
## Results
Gene X expression was 2.3-fold higher (p < 0.01).

## Discussion
The 2.3-fold increase in Gene X suggests possible pathway activation,
though additional experiments are needed to confirm this interpretation.
```

### 2. Vague Methods

❌ Bad:
```markdown
Performed standard differential expression analysis.
```

✅ Good:
```markdown
Performed differential expression using DESeq2 (v1.38.0) with:
- Model: ~condition
- Wald test for significance
- Benjamini-Hochberg correction
- Significance threshold: adjusted p < 0.05
```

### 3. Cherry-Picking Results

❌ Bad:
Only showing the one replicate that worked.

✅ Good:
```markdown
In 3 of 4 replicates, X increased Y. One replicate showed no effect
(possible technical issue with sample preparation noted in lab notes).
```

### 4. Overgeneralization

❌ Bad:
```markdown
Gene X regulates cell growth.
```

✅ Good:
```markdown
In HeLa cells under serum starvation, Gene X knockdown reduced proliferation
by 30% (Figure 2). Whether this occurs in other cell types or conditions
remains to be determined.
```

---

## Version Control Best Practices

### Commit Frequency

**Commit after**:
- Completing each major section
- Generating important figures
- Running long analyses
- Before major changes

**Commit message examples**:
```
feat: add differential expression analysis
fix: correct normalization procedure
docs: add background and hypothesis
results: generate volcano plots
```

### What to Commit

✅ Always commit:
- Notebook files (.ipynb, .md)
- Analysis scripts
- Small result files (<1MB)

❌ Never commit:
- Raw data files (usually in .gitignore)
- Large result files (>1MB, usually in .gitignore)
- Temporary files

### Git workflow

```bash
# After completing a section
git add notebook/labnote/Exp03_analysis.ipynb
git commit -m "results: complete differential expression analysis"

# Periodically push
git push
```

---

## Examples

### Example: Good Lab Notebook (Abbreviated)

```markdown
# Exp03_tcga-survival-analysis

**Date**: 2025-01-15
**Experimenter**: Jane Doe

---

## Hypothesis

High expression of gene signature identified in Exp02 will correlate with
poor survival in TCGA-BRCA cohort (HR > 2.0, p < 0.05).

**Expected outcome**: Patients in high-expression group show significantly
reduced overall survival compared to low-expression group.

## Background

Exp02 identified a 20-gene signature upregulated in aggressive tumor subtypes.
Literature suggests several of these genes (Gene-A, Gene-B) are involved in
metastasis (Smith 2024). This experiment tests whether the signature has
prognostic value.

[... Methods, Results, Discussion ...]

## Discussion

### Hypothesis Evaluation

- [x] Hypothesis supported

The 20-gene signature showed significant prognostic value (HR = 2.8,
p = 3e-5), supporting our hypothesis that high expression correlates
with poor survival.

### Limitations

1. Retrospective analysis cannot establish causation
2. Signature not validated in independent cohort
3. Does not account for treatment differences

### Next Steps

1. Validate in METABRIC cohort (Exp04)
2. Test multivariate model with clinical variables (Exp05)
```

---

## Jupyter-Specific Tips

### Code Cell Organization

**Structure code cells logically**:
1. Imports at top
2. Configuration/parameters
3. Data loading
4. Analysis steps (one concept per cell)
5. Visualization

### Cell Documentation

**Use markdown cells liberally**:
- Before major steps
- To explain rationale
- To highlight key results

### Output Management

**Be selective about output**:
- Clear unnecessary output before committing
- Save important figures as files
- Limit printed output (use `.head()` not full dataframes)

### Execution Order

**Always**:
- Run cells in order before finalizing
- Restart kernel and run all cells to verify reproducibility
- Fix any execution order dependencies

---

## Markdown-Specific Tips

### Code Blocks

Use language-specific code blocks:

````markdown
```python
import pandas as pd
data = pd.read_csv("data.csv")
```

```bash
samtools sort input.bam -o output.bam
```
````

### Linking Files

Use relative paths:
```markdown
![Figure 1](../../results/exp03_plot.png)
```

### Execution Documentation

For non-Python experiments, document exact commands:

```markdown
## Procedure

### Step 1: Alignment
```bash
bwa mem -t 8 ref.fa read1.fq read2.fq > aligned.sam
```

### Step 2: Sorting
```bash
samtools sort aligned.sam -o aligned.sorted.bam
```
```

---

## Integration with Project

### Before Starting

1. Check STEERING.md for current phase and priorities
2. Review notebook/tasks.md for planned experiments
3. Ensure experiment aligns with research question

### During Experiment

1. Update tasks.md with progress
2. Commit regularly
3. Document unexpected findings immediately

### After Completion

1. Mark complete in tasks.md
2. Update STEERING.md if milestone reached
3. Consider:
   - Need for hypothesis refinement? (hypothesis-driven skill)
   - Ready for report generation? (experiment-report skill)
   - Next experiment planning

---

## Resources

Additional references:
- `quality-standards.md` in research-project plugin
- `best-practices.md` in research-project plugin
- Lab-specific guidelines (if available in `notebook/knowledge/`)
