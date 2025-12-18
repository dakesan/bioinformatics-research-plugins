# Report Refinement Guide

## Overview

This guide provides criteria for improving existing reports through iterative refinement. Following the skill-creator pattern, refinement applies AI judgment to improve structure, scientific rigor, and writing quality.

---

## Refinement Dimensions

### 1. Structure & Organization

**Goal**: Logical flow, clear sections, appropriate emphasis

#### Executive Summary

- [ ] **Length**: 3-5 sentences (no more)
- [ ] **Content**: Captures essence of entire report
- [ ] **Structure**: Question → Approach → Findings → Implications
- [ ] **Independence**: Understandable without reading full report
- [ ] **Specificity**: Includes key quantitative findings
- [ ] **No**: Technical details, figure references, citations

**Common issues**:
- Too long (>5 sentences) or too short (<3)
- Too vague ("We found interesting results")
- Too detailed (includes statistics, methods)
- Doesn't capture main message

**Example refinement**:

❌ Before:
```markdown
## Executive Summary

We did RNA-seq analysis. We found many genes were different. Cell cycle
genes were enriched. We validated some genes. This is important for cancer.
More research is needed.
```

✅ After:
```markdown
## Executive Summary

We investigated transcriptional reprogramming in breast cancer using
integrated computational and experimental approaches. RNA-seq analysis of
TCGA data revealed 2,453 differentially expressed genes with significant
enrichment in cell cycle pathways (p < 0.01). Experimental validation
confirmed 90% of tested candidates, providing high-confidence biomarker
candidates for functional characterization.
```

#### Background

- [ ] **Research question**: Clearly stated upfront
- [ ] **Context**: Provides necessary background without literature review
- [ ] **Rationale**: Explains why this study matters
- [ ] **Scope**: Sets expectations for what follows
- [ ] **Length**: 2-4 paragraphs (not excessive)

**Common issues**:
- Missing research question
- Too much background (turns into review)
- Too little background (assumes expert knowledge)
- Doesn't explain why study was done

#### Methods

- [ ] **Appropriate detail**: High-level overview, not step-by-step
- [ ] **Organized**: Grouped by category (data, tools, procedures)
- [ ] **Accessible**: Non-experts can understand approach
- [ ] **Referenced**: Points to notebooks for full details
- [ ] **Complete**: All major analyses mentioned

**Common issues**:
- Too detailed (duplicates notebooks)
- Too vague ("standard methods")
- Missing key information (sample sizes, versions)
- Not organized logically

#### Findings

- [ ] **Organized by theme**: Not by experiment order
- [ ] **Consistent structure**: Each finding has observation + evidence + brief interpretation
- [ ] **Fact/interpretation separation**: Observations are factual
- [ ] **Evidence cited**: References to notebooks and figures
- [ ] **Complete**: All major results included

**Common issues**:
- Organized chronologically instead of thematically
- Mixed facts and interpretation
- Missing evidence citations
- Incomplete (cherry-picked results)

#### Synthesis

- [ ] **Integration**: Connects findings across experiments
- [ ] **Coherent narrative**: Tells a story
- [ ] **Evidence-based**: Every claim supported
- [ ] **Alternatives considered**: Acknowledges other explanations
- [ ] **Appropriate uncertainty**: Calibrated confidence language

**Common issues**:
- Just concatenates individual interpretations
- Overreaches beyond data
- Ignores alternative explanations
- Too certain or too hedged

#### Limitations

- [ ] **Honest**: Acknowledges real constraints
- [ ] **Specific**: Concrete limitations, not generic
- [ ] **Constructive**: Suggests how to address when possible
- [ ] **Prioritized**: Most important limitations first
- [ ] **Balanced**: Not overly apologetic

**Common issues**:
- Generic ("small sample size" without numbers)
- Missing obvious limitations
- Too apologetic (undermines findings)
- Too defensive (dismisses valid concerns)

#### Future Directions

- [ ] **Specific**: Concrete next experiments
- [ ] **Prioritized**: Ordered by importance
- [ ] **Justified**: Explains why each is needed
- [ ] **Feasible**: Realistic proposals
- [ ] **Connected**: Links to limitations and findings

**Common issues**:
- Vague ("more research needed")
- Unconnected list
- Unrealistic proposals
- Missing direct follow-ups

#### Conclusion

- [ ] **Concise**: 1-3 paragraphs
- [ ] **Recapitulates**: Briefly restates key findings
- [ ] **Synthesizes**: Main take-home message
- [ ] **Forward-looking**: Ends with implications/future
- [ ] **No new info**: Doesn't introduce new findings

**Common issues**:
- Too long or too short
- Just repeats abstract
- Introduces new information
- Ends abruptly without synthesis

---

### 2. Scientific Rigor

**Goal**: Maintain fact/interpretation separation, evidence-based claims, appropriate confidence

#### Fact vs Interpretation Separation

**Critical principle**: Observations (Level 1) must be separate from interpretation (Level 2) and conclusions (Level 3).

✅ Good separation:
```markdown
**Observation**: Gene X expression was 3.2-fold higher in tumors (adj. p < 0.001).

**Interpretation**: This suggests Gene X may contribute to tumor progression,
consistent with its known role in cell cycle regulation (Smith 2024).
```

❌ Poor separation:
```markdown
Gene X was upregulated, proving it drives tumor growth.
```

**Checklist**:
- [ ] Findings section contains primarily Level 1 statements
- [ ] Synthesis section contains Level 2 statements with reasoning
- [ ] Conclusion section contains Level 3 statements with caveats
- [ ] No causal language from correlational data
- [ ] Speculation is clearly labeled

#### Evidence-Based Claims

Every assertion must have supporting evidence.

✅ Good:
```markdown
Cell cycle pathway showed significant enrichment (hypergeometric p = 0.008,
2.1-fold, 45 genes; Exp03_pathway.ipynb).
```

❌ Bad:
```markdown
The cell cycle pathway is clearly activated.
```

**Checklist**:
- [ ] Every claim references specific evidence
- [ ] Evidence includes statistics where appropriate
- [ ] Source notebook cited
- [ ] Figure/table numbers provided
- [ ] No unsupported assertions

#### Appropriate Uncertainty

Use calibrated confidence language based on evidence strength.

| Evidence Strength | Language |
|------------------|----------|
| Very strong (multiple independent lines) | "demonstrate", "show", "establish" |
| Strong (reproducible, validated) | "indicate", "suggest strongly" |
| Moderate (single line, correlative) | "suggest", "consistent with" |
| Weak (preliminary, small sample) | "may", "could", "possible" |
| Speculative (hypothesis) | "we hypothesize", "one possibility" |

✅ Good calibration:
```markdown
The 90% validation rate (9/10 genes) strongly indicates these changes are
biologically relevant. However, the mechanism by which Gene X contributes
to proliferation remains unclear and will require functional studies to
determine.
```

❌ Poor calibration (too strong):
```markdown
We have proven that Gene X drives cancer through cell cycle activation.
```

❌ Poor calibration (too weak):
```markdown
Our data might possibly suggest that genes could be somewhat related to
cancer, though we cannot be certain.
```

**Checklist**:
- [ ] Confidence language matches evidence strength
- [ ] Strong claims have strong evidence
- [ ] Weak evidence presented cautiously
- [ ] Speculation clearly labeled
- [ ] Limitations acknowledged

#### Alternative Explanations

Good science considers alternative interpretations.

✅ Good:
```markdown
While the enrichment of cell cycle genes suggests enhanced proliferation,
alternative explanations include: (1) increased proportion of proliferating
cells rather than per-cell change, (2) compensation for increased apoptosis,
or (3) technical artifact from cell cycle phase imbalance in samples.
Single-cell profiling would distinguish these possibilities.
```

❌ Bad:
```markdown
The results clearly show enhanced proliferation with no other explanation.
```

**Checklist**:
- [ ] Major findings discuss alternatives
- [ ] Implausible alternatives dismissed with reasoning
- [ ] Plausible alternatives acknowledged
- [ ] Distinguishing experiments proposed
- [ ] Not dismissive of contradictory evidence

---

### 3. Writing Quality

**Goal**: Clear, concise, professional scientific communication

#### Clarity

**Checklist**:
- [ ] Sentences are clear and unambiguous
- [ ] Technical terms defined on first use
- [ ] Acronyms spelled out on first use
- [ ] Logical flow between paragraphs
- [ ] Transitions between sections smooth
- [ ] No jargon without necessity

**Common issues**:
- Undefined abbreviations
- Overly complex sentences
- Unclear antecedents ("this", "it", "they")
- Missing context

**Example refinement**:

❌ Before:
```markdown
They were significant. This suggests it is important.
```

✅ After:
```markdown
The 2,453 differentially expressed genes showed significant changes
(adj. p < 0.05). This widespread dysregulation suggests transcriptional
reprogramming plays an important role in tumor biology.
```

#### Conciseness

**Principle**: Communicate efficiently without losing meaning

**Checklist**:
- [ ] No unnecessary words
- [ ] No redundant statements
- [ ] Active voice used when clearer
- [ ] Nominalizations avoided ("utilize" → "use")
- [ ] Gets to the point

**Common verbosity patterns**:

| Verbose | Concise |
|---------|---------|
| "In order to" | "To" |
| "Due to the fact that" | "Because" |
| "It is important to note that" | [Delete] |
| "A number of" | "Several" or "Many" |
| "Serves the function of" | "Functions as" or "is" |

**Example refinement**:

❌ Before (47 words):
```markdown
It is important to note that the results that we obtained in the course
of our experiments clearly demonstrate beyond any reasonable doubt that
there is a significant difference in the expression levels of the genes
that we examined.
```

✅ After (13 words):
```markdown
Our experiments demonstrate significant differential expression of the
examined genes.
```

#### Terminology

**Checklist**:
- [ ] Consistent terms throughout (don't switch between synonyms)
- [ ] Standard field terminology used
- [ ] Technical terms used correctly
- [ ] Appropriate formality level
- [ ] Undefined neologisms avoided

**Common issues**:
- Switching between "tumor" and "cancer" and "neoplasm"
- Mixing "upregulated", "increased", "higher" inconsistently
- Inventing terms unnecessarily

**Example**:

❌ Inconsistent:
```markdown
Tumors showed higher expression. In cancers, we observed upregulation.
Neoplastic tissue had increased levels.
```

✅ Consistent:
```markdown
Tumors showed increased expression. In tumor tissue, we observed
upregulation. Tumor samples had higher levels.
```

#### Figures & References

**Checklist**:
- [ ] All figures/tables mentioned in text
- [ ] References use consistent format (e.g., "Figure 1", not "Fig. 1" then "Figure 2")
- [ ] Figure/table numbering sequential
- [ ] No broken references
- [ ] Citations properly formatted

**Common issues**:
- Figures created but never mentioned
- Inconsistent reference format
- Wrong figure numbers
- Missing figure captions in notebooks

---

## Refinement Process

### Step 1: Initial Assessment

Read entire report and identify:
1. **Major structural issues**: Missing sections, poor organization
2. **Scientific rigor issues**: Unsupported claims, poor fact/interpretation separation
3. **Writing issues**: Unclear passages, verbosity, inconsistencies

### Step 2: Prioritize Improvements

Categorize issues by severity:
- **Critical**: Scientific errors, unsupported claims, major structural flaws
- **Important**: Poor organization, unclear writing, missing evidence
- **Minor**: Stylistic improvements, minor inconsistencies

### Step 3: Implement Changes

Work through priorities:

1. **Critical fixes first**:
   - Correct scientific errors
   - Add missing evidence
   - Fix fact/interpretation mixing

2. **Important improvements**:
   - Reorganize for better flow
   - Clarify unclear passages
   - Add missing context

3. **Minor polishing**:
   - Improve conciseness
   - Enhance consistency
   - Fine-tune language

### Step 4: Verify Quality

Final checks:
- [ ] All sections present and appropriate length
- [ ] Executive summary stands alone
- [ ] Facts separated from interpretation
- [ ] All claims have evidence
- [ ] Confidence language calibrated
- [ ] Consistent terminology
- [ ] Clear and concise writing
- [ ] Figures/tables referenced correctly

---

## Common Refinement Patterns

### Pattern 1: Tighten Executive Summary

**Before** (too long, too detailed):
```markdown
We performed RNA-seq on TCGA-BRCA samples using DESeq2 normalization.
We found 2,453 genes that were differentially expressed with an adjusted
p-value less than 0.05 using the Benjamini-Hochberg method. Many of these
genes were in the cell cycle pathway based on pathway enrichment analysis
using hypergeometric testing. We also did qPCR validation on 10 genes and
9 of them validated. This is interesting for cancer research and more work
should be done.
```

**After** (concise, high-level):
```markdown
We investigated transcriptional reprogramming in breast cancer through
integrated computational and experimental analysis. RNA-seq revealed 2,453
differentially expressed genes with cell cycle pathway enrichment (p<0.01).
Experimental validation confirmed 90% of tested genes, providing high-
confidence candidates for mechanistic studies.
```

**Changes**:
- Removed methods details → high-level approach
- Removed statistics → key quantitative findings
- Shortened from 7 sentences → 3 sentences
- Added implications

### Pattern 2: Separate Facts from Interpretation

**Before** (mixed):
```markdown
### Finding 1
Gene X was upregulated 3-fold, indicating it drives tumor growth and causes
increased proliferation through cell cycle activation.
```

**After** (separated):
```markdown
### Finding 1: Gene X Upregulation

**Observation**: Gene X showed 3.2-fold increased expression in tumors
compared to normal tissue (adj. p < 0.001, n=1,100; Exp01).

**Evidence**: Lab notebook Exp01_rnaseq.ipynb, Figure 2A

**Interpretation**: The upregulation suggests Gene X may contribute to
tumor progression. Given Gene X's known role in cell cycle regulation
(Smith 2024), increased expression could enhance proliferation. However,
correlation does not establish causation; functional perturbation
experiments are needed to confirm a causal role.
```

**Changes**:
- Split into Observation (facts) and Interpretation (reasoning)
- Added evidence citation
- Changed "drives" and "causes" to "may contribute" and "could enhance"
- Acknowledged causation requires additional testing

### Pattern 3: Add Missing Evidence

**Before** (unsupported):
```markdown
The cell cycle pathway is clearly activated in tumors, leading to
enhanced proliferation.
```

**After** (evidence-based):
```markdown
Cell cycle genes showed 2.1-fold enrichment among upregulated transcripts
(hypergeometric p = 0.008, 45 genes; Exp03_pathway.ipynb, Table 1). This
over-representation is consistent with enhanced proliferation, a known
hallmark of cancer (Hanahan & Weinberg 2011).
```

**Changes**:
- Added specific statistics
- Cited source notebook and table
- Changed "clearly activated" to "over-representation consistent with"
- Added literature support

### Pattern 4: Restructure Findings by Theme

**Before** (chronological):
```markdown
### Finding 1: Exp01 Results
[RNA-seq results]

### Finding 2: Exp02 Results
[qPCR validation]

### Finding 3: Exp03 Results
[Pathway analysis]
```

**After** (thematic):
```markdown
### Finding 1: Widespread Transcriptional Changes
[RNA-seq showing 2,453 genes]

### Finding 2: Experimental Validation Confirms Predictions
[qPCR confirming RNA-seq, 90% validation rate]

### Finding 3: Cell Cycle Pathway Dysregulation
[Pathway enrichment from Exp03, supported by Exp01/02]
```

**Changes**:
- Organized by biological theme, not experiment order
- Descriptive titles capturing main message
- Cross-referenced experiments where relevant

### Pattern 5: Calibrate Confidence Language

**Before** (overconfident):
```markdown
We have proven that Gene X drives cancer progression through cell cycle
activation, establishing it as a therapeutic target.
```

**After** (appropriately calibrated):
```markdown
The consistent upregulation of Gene X (RNA-seq and qPCR validation)
combined with its known cell cycle role suggests it may contribute to
tumor progression. Functional studies are needed to establish causation
and evaluate therapeutic potential.
```

**Changes**:
- "proven" → "suggests"
- "drives" → "contribute to"
- "establishing" → "evaluate"
- Added caveat about need for functional studies

---

## Refinement Checklist

### Structure ✓
- [ ] Executive Summary: 3-5 sentences, captures essence
- [ ] Background: Question clearly stated, appropriate context
- [ ] Methods: High-level, organized, referenced
- [ ] Findings: Thematic organization, consistent structure
- [ ] Synthesis: Integrated narrative, evidence-based
- [ ] Limitations: Specific, honest, constructive
- [ ] Future Directions: Prioritized, specific, justified
- [ ] Conclusion: Concise, synthesized, forward-looking

### Scientific Rigor ✓
- [ ] Facts separated from interpretation
- [ ] All claims have supporting evidence
- [ ] Confidence language calibrated to evidence
- [ ] Alternative explanations considered
- [ ] Limitations acknowledged appropriately
- [ ] Causation vs correlation clearly distinguished
- [ ] Statistics reported properly

### Writing Quality ✓
- [ ] Clear and unambiguous
- [ ] Concise without losing meaning
- [ ] Consistent terminology
- [ ] Technical terms defined
- [ ] Logical flow and transitions
- [ ] Figures/tables properly referenced
- [ ] Professional tone

---

## Self-Review Questions

Before finalizing refinement, ask:

1. **Would a colleague understand this without asking questions?**
2. **Are any claims unsupported by evidence?**
3. **Am I conflating correlation with causation anywhere?**
4. **Is the executive summary truly self-contained?**
5. **Have I acknowledged all major limitations?**
6. **Is my confidence language appropriate throughout?**
7. **Could any section be more concise without losing meaning?**
8. **Are alternative explanations considered fairly?**
9. **Does the report tell a coherent story?**
10. **Would I be proud to share this with experts in the field?**

If any answer is "no" or "maybe", refinement is incomplete.

---

## Examples from Literature

### Example: Well-Written Report Section

> **Finding 2: Experimental Validation of Computational Predictions**
>
> **Observation**: Quantitative PCR confirmed differential expression for
> 9 of 10 candidate genes selected from RNA-seq analysis (Figure 2A). The
> correlation between RNA-seq and qPCR fold-changes was strong (Pearson
> r = 0.92, 95% CI: 0.74-0.98, p < 0.001, n=10 genes; Figure 2B).
>
> **Evidence**: Lab notebook Exp02_qpcr-validation.md; raw qPCR data in
> results/exp02/; primer sequences in Supplementary Table 1.
>
> **Interpretation**: The high validation rate (90%) and strong correlation
> indicate that RNA-seq accurately captured biological changes in gene
> expression. This concordance between platforms strengthens confidence
> in computationally identified candidates and demonstrates technical
> robustness of the RNA-seq findings. The single non-validated gene (GENE-Z)
> may reflect biological variability, primer design issues, or false positive
> in RNA-seq; follow-up with alternative primers is planned.

**Why it's good**:
- Clear fact/interpretation separation
- Specific statistics with confidence intervals
- Evidence fully cited
- Considers negative result (non-validated gene)
- Appropriate confidence ("indicate", "may reflect")
- Proposes follow-up

---

## Resources

For deeper guidance:
- `quality-standards.md` (research-project): Fact/interpretation/conclusion levels
- `best-practices.md` (research-project): Scientific writing principles
- `mapping-rules.md` (this plugin): How content should be synthesized
