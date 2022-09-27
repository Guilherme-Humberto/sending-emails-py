from string import Template

def createEmailTemplate(users: list, template: str):
    with open(template, 'r', encoding='utf-8') as html:
        htmlTemplate = Template(html.read())

    emails = []
    for user in users:
        emailBody = htmlTemplate.safe_substitute(
            name=user['name'],
            username=user['username'],
            email=user['email'],
            address_street=user['address_street'],
            address_city=user['address_city'],
            address_zipcode=user['address_zipcode']
        )
        emails.append(emailBody)

    return emails