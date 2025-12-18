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

Three levels of scientific statements:
1. **Facts**: Direct observations (e.g., "Gene X expression was 2.3-fold higher")
2. **Interpretation**: Reasoned explanation (e.g., "This suggests increased activity")
3. **Conclusion**: Broader implications (e.g., "Gene X may regulate pathway Y")

**In practice**:
- Lab notebooks: Focus on facts and observations
- Reports: Include interpretation with clear reasoning
- Always label speculation as such

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
