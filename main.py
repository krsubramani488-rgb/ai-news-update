from news_fetcher import fetch_all_news
from news_analyzer import analyze_and_pick_top10
from pdf_generator import generate_pdf
from email_sender import send_email

def run():
    print("📡 Fetching AI news from the world...")
    all_articles = fetch_all_news(max_per_source=10)
    print(f"   → {len(all_articles)} articles collected")

    print("🧠 Analyzing with AI...")
    top10 = analyze_and_pick_top10(all_articles)
    print(f"   → {len(top10)} top stories selected")

    print("📄 Generating PDF...")
    pdf_path = generate_pdf(top10, "ai_digest.pdf")

    print("📧 Sending to your inbox...")
    send_email(pdf_path)

    print("🎉 Done! Check your inbox.")

if __name__ == "__main__":
    run()
