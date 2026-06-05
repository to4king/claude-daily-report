# claude-daily-report

Claude / Anthropic の最新情報を毎日自動収集し、Slack Canvas にレポートを作成する日次ワークフローです。

## 概要

- **実行タイミング**: 毎朝（JST 基準）
- **情報ソース**: Anthropic News / Claude ドキュメント / Claude Code 変更履歴
- **成果物**: Slack Canvas へのレポート作成 + `#claude-daily` への通知

## ファイル構成

| ファイル | 役割 |
|---|---|
| `generate_report.py` | レポート生成ユーティリティ（情報収集ソース定数・メッセージフォーマッター） |
| `CLAUDE.md` | Routines セッション向け運用ルール |

## 出力フォーマット

### 新発表があった場合
各発表について「タイトル / 概要 / 公式リンク / 実務での使いどころ」を記載。

### 新発表がなかった場合
スラッシュコマンド・標準スキル・著名プラグインの活用 Tips を 3 件掲載。
