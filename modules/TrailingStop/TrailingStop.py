import sys, os
sys.path.insert(0,os.path.abspath("./"))

from resources.indices import index
from resources.Stock.stock import Stock
from resources.TD.td import TD
from config.config import config
from main import stockDict

api = TD()

def main():

    # Get the config information and save it as a dictionary
    ThisConfig = [module for module in config['modules'] if module['module'] == 'Trailing_Stop'][0]

    # Get the index and trail percentage from the config
    stockObjects = index[ThisConfig['index']]
    trailPercentage = ThisConfig['Trail_Percentage']
    
    currentPositions = api.getPositions()
    buyList = []
    sellList = []

    # find stock object in current positions
    for stock in stockObjects:
        if stock.ticker in currentPositions:

            # These are the only two values we need to perform this function
            currentPrice = stock.getCurrentPrice()
            sellPrice = currentPrice - (currentPrice * (trailPercentage / 100))

            # This will be used as a flag for print statement
            trajectory = ""

            if stock.hasattr('trailingStop'):
                if stock.trailingStop >= currentPrice:
                    sellList.append(stock)
                    trajectory = "STOCK SOLD"

                elif stock.trailingStop < sellPrice:
                    stock.trailingStop = sellPrice
                    trajectory = "TRAILING STOP INCREASED"

                else:
                    trajectory = "PRICE FELL. TRAILING STOP REMAINED CONSTANT"

            else:
                stock.trailingStop = sellPrice
                trajectory = "INITIAL TRAILING STOP ESTABLISHED"

        else:
            pass

        print(stock.ticker + " TRAILING STOP PRICE: " + str(stock.trailingStop))
        print(trajectory)
    
    return buyList, sellList


    

main()