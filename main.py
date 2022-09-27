from src.config import config
from src.smtp.smtp import smptServer
from src.users.getUsers.user import readUsersCsvFile
from src.email.message.message import configEmailMessage
from src.email.template.template import createEmailTemplate

usersCsvFile = './src/users/csv/users.csv'
emailTplFile = './src/email/html/email.html'

users = readUsersCsvFile(usersCsvFile)
emails = createEmailTemplate(users, emailTplFile)

def sendEmail():
    for index, user in enumerate(users):
        sender = configEmailMessage(
            emailMessage=emails[index], 
            emailConfig={
                'emailFrom': config.emailSender,
                'emailTo': user['email'],
                'emailSubject': 'Teste envio de email com python'
            })

        smptServer(msg=sender, email={
            'emailFrom': config.emailSender, 
            'emailTo': user['email'] 
        })

sendEmail()