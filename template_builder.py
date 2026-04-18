import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(BASE_DIR, "templates/email_template.html")


def build_email_body(file_path):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    jobs_html = ""

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for job in reader:
            jobs_html += f"""
                <li style="padding:8px; border-radius:10px;">
                    <strong>{job.get('title')}</strong></br>
                    {job.get('company')}<br>
                    <a href="{job.get('job_url')}">View Job</a>
                </li>
            """
    return template.replace("{{jobs}}", jobs_html)
