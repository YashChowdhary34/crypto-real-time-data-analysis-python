# Crypto Realtime Data Analysis with Automated Reporting

<div align="center">
    <img src="https://github.com/user-attachments/assets/e5a594ab-ce2b-4a42-a071-28806c29e833" alt="Coingecko Logo" height="300" width="500">
</div>

---

## Overview

This project is a Python-based system that fetches real-time cryptocurrency data daily from the CoinGecko API, processes the data to identify key trends, and sends an automated email report with detailed analysis. The focus is on automation, combining API integration, data analysis, and email communication.

---

## Table of Contents

- [Introduction](#introduction)
- [Tech Stack](#tech-stack)
- [Email Report Example](#email-report-example)
- [Code Breakdown](#code-breakdown)
  - [1. Fetching Crypto Data](#1-fetching-crypto-data)
  - [2. Processing and Saving Data](#2-processing-and-saving-data)
  - [3. Email Automation](#3-email-automation)
  - [4. Scheduling Daily Execution](#4-scheduling-daily-execution)
- [Future Work](#future-work)
- [Conclusion](#conclusion)

---

## Introduction

The cryptocurrency market is highly volatile, with prices fluctuating every second. Staying on top of these changes can be overwhelming. This project addresses that challenge by automating the retrieval, analysis, and reporting of crypto market trends daily. The core functionality includes:

1. Fetching data from the CoinGecko API.
2. Identifying the top 10 gainers and losers in terms of percentage price change.
3. Sending an email report with both a summary and detailed `.csv` files.
4. Running this workflow automatically every day at 8:00 AM.

---

## Tech Stack

The following technologies and libraries were used in this project:

- **Python**: Programming language for building the solution.
- **`requests`**: For making API calls to CoinGecko.
- **`pandas`**: For data manipulation and analysis.
- **`smtplib` and `email`**: For email automation.
- **`schedule`**: For scheduling daily task execution.
- **`time`**: For loop delays to manage scheduling.
- **`datetime`**: For timestamping and file naming.

---

## Email Report Example

<img src="https://github.com/user-attachments/assets/b04c817b-4a84-4f1f-a689-cf563661722a" alt="Email Screenshot" width="800" height="400">

---

## Code Breakdown

### 1. Fetching Crypto Data
This section retrieves real-time cryptocurrency data from the CoinGecko API.

```python
import requests
import pandas as pd
from datetime import datetime

def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 250,
        'page': 1,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print('Data received')
        return response.json()
    else:
        print('Failed to fetch data')
        return None
```

### 2. Processing and Saving Data
The fetched data is processed, and the top gainers and losers are saved into `.csv` files.

```python
from datetime import datetime

def process_data(data):
    df = pd.DataFrame(data)
    df = df[["id", "name", "current_price", "market_cap", "total_volume", "high_24h", "low_24h", "price_change_percentage_24h", "last_updated"]]

    today = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    df['time_stamp'] = today

    # Save overall data
    df.to_csv(f'crypto_data_{today}.csv', index=False)

    # Save top 10 gainers and losers
    df.nsmallest(10, 'price_change_percentage_24h').to_csv(f'top_price_decrease_{today}.csv', index=False)
    df.nlargest(10, 'price_change_percentage_24h').to_csv(f'top_price_increase_{today}.csv', index=False)

    print('Data saved locally')
```

### 3. Email Automation
The `send_mail` function sends the processed `.csv` files via email.

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders as Encoders

def send_mail(subject, body, filename):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    email_password = 'your_password'
    receiver_email = 'recipient_email@gmail.com'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={filename}')
        message.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')
```

### 4. Scheduling Daily Execution
The `schedule` library is used to run the task daily at 8:00 AM.

```python
import schedule
import time

if __name__ == '__main__':
    schedule.every().day.at('08:00').do(get_crypto_data)

    while True:
        schedule.run_pending()
        time.sleep(1)
```

---

## Future Work

To make this system more insightful and actionable, I plan to:

1. **Develop an automated data analysis system**:
    - Use machine learning to predict trends based on historical data.
    - Generate interactive visualizations using tools like Plotly or Matplotlib.
2. **Store data in a database**:
    - Integrate a database like MongoDB or PostgreSQL for better data management.
    - Build a dashboard for real-time monitoring of cryptocurrency trends.
3. **Enhance email reports**:
    - Include graphical summaries of top gainers/losers.
    - Add multi-recipient functionality.

---

## Conclusion

This project demonstrates the power of automation in simplifying complex tasks like real-time data analysis and reporting. By combining Python libraries with API integration, email automation, and scheduling, this project serves as a robust tool for staying informed about the volatile cryptocurrency market. Future enhancements will make it even more scalable and insightful.
