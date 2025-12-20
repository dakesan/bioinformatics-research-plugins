# experiment-report Plugin

Integrated report generation and refinement from lab notebook results.

## Overview

The `experiment-report` plugin handles both report generation (mechanical extraction and templating) and refinement (AI-guided improvement). Following the skill-creator pattern, it provides complete workflow from raw notebooks to polished reports.

## Features

- **Generation**: Mechanical extraction from lab notebooks using templates
- **Refinement**: AI-guided improvement for scientific rigor and clarity
- **Quality Standards**: Maintains fact/interpretation separation
- **Integration**: Synthesizes findings across multiple experiments
- **Figure Integration**: Structured workflow for incorporating images from notebooks
- **PDF Export**: Generate publication-ready PDFs using pandoc + typst

## Commands

### /research-report

Generate new integrated report from lab notebooks.

**Workflow** (execute from project root):
1. Specify lab notebooks to include
2. Run `init_report.py` to extract content
3. Apply mapping rules (`references/mapping-rules.md`)
4. Generate template with placeholders
5. AI fills in synthesis sections
6. Output: `notebook/report/Report_[title].md`

Usage:
```
/research-report
```

### /research-refine

Improve existing report quality.

**Workflow**:
1. Specify report to refine
2. Evaluate against criteria (`references/refinement-guide.md`):
   - Structure & organization
   - Scientific rigor
   - Writing quality
3. Provide specific improvement suggestions
4. Implement changes (with user approval)

Usage:
```
/research-refine
```

## Report Structure

Standard sections:
1. **Executive Summary**: 3-5 sentence overview
2. **Background**: Research question and context
3. **Materials and Methods**: Consolidated procedures
4. **Findings**: Observations organized by theme
5. **Synthesis**: Integrated interpretation
6. **Limitations**: Acknowledged constraints
7. **Future Directions**: Prioritized next steps
8. **Conclusion**: Final synthesis
9. **Appendix**: Notebook references

## Mapping Rules

Lab notebook content transforms to report sections:

| Lab Notebook | Report | Transformation |
|-------------|--------|----------------|
| Hypothesis + Background | Background | Synthesis |
| Materials & Methods | Methods Summary | Abstraction |
| Results | Findings | Structuring by theme |
| Discussion | Synthesis | Integration |
| Limitations | Limitations | Consolidation |
| Next Steps | Future Directions | Prioritization |
| All sections | Executive Summary | Distillation |

See `references/mapping-rules.md` for details.

## Refinement Criteria

Reports are evaluated on three dimensions:

### 1. Structure
- Executive Summary: 3-5 sentences, self-contained
- Logical flow between sections
- Findings organized by theme
- No redundancy

### 2. Scientific Rigor
- Facts separated from interpretation
- All claims evidence-based
- Confidence language calibrated
- Alternative explanations considered
- Limitations acknowledged

### 3. Writing Quality
- Clear and concise
- Consistent terminology
- Professional tone
- Proper figure references

See `references/refinement-guide.md` for detailed checklist.

## Usage Patterns

### Single Experiment Report

For documenting one completed experiment:

```
/research-report  # Select Exp03
→ Review generated template
/research-refine  # Improve clarity
```

### Multi-Experiment Integration

For synthesizing related experiments:

```
/research-report  # Select Exp01-Exp05
→ AI synthesizes findings
→ Manual review of integration
/research-refine  # Polish for presentation
```

### Iterative Refinement

For improving existing reports:

```
/research-refine  # First pass: structure
→ Review and implement
/research-refine  # Second pass: rigor
→ Review and implement
/research-refine  # Final pass: writing
```

## Files

### Scripts

- `scripts/init_report.py` - Report generation script (executable)
- `scripts/export_pdf.sh` - PDF export script using pandoc + typst

### Commands

- `commands/research-report.md` - Generation command
- `commands/research-refine.md` - Refinement command

### References

- `references/mapping-rules.md` - Notebook → report section mapping
- `references/refinement-guide.md` - Quality criteria and improvement patterns

### Templates

- `assets/templates/report-template.md` - Markdown report template
- `assets/templates/report.typ` - typst template for PDF export

## Quality Standards

Following research-project quality-standards.md:

**Level 1 (Facts)**: Findings section contains observations
**Level 2 (Interpretation)**: Synthesis section contains reasoning
**Level 3 (Conclusion)**: Conclusion section contains implications

## Best Practices

### When to Generate Reports

**IMPORTANT**: Report generation is designed for **after all experiments are complete**.
- Create reports to **integrate findings** from multiple related experiments
- Synthesize results across Exp01, Exp02, Exp03, etc. into a cohesive narrative
- Use when project milestone reached (e.g., end of Execution phase)
- Preparing for presentation/manuscript
- Need formal documentation

**Workflow**:
1. Complete all planned experiments (Exp01-ExpN)
2. Each experiment has saved figures to `results/` directory
3. Run `/research-report` to integrate all experiments
4. Report references all saved figures from individual experiments

### Before Generation

- Ensure lab notebooks complete
- Review notebook quality
- Identify key findings to highlight

### After Generation

- Review mapping accuracy
- Fill in synthesis sections
- Add cross-references
- Verify evidence citations

### PDF Export

Export finalized reports to PDF using the provided script:

```bash
# Basic export (output: Report_Exp01-02_analysis.pdf)
/path/to/plugins/experiment-report/scripts/export_pdf.sh Report_Exp01-02_analysis.md

# Custom output filename
/path/to/plugins/experiment-report/scripts/export_pdf.sh Report_Exp01-02_analysis.md custom_output.pdf
```

The script automatically:
- Detects template location (`assets/templates/report.typ`)
- Validates prerequisites (pandoc, typst)
- Reports file size on success

**Prerequisites**: pandoc, typst

```bash
# Install prerequisites
brew install pandoc typst
```

### Refinement Tips

1. **Multiple passes**: Structure → Rigor → Writing
2. **Specific feedback**: "Improve executive summary"
3. **Version control**: Commit before/after changes

## Common Improvements

**Executive Summary**:
- Tighten from verbose to 3-5 sentences
- Remove technical details
- Add quantitative highlights

**Findings**:
- Reorganize from chronological to thematic
- Separate facts from interpretation
- Add missing evidence citations

**Synthesis**:
- Integrate across experiments
- Calibrate confidence language
- Consider alternative explanations

**Limitations**:
- Make specific (not generic)
- Be constructive
- Suggest solutions

## Installation

```bash
/plugin install experiment-report@bioinformatics-research
```

## Integration

**Follows**:
- Lab notebook completion (lab-notebook)
- Hypothesis refinement (hypothesis-driven)

**Enables**:
- Project phase transitions (research-project)
- Publication preparation

## License

MIT
