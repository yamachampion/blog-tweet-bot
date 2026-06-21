import os
import feedparser
import google.generativeai as genai

# デバッグ用：キーが存在するか確認
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("エラー: GEMINI_API_KEY が環境変数に見つかりません！")
    exit(1)

genai.configure(api_key=api_key)
# ...以下略
