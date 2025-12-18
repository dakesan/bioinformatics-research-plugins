# Lab Notebook to Report Mapping Rules

## Overview

This document defines how content from lab notebooks should be extracted and transformed when generating integrated reports. The goal is to maintain scientific rigor while creating coherent, synthesized documentation.

---

## Section Mapping

### Lab Notebook → Report Section Mapping

| Lab Notebook Section | Report Section | Transformation Type | Notes |
|---------------------|----------------|---------------------|-------|
| Hypothesis | Background | Synthesis | Combine with context |
| Background | Background | Consolidation | Merge related background |
| Materials & Methods → Data | Methods → Data Sources | Summary | List all datasets used |
| Materials & Methods → Tools | Methods → Analysis Tools | Summary | List unique tools/versions |
| Materials & Methods → Procedure | Methods → Procedures | Abstraction | High-level overview |
| Results | Findings | Structuring | Organize by theme |
| Discussion → Interpretation | Synthesis | Integration | Connect across experiments |
| Discussion → Hypothesis Evaluation | Synthesis | Integration | Overall assessment |
| Discussion → Limitations | Limitations | Consolidation | Collect all caveats |
| Discussion → Next Steps | Future Directions | Prioritization | Rank by importance |
| (Derived from all sections) | Executive Summary | Distillation | 3-5 key sentences |
| (Derived from all sections) | Conclusion | Synthesis | Final takeaways |

---

## Detailed Mapping Rules

### 1. Executive Summary

**Source**: Key conclusions from all notebooks

**Transformation**: **Distillation**

**Rules**:
- Length: 3-5 sentences maximum
- Content: Highest-level findings only
- Structure:
  1. Research question (1 sentence)
  2. Approach (1 sentence, optional)
  3. Key findings (1-2 sentences)
  4. Implications (1 sentence)
- Avoid: Technical details, statistics, figure references

**Example**:

From notebooks:
- Exp01: "Found 2,453 differentially expressed genes..."
- Exp02: "Validated top 10 genes by qPCR..."
- Exp03: "Cell cycle pathway enriched (p<0.01)..."

Executive Summary:
```markdown
We investigated transcriptional changes in breast cancer using RNA-seq and validation approaches. Analysis of TCGA-BRCA data revealed 2,453 differentially expressed genes, with significant enrichment in cell cycle pathways. Validation confirmed upregulation of key proliferation markers, suggesting enhanced cell division as a hallmark of tumor progression. These findings provide candidate biomarkers for further functional studies.
```

---

### 2. Background

**Source**: Hypothesis + Background sections from all notebooks

**Transformation**: **Synthesis**

**Rules**:
- Combine related context from multiple notebooks
- Eliminate redundancy
- Organize hierarchically:
  1. Research Question (overarching)
  2. Context (broader field)
  3. Rationale (why this study)
  4. Specific Aims (if multiple experiments)
- Cite shared references once
- Link experiments: "Building on initial findings (Exp01), we..."

**Example**:

From Exp01 Background:
```markdown
Breast cancer is characterized by transcriptional dysregulation...
```

From Exp02 Background:
```markdown
RNA-seq findings need validation to confirm biological relevance...
```

Synthesized Report Background:
```markdown
## Background

### Research Question
How does gene expression reprogramming contribute to breast cancer progression?

### Context
Breast cancer arises from accumulated genetic and epigenetic alterations that
reprogram cellular transcription. Understanding these changes can identify
therapeutic targets and prognostic markers.

### Rationale
While large-scale datasets like TCGA provide comprehensive expression profiles,
computational findings require experimental validation to confirm biological
relevance and guide functional studies.

### Approach
We performed computational analysis of TCGA-BRCA data (Exp01) followed by
experimental validation of top candidates (Exp02) and pathway analysis (Exp03)
to characterize transcriptional reprogramming in breast cancer.
```

---

### 3. Materials and Methods

**Source**: Materials & Methods sections from all notebooks

**Transformation**: **Consolidation + Abstraction**

**Rules**:
- **Data Sources**: List all datasets with versions
- **Analysis Tools**: List unique tools/versions (don't repeat)
- **Procedures**: High-level workflow, not step-by-step
- Organize by experiment if procedures differ significantly
- Reference notebooks for full details

**Example**:

From Exp01 Methods:
```markdown
### Data
- TCGA-BRCA RNA-seq (1,100 samples)
- Downloaded 2025-01-15

### Tools
- Python 3.10, pandas 1.5.2, DESeq2 1.38.0

### Procedure
1. Load counts
2. Filter low-count genes
3. Normalize with DESeq2
4. Differential expression testing
```

From Exp02 Methods:
```markdown
### Data
- qPCR data for 10 genes

### Tools
- Primer3 for primer design
- QuantStudio qPCR system

### Procedure
1. Design primers
2. Extract RNA
3. Perform qPCR
```

Consolidated Report Methods:
```markdown
## Materials and Methods

### Data Sources

**Computational Analysis** (Exp01):
- TCGA-BRCA RNA-seq data: 1,100 tumor samples, 20,530 genes (GDC portal, 2025-01-15)

**Experimental Validation** (Exp02):
- qPCR validation: 10 candidate genes in 30 samples

### Analysis Tools

- Computational: Python 3.10, DESeq2 1.38.0, pandas 1.5.2
- Experimental: QuantStudio qPCR system, Primer3

### Procedures

**RNA-seq Analysis**: Differential expression was performed using DESeq2
with standard normalization and Benjamini-Hochberg correction (Exp01).

**Validation**: Top differentially expressed genes were validated by qPCR
using gene-specific primers designed with Primer3 (Exp02).

Full methods available in individual lab notebooks (see Appendix).
```

---

### 4. Findings

**Source**: Results sections from all notebooks

**Transformation**: **Structuring by theme**

**Rules**:
- Organize by finding, not by experiment
- Each finding includes:
  - **Title**: Descriptive name
  - **Observation**: Factual description (Level 1)
  - **Evidence**: Notebook references, figures, statistics
  - **Interpretation**: Brief explanation (Level 2, minimal)
- Maintain fact/interpretation separation
- Cross-reference experiments when relevant
- Use consistent terminology

**Example**:

From Exp01 Results:
```markdown
## Results
2,453 genes differentially expressed (adj.p < 0.05).
Median fold-change: 1.8.
```

From Exp02 Results:
```markdown
## Results
9 of 10 candidate genes confirmed by qPCR.
Correlation with RNA-seq: r = 0.92.
```

From Exp03 Results:
```markdown
## Results
Cell cycle pathway enriched (p < 0.01, 45 genes).
```

Structured Report Findings:
```markdown
## Findings

### Finding 1: Widespread Transcriptional Reprogramming

**Observation**: RNA-seq analysis identified 2,453 genes with significant
differential expression between tumor and normal tissue (adjusted p < 0.05),
representing 12% of the transcriptome (Exp01).

**Evidence**:
- 2,453 DE genes (1,342 up, 1,111 down)
- Median log2 fold-change: 1.8 (range: -4.8 to 5.3)
- Lab notebook: Exp01_rnaseq.ipynb, Figure 1A

**Interpretation**: The magnitude of transcriptional changes indicates
substantial reprogramming of cellular function in breast tumors.

### Finding 2: Validation of Computational Predictions

**Observation**: Experimental validation by qPCR confirmed 9 of 10 top
differentially expressed genes identified computationally, with strong
correlation (r = 0.92, p < 0.001) between RNA-seq and qPCR fold-changes (Exp02).

**Evidence**:
- 90% validation rate (9/10 genes)
- RNA-seq vs qPCR correlation: r = 0.92 (p < 0.001)
- Lab notebook: Exp02_qpcr-validation.md, Figure 2B

**Interpretation**: High validation rate demonstrates technical reliability
of RNA-seq findings and biological relevance of identified changes.

### Finding 3: Cell Cycle Pathway Dysregulation

**Observation**: Pathway enrichment analysis revealed significant
over-representation of cell cycle genes among upregulated transcripts
(hypergeometric p = 0.008, 45 genes, 2.1-fold enrichment) (Exp03).

**Evidence**:
- 45 cell cycle genes upregulated
- Enrichment: 2.1-fold (p = 0.008)
- Lab notebook: Exp03_pathway-analysis.ipynb, Table 1

**Interpretation**: Enrichment of proliferation-related genes is consistent
with enhanced cell division, a hallmark of cancer.
```

---

### 5. Synthesis

**Source**: Discussion → Interpretation sections from all notebooks

**Transformation**: **Integration across experiments**

**Rules**:
- Integrate interpretations, don't just concatenate
- Build coherent narrative connecting findings
- Cite supporting evidence from multiple experiments
- Acknowledge alternative explanations
- Maintain appropriate uncertainty language
- Reference external literature
- Distinguish strong vs weak conclusions

**Example**:

From individual notebooks:
- Exp01 Discussion: "Changes suggest pathway activation..."
- Exp02 Discussion: "Validation confirms biological relevance..."
- Exp03 Discussion: "Cell cycle enrichment indicates proliferation..."

Integrated Report Synthesis:
```markdown
## Synthesis

The integration of computational and experimental approaches provides
converging evidence for transcriptional reprogramming in breast cancer.

**Biological Significance**: The widespread nature of expression changes
(12% of transcriptome, Finding 1) combined with high validation rate
(90%, Finding 2) demonstrates this is a robust and biologically relevant
phenomenon. The specific enrichment of cell cycle genes (Finding 3) suggests
enhanced proliferation as a key driver of tumor progression, consistent with
known cancer biology (Hanahan & Weinberg 2011).

**Mechanistic Insights**: While our data demonstrate correlation between
cell cycle gene expression and cancer, causation requires further validation.
The upregulation could be a consequence of enhanced proliferation rather than
a driver. Functional studies (knockdown, overexpression) would clarify
causal relationships.

**Comparison to Literature**: Our findings align with previous reports of
cell cycle dysregulation in breast cancer (Smith et al. 2024). However, we
extend these observations by providing experimental validation and quantifying
the magnitude of enrichment (2.1-fold), which is more modest than some prior
reports. This difference may reflect dataset composition or analysis methods.

**Implications**: The validated gene signature provides candidate biomarkers
for further study. Genes showing both computational and experimental support
(e.g., GENE-X, GENE-Y) are high-priority targets for functional characterization.
The pathway-level analysis suggests existing cell cycle inhibitors merit
evaluation in breast cancer models.
```

---

### 6. Limitations

**Source**: Discussion → Limitations sections from all notebooks

**Transformation**: **Consolidation without redundancy**

**Rules**:
- Collect limitations from all experiments
- Group by category (technical, biological, interpretive)
- Eliminate redundant statements
- Be constructive (suggest solutions where possible)
- Prioritize most important limitations
- Acknowledge without being overly apologetic

**Example**:

From notebooks:
- Exp01: "Cross-sectional design limits causal inference..."
- Exp01: "Bulk RNA-seq cannot resolve cell-type differences..."
- Exp02: "Small validation cohort (n=30)..."
- Exp03: "Pathway enrichment is correlative..."

Consolidated Report Limitations:
```markdown
## Limitations

**Study Design**:
1. **Cross-sectional data**: TCGA samples represent single timepoints, preventing
   inference of temporal dynamics or causal relationships. Longitudinal studies
   would clarify whether gene expression changes precede or follow transformation.

2. **Bulk tissue analysis**: RNA-seq from bulk tumors reflects average expression
   across heterogeneous cell populations. Single-cell approaches would identify
   cell-type-specific programs masked in bulk analysis.

**Sample Size**:
3. **Limited validation cohort**: Experimental validation was performed in
   30 samples for 10 genes. Larger validation studies across diverse sample
   types would strengthen generalizability.

**Methodology**:
4. **Correlative pathway analysis**: Enrichment of cell cycle genes demonstrates
   association but not causation. Functional perturbation experiments are needed
   to establish causal roles.

5. **Confounding variables**: Potential batch effects and clinical heterogeneity
   in TCGA data were not fully addressed. Matched normal samples from the same
   patients would reduce confounding.

**Solutions**: Future work incorporating single-cell profiling, larger validation
cohorts, and functional perturbation studies would address these limitations and
strengthen mechanistic conclusions.
```

---

### 7. Future Directions

**Source**: Discussion → Next Steps sections from all notebooks

**Transformation**: **Prioritization and organization**

**Rules**:
- Collect next steps from all notebooks
- Prioritize by:
  1. Direct follow-ups (validate key findings)
  2. Mechanism elucidation
  3. Broader implications
- Organize hierarchically (immediate → long-term)
- Be specific (not "more research needed")
- Link to limitations

**Example**:

From notebooks:
- Exp01: "Validate top 10 genes (Exp02)"
- Exp02: "Test functional role of GENE-X"
- Exp03: "Examine temporal dynamics of pathway activation"
- Exp03: "Test cell cycle inhibitors"

Prioritized Report Future Directions:
```markdown
## Future Directions

### Immediate Priorities

1. **Functional Validation** (addresses Limitation 4):
   Design knockdown/overexpression experiments for top validated genes
   (GENE-X, GENE-Y, GENE-Z) to test causal roles in proliferation, migration,
   and invasion. Expected completion: 6-8 weeks.

2. **Single-Cell Profiling** (addresses Limitation 2):
   Perform scRNA-seq on representative tumor samples to identify cell-type-
   specific expression programs. This will clarify whether cell cycle
   upregulation is tumor-cell-intrinsic or reflects increased proliferative
   cell populations.

### Mechanistic Studies

3. **Temporal Dynamics**:
   Use inducible systems or time-course studies to determine whether gene
   expression changes precede phenotypic alterations (addresses Limitation 1).

4. **Pathway Perturbation**:
   Test cell cycle inhibitors (CDK4/6 inhibitors) in cell line models to
   evaluate therapeutic potential of targeting upregulated pathways.

### Translational Applications

5. **Clinical Validation**:
   Validate gene signature prognostic value in independent clinical cohorts
   (METABRIC, others) to assess biomarker potential.

6. **Therapeutic Target Prioritization**:
   Integrate expression data with druggability databases to identify
   actionable targets among validated genes.

### Long-Term Goals

7. **Comprehensive Characterization**:
   Expand multi-omics integration (genomics, proteomics, metabolomics) to
   build comprehensive model of breast cancer reprogramming.
```

---

### 8. Conclusion

**Source**: Overall synthesis from all findings

**Transformation**: **Final distillation**

**Rules**:
- 1-3 paragraphs maximum
- Reiterate key findings (briefly)
- State main conclusion
- Broader implications
- End with forward-looking statement
- Avoid introducing new information

**Example**:

Report Conclusion:
```markdown
## Conclusion

This integrated study demonstrates widespread transcriptional reprogramming
in breast cancer, with experimental validation confirming computational
predictions. The specific enrichment of cell cycle pathways among upregulated
genes suggests enhanced proliferation as a key feature of tumor progression.

These findings provide a foundation for future mechanistic studies. The
validated gene signature offers candidate biomarkers and potential therapeutic
targets. While current data are correlative, functional studies now in
planning will clarify causal relationships and therapeutic potential.

By combining computational power of large datasets with experimental rigor
of focused validation, this work exemplifies an effective strategy for
biological discovery. The approach and findings inform ongoing efforts to
understand and ultimately combat breast cancer.
```

---

## Transformation Types Explained

### 1. Distillation

**Definition**: Reducing content to essential points only

**Use**: Executive Summary, Conclusion

**Process**:
1. Identify highest-level findings
2. Remove all technical details
3. Compress to minimum viable expression
4. Ensure coherent narrative

### 2. Synthesis

**Definition**: Combining related content into coherent whole

**Use**: Background, Synthesis sections

**Process**:
1. Identify common themes across notebooks
2. Eliminate redundancy
3. Build logical flow
4. Create unified narrative
5. Add connecting statements

### 3. Consolidation

**Definition**: Collecting and merging similar content

**Use**: Methods, Limitations

**Process**:
1. Collect all instances
2. Remove duplicates
3. Group by category
4. Maintain completeness

### 4. Structuring

**Definition**: Organizing content by theme/concept

**Use**: Findings section

**Process**:
1. Extract observations from all notebooks
2. Group by biological theme (not experiment)
3. Create finding units with evidence
4. Maintain fact/interpretation separation

### 5. Abstraction

**Definition**: Moving from specific to general

**Use**: Methods summary

**Process**:
1. Identify common procedure types
2. Describe at high level
3. Omit details available in notebooks
4. Reference notebooks for specifics

### 6. Prioritization

**Definition**: Ordering by importance/urgency

**Use**: Future Directions

**Process**:
1. Collect all proposed next steps
2. Assess importance and feasibility
3. Rank by priority
4. Organize hierarchically

---

## Quality Checks

After mapping, verify:

- [ ] No important information lost
- [ ] Redundancy eliminated
- [ ] Logical flow maintained
- [ ] Facts separated from interpretation
- [ ] Evidence properly cited
- [ ] Notebooks referenced in appendix
- [ ] Consistent terminology throughout
- [ ] No contradictions introduced

---

## Examples of Common Mistakes

### Mistake 1: Verbatim Copying

❌ Bad (copied verbatim from one notebook):
```markdown
### Finding 1
In Exp01, we found 2,453 genes were differentially expressed. We used
DESeq2 with default parameters. The median fold-change was 1.8.
```

✅ Good (synthesized and structured):
```markdown
### Finding 1: Widespread Transcriptional Reprogramming

**Observation**: RNA-seq identified 2,453 differentially expressed genes
(12% of transcriptome).

**Evidence**: Exp01_rnaseq.ipynb; median |log2FC| = 1.8

**Interpretation**: Magnitude indicates substantial cellular reprogramming.
```

### Mistake 2: Not Integrating

❌ Bad (separate findings for related results):
```markdown
### Finding 1: Exp01 found 2,453 DE genes
### Finding 2: Exp02 validated 9 genes
```

✅ Good (integrated narrative):
```markdown
### Finding 1: Validated Transcriptional Changes

**Observation**: RNA-seq identified 2,453 DE genes (Exp01), with 90%
validation rate by qPCR (9/10 genes, Exp02).
```

### Mistake 3: Losing Fact/Interpretation Separation

❌ Bad (mixed levels):
```markdown
**Observation**: Cell cycle pathway is activated, causing increased proliferation.
```

✅ Good (separated):
```markdown
**Observation**: Cell cycle genes showed 2.1-fold enrichment (p=0.008).

**Interpretation**: This suggests enhanced proliferation in tumors.
```

---

## References

These mapping rules ensure:
- Scientific rigor (quality-standards.md)
- Appropriate synthesis vs raw data
- Coherent narrative structure
- Proper attribution to source notebooks
