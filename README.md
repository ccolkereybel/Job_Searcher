# Job Alert Automation System

A Python automation tool that scrapes job listings using **JobSpy**, saves them to a CSV file, and automatically emails the results on a schedule.

---

## What it does

- Scrapes job listings using `python-jobspy`
- Saves results to a CSV file
- Emails the CSV automatically via Gmail SMTP
- Runs on a schedule (Tuesday & Thursday via cron)

---

## Tech Stack

- Python 3
- JobSpy (job scraping)
- SMTP (email automation)
- python-dotenv (environment variables)
- cron (task scheduling)

---

## Environment Variables
Create a `.env` file:

## Environment Variables

Create a `.env` file:

```env
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient_email@gmail.com
```
⚠️ Gmail requires an App Password (not your normal password)

## Run Locally

Install dependencies:

```bash
pip install python-jobspy python-dotenv
```
Run the project:
```bash
python3 main.py
```
