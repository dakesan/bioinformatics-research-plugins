---
name: experiment-report
description: This skill should be used when generating integrated reports from lab notebooks or improving existing reports. Triggered by requests like "generate report", "create summary", "refine report", "improve report", or "レポートを作成". Handles both initial generation (mechanical) and iterative refinement (AI-guided).
---

# Experiment Report Management

## Overview

Provides comprehensive report generation and refinement capabilities. Following the skill-creator pattern, this plugin handles both:
1. **Init (Generation)**: Mechanical extraction and templating from lab notebooks
2. **Refine (Improvement)**: AI-guided improvement for scientific rigor and clarity

## Core Capabilities

### 1. Report Generation

Create integrated reports from completed lab notebooks using `scripts/init_report.py`.

**When to use**: When ready to synthesize multiple experiments into a cohesive report.

**Workflow**:
1. Identify completed lab notebooks to include
2. Run init script: `python scripts/init_report.py --labnote [paths] --output notebook/report/`
3. Script extracts content using `references/mapping-rules.md`
4. Generates report template with placeholder sections
5. AI fills in synthesis and analysis sections
6. Output: `notebook/report/Report_[title].md`

**Mapping rules** (from lab notebooks to report):

| Lab Notebook Section | Report Section | Transformation |
|---------------------|----------------|----------------|
| Hypothesis + Background | Background | Synthesize context |
| Materials & Methods | Methods Summary | Consolidate procedures |
| Results (observations) | Findings | Structure by theme |
| Discussion (interpretation) | Synthesis | Integrate interpretations |
| Limitations | Limitations | Consolidate caveats |
| Next Steps | Future Directions | Prioritize follow-ups |
| Key conclusion | Executive Summary | Distill to 3-5 sentences |

**Command**: `/research-report`

### 2. Report Refinement

Improve existing reports using `references/refinement-guide.md` criteria.

**When to use**: After initial report generation or when report needs improvement.

**Workflow**:
1. User specifies existing report to refine
2. Read current report content
3. Evaluate against refinement criteria:
   - **Structure**: Logical flow, clear sections
   - **Scientific rigor**: Fact/interpretation separation, evidence-based claims
   - **Clarity**: Concise writing, proper terminology
4. Provide specific improvement suggestions
5. Implement improvements (with user approval)

**Refinement dimensions**:

1. **Structure & Organization**:
   - Executive Summary: 3-5 sentences, captures essence
   - Logical flow: Each section builds on previous
   - Redundancy: No unnecessary repetition
   - Completeness: All findings addressed

2. **Scientific Accuracy**:
   - Facts vs interpretation: Clearly separated
   - Evidence: Every claim supported by data
   - Limitations: Acknowledged appropriately
   - Alternatives: Considered and discussed
   - Statistics: Properly reported

3. **Writing Quality**:
   - Clarity: Precise, unambiguous language
   - Conciseness: Efficient communication
   - Terminology: Consistent and appropriate
   - Figures: Properly referenced
   - Citations: Accurate and complete

**Command**: `/research-refine`

### 3. Report Structure

Standard report structure:

```markdown
# [Report Title]

**Date**: YYYY-MM-DD
**Report Type**: Integrated Analysis Report

---

## Executive Summary

[3-5 sentences capturing key findings and implications]

## Background

[Research question, context, and rationale]

## Materials and Methods

[Consolidated methods from experiments]

## Findings

### Finding 1: [Title]
- **Observation**: [Factual description]
- **Evidence**: [Lab notebook references, figures]

### Finding 2: [Title]
[Repeat structure]

## Synthesis

[Integrated interpretation of findings]

## Limitations

[Acknowledged constraints and caveats]

## Future Directions

[Prioritized next steps]

## Conclusion

[Final synthesis and key takeaways]

## References

[Citations]

---

## Appendix

### Lab Notebooks
- Exp01_[name].ipynb
- Exp02_[name].md

### Supplementary Figures
[Links]
```

### 4. Quality Standards

Reports maintain separation between facts and interpretation (from research-project quality-standards.md):

**In Findings section** (Level 1: Facts):
- Present observations directly
- Reference source notebooks
- Include exact measurements
- Avoid interpretation

**In Synthesis section** (Level 2: Interpretation):
- Connect observations to meaning
- Cite supporting evidence
- Acknowledge assumptions
- Consider alternatives

**In Conclusion section** (Level 3: Broader implications):
- Synthesize evidence
- State confidence appropriately
- Suggest applications
- Identify unknowns

## Workflow Patterns

### Pattern 1: Single Experiment Report

**Scenario**: Document one completed experiment

**Steps**:
1. Ensure lab notebook complete
2. Run: `/research-report` specifying single notebook
3. Review generated report
4. Refine: `/research-refine` to improve clarity

**Use case**: Individual experiment worthy of formal documentation

### Pattern 2: Integrated Multi-Experiment Report

**Scenario**: Synthesize multiple related experiments

**Steps**:
1. Identify notebooks to include (e.g., Exp01-Exp05)
2. Run: `/research-report` specifying all notebooks
3. Script extracts and consolidates content
4. AI synthesizes findings across experiments
5. Refine: `/research-refine` to improve integration

**Use case**: Project milestone, manuscript preparation

### Pattern 3: Iterative Refinement

**Scenario**: Improve existing report quality

**Steps**:
1. Identify report needing improvement
2. Run: `/research-refine` on existing report
3. Review suggestions organized by category:
   - Structure improvements
   - Scientific rigor issues
   - Writing clarity enhancements
4. Approve and implement changes
5. Iterate if needed

**Use case**: Preparing for presentation, submission, or review

## Resources

### scripts/

- `init_report.py`: Report generation script (executable)

### commands/

- `research-report.md`: Report generation command (`/research-report`)
- `research-refine.md`: Report refinement command (`/research-refine`)

### references/

- `mapping-rules.md`: Lab notebook → report section mapping
- `refinement-guide.md`: Quality criteria for report improvement

## Usage Notes

### Generation Best Practices

1. **Timing**: Generate reports when:
   - Multiple related experiments complete
   - Ready for project milestone
   - Preparing manuscript
   - Need formal documentation

2. **Scope**: Include notebooks that:
   - Address related questions
   - Build on each other
   - Collectively tell a story

3. **Preparation**: Before generating:
   - Ensure all lab notebooks complete
   - Review notebook quality
   - Identify key findings

### Refinement Best Practices

1. **Multiple passes**: Refine in stages:
   - First pass: Structure and organization
   - Second pass: Scientific rigor
   - Third pass: Writing quality

2. **Specific feedback**: Request targeted improvements:
   - "Improve executive summary"
   - "Check fact/interpretation separation"
   - "Enhance clarity in Methods"

3. **Version control**: Commit before and after refinement

### Common Improvements

**Executive Summary**:
- ❌ Too long (>5 sentences) or too vague
- ✅ Concise (3-5 sentences), captures essence

**Findings**:
- ❌ Mixed facts and interpretation
- ✅ Pure observations, references to notebooks

**Synthesis**:
- ❌ Unsupported claims, circular reasoning
- ✅ Evidence-based, acknowledges limitations

**Limitations**:
- ❌ Missing or too apologetic
- ✅ Honest, constructive, identifies solutions

**Future Directions**:
- ❌ Vague ("more research needed")
- ✅ Specific next experiments with rationale

### Integration with Workflow

**Typical flow**:
1. Complete experiments → Lab notebooks (lab-notebook)
2. Refine hypotheses → Hypothesis validation (hypothesis-driven)
3. Generate report → Synthesis (experiment-report: init)
4. Improve quality → Refinement (experiment-report: refine)
5. Update project → STEERING.md (research-project)

**Report triggers phase transitions**:
- Generating report often signals end of Execution phase
- Moving to Integration or Publication phase
- Update STEERING.md accordingly

## Examples

### Example 1: Quick Single-Experiment Report

```
User: "Create a report for Exp03"