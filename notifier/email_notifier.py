import os
import smtplib
from email.mime.text import MIMEText

def send_email(jobs):
    sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
    receiver = os.environ.get("EMAIL_RECEIVER")

    content = "\n".join([f"{job['title']} at {job['company']} - {job['url']}" for job in jobs])
    msg = MIMEText(content)
    msg['Subject'] = '📬 New Job Alerts'
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        print(f"✅ Email sent to {receiver}")
