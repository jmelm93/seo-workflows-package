import yagmail
import pandas as pd

import sys
sys.path.insert(0, '..')

def send_gmail(email_to_list, email_from, email_password, subject, message, attachment="No Attachment"):

  try:
    if attachment == "No Attachment":
      contents=f'{message}'
    else:
      contents=[f'{message}',attachment]
    
    yag = yagmail.SMTP(user=email_from, password=email_password)

    for email in email_to_list:
      yag.send(to=email, subject=subject, contents=contents)
      print(subject)

  except Exception as e:
    exception_value = f"UnidentifiedError: {e}"
    raise Exception(exception_value)

def error_notification_email(tool_name, error_message, uid):
  send_gmail(
    email_to_list = [],
    email_from= '',
    email_password='',
    subject=f'Alert: Tool Error - {error_message} - ({tool_name})',
    # attachment=semrush_csvs,
    message= f"""
    <b>UID<b>: {uid}<br>
    <b>Context</b>: There has been an unidentified error on {tool_name} tool backend Python script. <br>
    <b>UnidentifiedError</b>: {error_message} <br>
    """)