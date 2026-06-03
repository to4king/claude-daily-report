# claude-daily-report

Claude / Anthropic の最新情報を毎日自動収集し、Google Drive への保存と Slack への通知を行う日次レポートワークフローです。

## 概要

- **実行タイミング**: 毎朝（JST 基準）
- **情報ソース**: Anthropic News / Claude ドキュメント / Claude Code 変更履歴
- **成果物**: Google Drive への HTML レポート保存 + Slack `#claude-daily` への通知

## ファイル構成

| ファイル | 役割 |
|---|---|
| `generate_report.py` | レポート生成スクリプト（情報収集・HTML 生成） |
| `html_to_pdf.js` | Playwright/Chromium を使った HTML→PDF 変換 |
| `CLAUDE.md` | Routines セッション向け運用ルール |

## 出力フォーマット

### 新発表があった場合
各発表について「タイトル / 概要 / 公式リンク / 実務での使いどころ」を記載。

### 新発表がなかった場合
スラッシュコマンド・標準スキル・著名プラグインの活用 Tips を 3 件掲載。

## 既知の制限

- Drive MCP のアップロード上限（約 200KB）のため、現在は HTML 形式で保存
- Playwright 生成 PDF は約 1MB になるため base64 アップロードが困難
