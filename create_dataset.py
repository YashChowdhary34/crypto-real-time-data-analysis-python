import requests
import schedule
import time
import pandas as pd
from datetime import datetime
from schedule_mail import send_mail
from create_notebook import create_daily_report  # Importing notebook creation function

def get_crypto_data():
  # API info
  url = 'https://api.coingecko.com/api/v3/coins/markets'

  param = {
      'vs_currency': 'usd',
      'order': 'market_cap_desc',
      'per_page': 250,
      'page': 1,
  }

  # Sending request to the API
  response = requests.get(url, params=param)

  if response.status_code == 200:
    print('Data received')
    data = response.json()
    
    df = pd.DataFrame(data)

    # Filtering the data to get only the columns we need
    df = df[["id", "name", "current_price", "market_cap", "total_volume", "high_24h", "low_24h", "price_change_percentage_24h", "last_updated"]]

    # Creating a new column to store timestamp
    today = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    df['time_stamp'] = today

    # Save the complete dataset
    csv_filepath = f'crypto_data_{today}.csv'
    df.to_csv(csv_filepath, index=False)

    # Generate the Jupyter Notebook for analysis and forecasting
    notebook_filepath = create_daily_report(csv_filepath)

    # Prepare email content
    subject = f'Crypto Data Report for {today}'
    body = f"""
    Good Morning!\n

    Your daily crypto data report is ready. Please find the attached files for more details.\n\n
    - Attached is the complete data of all cryptocurrencies.
    - Also attached is a detailed analysis and forecasting report (Jupyter Notebook).\n\n

    Regards,\n
    Yash
    """

    # Send email with both CSV and Notebook
    send_mail(subject, body, csv_filepath, notebook_filepath)
    print("Email sent successfully with both attachments.")

  else:
      print('Failed to get data from API')

# Main execution and scheduling
if __name__ == '__main__':
    get_crypto_data()
    # Schedule the function to run everyday at 8:00 AM
    schedule.every().day.at('08:00').do(get_crypto_data)

    while True:
        schedule.run_pending()
        time.sleep(1)
