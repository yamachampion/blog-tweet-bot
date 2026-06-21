import os
import feedparser
import google.generativeai as genai
import sys

# デバッグ用：キーが存在するか確認
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("エラー: GEMINI_API_KEY が取得できていません")
    sys.exit(1)

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    rss_url = "https://yamachampion.com/feed"
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        print("エラー: RSS記事が見つかりません")
        sys.exit(1)
        
    entry = feed.entries[0]
    prompt = f"以下のブログ記事の紹介文とハッシュタグ5つを作成して：\nタイトル: {entry.title}\nURL: {entry.link}"
    response = model.generate_content(prompt)
    print(response.text)

except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
    sys.exit(1)
