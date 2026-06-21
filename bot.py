import os
import feedparser
import google.generativeai as genai

# 環境変数からキーを取得
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

rss_url = "https://yamachampion.com/feed"
feed = feedparser.parse(rss_url)
entry = feed.entries[0]

prompt = f"以下のブログ記事の紹介文とハッシュタグ5つを作成して：\nタイトル: {entry.title}\nURL: {entry.link}"
response = model.generate_content(prompt)

print(response.text)
