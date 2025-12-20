# bioinformatics-research-plugins Project Context

## Core Principles

このプラグイン群が重視する研究原則:

- **Hypothesis-Driven**: 仮説を明確にしてから実験を設計
- **Fact/Interpretation Separation**: 観察事実と解釈を厳密に分離
- **Reproducibility**: 再現可能な記録を残す
- **Evidence Traceability**: 主張は必ず証拠にリンク
- **Calibrated Uncertainty**: 不確実性を適切な言葉で表現

## Plugins

### research-project (v0.2.1)

プロジェクト管理とフェーズ制御

- Skills: `research-project`
- Commands: `/research-init`, `/research-status`
- Scripts: `scripts/init_project.py --path <target>`
- References: `phases.md`, `best-practices.md`, `quality-standards.md`

### lab-notebook (v0.1.0)

実験ごとのラボノートブック作成

- Skills: `lab-notebook`
- Commands: `/research-exp`
- References: `notebook-guidelines.md`

### experiment-report (v0.2.1)

ラボノートからの統合レポート生成

- Skills: `experiment-report`
- Commands: `/research-report`, `/research-refine`
- Scripts: `scripts/export_pdf.sh <input.md> [output.pdf]`
- References: `mapping-rules.md`, `refinement-guide.md`

### hypothesis-driven (v0.1.0)

仮説の検証と改良

- Skills: `hypothesis-driven`
- Commands: なし
- References: `validation-criteria.md`

### inbox-processor (v0.2.0)

入力ファイルの分類と処理

- Skills: `inbox-processor`
- Commands: `/inbox-process`
- References: `classification-rules.md`

## Coding Rules

### Version Management

編集後は必ず `plugin.json` のバージョンを更新すること。

- Semantic versioning:
  - Patch (0.0.x): バグ修正、ドキュメント修正
  - Minor (0.x.0): 新機能
  - Major (x.0.0): 破壊的変更
- `plugin.json` の keywords も必要に応じて更新
- バージョン変更は関連する変更と一緒にコミット

## Important Guidelines

- ドキュメント内のスクリプトパスは絶対パスで記載
- references/ 配下のガイドラインは各プラグインの核となる知識
