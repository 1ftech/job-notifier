import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_email(jobs: dict):
    sender = os.environ["EMAIL_SENDER"].strip()
    password = os.environ["EMAIL_PASSWORD"].strip()
    receiver = os.environ["EMAIL_RECEIVER"].strip()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "🔥 New Job Listings Found!"
    msg["From"] = sender
    msg["To"] = receiver

    html_content = ""
    for site, job_list in jobs.items():
        if job_list:
            html_content += f"<h2>{site}</h2><ul>"
            for job in job_list:
                html_content += f"<li><a href='{job['link']}'>{job['title']}</a> - {job['company']} ({job['location']})</li>"
            html_content += "</ul><br>"

    if not html_content:
        html_content = "<p>No new jobs found today.</p>"

    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)

