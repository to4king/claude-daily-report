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
# Slack
# ============================================================

def format_slack_message(date: str, summary: str, canvas_url: str) -> str:
    """Slack投稿メッセージを生成する。区切り線(---)は含めない。"""
    return f"📋 Claude日次レポート({date})\n{summary}\n\nCanvas: {canvas_url}"
