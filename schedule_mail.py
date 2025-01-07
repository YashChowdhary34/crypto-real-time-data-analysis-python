import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail(subject, body, csv_filepath, notebook_filepath):
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587
  sender_email = 'ychowdhary777@gmail.com'
  email_password = 'app_password'  # Replace with an actual app password
  receiver_email = 'yashchowdhary34@gmail.com'

  try:
      # Compose the email
      message = MIMEMultipart()
      message['From'] = sender_email
      message['To'] = receiver_email
      message['Subject'] = subject

      # Attach the email body
      message.attach(MIMEText(body, 'plain'))

      # Attach the CSV file
      with open(csv_filepath, 'rb') as f:
          part = MIMEBase('application', 'octet-stream')
          part.set_payload(f.read())
          encoders.encode_base64(part)
          part.add_header('Content-Disposition', f'attachment; filename={csv_filepath.split("/")[-1]}')
          message.attach(part)

      # Attach the Jupyter Notebook file
      with open(notebook_filepath, 'rb') as f:
          part = MIMEBase('application', 'octet-stream')
          part.set_payload(f.read())
          encoders.encode_base64(part)
          part.add_header('Content-Disposition', f'attachment; filename={notebook_filepath.split("/")[-1]}')
          message.attach(part)

      # Connect to the server and send the email
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(sender_email, email_password)
          text = message.as_string()
          server.sendmail(sender_email, receiver_email, text)
          print('Email sent successfully')

  except Exception as e:
      print('Failed to send email')
      print(e)
