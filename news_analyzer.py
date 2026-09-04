import requests
import json
import os

def analyze_and_pick_top10(articles: list) -> list:
    api_key = os.environ["GEMINI_API_KEY"]

    headlines_text = ""
    for i, a in enumerate(articles):
        headlines_text += f"{i}. [{a['source']}] {a['title']}\n   {a['summary'][:200]}\n\n"

    prompt = f"""You are an AI news curator. Below are {len(articles)} recent AI news articles.
Select the TOP 10 most significant, interesting and verified AI news stories.
Return ONLY a JSON array of selected index numbers like: [3, 7, 12, 15, 20, 25, 31, 40, 45, 52]

Articles:
{headlines_text}

Return ONLY the JSON array, nothing else."""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, json=payload, timeout=30)
    result = response.json()
    text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
    indices = json.loads(text)
    top10 = [articles[i] for i in indices if i < len(articles)]
    return top10[:10]
