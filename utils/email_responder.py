import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

class EmailResponder:
    def __init__(self):
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_auto_reply(self, to_email, original_subject,content):
        reply = EmailMessage()
        reply["From"] = self.email_address
        reply["To"] = to_email
        reply["Subject"] = f"Re: {original_subject}"
        reply.set_content(content)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(self.email_address, self.email_password)
            smtp.send_message(reply)
            print(f"Replied to {to_email}")