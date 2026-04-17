from dotenv import load_dotenv
import os
from job_spy import run_job_scraper
from emailer import send_email

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

file_path = run_job_scraper()
send_email(file_path, sender_email, password, recipient_email)
