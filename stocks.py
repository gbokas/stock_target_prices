import pandas as pd
import numpy as np
#from pandas_datareader import data as web
import datetime
import matplotlib.pyplot as plt
import time
from sys import argv
from rtstock.stock import Stock
from urllib.error import HTTPError
from yahoo_finance import Share


price = {}
target = []

all_stocks = ('AAPL', 'AKAM', 'YHOO', 'ADBE', 'TTWO', 'ADNT', 'ORCL', 'TSLA', 'MSFT', 'GOOG', 'GOOGL', 'AMD', 'MU', 'VEEV', 'FB', 'FIT', 'YELP', 'V', 'FCAU', 'TWTR', 'AMAT', 'UNH', 'BAC', 'BA', 'DIS', 'NOK', 'RHT', 'WDC', 'WFT', 'INTC', 'CELG', 'KLAC', 'SHOP', 'SBUX', 'MMM', 'ABT', 'ATVI', 'AAP', 'APD', 'LNT', 'AAL', 'AXP', 'AMGN', 'ADI', 'T', 'ADSK', 'ADP', 'BBY', 'BIIB', 'BSX', 'AVGO', 'KMX', 'CAT', 'CSCO', 'KO', 'CL', 'CMCSA', 'DAL', 'EBAY', 'EA', 'EXPE', 'XOM', 'F', 'GE', 'GILD', 'GS', 'GT', 'HOG', 'ITW', 'IBM', 'JNJ', 'JPM', 'LRCX', 'LMT', 'MA', 'MS', 'NFLX', 'NKE', 'NVDA', 'PFE', 'RL', 'PCLN', 'PG', 'QCOM', 'RTN', 'STX', 'LUV', 'SYMC', 'TDC', 'TXN', 'TMO', 'WFC' , 'SWKS', 'AAOI', 'CRUS', 'ACIA', 'BRKS', 'ASML', 'CCMP', 'CY', 'AEO', 'BBRY', 'BOX', 'FEYE', 'KATE', 'IRWD', 'TELL', 'BIDU', 'CRM', 'MBLY', 'WATT', 'GSIT')
#all_stocks=all_stocks[-5:]

for i in all_stocks:
    try:
#    price.append(float(Share(i).get_price()))
        price[i] = float(Share(i).get_one_yr_target_price())
        price[i] -= float(Share(i).get_price())
        price[i] = price[i]/float(Share(i).get_price())*100
#        print(i, Stock(i).get_latest_price())
    except HTTPError as e:
        time.sleep(1)
        content = e.read()
        price[i] = float(Share(i).get_one_yr_target_price())
        print(i, price[i])
        price[i] -= float(Share(i).get_price())
        time.sleep(1)
        price[i] = price[i]/float(Share(i).get_price())*100
#        print(i, Stock(i).get_latest_price())
#    target.append(float(Share(i).get_one_yr_target_price()))
#    print(i, Share(i).get_price(), Share(i).get_one_yr_target_price())

#print(all_stocks[price.index(max(price))])
#print((np.array(target)-np.array(price))/np.array(target)*100)
teliko = pd.DataFrame.from_dict(price, orient='index')
teliko.columns = ['Target_price_percentage']



print(teliko.sort(['Target_price_percentage']))
print(sorted(price.items(), key=lambda x:(x[1],x[0])))


start =datetime.datetime(2010,1,1)
end = datetime.date.today()
start2=datetime.datetime(2016,1,1)


