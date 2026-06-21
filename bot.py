import os
import feedparser
import google.generativeai as genai

# APIキーの設定
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 最新のモデルを指定
model = genai.GenerativeModel('gemini-2.0-flash')

# RSSからブログ記事を取得
rss_url = "https://yamachampion.com/feed"
feed = feedparser.parse(rss_url)

if feed.entries:
    entry = feed.entries[0]
    prompt = f"以下のブログ記事の紹介文とハッシュタグ5つを作成して：\nタイトル: {entry.title}\nURL: {entry.link}"
    response = model.generate_content(prompt)
    print(response.text)
else:
    print("記事が見つかりませんでした")
