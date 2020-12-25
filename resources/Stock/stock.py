# TraderPY Stock Class
#
# Written By Sam Gulinello
# MIT Licensed
#
# For More Information About This Project Go to 
# https://github.com/SamGulinello/TraderPY

import requests
from config.config import config
client_id = config["client_id"]

# Each ticker will be converted to a stock object
class Stock():

    def __init__(self,ticker):
        self.ticker = ticker

    def getCurrentPrice(self):

        # Get ticker value
        ticker = self.ticker
        print("grabbing current price of " + ticker)

        # Define the endpoint
        endpoint = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker)

        # Define the payload
        payload = {'apikey':client_id,
                    'periodType':'day',
                    'freqencyType':'minute',
                    'frequency':'1',
                    'period':'1',
                    'needExtendedHoursData':'true'}

        # Send the request and recieve data      
        content = requests.get(url=endpoint, params=payload)

        # Convert the data into a list of prices
        data = content.json()
        data = data['candles']
        data = data[-1]

        currentPrice = data['close']
        self.currentPrice = currentPrice
        print("Current Price: " + str(currentPrice))
        return(currentPrice)

    # Method to determine and return the 10 day average stock price of a company
    def tenDayAverage(self):
        # Get ticker value
        ticker = self.ticker
        #print("grabbing ten day average of " + ticker)

        # Define the endpoint
        endpoint = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker)

        # Define the payload
        payload = {'apikey':client_id,
                    'periodType':'day',
                    'freqencyType':'minute',
                    'frequency':'1',
                    'period':'10',
                    'needExtendedHoursData':'true'}

        # Send the request and recieve data      
        content = requests.get(url=endpoint, params=payload)

        # Convert the data into a list of prices
        data = content.json()
        data = data['candles']

        # Average the values of all the prices
        averagePrice = 0
        for i in data:
            openPrice = i['open']
            averagePrice = averagePrice + openPrice
            
        averagePrice = averagePrice / len(data)
        
        print("Ten Day Average: " + str(averagePrice))
        return averagePrice


    def thirtyDayAverage(self):

        # Get ticker value
        ticker = self.ticker
        #print("grabbing thirty day average of " + ticker)

        # Define the endpoint
        endpoint = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker)

        # Define the payload
        payload = {'apikey':client_id,
                    'periodType':'month',
                    'freqencyType':'minute',
                    'frequency':'1',
                    'period':'1',
                    'needExtendedHoursData':'true'}

        # Send the request and recieve the data       
        content = requests.get(url=endpoint, params=payload)

        # Convert the data into a list of prices
        data = content.json()
        data = data['candles']

        # Average the values of all the prices
        averagePrice = 0
        for i in data:
            openPrice = i['open']
            averagePrice = averagePrice + openPrice

        averagePrice = averagePrice / len(data)

        print("Thirty day average: " + str(averagePrice))
        return averagePrice

    def buyStock(self,quantity,account_id,headers):

        # define our headers
        header = headers

        # define the endpoint for Saved orders, including your account ID
        endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders".format(account_id)

        # define the payload, in JSON format
        payload = {'orderType':'MARKET',
                'session':'NORMAL',
                'duration':'DAY',
                'orderStrategyType':'SINGLE',
                'orderLegCollection':[{'instruction':'Buy','quantity':quantity,'instrument':{'symbol':self.ticker,'assetType':'EQUITY'}}]}


        # Send the request
        requests.post(url = endpoint, json = payload, headers = header)

    def sellStock(self,quantity,account_id,headers):

        # define our headers
        header = headers

        # define the endpoint for Saved orders, including your account ID
        endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders".format(account_id)

        # define the payload, in JSON format
        payload = {'orderType':'MARKET',
                'session':'NORMAL',
                'duration':'DAY',
                'orderStrategyType':'SINGLE',
                'orderLegCollection':[{'instruction':'Sell','quantity':quantity,'instrument':{'symbol':self.ticker,'assetType':'EQUITY'}}]}


        # Send the request
        requests.post(url = endpoint, json = payload, headers = header)