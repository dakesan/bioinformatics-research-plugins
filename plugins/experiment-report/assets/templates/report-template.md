# Report: [Title]

**Date**: [YYYY-MM-DD]

**Author**: [Name]

**Experiments Covered**: [Exp##, Exp##, ...]

**Project Goal**: [Link to STEERING.md or brief statement of overarching research objective]

---

## Executive Summary

[3-5 sentences: Research question → Approach → Key findings (with numbers) → Implications]

<!-- Quality Gate: Executive Summary
- [ ] Length: 3-5 sentences (no more)
- [ ] Contains quantitative highlight (e.g., "2,453 genes", "90% validation")
- [ ] Self-contained: understandable without reading full report
- [ ] No technical jargon or figure references
- [ ] Covers: question, approach, finding, implication
-->

---

## Background

### Research Context

[Background and motivation for this work]

### Research Question

[The specific question being addressed]

### Hypotheses Tested

| ID | Hypothesis | Source Experiment | Status |
|----|------------|-------------------|--------|
| H1 | [Testable statement] | Exp## | Supported/Rejected/Inconclusive |
| H2 | [Testable statement] | Exp## | Supported/Rejected/Inconclusive |

---

## Methods

### Data Sources

| Dataset | Version/Date | Source | Experiments Used |
|---------|--------------|--------|------------------|
| [Name] | [v1.0 / 2025-01-15] | [URL/path] | Exp##, Exp## |

### Analysis Environment

| Component | Specification |
|-----------|---------------|
| OS | [e.g., macOS 14.0 / Ubuntu 22.04] |
| Python | [e.g., 3.11.5] |
| Key packages | [e.g., pandas 2.0.3, numpy 1.24.0] |
| Random seed | [e.g., 42] |
| Hardware | [e.g., M2 Max, 32GB RAM] |

### Tools and Versions

| Tool | Version | Purpose |
|------|---------|---------|
| [Tool name] | [Version] | [Brief purpose] |

### Procedures

[High-level overview of analysis workflow]

<!-- Quality Gate: Methods
- [ ] All datasets have version/date
- [ ] All tools have versions
- [ ] Environment reproducible (OS, packages, seed)
- [ ] Procedures detailed enough for replication
-->

---

## Findings

<!--
IMPORTANT: Use Claim-Evidence structure for each finding.
Each finding must have:
1. Claim/Theme: What you observed
2. Observation: Factual description (Level 1)
3. Evidence: Specific references to notebooks, figures, statistics
4. Uncertainty: Confidence level and caveats
5. Alternative interpretations: Other possible explanations
-->

### Finding 1: [Theme/Claim Title]

**Claim**: [One sentence stating the main observation]

**Observation** (Level 1 - Facts only):

[Factual description without interpretation]

**Evidence Table**:

| Evidence Type | Location | Value/Description |
|---------------|----------|-------------------|
| Lab Notebook | `../labnote/Exp##_*.ipynb` | [Section reference] |
| Figure | `../results/exp##/fig##_*.png` | [Brief description] |
| Statistic | [Source] | [e.g., p < 0.001, FC = 2.3] |
| Raw Data | `../results/exp##/*.csv` | [Description] |

**Uncertainty & Confidence**:
- Confidence level: [Strong/Moderate/Weak]
- Key caveats: [List limitations specific to this finding]

**Alternative Interpretations**:
- [Alternative explanation 1]
- [Alternative explanation 2]

---

### Finding 2: [Theme/Claim Title]

**Claim**: [One sentence stating the main observation]

**Observation** (Level 1 - Facts only):

[Factual description without interpretation]

**Evidence Table**:

| Evidence Type | Location | Value/Description |
|---------------|----------|-------------------|
| Lab Notebook | `../labnote/Exp##_*.ipynb` | [Section reference] |
| Figure | `../results/exp##/fig##_*.png` | [Brief description] |
| Statistic | [Source] | [Value] |

**Uncertainty & Confidence**:
- Confidence level: [Strong/Moderate/Weak]
- Key caveats: [List limitations]

**Alternative Interpretations**:
- [Alternative explanation]

---

<!-- Add more findings as needed using the same structure -->

<!-- Quality Gate: Findings
- [ ] Each finding has Claim-Evidence structure
- [ ] All evidence paths exist and are correct (verify: ../labnote/, ../results/)
- [ ] Statistics include test type, p-value, effect size
- [ ] Observations are factual (no interpretation)
- [ ] Uncertainty level stated for each finding
- [ ] Alternative interpretations considered
- [ ] Figures numbered and referenced correctly
-->

---

## Synthesis

### Integration of Findings

[How do the findings connect? What story do they tell together?]

**Claim-Evidence Summary**:

| Main Claim | Supporting Findings | Confidence | Key Evidence |
|------------|---------------------|------------|--------------|
| [Integrated claim 1] | F1, F2 | Strong/Moderate/Weak | [Key stats/figures] |
| [Integrated claim 2] | F2, F3 | Strong/Moderate/Weak | [Key stats/figures] |

### Hypothesis Evaluation

| Hypothesis | Verdict | Evidence Summary | Confidence |
|------------|---------|------------------|------------|
| H1: [Statement] | Supported/Rejected/Inconclusive | [Brief evidence] | Strong/Moderate/Weak |
| H2: [Statement] | Supported/Rejected/Inconclusive | [Brief evidence] | Strong/Moderate/Weak |

### Interpretation (Level 2)

[What do these findings mean? Connect to broader biological context]

<!-- Quality Gate: Synthesis
- [ ] Claims clearly separated from facts
- [ ] Each claim links to specific findings
- [ ] Confidence language calibrated (see refinement-guide.md)
- [ ] Alternative explanations discussed
- [ ] Hypotheses evaluated with explicit verdict
- [ ] No unsupported assertions
-->

---

## Limitations

### Methodological Constraints

| Limitation | Impact | Potential Solution |
|------------|--------|-------------------|
| [Specific limitation 1] | [How it affects conclusions] | [How to address] |
| [Specific limitation 2] | [How it affects conclusions] | [How to address] |

### Interpretive Caveats

[Broader constraints on interpretation: correlation vs causation, generalizability, etc.]

<!-- Quality Gate: Limitations
- [ ] Limitations are specific (not generic)
- [ ] Impact on conclusions stated
- [ ] Solutions or mitigations suggested
- [ ] Honest without being apologetic
-->

---

## Future Directions

### Immediate Next Steps

| Priority | Action | Addresses | Expected Outcome |
|----------|--------|-----------|------------------|
| 1 | [Specific experiment/analysis] | [Which limitation/question] | [What we'll learn] |
| 2 | [Specific experiment/analysis] | [Which limitation/question] | [What we'll learn] |

### Long-term Directions

[Broader research directions suggested by this work]

<!-- Quality Gate: Future Directions
- [ ] Next steps are specific and actionable
- [ ] Linked to limitations or open questions
- [ ] Prioritized by importance
- [ ] Expected outcomes stated
-->

---

## Conclusion

[1-3 paragraphs: Restate key findings → Main takeaway → Broader implications → Forward-looking statement]

<!-- Quality Gate: Conclusion
- [ ] Length: 1-3 paragraphs
- [ ] Restates key findings briefly
- [ ] Clear main takeaway message
- [ ] No new information introduced
- [ ] Appropriate confidence level
-->

---

## References

1. [Author et al. (Year). Title. Journal. DOI]

---

## Appendix

### A. Lab Notebooks

| Experiment | Notebook Path | Status | Key Outputs |
|------------|---------------|--------|-------------|
| Exp## | `../labnote/Exp##_*.ipynb` | Complete | [List figures/tables] |

### B. Figure Index

| Figure | Path | Description | Used In |
|--------|------|-------------|---------|
| Fig 1 | `../results/exp##/fig01_*.png` | [Description] | Finding 1 |

### C. Reproducibility Information

**Report Generation** (from project root):
```bash
# Generate report (adjust path to init_report.py as needed)
python path/to/init_report.py --labnote notebook/labnote/Exp*.ipynb --output notebook/report/

# Export to PDF (from notebook/report/ directory)
cd notebook/report/
pandoc Report_*.md -o report.pdf --pdf-engine=typst
```

**Data Availability**:
- Raw data: [Location/repository]
- Processed data: `../results/`
- Code: [Location/repository]

### D. Supplementary Materials

[Links to additional data, code, or documentation]

---

<!--
FINAL QUALITY CHECKLIST (before submission)

Structure:
- [ ] All sections complete
- [ ] Logical flow between sections
- [ ] No redundancy

Evidence:
- [ ] All figure paths verified (exist in ../results/)
- [ ] All notebook paths verified (exist in ../labnote/)
- [ ] All statistics include test, p-value, effect size
- [ ] Evidence tables complete for each finding

Scientific Rigor:
- [ ] Facts (Observations) separated from interpretation (Synthesis)
- [ ] Confidence language calibrated throughout
- [ ] Alternative explanations considered
- [ ] Limitations honestly acknowledged

Writing:
- [ ] Concise and clear
- [ ] Consistent terminology
- [ ] Figures referenced in text
- [ ] References properly formatted

See references/refinement-guide.md for detailed criteria.
-->
