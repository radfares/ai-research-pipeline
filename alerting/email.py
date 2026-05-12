"""Email alerting with SMTP."""
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_alert(subject, body):
    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER")
    passwd = os.getenv("SMTP_PASS")
    to = os.getenv("ALERT_RECIPIENTS", "").split(",")
    if not all([host, user, passwd]):
        print("SMTP not configured. Skipping alert.")
        return
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = ", ".join(to)
    with smtplib.SMTP(host, port) as s:
        s.starttls()
        s.login(user, passwd)
        s.sendmail(user, to, msg.as_string())
