import os
from google import genai
import feedparser

# APIキーの設定
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY が設定されていません。GitHub Secretsを確認してください。")

client = genai.Client(api_key=api_key)

# RSSからブログ記事を取得
rss_url = "https://yamachampion.com/feed"
feed = feedparser.parse(rss_url)

if feed.entries:
    entry = feed.entries[0]
    prompt = f"以下のブログ記事の紹介文とハッシュタグ5つを作成して：\nタイトル: {entry.title}\nURL: {entry.link}"
    
    # モデル名を指定せず、gemini-2.0-flash を直接指定して生成
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
    )
    print(response.text)
else:
    print("記事が見つかりませんでした")
