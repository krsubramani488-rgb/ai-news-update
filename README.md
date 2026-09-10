# 🤖 AI News Digest Bot

An automated Python bot that scrapes AI news from sources around the world, filters the **Top 10 most important stories** using Google Gemini AI, generates a clean PDF digest, and delivers it directly to your Gmail inbox every morning.

> Built with Python · Gemini API · GitHub Actions · Runs 100% free on the cloud

---

## 📬 What It Does

Every morning at **6:00 AM IST**, this bot automatically:

1. 📡 Scrapes 50–80 fresh AI news articles from 10+ global RSS feeds
2. 🧠 Uses Google Gemini AI to pick the Top 10 most significant stories
3. 📄 Generates a clean, readable PDF digest
4. 📧 Sends the PDF directly to your Gmail inbox

No manual work. No server needed. Runs entirely free on GitHub Actions.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| `feedparser` | RSS feed scraping |
| `requests` | Gemini REST API calls |
| `reportlab` | PDF generation |
| `smtplib` | Gmail email sending |
| Google Gemini API | AI-powered news filtering |
| GitHub Actions | Free cloud scheduler (cron) |

---

## 📁 Project Structure

```
ai-news-update/
├── main.py               # Orchestrator — runs all steps
├── news_fetcher.py       # Scrapes RSS feeds worldwide
├── news_analyzer.py      # Gemini AI picks Top 10 stories
├── pdf_generator.py      # Generates the PDF digest
├── email_sender.py       # Sends PDF to Gmail inbox
├── requirements.txt      # Python dependencies
└── .github/
    └── workflows/
        └── daily_news.yml  # GitHub Actions cron schedule
```

---

## 🌍 News Sources

Pulls from 10+ top AI RSS feeds globally:

- TechCrunch AI
- VentureBeat AI
- The Verge AI
- Wired AI
- MIT Technology Review AI
- AI News
- DeepMind Blog
- OpenAI Blog
- Google AI Blog
- ArXiv CS.AI (Research Papers)

---

## ⚙️ How It Works

```
RSS Feeds (10+ sources)
        ↓
news_fetcher.py   →  Collects 50-80 raw articles (last 24 hours)
        ↓
news_analyzer.py  →  Gemini AI selects Top 10 verified stories
        ↓
pdf_generator.py  →  Builds a clean PDF with title, summary, source
        ↓
email_sender.py   →  Attaches PDF and sends to Gmail
        ↓
GitHub Actions    →  Triggers at 6:00 AM IST every day ☀️
```

---

## 🚀 Setup & Deployment

### 1. Clone the repo
```bash
git clone https://github.com/krsubramani488-rgb/ai-news-update.git
cd ai-news-update
```

### 2. Get your free Gemini API key
1. Go to → [aistudio.google.com](https://aistudio.google.com)
2. Click **"Get API key"** → **"Create API key"**
3. Copy the key (starts with `AIza...`)

### 3. Get Gmail App Password
1. Go to → [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Create an app password for "Mail"
3. Copy the 16-character password

### 4. Add GitHub Secrets
In your repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret Name | Value |
|---|---|
| `GEMINI_API_KEY` | Your Gemini API key |
| `GMAIL_USER` | yourname@gmail.com |
| `GMAIL_APP_PASS` | 16-char App Password |
| `RECIPIENT_EMAIL` | yourname@gmail.com |

### 5. Push and run
```bash
git add .
git commit -m "first commit"
git push -u origin main
```

Then go to **Actions tab → Run workflow** to test immediately!

---

## 📄 Sample Output

The bot generates a PDF like this every morning:

```
🤖 Daily AI News Digest
Your Top 10 AI Stories — Friday, 04 September 2026

#1 — OpenAI launches Astra, its powerful new model
Source: TechCrunch AI | Thu, 03 Sep 2026
OpenAI claims that Astra represents "a new frontier on computer
and browser use"...

#2 — Nvidia confirms it will buy Hugging Face for $12.9 billion
Source: TechCrunch AI | Thu, 03 Sep 2026
Nvidia said Hugging Face hosts over 3 million models and is
used by over 18 million developers...

... and 8 more top stories
```

---

## ⏰ Schedule

Runs automatically at **6:00 AM IST (12:30 AM UTC)** every day via GitHub Actions cron:

```yaml
- cron: "30 0 * * *"
```

You can also trigger it manually anytime from the **Actions tab → Run workflow**.

---

## 💡 Key Learnings

- Used Gemini REST API directly via `requests` instead of the `google-generativeai` SDK to avoid gRPC loop errors
- Added try/except fallback in case Gemini returns unexpected responses
- GitHub Actions handles all cloud execution — no local setup or server needed
- Fully free stack: Gemini free tier + GitHub Actions free tier + Gmail SMTP

---

## 🔧 Possible Improvements

- Add more RSS feeds for broader global coverage
- Categorize news (Research / Policy / Products / Funding)
- Add WhatsApp delivery using Twilio free tier
- Support multiple recipient emails
- Add news sentiment analysis

---

## 👤 Author

**Subramani R** — [@krsubramani488-rgb](https://github.com/krsubramani488-rgb)

---

## 📜 License

MIT License — free to use and modify
