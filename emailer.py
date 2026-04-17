import smtplib
from email.message import EmailMessage
import os


def send_email(file_path, email_address, email_password, recipient):
    # 1. Create the email container
    msg = EmailMessage()
    msg["Subject"] = "Daily Job Listings"
    msg["From"] = email_address
    msg["To"] = recipient
    msg.set_content("Job listings attached")

    # 2. Open and attach the file
    # Use 'rb' (read binary) for compatibility with all file types
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = file_path
        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name,
        )

    # 3. Connect and send using SMTP
    # Port 587 is standard for STARTTLS security
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(email_address, email_password)
        server.send_message(msg)
