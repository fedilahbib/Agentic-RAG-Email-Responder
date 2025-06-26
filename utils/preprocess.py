from bs4 import BeautifulSoup
from email.header import decode_header

def clean_html(raw_email):
    soup = BeautifulSoup(raw_email, "html.parser")
    return soup.get_text()
import re

def remove_signature(text):
    signature_patterns = [
        r"--\s*\n.*",                          # "--" followed by signature
        r"(Thanks|Regards|Best|Sincerely|Cheers)[\s\S]{0,100}$",  # closing phrases
        r"Sent from my.*"                      # mobile signatures
    ]
    for pattern in signature_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()
def strip_noise(text):
    text = re.split(r"(On\s.+?wrote:)", text)[0]
    text = re.sub(r"View this email in your browser.*", "", text)
    text = re.sub(r"http\S+", "", text)
    return text.strip()
def clean_email(raw_email):
    plain_text = clean_html(raw_email)
    no_signature = remove_signature(plain_text)
    cleaned_text = strip_noise(no_signature)
    return cleaned_text

def clean_subject(subject):
    decoded, encoding = decode_header(subject)[0]
    if isinstance(decoded, bytes):
        return decoded.decode(encoding if encoding else "utf-8")
    return decoded