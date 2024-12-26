import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase  
import email.encoders as Encoders

import requests
import schedule
from datetime import datetime
import time
import pandas as pd

from create_dataset import get_crypto_data

def send_mail(receiver_email, subject, body, file_name):
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587
  sender_email = 'ychowdhary777@gmail.com'
  email_password = 'password@2608'
  
  #compose the email
  message = MIMEMultipart()
  message['From'] = sender_email
  message['To'] = receiver_email
  message['Subject'] = subject

  #attach the body
  message.attach(MIMEText(body, 'plain'))
  