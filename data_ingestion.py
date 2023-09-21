# get API Key From https://www.alphavantage.co/


import requests
import pandas as pd
import time
from datetime import datetime


if datetime.now().month <= 9:
    limit = f'{datetime.now().year}0{datetime.now().month}'
else:
    limit = f'{datetime.now().year}{datetime.now().month}'


year = 2018
month = '01'
api_key = 'demo'
symbol = 'TCS'


count = 1

while True:
    print(f'Pulling data for {year}-{month}')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&month={year}-{month}&outputsize=full&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    if data.get('Time Series (5min)') == None:
        print(data)
        print(f'Sleeping the Job for 90 Sec total count API calls {count}')
        time.sleep(90)
        
        if count > 100:
            break
        continue

    count += 1
    
    time_data = data['Time Series (5min)']

    json_data = []

    for i in time_data.keys():
        temp_data = {
                    'Symbol':symbol,
                    'open': time_data[i]['1. open'],
                    'high': time_data[i]['2. high'],
                    'low': time_data[i]['3. low'],
                    'close': time_data[i]['4. close'],
                    'volume': time_data[i]['5. volume'],
                    'timestamp': i
                    }
        
        json_data.append(temp_data)


    df = pd.json_normalize(json_data)
    df.to_csv(f'{symbol}_Stock_Data.csv', mode='a' , sep=',', encoding='utf-8')

    month = int(month)
    if int(f'{year}{month}') < limit:
        if month == 12:
            year += 1
            month = '01'
        else:
            month += 1
            if month < 10:
                month = f'0{month}'
    else:
        break







