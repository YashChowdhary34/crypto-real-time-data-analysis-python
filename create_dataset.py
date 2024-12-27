# requests
# pandas
# datetime

#This function is to get real time data from crypto currencty API everyday at 8:00 AM and will save the data into as a csv file

import requests
import schedule
import time
import pandas as pd
from datetime import datetime
from schedule_mail import send_mail

def get_crypto_data():
# API info
  url = 'https://api.coingecko.com/api/v3/coins/markets'

  param = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,
    'page': 1,
  }

  #sending request to the API
  response = requests.get(url, params=param)

  if response.status_code == 200:
    print('Data received')
    data = response.json()
    
    df = pd.DataFrame(data)
    
    #filtering the data to get only the columns we need
    df = df[["id", "name", "current_price", "market_cap", "total_volume", "high_24h", "low_24h", "price_change_percentage_24h", "last_updated"]]

    #creating a new column to store timestamp
    today = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    df['time_stamp'] = today

    #sorted_df = df.sort_values(by='price_change_percentage_24h', ascending=True)

    #getting bottom 10
    top_negative = df.nsmallest(10, 'price_change_percentage_24h')
    top_negative.to_csv(f'top_price_decrease_{today}.csv', index=False)
    #getting top 10
    top_positive = df.nlargest(10, 'price_change_percentage_24h')
    top_positive.to_csv(f'top_price_increase_{today}.csv', index=False) 

    #saving the data into a csv file
    df.to_csv(f'crypto_data_{today}.csv', index=False)
    print('Data saved in local directory')

    #call email function to send report
    subject = f'Crypto Data Report for {today}'
    body = f"""
    Good Morning!\n

    Your daily crypto data report is ready. Please find the attached files for more details.\n\n
    
    Top 10 cryptocurrencies with highest price increase in last 24 hours are attached.\n
    {top_positive}\n\n\n
    Top 10 cryptocurrencies with highest price decrease in last 24 hours are attached.\n
    {top_negative}\n\n\n

    Acctached is the complete data of all cryptocurrencies.\n\n

    Regards,\n
    Yash777
    """
    send_mail(subject, body, f'crypto_data_{today}.csv')

  else:
    print('Failed to get data from API')


#this will get executed only if we run this function
if __name__ == '__main__':
  get_crypto_data()
  #schedule the function to run everyday at 8:00 AM
  schedule.every().day.at('08:00').do(get_crypto_data)

  while True:
    schedule.run_pending()
    time.sleep(1)