import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'shreyashsingh17@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('sksinghjunior@gmail.com', 'bc5df643')
  smtp.send_message(email)
  print('all good boss!')