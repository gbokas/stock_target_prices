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

def target2(i):
    global price
    global target
    global average_vol
    global market_cap
    global lower
    global earning
    try:
        price[i] = float(Share(i).get_one_yr_target_price())
        price[i] -= float(Share(i).get_price())
        price[i] = price[i]/float(Share(i).get_one_yr_target_price())
        target[i] = float(Share(i).get_one_yr_target_price())
        market_cap[i] = Share(i).get_market_cap()
        average_vol[i] = float(Share(i).get_avg_daily_volume())
        lower[i] = Share(i).get_percent_change_from_year_high()
        earning[i] = float(Share(i).get_price_earnings_growth_ratio())
    except HTTPError as e:
        target2(i)
    return True

price = {}
target = {}
average_vol = {}
market_cap = {}
lower = {}
earning = {}

all_stocks = ('AAPL', 'AKAM', 'YHOO', 'ADBE', 'TTWO', 'ADNT', 'ORCL', 'TSLA', 'MSFT', 'GOOG', 'GOOGL', 'AMD', 'MU', 'VEEV', 'FB', 'FIT', 'YELP', 'V', 'FCAU', 'TWTR', 'AMAT', 'UNH', 'BAC', 'BA', 'DIS', 'NOK', 'RHT', 'WDC', 'WFT', 'INTC', 'CELG', 'KLAC', 'SHOP', 'SBUX', 'MMM', 'ABT', 'ATVI', 'AAP', 'APD', 'LNT', 'AAL', 'AXP', 'AMGN', 'ADI', 'T', 'ADSK', 'ADP', 'BBY', 'BIIB', 'BSX', 'AVGO', 'KMX', 'CAT', 'CSCO', 'KO', 'CL', 'CMCSA', 'DAL', 'EBAY', 'EA', 'EXPE', 'XOM', 'F', 'GE', 'GILD', 'GS', 'GT', 'HOG', 'ITW', 'IBM', 'JNJ', 'JPM', 'LRCX', 'LMT', 'MA', 'MS', 'NFLX', 'NKE', 'NVDA', 'PFE', 'RL', 'PCLN', 'PG', 'QCOM', 'RTN', 'STX', 'LUV', 'SYMC', 'TDC', 'TXN', 'TMO', 'WFC' , 'SWKS', 'AAOI', 'CRUS', 'ACIA', 'BRKS', 'ASML', 'CCMP', 'CY', 'AEO', 'BBRY', 'BOX', 'FEYE', 'KATE', 'IRWD', 'TELL', 'BIDU', 'CRM', 'MBLY', 'WATT', 'GSIT', 'AMBA', 'TRIP', 'ALK', 'SQ', 'TWLO', 'BABA', 'EXAS', 'TREE', 'WYNN', 'EXC', 'JWN', 'AYI', 'RIG', 'ARNC', 'MNK', 'PWR', 'MOS', 'JEC', 'FRT', 'HBI', 'AXTA', 'BK', 'CHTR', 'COST', 'DNOW', 'DVA', 'FOXA', 'GHC', 'GM', 'LBTYA', 'LSXMA', 'LSXMK', 'MCO', 'MDLZ', 'MON', 'MTB', 'PSX', 'QSR', 'SIRI', 'SNY', 'TMK', 'UAL', 'UPS', 'USB', 'USG', 'VRSK', 'VRSN', 'VZ', 'WBC', 'WMT', 'CAMP', 'RARE', 'RDUS', 'MCHP', 'IDTI', 'MXIM', 'SMTC', 'SLAB', 'ON', 'SPWR', 'RUN')
#all_stocks= ('LSXMA', 'LSXMK', 'AAPL')
#all_stocks = ('AAPL', 'AKAM', 'YHOO', 'ADBE', 'TTWO', 'ADNT', 'ORCL', 'TSLA', 'MSFT', 'GOOG', 'GOOGL', 'AMD', 'MU', 'VEEV', 'FB', 'FIT', 'YELP', 'V', 'TWTR', 'AMAT', 'UNH', 'BAC', 'BA', 'DIS', 'NOK', 'RHT', 'WDC', 'INTC', 'CELG', 'KLAC', 'SHOP', 'SBUX', 'MMM', 'ABT', 'ATVI', 'APD', 'LNT', 'AAL', 'AMGN', 'ADI', 'ADP', 'BIIB', 'AVGO', 'CSCO', 'CMCSA', 'DAL', 'EBAY', 'EA', 'EXPE', 'XOM', 'F', 'GE', 'GS', 'IBM', 'JNJ', 'JPM', 'LRCX', 'LMT', 'MA', 'MS', 'NFLX', 'NKE', 'NVDA', 'PFE', 'PCLN', 'PG', 'QCOM', 'RTN', 'STX', 'LUV', 'TXN', 'TMO', 'SWKS', 'AAOI', 'ACIA', 'CY', 'BOX', 'KATE', 'CRM', 'AMBA', 'ALK', 'SQ', 'TWLO')
#print(len(all_stocks))

for i in all_stocks:
    print(i)
#    try:
#        price[i] = float(Share(i).get_one_yr_target_price())
#        price[i] -= float(Share(i).get_price())
#        price[i] = price[i]/float(Share(i).get_price())*100
    target2(i)
#    except HTTPError as e:
#        try:
#            time.sleep(1)
#            content = e.read()
#            price[i] = float(Share(i).get_one_yr_target_price())
#            print(i, price[i])
#            price[i] -= float(Share(i).get_price())
#            time.sleep(1)
#            price[i] = price[i]/float(Share(i).get_price())*100
#        except HTTPError as e:
#            time.sleep(1)
#            content = e.read()
#            price[i] = float(Share(i).get_one_yr_target_price())
#            print(i, price[i])
#            price[i] -= float(Share(i).get_price())
#            time.sleep(1)
#            price[i] = price[i]/float(Share(i).get_price())*100
#        print(i, Stock(i).get_latest_price())
#    target.append(float(Share(i).get_one_yr_target_price()))
#    print(i, Share(i).get_price(), Share(i).get_one_yr_target_price())

#print(all_stocks[price.index(max(price))])
#print((np.array(target)-np.array(price))/np.array(target)*100)
#teliko = pd.DataFrame.from_dict(price, orient='index')
teliko = pd.DataFrame([price, target, average_vol, market_cap, lower, earning])
teliko = teliko.T
teliko =teliko.rename(columns={0:'Target_price_percentage', 1:'Target price', 2:'Average Volume', 3:'Market Cap', 4:'Percentage Lower than Year High', 5:'EPS'})

#teliko.columns = ['Target_price_percentage']
#teliko['Target'] = target

teliko.sort(['Target_price_percentage']).to_csv('out.csv')

#teliko.to_csv('out.csv')
#print(teliko.sort(['Target_price_percentage']))
print(teliko)
#print(sorted(price.items(), key=lambda x:(x[1],x[0])))


start =datetime.datetime(2010,1,1)
end = datetime.date.today()
start2=datetime.datetime(2016,1,1)


