from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv
load_dotenv()

import os

def send_email(subject_line, content):

    email_from = os.environ.get('SENDGRID_FROM')
    email_to = os.environ.get('SENDGRID_TO')

    message = Mail(
        from_email=email_from,
        to_emails=email_to,
        subject=subject_line,
        html_content=content )

    try:
        api_key = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(api_key)
        # sg = SendGridAPIClient(sendgrid_api)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        
    except Exception as e:
        print(e.message)