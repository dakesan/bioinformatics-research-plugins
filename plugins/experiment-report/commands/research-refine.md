---
description: Refine and improve an existing report
---

Use the `experiment-report` skill to refine an existing report.

## Refinement Dialogue Flow

When user requests refinement, engage in structured dialogue:

### Step 1: Initial Assessment Questions

Ask the user:
1. "Which report do you want to refine?" (path)
2. "What is your primary concern?" (structure/rigor/clarity/all)
3. "Is this for internal review or external sharing?"

### Step 2: Focus Area Selection

Based on user response, prioritize one of:

**Structure Focus**:
- Executive Summary length and completeness
- Logical flow between sections
- Redundancy elimination

**Scientific Rigor Focus**:
- Claim-evidence alignment
- Fact/interpretation separation
- Confidence language calibration

**Clarity Focus**:
- Conciseness
- Terminology consistency
- Figure references

### Step 3: Claim-Evidence Audit

For each finding, verify:
- [ ] Claim is stated clearly
- [ ] Evidence table is complete (notebook path, figure path, statistics)
- [ ] All paths exist and are accessible
- [ ] Uncertainty level is stated
- [ ] Alternative interpretations are considered

**Questions to identify gaps**:
- "For Finding X, what is the primary evidence?"
- "Is there a figure that supports this claim?"
- "What confidence level is appropriate here?"
- "What alternative explanations should we mention?"

### Step 4: Confidence Language Calibration

Check each claim against evidence strength:

| Evidence Strength | Appropriate Language |
|------------------|---------------------|
| Very strong (multiple lines) | "demonstrate", "show", "establish" |
| Strong (validated) | "indicate", "suggest strongly" |
| Moderate (single line) | "suggest", "consistent with" |
| Weak (preliminary) | "may", "could", "possible" |
| Speculative | "we hypothesize", "one possibility" |

**Ask user**:
- "Are there any claims that feel overconfident?"
- "Are there any claims that are too hedged?"

### Step 5: Quality Gate Verification

Apply checklist from `references/refinement-guide.md`:

**Structure**:
- [ ] Executive Summary: 3-5 sentences
- [ ] All sections present
- [ ] No redundancy

**Evidence**:
- [ ] All figure paths verified
- [ ] All notebook paths verified
- [ ] Statistics include test, p-value, effect size

**Rigor**:
- [ ] Facts separated from interpretation
- [ ] Confidence language calibrated
- [ ] Alternative explanations considered
- [ ] Limitations acknowledged

**Writing**:
- [ ] Concise and clear
- [ ] Consistent terminology
- [ ] Figures referenced in text

### Step 6: Implementation

After identifying issues:
1. Prioritize by severity (Critical > Important > Minor)
2. Present proposed changes to user
3. Implement with user approval
4. Verify improvements

## Minimal Refinement (Quick Pass)

If user wants fast refinement, focus on these 3 critical checks:
1. **Claim-Evidence Links**: Is every claim backed by evidence?
2. **Fact/Interpretation Separation**: Are observations in Findings, interpretations in Synthesis?
3. **Confidence Calibration**: Does language match evidence strength?

See `references/refinement-guide.md` for detailed criteria.
