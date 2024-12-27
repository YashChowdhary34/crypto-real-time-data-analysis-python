import smtplib 
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase  
import email.encoders as Encoders


def send_mail(subject, body, filename):
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587
  sender_email = 'ychowdhary777@gmail.com'
  email_password = 'app_password'
  receiver_email = 'yashchowdhary34@gmail.com'

  #compose the email
  message = MIMEMultipart()
  message['From'] = sender_email
  message['To'] = receiver_email
  message['Subject'] = subject

  #attach the body
  message.attach(MIMEText(body, 'plain'))
  

  #attach csv file
  with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    email.encoders.encode_base64(part) #encode the attachment
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')
    message.attach(part)

  #connect to the server
  try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
      server.starttls() #secure connection
      server.login(sender_email, email_password)
      text = message.as_string() #convert the message to a string
      server.sendmail(sender_email, receiver_email, text)
      print('Email sent successfully')
  except Exception as e:
    print('Failed to connect to the server')
    print(e)