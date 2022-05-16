# TraderPY Main File
#
# Written By Sam Gulinello
# MIT Licensed
#
# For More Information About This Project Go to 
# https://github.com/SamGulinello/TraderPY

# Imports required for the program to work properly
from datetime import time, datetime, date

# Add this as the root directory on the PATH
# Sources said this was a terrible solution but
# never provided a working option so...
import sys, os
sys.path.insert(0,os.path.abspath("./"))

from resources.indices import index
from resources.TD.td import TD
from resources.Stock.stock import Stock
from config.config import config
import time
import importlib
import operator
import threading

# Create Dictionary to be Used as Reference Throughout Program
stockDict = {
    "currentHoldings" : {},
    "buyList" : [],
    "sellList" : [],
}

# Function to find and return current time
def getTime():
    currentTime = datetime.now()
    currentTime = time.strftime("%H%M%S")
    
    return currentTime

def TraderPy():

    # First Check to Ensure Program is Working Properly
    print("running")

    # Instantiate each stock into a Stock object and append it to the stockObjects Array
    for i in index:
        for n, j in enumerate(index[i]):
            index[i][n] = Stock(index[i][n])

    # Instantiate the TD class and authorize the account with TD
    api = TD()

    # This program is designed to run continuously and execute at the close of the markets
    while(True):
        if getTime() == "163000":

            print("----------- Current Date: {} ----------".format(date.today()))
         
            stockDict["currentHoldings"] = api.getPositions()
            
            # Cycle through the modules listed in config file
            # Each module with add to the buy and sell list
            for module in config["modules"]:
                current = module["module"]    
                fullname = 'modules.' + current + '.' + current

                currentmodule = importlib.import_module(fullname)
                buyList, sellList = currentmodule.main()
                stockDict['buyList'].extend(buyList)
                stockDict['sellList'].extend(sellList)

            accountID = api.accountID
            headers = api.headers

            # Sell everything in sellList
            print("selling items on sellList")

            for i in stockDict['sellList']:
                print('selling ' + i.ticker)
                i.sellStock(1,accountID,headers)
                stockDict['currentHoldings'].pop(i.ticker)
                time.sleep(2)

            # Buy items off buy list
            print("buying items on buyList")

            buyingPower = api.getBuyingPower()

            for i in buyList:
                sharePrice = i.getCurrentPrice() 
                
                # ensure program never attempts to buy more than what can be afforded
                if sharePrice < buyingPower:
                    print("buying " + i.ticker)
                    
                    # function needs number of shares, TD Accound ID, and Headers gathered from authorization
                    i.buyStock(1,accountID,headers)
                    stockDict['currentHoldings'].update({i.ticker:1})
                    
                    buyingPower = buyingPower - sharePrice
                    time.sleep(2)
                else:
                    break
            
            # convert the objects in both lists to strings
            for i in stockDict['buyList']:
                i = i.ticker
                
            for i in stockDict['sellList']:
                i = i.ticker
                
            print(stockDict)

            # Clear the buy and sell list to get ready for the next day
            stockDict['buyList'].clear()
            stockDict['sellList'].clear()

            print(stockDict)

        else:
            pass