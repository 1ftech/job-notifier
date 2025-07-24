import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(jobs):
    sender = os.environ["EMAIL_SENDER"]
    password = os.environ["EMAIL_PASSWORD"]
    receiver = os.environ["EMAIL_RECEIVER"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "🧠 New Job Postings for You"
    msg["From"] = sender
    msg["To"] = receiver

    html_content = "<h2>Here are the latest jobs:</h2>"

    for site, job_list in jobs.items():
        html_content += f"<h3>{site}</h3><ul>"
        for job in job_list:
            if all(k in job for k in ("link", "title", "company", "location")):
                html_content += (
                    f"<li><a href='{job['link']}' target='_blank'>{job['title']}</a> "
                    f"- {job['company']} ({job['location']})</li>"
                )
            else:
                # Optional: log missing fields
                print(f"⛔ Skipping incomplete job entry: {job}")
        html_content += "</ul>"

    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("✅ Email sent successfully.")
    except Exception as e:
        print("🚨 Failed to send email:", e)


