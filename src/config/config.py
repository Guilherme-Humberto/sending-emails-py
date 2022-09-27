import os
from dotenv import load_dotenv

load_dotenv()

smtpPort = os.getenv("SMTP_PORT")
smtpHost = os.getenv("SMTP_HOST")
emailSender = os.getenv("EMAIL_SENDER")
gmailAppPassword = os.getenv("GMAIL_APP_PASSWORD")