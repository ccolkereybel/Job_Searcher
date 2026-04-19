import smtplib
from email.message import EmailMessage


def send_email(html_content, email_address, email_password, recipient):
    # 1. Create the email container
    msg = EmailMessage()
    msg["Subject"] = "Daily Job Listings"
    msg["From"] = email_address
    msg["To"] = recipient

    msg.set_content("Job listings attached")
    msg.add_alternative(html_content, subtype="html")

    # 2. Connect and send using SMTP
    # Port 587 is standard for STARTTLS security
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(email_address, email_password)
        server.send_message(msg)
