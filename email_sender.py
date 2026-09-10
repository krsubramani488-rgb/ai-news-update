import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import os

def send_email(pdf_path: str):
    GMAIL_USER  = os.environ["GMAIL_USER"]     # your Gmail address
    GMAIL_PASS  = os.environ["GMAIL_APP_PASS"] # Gmail App Password (16-char)
    RECIPIENT   = os.environ["RECIPIENT_EMAIL"] # where to deliver

    today = datetime.now().strftime("%d %b %Y")
    subject = f"🤖 AI News Digest — Top 10 Stories | {today}"

    msg = MIMEMultipart()
    msg["From"]    = GMAIL_USER
    msg["To"]      = RECIPIENT
    msg["Subject"] = subject

    body = MIMEText(f"""Good morning Mani 🌅

Your daily AI digest is ready. Today's top 10 stories from around the world are attached as a PDF.

Stay ahead of the curve. 🚀

— Your AI News Bot
""")
    msg.attach(body)

    # Attach PDF
    with open(pdf_path, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="pdf")
        attachment.add_header("Content-Disposition", "attachment",
                               filename=f"AI_Digest_{today}.pdf")
        msg.attach(attachment)

    # Send via Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, RECIPIENT, msg.as_string())

    print(f"✅ Email sent to {RECIPIENT}")
