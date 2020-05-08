#!/usr/bin/env checkio --domain=py run sendgrid-sendone

# To solve this mission you must use theSendGrid API Key(this video will explainhow to create your own API Key). Check out thesePython examples.
# 
# It all starts with your first email. Let’s try to send one.
# 
# Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and the name of the user.
# 
# Subject of the email should be "Welcome" and body simply "Hi {name}" ({name} should be replaced by a user's name)
# 
# Input:Two arguments: email and a username.
# 
# Output:None. You should send an email. You don’t need to return anything.
# 
# 
# send_email('a.lyabah@checkio.org', 'oduvan')
# send_email('somebody@gmail.com', 'Some Body')
# 
# END_DESC

import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
SUBJECT = 'Welcome'
# BODY = f'Hi {name}'


sg = sendgrid.SendGridAPIClient(API_KEY)



def send_email(email, name):
    message = Mail(
    from_email='andreyihnatchenko@gmail.com',
    to_emails=email,
    subject=SUBJECT,
    plain_text_content = f'Hi {name}')
    try:
        
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('andreyihnatchenko@gmail.com', 'Alex')
    print('Done')