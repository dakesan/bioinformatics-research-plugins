# Research Best Practices

## Core Principles

### 1. Hypothesis-Driven Research

**Always start with testable hypotheses**

Good hypotheses are:
- **Specific**: Clearly defined variables and relationships
- **Testable**: Can be evaluated with available data and methods
- **Falsifiable**: Can be proven wrong
- **Meaningful**: Address important research questions

**Example**:
- ❌ Bad: "Gene X is important"
- ✅ Good: "Knockout of gene X reduces cell proliferation by >30% in condition Y"

### 2. Separate Facts from Interpretation

**Maintain clear boundaries between observation and conclusion**

> **Detailed specification**: See `references/quality-standards.md` for the complete
> three-level framework (Facts → Interpretation → Conclusion) with examples and
> quality checklist.

Three levels of scientific statements:
1. **Facts**: Direct observations (e.g., "Gene X expression was 2.3-fold higher")
2. **Interpretation**: Reasoned explanation (e.g., "This suggests increased activity")
3. **Conclusion**: Broader implications (e.g., "Gene X may regulate pathway Y")

**In practice**:
- Lab notebooks: Focus on facts and observations (Level 1)
- Reports: Include interpretation with clear reasoning (Level 2)
- Always label speculation as such
- Use calibrated language for uncertainty (see `quality-standards.md`)

### 3. Document Everything

**Write for reproducibility**

Lab notebooks should contain:
- Complete procedure (someone else could replicate)
- All parameters and settings
- Unexpected observations
- Dead ends and failed attempts
- Reasons for decisions

**Why document failures**:
- Prevent repeating mistakes
- Understand method limitations
- Build institutional knowledge

### 4. Question Assumptions

**Stay with uncertainty until evidence is sufficient**

Never rush to conclusions:
- Consider alternative explanations
- Identify what would disprove your hypothesis
- Acknowledge limitations explicitly
- Separate correlation from causation

**Red flags**:
- "Obviously..."
- "Clearly..."
- "It must be..."

Better phrases:
- "The data suggest..."
- "One possible explanation..."
- "This is consistent with..."

---

## Experimental Design

### Start Simple

**KISS (Keep It Simple, Stupid)**

- Begin with simplest test of hypothesis
- Add complexity only when justified
- Control one variable at a time
- Use positive and negative controls

### Plan for Iteration

**Research is iterative, not linear**

1. Initial hypothesis
2. Simple experiment
3. Refine hypothesis based on results
4. Design next experiment
5. Repeat

Accept that:
- First experiments rarely answer everything
- Negative results inform next steps
- Iteration is normal and valuable

### Statistical Considerations

**Design for statistical power**

- Define success criteria before starting
- Calculate required sample size
- Plan for technical replicates
- Consider batch effects
- Document randomization scheme

---

## Data Management

### Organization

**Standardize naming and structure**

File naming convention:
```
Exp##_[brief-description]_[date].ext

Examples:
Exp01_rnaseq-analysis_2025-01-15.ipynb
Exp02_protein-quantification_2025-01-20.md
```

Directory structure:
- `data/raw/`: Original unprocessed data (never modify)
- `results/`: Analysis outputs (reproducible from code)
- `notebook/labnote/`: Individual experiments
- `notebook/report/`: Integrated analyses

### Figure Management

**Save all figures with descriptive names for future reference**

When running Jupyter notebooks or generating visualizations:

1. **Save figures to `results/` directory**
   ```python
   # Good practice
   fig.savefig('results/exp01_volcano_plot.png', dpi=300, bbox_inches='tight')
   fig.savefig('results/exp01_volcano_plot.pdf')  # Also save as vector format
   ```

2. **Use descriptive filenames**
   ```
   Good: exp01_volcano_plot.png, exp02_survival_curve.png
   Bad: figure1.png, plot.png, output.png
   ```

3. **Naming convention for figures**
   ```
   exp##_[figure-description].[ext]

   Examples:
   exp01_volcano_plot.png
   exp02_heatmap_top100genes.png
   exp03_survival_kaplan_meier.pdf
   ```

4. **Reference figures in notebooks**
   ```markdown
   ![Figure 1: Volcano plot](../../results/exp01_volcano_plot.png)
   *Figure 1: Volcano plot showing differential expression...*
   ```

5. **Save both raster and vector formats**
   - PNG for embedding in notebooks (300 dpi minimum)
   - PDF/SVG for publications and reports

6. **Version figures with experiments**
   - Each experiment's figures should be clearly labeled (exp##_)
   - Enables easy figure retrieval when creating reports
   - Maintains figure-experiment traceability

### Version Control

**Track changes systematically**

- Use git for code and text files
- Commit with meaningful messages
- Tag important milestones
- Document data provenance

### Backup Strategy

**Protect against data loss**

- Raw data: Multiple backups, never modify originals
- Code: Version controlled (git)
- Results: Reproducible from code + data
- Lab notebooks: Regular commits

---

## Scientific Writing

### Progressive Disclosure

**Structure information hierarchically**

1. **Executive summary**: 2-3 sentence overview
2. **Key findings**: High-level results
3. **Details**: Methods, data, analysis
4. **Appendix**: Supplementary information

Let readers drill down based on interest.

### Clear Communication

**Write for understanding**

- Use active voice
- Define technical terms
- One idea per paragraph
- Link claims to evidence
- Use figures to clarify

### Evidence-Based Claims

**Support every assertion**

Format: `[Claim] (evidence: notebook/figure/table)`

Example:
- "Gene X expression increased 2.3-fold (Figure 2A, Exp03_rnaseq.ipynb)"

---

## Report Generation Workflow

### Traceability: Claims to Evidence

Every claim must link to verifiable evidence. Report traceability structure:
```
Claim → Evidence Path → Figure/Table ID → Uncertainty Level → Open Issues
```

Template for each finding in report:

```markdown
### Finding: [Title]

**Claim**: [Specific, quantitative statement]

**Evidence**:
| Type | ID | Path | Description |
|------|-----|------|-------------|
| Notebook | Exp01 | notebook/labnote/Exp01_analysis.ipynb | Primary analysis |
| Figure | Fig1A | results/exp01_volcano.png | Volcano plot |
| Table | Tab1 | results/exp01_deg_table.csv | DE gene list |

**Uncertainty Level**: [High/Medium/Low]
- Confidence basis: [Statistical significance, replication, etc.]
- Known caveats: [Sample size, model limitations, etc.]

**Open Issues**:
- [ ] [Remaining question or validation needed]
- [ ] [Follow-up experiment required]
```

### Claim-Evidence Mapping Checklist

Before report submission, verify:

- [ ] Every factual claim has an evidence path
- [ ] All figures/tables are referenced by ID
- [ ] Source notebooks are specified for each finding
- [ ] Statistical values are complete (test name, n, effect size, p-value)
- [ ] Uncertainty level is explicitly stated
- [ ] Open issues are documented (not hidden)

### Example: Complete Finding Block

```markdown
### Finding: Gene X Upregulation in Tumors

**Claim**: Gene X expression is 2.3-fold higher in tumor samples compared
to normal tissue (adjusted p < 0.001, n=1,100 tumors, n=113 normal).

**Evidence**:
| Type | ID | Path | Description |
|------|-----|------|-------------|
| Notebook | Exp03 | notebook/labnote/Exp03_differential_expression.ipynb | DESeq2 analysis |
| Figure | Fig2A | results/exp03_volcano_plot.png | Volcano plot with Gene X highlighted |
| Figure | Fig2B | results/exp03_genex_boxplot.png | Expression boxplot tumor vs normal |
| Table | Tab2 | results/exp03_top50_genes.csv | Top 50 DE genes with statistics |

**Uncertainty Level**: Medium
- Confidence basis: Large sample size, adjusted p < 0.001
- Known caveats: Cross-sectional design, bulk RNA-seq averages cell types

**Open Issues**:
- [ ] Validate with qPCR in independent cohort
- [ ] Determine cell-type specificity with scRNA-seq
```

---

## Reproducibility Requirements

### Reproducibility Block

Required metadata for every report. Include a reproducibility block before submission:

```markdown
## Reproducibility Information

### Environment
- **OS**: [e.g., Ubuntu 22.04, macOS 14.0]
- **Python**: [e.g., 3.10.8]
- **R**: [e.g., 4.3.1] (if applicable)

### Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| pandas | 1.5.2 | Data manipulation |
| numpy | 1.24.0 | Numerical operations |
| matplotlib | 3.7.0 | Visualization |
| DESeq2 | 1.38.0 | Differential expression |

### Data Sources
| Dataset | Version/Date | Source | Access |
|---------|--------------|--------|--------|
| TCGA-BRCA | 2024-01-15 | GDC Portal | Public |
| Reference genome | GRCh38.p14 | NCBI | Public |

### Random Seeds
- Analysis: `random_state=42`
- Train/test split: `seed=123`

### Command History
Key commands executed (in order):
1. `python scripts/01_preprocess.py --input data/raw/counts.tsv`
2. `python scripts/02_normalize.py --method deseq2`
3. `python scripts/03_differential.py --comparison tumor_vs_normal`
```

### Pre-Submission Reproducibility Checklist

Before finalizing report:

- [ ] Environment documented: OS, Python/R version specified
- [ ] Dependencies listed: All packages with exact versions
- [ ] Data sources specified: Dataset name, version/date, access method
- [ ] Random seeds recorded: All stochastic operations reproducible
- [ ] Command history preserved: Key commands in execution order
- [ ] File paths verified: All referenced files exist and are accessible
- [ ] Code committed: All analysis code in version control with tag
- [ ] Results reproducible: Re-running commands produces same output

### Dependency Lock File

For Python projects, generate dependency snapshot:

```bash
# Create exact dependency list
uv pip freeze > requirements.lock.txt

# Or with uv (recommended)
uv lock
```

Include `requirements.lock.txt` or `uv.lock` in version control.

---

## Quality Control

### Sanity Checks

**Validate at every step**

- Check data distributions
- Verify expected controls
- Look for outliers
- Compare to literature
- Cross-validate methods

### Peer Review

**Get feedback early and often**

- Discuss hypotheses before executing
- Show preliminary results to colleagues
- Request code review
- Present work in lab meetings

### Documentation Review

**Self-review before sharing**

Checklist:
- [ ] Can I reproduce this in 6 months?
- [ ] Are all parameters documented?
- [ ] Are figures properly labeled?
- [ ] Are limitations acknowledged?
- [ ] Is code readable?

---

## Common Pitfalls

### Confirmation Bias

**Actively seek disconfirming evidence**

- Test null hypothesis explicitly
- Look for alternative explanations
- Don't cherry-pick results
- Report negative findings

### P-Hacking

**Avoid multiple testing without correction**

- Define analysis plan beforehand
- Correct for multiple comparisons
- Don't fish for significance
- Report all tests performed

### Overfitting

**Ensure models generalize**

- Use train/test splits
- Validate on independent data
- Prefer simpler models
- Report cross-validation results

### HARKing (Hypothesizing After Results Known)

**Be honest about post-hoc hypotheses**

- Clearly label exploratory vs confirmatory
- Acknowledge hypothesis refinement
- Plan confirmatory experiments
- Don't pretend you predicted everything

---

## Collaboration

### Clear Communication

**Make expectations explicit**

- Document roles and responsibilities
- Set regular check-in meetings
- Share progress transparently
- Ask for help early

### Code Sharing

**Write for others**

- Use consistent style
- Comment non-obvious code
- Include README files
- Provide usage examples

### Knowledge Transfer

**Build institutional knowledge**

- Document procedures in `notebook/knowledge/`
- Create reusable workflows
- Share lessons learned
- Mentor others

---

## Time Management

### Realistic Planning

**Estimate conservatively**

- Research takes longer than expected
- Buffer for failed experiments
- Account for iteration
- Plan review time

### Prioritization

**Focus on critical path**

- What needs to be done first?
- What can be parallelized?
- What can be deferred?
- What can be skipped?

### Regular Reviews

**Assess progress systematically**

Weekly:
- Update tasks.md
- Review experimental results
- Plan next week

Monthly:
- Update STEERING.md
- Consider phase transitions
- Reflect on methods

---

## References

These best practices are informed by:
- Scientific method fundamentals
- Reproducible research principles
- Agile research methodologies
- Open science practices
