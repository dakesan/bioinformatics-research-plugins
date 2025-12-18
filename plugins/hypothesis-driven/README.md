# hypothesis-driven Plugin

Hypothesis refinement and validation for scientific research.

## Overview

The `hypothesis-driven` plugin helps refine hypotheses after experiments, ensuring they are testable, specific, quantitative, and falsifiable. Used AFTER experiment execution to improve hypotheses based on observations.

## Features

- **Hypothesis Refinement**: Transform vague ideas into testable predictions
- **Quality Scoring**: Evaluate hypotheses against multiple criteria
- **Verification Strategy**: Design experiments to test hypotheses
- **Testability Validation**: Check if hypotheses can be practically tested

## Core Principles

Good hypotheses are:
1. **Testable**: Can be evaluated with available methods
2. **Specific**: Variables and relationships clearly defined
3. **Quantitative**: Include measurable predictions
4. **Falsifiable**: Can be proven wrong

## Usage

This skill is triggered by requests like:
- "Refine this hypothesis"
- "Is this hypothesis testable?"
- "How can I improve this hypothesis?"
- "Design verification strategy"
- "仮説をリファインして"

## Output Format

```markdown
## Original Hypothesis
[User's hypothesis]

## Refined Hypothesis
[Improved version]

## Verification Strategy
[How to test]
[Expected results]

## Quality Check
- [x] Testable
- [x] Specific
- [x] Evidence-based
- [x] Distinguishable

## Improvement Notes
[Explanation of changes]
```

## Quality Scoring

Each hypothesis is evaluated on 0-3 scale across 4 dimensions:

| Dimension | Description |
|-----------|-------------|
| Testability | Can it be evaluated with practical experiments? |
| Specificity | Are variables clearly defined? |
| Quantitativeness | Does it include measurable predictions? |
| Falsifiability | Can it be proven wrong? |

**Total possible**: 12 points
- 10-12: Excellent (ready for testing)
- 7-9: Good (minor refinement)
- 4-6: Weak (major refinement needed)
- 0-3: Poor (reformulation required)

## Examples

### Example 1: Vague → Specific

❌ **Bad**: "Gene X is important for cancer"

**Problems**: Vague, not testable, no prediction

✅ **Refined**: "Knockout of Gene X reduces cancer cell proliferation by >30% compared to wild-type in HeLa cells"

**Improvements**: Specific intervention, quantitative prediction, clear comparison

### Example 2: Qualitative → Quantitative

❌ **Bad**: "Treatment will improve survival"

✅ **Refined**: "Treatment will improve median survival by ≥3 months (HR < 0.7, p < 0.05)"

**Improvements**: Quantitative threshold, statistical criteria

## Workflow

Typical usage pattern:

1. **After experiment**: User completes Exp03
2. **Extract hypothesis**: Read from lab notebook
3. **Evaluate quality**: Apply validation criteria
4. **Refine**: Improve specificity and testability
5. **Verify**: Design next experiment
6. **Update**: User updates notebook

## Files

### References

- `references/validation-criteria.md` - Detailed quality assessment criteria with examples

## Best Practices

### Do:
- Base hypotheses on observations
- Be specific with measurable variables
- Include quantitative predictions
- Consider alternative explanations
- Iterate based on evidence

### Don't:
- Use vague terms ("important", "relevant")
- Make unfalsifiable statements
- Claim causation from correlation
- Cherry-pick supporting evidence
- Use excessive hedging ("might", "could")

## Common Patterns

**Broadening → Narrowing**:
- "Gene X affects cancer" → "Gene X knockdown reduces migration by >50% in MDA-MB-231 cells"

**Qualitative → Quantitative**:
- "Expression changes" → "≥200 genes change >2-fold (p < 0.05)"

**Vague → Mechanistic**:
- "Pathway involved" → "Pathway Y activation (pZ >2-fold) within 30min of stimulus"

## Installation

```bash
/plugin install hypothesis-driven@bioinformatics-research
```

## Integration

Used AFTER:
- Exploratory experiments (lab-notebook)
- Initial data analysis

Used BEFORE:
- Confirmatory experiments
- Report generation (experiment-report)

## License

MIT
