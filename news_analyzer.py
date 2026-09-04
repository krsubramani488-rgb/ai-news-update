import requests
import json
import os

def analyze_and_pick_top10(articles: list) -> list:
    api_key = os.environ["GEMINI_API_KEY"]

    headlines_text = ""
    for i, a in enumerate(articles):
        headlines_text += f"{i}. [{a['source']}] {a['title']}\n   {a['summary'][:200]}\n\n"

    prompt = f"""You are an AI news curator. Below are {len(articles)} recent AI news articles.
Select the TOP 10 most significant and interesting AI news stories.
Return ONLY a JSON array of index numbers like: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Articles:
{headlines_text}

Return ONLY the JSON array, nothing else."""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, json=payload, timeout=30)
        result = response.json()

        # Print full response for debugging
        print("Gemini response:", json.dumps(result, indent=2)[:500])

        if "candidates" not in result:
            print("No candidates — using first 10 articles as fallback")
            return articles[:10]

        text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
        
        # Clean text in case Gemini adds extra characters
        text = text.replace("```json", "").replace("```", "").strip()
        
        indices = json.loads(text)
        top10 = [articles[i] for i in indices if i < len(articles)]
        return top10[:10]

    except Exception as e:
        print(f"Gemini error: {e} — using first 10 articles as fallback")
        return articles[:10]
