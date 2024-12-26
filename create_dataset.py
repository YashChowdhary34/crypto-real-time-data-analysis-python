# requests
# pandas
# datetime

#This function is to get real time data from crypto currencty API everyday at 8:00 AM and will save the data into as a csv file

import requests
import pandas as pd
from datetime import datetime

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
  else:
    print('Failed to get data from API')

