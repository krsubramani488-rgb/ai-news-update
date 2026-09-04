# news_analyzer.py

import google.generativeai as genai
import json
import os

def analyze_and_pick_top10(articles: list) -> list:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    headlines_text = ""
    for i, a in enumerate(articles):
        headlines_text += f"{i}. [{a['source']}] {a['title']}\n   {a['summary'][:200]}\n\n"

    prompt = f"""You are an AI news curator. Below are {len(articles)} recent AI news articles.
Select the TOP 10 most significant, interesting, and verified AI news stories.
Prioritize: major model releases, breakthroughs, policy/regulation, company moves, research.
Avoid duplicates, avoid clickbait, ensure diversity.
Return ONLY a JSON array of selected index numbers (0-based), like: [3, 7, 12, 15, 20, 25, 31, 40, 45, 52]

Articles:
{headlines_text}

Return ONLY the JSON array, nothing else."""

    response = model.generate_content(prompt)
    indices = json.loads(response.text.strip())
    top10 = [articles[i] for i in indices if i < len(articles)]
    return top10[:10]
