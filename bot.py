import os
import feedparser
import google.generativeai as genai
import sys

# 診断用コード
print("--- 診断開始 ---")
api_key = os.getenv("GEMINI_API_KEY")
print(f"APIキーの取得状況: {'OK' if api_key else 'エラー！空です'}")

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("モデルの準備完了")
    
    rss_url = "https://yamachampion.com/feed"
    feed = feedparser.parse(rss_url)
    print(f"フィード取得完了: {len(feed.entries)} 件の記事が見つかりました")
    
    if len(feed.entries) > 0:
        entry = feed.entries[0]
        print(f"最新記事: {entry.title}")
    
    print("--- 診断終了 (成功) ---")

except Exception as e:
    print(f"エラー発生: {e}")
    sys.exit(1)
