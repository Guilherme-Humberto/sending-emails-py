from typing import TypedDict
from email.message import Message

class EmailConfig(TypedDict):
    emailFrom: str
    emailTo: str
    emailSubject: str

def configEmailMessage(emailMessage: str, emailConfig: EmailConfig):
    message = Message()
    message['from'] = emailConfig['emailFrom']
    message['to'] = emailConfig['emailTo']
    message['subject'] = emailConfig['emailSubject']
    message.add_header('Content-type', 'text/html')
    message.set_payload(emailMessage)
    return message