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
            <li style="
                margin-bottom:15px;
                padding:12px;
                border:1px solid #eee;
                border-radius:8px;
                background:#fafafa;
            ">
                <strong style="font-size:16px;">{job.get('title')}</strong><br>
                <span style="color:#555;">{job.get('company')}</span><br>
                <a href="{job.get('job_url')}" style="color:#1e88e5;">View Job</a>
            </li>
            """
    return template.replace("{{jobs}}", jobs_html)
