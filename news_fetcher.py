# news_fetcher.py

import feedparser
from datetime import datetime, timedelta

# ── Snippet 1: The RSS sources list ──────────────────────
AI_RSS_FEEDS = [
    ("TechCrunch AI",      "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("VentureBeat AI",     "https://venturebeat.com/ai/feed/"),
    ("The Verge AI",       "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml"),
    ("Wired AI",           "https://www.wired.com/feed/tag/artificial-intelligence/rss"),
    ("AI News",            "https://www.artificialintelligence-news.com/feed/"),
    ("MIT Tech Review AI", "https://www.technologyreview.com/topic/artificial-intelligence/feed"),
    ("DeepMind Blog",      "https://deepmind.google/blog/rss.xml"),
    ("OpenAI Blog",        "https://openai.com/blog/rss.xml"),
    ("Google AI Blog",     "https://blog.google/technology/ai/rss/"),
    ("ArXiv CS.AI",        "https://arxiv.org/rss/cs.AI"),
]

# ── Snippet 2: The fetch function (uses the list above) ──
def fetch_all_news(max_per_source=10):
    all_articles = []
    cutoff = datetime.now() - timedelta(hours=24)

    for source_name, url in AI_RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_per_source]:
            pub_date = entry.get("published_parsed") or entry.get("updated_parsed")
            if pub_date:
                pub_dt = datetime(*pub_date[:6])
                if pub_dt < cutoff:
                    continue

            all_articles.append({
                "title":   entry.get("title", "No Title"),
                "summary": entry.get("summary", "")[:500],
                "url":     entry.get("link", ""),
                "source":  source_name,
                "date":    entry.get("published", "Unknown date"),
            })

    return all_articles