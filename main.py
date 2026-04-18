from dotenv import load_dotenv
import os
from job_spy import run_job_scraper
from emailer import send_email
from template_builder import build_email_body

load_dotenv()


def preview_email(html_content):
    with open("preview.html", "w", encoding="utf-8") as f:
        f.write(html_content)


sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

file_path = run_job_scraper()
html_content = build_email_body(file_path)
send_email(html_content, sender_email, password, recipient_email)
