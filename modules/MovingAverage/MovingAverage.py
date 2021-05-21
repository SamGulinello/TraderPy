# TraderPY MovingAverage Module
#
# Written By Sam Gulinello
# MIT Licensed
#
# For More Information About This Project Go to 
# https://github.com/SamGulinello/TraderPY

# import time
# import operator
from resources.indices import index
from resources.Stock.stock import Stock
from resources.TD.td import TD
from config.config import config
from main import stockDict

import sys

api = TD()

def printProgressBar(i,maximum, ticker):

    n_bar = 100
    j = i/maximum

    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(n_bar * j):{n_bar}s}] {int(100 * j)}%")
    sys.stdout.write('\r')
    sys.stdout.flush()

def main():
    # Get the config information and save it as a dictionary
    ThisConfig = [module for module in config['modules'] if module['module'] == 'MovingAverage'][0]
    print(ThisConfig)
    
    # Get the index from the config
    stockObjects = index[ThisConfig['index']]
    buyingPowerScale = ThisConfig['buying_power_allocation']/100
    buyingPower = api.getBuyingPower() * (buyingPowerScale)

    # Create a reference attribute for each Stock object
    # This should only be done the first time through
    for i in stockObjects:
        if hasattr(i, 'reference'):
            pass
        else:
            i.reference = None

    # These will be populated and returned to the main module
    buyList, sellList = [],[]

    count = 0
    print("UPDATING MOVING AVERAGES")
    for i in stockObjects:
        # This will be used to compare to new comparison of 10 vs 30 Day
        reference = i.reference

        # print('evaluating ' + str(i.ticker) + ' ...')
        
        # Get new 10 and 30 day averages
        try:
            lowerBound = i.tenDayAverage()
            upperBound = i.thirtyDayAverage()
            # Determine new references
            if lowerBound < upperBound:
                i.reference = 'below'
            elif lowerBound > upperBound:
                i.reference = 'above'
            else:
                pass
        except:
             print("failed to retrieve information on " + i.ticker)
             pass
        

        
        # Determine buy, sell, or pass
        if reference == i.reference:
            pass
        elif reference != i.reference:
            if reference == 'above':
                buyList.append(i)
            elif reference == 'below' and i.ticker in stockDict["currentHoldings"]:
                sellList.append(i)
            else:
                pass
        
        printProgressBar(count, len(stockObjects), i.ticker)
        count += 1;
            
    #sort buyList in ascending order    
    buyList.sort(key=lambda Stock: Stock.getCurrentPrice())
    
    #ensure buyList total is less than allocated buying power
    totalPrice = 0
    for stock in buyList:
        totalPrice = totalPrice + stock.getCurrentPrice()
        if totalPrice > buyingPower:
            buyList.remove(stock)

    # Prep stocks to be printed to consol
    printList = []
    for stock in buyList:
        printList.append(stock.ticker)

    print("BUY LIST: " + str(printList))

    return buyList, sellList




