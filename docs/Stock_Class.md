# **TD Ameritrade API**
This class is what interacts with the TD Ameritrade API to retrieve information about specific assets. It's main tool is the 'Requests' library since the API is designed to retrieve HTTP requests and return the data in the form of JSON. Below are all the methods and attributes that can be used with this class. Each ticker symbol is converted to a Stock object at the beginnig of the program being run. If you feel like some functionality is missing, please reach out. This class and documentation will be added too continuously as development continues.

---

## Table of Contents
1. [Methods](#Methods)
2. [Attributes](#attributes)
3. [Example](#example-script)

# Methods

## Get Current Price
   This method is pretty simple and requires no input. It takes the ticker attribute of the Stock object and returns the current price of a single share of the stock. 

   Example 
 ```
   ticker = "FB"
   ticker = Stock(ticker)

   ticker.getCurrentPrice()

   #Output
   grabbing current price of FB
   Current Price: 373.22
   ```

## Get Ten Day Average of Stock
This method requires no input and will return a Float value equal to the 10 day average of a specific stock. It is intended to track the moving average of a specific asset.

    Example
    
    ticker = "FB"
    ticker = Stock(ticker)

    print(ticker.tenDayAverage())

    #Output
    350.92879236507594
    

## Get Thirday Day Average of Stock
This method is identical to the ten day average method except it calculates the average stock price of the past thirty days.

Example
```
ticker = "FB"
ticker = Stock(ticker)

print(ticker.thirtyDayAverage())

#Output
351.46799999999996
```

## Buy and Sell a Specific Stock
These are two sepreate methods but are nearly identical besides one selling a stock and one buying it. These methods require three inputs. First is the quantity of stocks to be bought/sold in the transactin. The method also requires the headers derived from authorizing the TD account, and the account ID. These values can be derived from the [TD Class](TD_Class.md).

Example
```
ticker="FB"
ticker = Stock(ticker)

ticker.buyStock(2,account_ID, headers)
```

# Attributes
1. Stock.ticker
   
# Example
Below is an example script that incorporates some of the methods descibed above to give a better understanding of how to use this class.

```
ticker = "FB"
stock_object = Stock(ticker)

tenDay = stock_oject.tenDayAverage()
thirtyDay = stock_oject.thirtyDayAverage()

if tenDay >= thirtyDay:
    stock_object.buyStock
else:
    pass
```