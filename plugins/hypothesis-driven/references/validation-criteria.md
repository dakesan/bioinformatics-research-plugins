# Hypothesis Validation Criteria

## Overview

This document provides detailed criteria for evaluating and refining scientific hypotheses. Strong hypotheses are testable, specific, quantitative, and falsifiable.

---

## Core Criteria

### 1. Testability

**Definition**: Can the hypothesis be evaluated with practical experiments using available methods?

**Questions to ask**:
- What experiment would test this?
- What measurements would be taken?
- Are the methods available?
- Is the experiment feasible?

**Levels**:

**Level 0 - Untestable**:
- Cannot be evaluated with any conceivable experiment
- Example: "Gene X has a spiritual essence"

**Level 1 - Theoretically testable, practically difficult**:
- Requires method development or rare resources
- Example: "Gene X affects lifespan in humans" (would require decades)

**Level 2 - Testable with standard methods**:
- Can be tested with established approaches
- Example: "Gene X knockout reduces cell proliferation" (standard assay)

**Level 3 - Easily testable**:
- Methods readily available, data may already exist
- Example: "Gene X expression correlates with survival in TCGA data" (public data)

**Common untestable patterns**:
❌ "Gene X is important" - too vague to test
❌ "The universe tends toward complexity" - unfalsifiable
❌ "This is the best approach" - subjective

---

### 2. Specificity

**Definition**: Are variables, relationships, and conditions clearly defined without ambiguity?

**Questions to ask**:
- What exactly is being measured?
- What are the exact conditions?
- What counts as a positive result?
- Could two people interpret this differently?

**Levels**:

**Level 0 - Extremely vague**:
- Multiple interpretations possible
- Example: "Things change under stress"

**Level 1 - Somewhat specific**:
- Main variables defined but conditions unclear
- Example: "Gene X affects cell growth" - which cells? how measured? what constitutes "affects"?

**Level 2 - Specific with minor gaps**:
- Most details defined, small ambiguities remain
- Example: "Gene X increases cell proliferation" - by how much? in what cells?

**Level 3 - Completely specific**:
- All variables, conditions, and criteria clearly defined
- Example: "Gene X knockout reduces proliferation by >30% in HeLa cells measured by MTT assay at 72h"

**Specificity checklist**:
- [ ] Variables clearly defined
- [ ] Conditions specified (cell type, time, concentration, etc.)
- [ ] Measurement method stated
- [ ] Success criteria明确

**Vague terms to avoid**:
- "Important", "significant" (statistically or biologically?)
- "Affects", "influences" (direction? magnitude?)
- "Changes", "alters" (increases? decreases?)
- "Related to", "involved in" (how?)

---

### 3. Quantitativeness

**Definition**: Does the hypothesis include measurable, quantitative predictions?

**Questions to ask**:
- What is the expected magnitude?
- What threshold defines success?
- What statistics will be used?
- What confidence level is required?

**Levels**:

**Level 0 - No quantitative prediction**:
- Purely qualitative
- Example: "Gene X is expressed"

**Level 1 - Qualitative comparison**:
- Direction specified but no magnitude
- Example: "Gene X is higher in cancer than normal"

**Level 2 - Approximate magnitude**:
- Rough effect size specified
- Example: "Gene X is >2-fold higher in cancer" or "correlation r > 0.5"

**Level 3 - Specific prediction with confidence**:
- Precise effect size, statistics, and confidence
- Example: "Gene X is 3-5 fold higher in cancer (adjusted p < 0.01, n=100 per group)"

**Adding quantitativeness**:

Before: "Treatment improves survival"
After: "Treatment improves median survival by ≥3 months (HR < 0.7, p < 0.05, 80% power)"

Before: "Genes are differentially expressed"
After: "≥200 genes will show >2-fold change (adjusted p < 0.05) between conditions"

**Appropriate quantitative elements**:
- Fold-changes (1.5×, 2×, 10×)
- Percentages (30% reduction, 50% increase)
- Absolute values (3-month improvement, 10 mmHg decrease)
- Statistical thresholds (p < 0.05, FDR < 0.1)
- Effect sizes (Cohen's d > 0.8, HR > 2.0)
- Sample size and power (n=50 per group, 80% power)

---

### 4. Falsifiability

**Definition**: Can the hypothesis be proven wrong? What result would reject it?

**Questions to ask**:
- What result would disprove this hypothesis?
- Can you define failure criteria?
- Is it possible to be wrong?
- Are we protected from confirmation bias?

**Levels**:

**Level 0 - Unfalsifiable**:
- No conceivable result could disprove it
- Example: "Gene X might have some function" - always possibly true

**Level 1 - Very difficult to falsify**:
- Only extreme results would disprove
- Example: "Gene X affects some aspect of biology" - nearly unfalsifiable

**Level 2 - Falsifiable with enough data**:
- Clear failure criteria but may require extensive testing
- Example: "Gene X is involved in pathway Y" - testable but complex

**Level 3 - Clearly falsifiable**:
- Single experiment could definitively reject
- Example: "Gene X knockout is embryonic lethal in mice" - try knockout, see if embryos die

**Falsifiability test**:

Good hypothesis: "Drug X reduces tumor size by >50% in mouse model"
- Falsified by: Tumor size reduction <50% or no effect

Good hypothesis: "Gene X expression correlates with survival (HR > 2, p < 0.05)"
- Falsified by: No correlation or HR < 2 or p ≥ 0.05

Bad hypothesis: "Gene X is biologically relevant"
- Cannot be falsified: Even if no function found, might be "relevant" in untested context

**Red flags for unfalsifiability**:
- Hedge words: "might", "could", "possibly"
- Vague terms: "relevant", "important", "interesting"
- No failure criteria defined
- Success redefined after seeing results (HARKing)

---

## Hypothesis Quality Scoring

### Scoring System

Evaluate each criterion (1-4 above) on 0-3 scale, total possible = 12.

| Total Score | Quality | Action |
|-------------|---------|--------|
| 10-12 | Excellent | Ready for testing |
| 7-9 | Good | Minor refinement recommended |
| 4-6 | Weak | Major refinement needed |
| 0-3 | Poor | Complete reformulation required |

### Scoring Examples

**Example 1**: "Gene X affects cancer"
- Testability: 1 (vague, but could design tests)
- Specificity: 0 (which gene function? which cancer? how measured?)
- Quantitativeness: 0 (no prediction)
- Falsifiability: 0 (too vague to falsify)
- **Total: 1/12 (Poor)**

Refined: "Knockout of Gene X reduces proliferation by >30% in MDA-MB-231 breast cancer cells at 72h"
- Testability: 3 (standard assay)
- Specificity: 3 (all variables defined)
- Quantitativeness: 2 (threshold defined, no statistics)
- Falsifiability: 3 (clear failure: <30% reduction)
- **Total: 11/12 (Excellent)**

**Example 2**: "There will be gene expression differences"
- Testability: 3 (easy to test)
- Specificity: 1 (what genes? what conditions?)
- Quantitativeness: 0 (no magnitude)
- Falsifiability: 0 (trivially true)
- **Total: 4/12 (Weak)**

Refined: "≥200 genes will be differentially expressed >2-fold (adjusted p < 0.05) in breast tumors vs normal tissue"
- Testability: 3 (standard RNA-seq)
- Specificity: 3 (all defined)
- Quantitativeness: 3 (count, fold-change, p-value)
- Falsifiability: 3 (clear failure: <200 genes)
- **Total: 12/12 (Excellent)**

---

## Common Problems and Solutions

### Problem 1: Too Vague

**Pattern**: Undefined terms and relationships

**Examples**:
❌ "Gene X is related to disease Y"
❌ "Pathway Z is involved"
❌ "Factor A affects outcome B"

**Solution**: Define specific variables and relationships

✅ "Gene X expression (measured by qPCR) correlates with disease Y severity (measured by clinical scale) with r > 0.5, p < 0.05"
✅ "Knockdown of pathway Z components reduces phenotype by >50%"
✅ "Factor A concentration >10 μM increases outcome B by 2-fold within 24h"

### Problem 2: Unfalsifiable

**Pattern**: No conceivable negative result

**Examples**:
❌ "Gene X might be relevant"
❌ "This could be important for biology"
❌ "Further investigation may reveal insights"

**Solution**: Define specific failure criteria

✅ "If Gene X knockout shows <10% phenotypic change, it is not essential for this process"
✅ "If correlation is r < 0.3 or p > 0.05, Gene X does not predict outcome"

### Problem 3: Not Testable

**Pattern**: Cannot be evaluated experimentally

**Examples**:
❌ "The optimal evolutionary strategy was employed"
❌ "Nature intends for this pathway to regulate X"
❌ "This is the best possible design"

**Solution**: Reformulate as testable prediction

✅ "This strategy provides fitness advantage >20% in simulated evolution"
✅ "Pathway mutations reduce fitness by >30% in selective environment"
✅ "Alternative designs X, Y, Z perform worse by metrics A, B, C"

### Problem 4: No Quantitative Prediction

**Pattern**: Only qualitative statements

**Examples**:
❌ "Treatment improves outcome"
❌ "Gene expression changes"
❌ "Survival is better"

**Solution**: Add magnitude and statistics

✅ "Treatment improves outcome by ≥30% (p < 0.05)"
✅ "Gene expression increases >2-fold (adjusted p < 0.01)"
✅ "Median survival improves by ≥6 months (HR < 0.6, p < 0.01)"

### Problem 5: Correlation Stated as Causation

**Pattern**: Observational claims presented as causal

**Examples**:
❌ "Gene X causes disease Y" (based on correlation)
❌ "Factor A drives outcome B" (no intervention)
❌ "Pathway Z controls phenotype P" (association study)

**Solution**: State correlational hypotheses accurately, propose causal test

✅ Correlational: "Gene X expression correlates with disease Y severity (r > 0.5)"
✅ Causal test: "Knockdown of Gene X will reduce disease phenotype by >30%, confirming causal role"

### Problem 6: Post-Hoc Hypothesizing (HARKing)

**Pattern**: Hypothesis created after seeing results

**Examples**:
❌ Claiming to have predicted unexpected finding
❌ Adjusting hypothesis to match observed results
❌ Selectively reporting hypotheses that succeeded

**Solution**: Clearly label exploratory vs confirmatory

✅ "Exploratory analysis revealed unexpected correlation. We hypothesize this reflects [mechanism] and will test this in Exp05"
✅ "Initial hypothesis not supported (Exp03). Refined hypothesis based on observations: [new hypothesis]"

---

## Good vs Bad Examples

### Topic: Gene Expression and Cancer

#### Bad Hypothesis Series

1. "Gene X is important for cancer"
   - Vague, not testable, no prediction

2. "Gene X is differentially expressed"
   - Trivial, no magnitude, not falsifiable

3. "Gene X might affect tumor growth"
   - Hedged, vague mechanism, no prediction

4. "Gene X probably regulates cancer through some pathway"
   - Multiple vague terms, not specific

#### Good Hypothesis Series

1. **Correlational**: "Gene X expression is ≥3-fold higher in breast tumors vs normal tissue (adjusted p < 0.01, n≥100 per group, TCGA data)"
   - Testable, specific, quantitative, falsifiable

2. **Mechanistic**: "High Gene X expression (top quartile) correlates with poor survival (HR > 2.0, p < 0.05) through enhanced metastatic signaling (enrichment of EMT genes, p < 0.01)"
   - Specific mechanism, quantitative thresholds, testable prediction

3. **Causal**: "Knockdown of Gene X by ≥70% (validated by qPCR) will reduce tumor cell migration by >50% in transwell assay (p < 0.05, n=3 replicates)"
   - Intervention defined, quantitative outcome, clear success criteria

4. **Translational**: "Pharmacological inhibition of Gene X with compound Y will reduce tumor growth by ≥40% in xenograft model (p < 0.05, vehicle control, n≥8 mice per group)"
   - Specific intervention, quantitative endpoint, proper controls

### Topic: Computational Prediction

#### Bad Hypotheses

1. "Machine learning can predict disease"
   - No algorithm specified, no performance threshold

2. "A model will classify patients"
   - Trivial (any model classifies), no accuracy requirement

3. "Better predictions are possible"
   - Vague, no comparison, no metrics

#### Good Hypotheses

1. "Random forest classifier trained on Gene X, Y, Z expression will predict disease with AUC > 0.80 (95% CI: 0.75-0.85) in held-out test set (n=200)"
   - Specific algorithm, quantitative performance, validation strategy

2. "Adding clinical variables to gene expression model will improve AUC by ≥0.05 compared to genes-only model (DeLong test p < 0.05)"
   - Clear comparison, quantitative improvement, statistical test

3. "Model trained on cohort A will validate with AUC > 0.75 in independent cohort B, demonstrating generalizability across institutions"
   - External validation, performance threshold, specificity

---

## Hypothesis Development Process

### Step 1: Initial Observation

Record factual observation without interpretation.

Example: "In Exp03, observed 2,453 differentially expressed genes between tumor and normal"

### Step 2: Exploratory Hypothesis

Formulate initial explanation (can be vague at this stage).

Example: "Gene expression changes may indicate altered pathway activity in tumors"

### Step 3: Refinement

Apply validation criteria to improve hypothesis.

Questions:
- Testable? "Yes, can test pathway activity"
- Specific? "No - which pathways?"
- Quantitative? "No - how much change?"
- Falsifiable? "No - too vague"

Refined: "Cell cycle pathway genes are enriched among upregulated genes (p < 0.01, hypergeometric test), indicating enhanced proliferation in tumors"

### Step 4: Design Verification

Plan experiment to test refined hypothesis.

```markdown
## Verification Strategy

**Hypothesis**: Cell cycle genes enriched in upregulated genes

**Test**: Pathway enrichment analysis (hypergeometric test)
- Null: No enrichment (p ≥ 0.05)
- Alternative: Significant enrichment (p < 0.01)

**Expected result if true**: Cell cycle pathway p < 0.01, enrichment >2-fold
**Expected result if false**: Cell cycle pathway p ≥ 0.05 or enrichment <1.5

**Follow-up if supported**: Test cell proliferation markers (Ki-67, PCNA)
**Follow-up if rejected**: Test alternative pathways (apoptosis, differentiation)
```

### Step 5: Iteration

After testing, refine hypothesis based on results.

- If supported: Make more specific predictions
- If rejected: Formulate alternative hypotheses
- If inconclusive: Improve experimental design

---

## Red Flags

### Indicators of Poor Hypotheses

1. **Hedging language**:
   - "might", "could", "possibly", "perhaps"
   - Suggests hypothesis not well-formed

2. **Circular reasoning**:
   - "Gene X is upregulated because it's important, and it's important because it's upregulated"

3. **Unfalsifiable by design**:
   - "Gene X plays a role in some biological process"
   - Can always find some context where it's true

4. **Lack of specificity**:
   - "Further research may reveal insights"
   - Not actually a hypothesis

5. **Post-hoc justification**:
   - Hypothesis perfectly matches observed data
   - Suspiciously accommodates all findings

6. **No quantitative prediction**:
   - "Will be different" vs "Will be >2-fold higher"

7. **Confirmation bias indicators**:
   - Only hypotheses that confirm expectations
   - No consideration of alternatives

### Warning Signs in Refinement

**If you find yourself**:
- Adding caveats to make hypothesis unfalsifiable
- Removing quantitative predictions to avoid being wrong
- Making hypothesis so broad it's trivially true
- Designing "test" that can't disprove hypothesis

**Then you are**:
- Moving away from good hypothesis
- Engaging in motivated reasoning
- Protecting ego over seeking truth

**Instead**:
- Make bold, specific, testable predictions
- Define clear failure criteria
- Accept that good hypotheses risk being wrong
- Learn more from rejected hypotheses than confirmed ones

---

## Checklist for Hypothesis Quality

Before finalizing a hypothesis, check:

### Testability
- [ ] Can be tested with available methods
- [ ] Experiment design is clear
- [ ] Measurements are defined
- [ ] Feasible to perform

### Specificity
- [ ] All variables defined
- [ ] Conditions specified (cell type, time, dose, etc.)
- [ ] Measurement method stated
- [ ] No ambiguous terms

### Quantitativeness
- [ ] Expected magnitude stated
- [ ] Threshold for success defined
- [ ] Statistical criteria specified
- [ ] Sample size considered

### Falsifiability
- [ ] Failure criteria clearly stated
- [ ] Results that would disprove hypothesis identified
- [ ] Not trivially true
- [ ] Not protected by hedge words

### Scientific Rigor
- [ ] Based on observations/evidence
- [ ] Alternative explanations considered
- [ ] Simplest explanation (parsimony)
- [ ] Appropriate scope (not overgeneralized)

---

## References

These criteria are derived from:
- Scientific method fundamentals
- Hypothesis testing in statistics
- Best practices in experimental design
- Reproducibility and rigor standards
