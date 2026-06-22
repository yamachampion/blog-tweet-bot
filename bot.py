import os
from google import genai
import feedparser

# 1. APIキーの設定
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY が環境変数に設定されていません")

# 2. クライアントの初期化
client = genai.Client(api_key=api_key)

# 3. RSSの読み込み
rss_url = "https://yamachampion.com/feed"
feed = feedparser.parse(rss_url)

if feed.entries:
    entry = feed.entries[0]
    prompt = f"以下のブログ記事の紹介文とハッシュタグ5つを作成して：\nタイトル: {entry.title}\nURL: {entry.link}"
    
    # 4. モデル生成 (最も制限が緩い gemini-1.5-flash-8b を使用)
    response = client.models.generate_content(
        model='gemini-1.5-flash-8b',
        contents=prompt,
    )
    print(response.text)
else:
    print("記事が見つかりませんでした")
