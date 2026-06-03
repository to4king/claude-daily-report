"""
Claude日次レポート生成スクリプト
情報収集ソースの定数定義とレポート生成ユーティリティ
"""

# ============================================================
# 情報収集ソース
# ============================================================

OFFICIAL_SOURCES = [
    {
        "name": "Anthropic News",
        "url": "https://www.anthropic.com/news",
        "fallback": "WebSearch: site:anthropic.com/news",
    },
    {
        "name": "Claude Docs Release Notes",
        "url": "https://docs.claude.com/release-notes",
        "fallback": "WebSearch: Claude release notes site:docs.claude.com",
    },
    {
        "name": "Claude Code Changelog",
        "url": "https://code.claude.com/release-notes",
        "fallback": "https://github.com/anthropics/claude-code/releases",
    },
]

# HTTP 403 が返ることが確認されているソース（WebSearch で代替）
KNOWN_403_SOURCES = [
    "https://www.anthropic.com/news",
    "https://docs.anthropic.com",
]

# ============================================================
# Google Drive
# ============================================================

# HTML は text_content フィールドで渡す（base64_content はMCPペイロード上限に引っかかるため）

# ============================================================
# Slack
# ============================================================

# ============================================================
# レポートテンプレート
# ============================================================

REPORT_TEMPLATE_WITH_NEWS = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Claude日次レポート {date}</title>
<style>
  body {{ font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; }}
  h1 {{ border-bottom: 2px solid #333; }}
  h2 {{ border-left: 4px solid #0066cc; padding-left: 0.5rem; }}
  .meta {{ color: #666; font-size: 0.9rem; }}
  .tip {{ background: #f5f5f5; padding: 1rem; border-radius: 4px; margin: 1rem 0; }}
</style>
</head>
<body>
<h1>📋 Claude日次レポート</h1>
<p class="meta">実行日: {date} (JST)</p>
{content}
</body>
</html>
"""


def format_slack_message(date: str, summary: str, drive_url: str) -> str:
    """Slack投稿メッセージを生成する。区切り線(---)は含めない。"""
    return f"📋 Claude日次レポート({date})\n{summary}\n\nDrive: {drive_url}"
