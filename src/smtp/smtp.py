from smtplib import SMTP
from typing import TypedDict
from src.config import config

class SmtpServer(TypedDict):
    emailFrom: str
    emailTo: str

def smptServer(msg, email: SmtpServer):
    with SMTP(host=config.smtpHost, port=config.smtpPort) as smtp:
        smtp.starttls()
        smtp.login(
            user=config.emailSender, 
            password=config.gmailAppPassword
        )
        smtp.sendmail(
            from_addr=email['emailFrom'], 
            to_addrs=email['emailTo'], 
            msg=msg.as_string().encode('utf-8')
        )

    print(f'Email enviado para {email["emailTo"]}')