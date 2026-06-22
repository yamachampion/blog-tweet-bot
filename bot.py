import os
from google import genai
import feedparser

# APIキーの設定
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# RSSからブログ記事を取得
rss_url = "https://yamachampion.com/feed"
feed = feedparser.parse(rss_url)

if feed.entries:
    entry = feed.entries[0]
    prompt = f"以下のブログ記事の紹介文とハッシュタグ5つを作成して：\nタイトル: {entry.title}\nURL: {entry.link}"
    
    # 新しいSDKでの生成方法
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
    )
    print(response.text)
else:
    print("記事が見つかりませんでした")
