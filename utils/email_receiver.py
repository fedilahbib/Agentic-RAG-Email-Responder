import imaplib
import email
import os
from dotenv import load_dotenv
from utils.preprocess import clean_subject

load_dotenv()

class EmailReceiver:
    def __init__(self):
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.imap_server = "imap.gmail.com"
        self.emails = []
    def fetch_unread_emails(self):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_address, self.email_password)
        mail.select("inbox")

        status, messages = mail.search(None, '(UNSEEN)')
        email_ids = messages[0].split()

        for email_id in email_ids:
            _, msg_data = mail.fetch(email_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = clean_subject(msg["Subject"])
                    from_addr = msg["From"]
                    content = self.get_email_body(msg)

                    self.emails.append({"subject":subject,"content":content,"from_addr":from_addr})
        mail.logout()

    def get_email_body(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if content_type == "text/plain" and "attachment" not in content_disposition:
                    return part.get_payload(decode=True).decode(errors="ignore")
        else:
            return msg.get_payload(decode=True).decode(errors="ignore")
        return ""
