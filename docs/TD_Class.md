# **TD Ameritrade API**
This class is what interacts with the TD Ameritrade API. It's main tool is the 'Requests' library since the API is designed to retrieve HTTP requests and return the data in the form of JSON. Below are all the methods and attributes that can be used with this class. If you feel like some functionality is missing, please reach out. This class and documentation will be added too continuously as development continues.

---

## Table of Contents
1. [Methods](#Methods)
2. [Attributes](#attributes)
3. [Example](#example-script)

---
# Methods

## Authorize Your Account
   This method is **NECESSARY FOR OTHER REQUESTS TO BE MADE**. It should be executed at the beginning of the module. It authorizes the app with TD Ameritrade and returns a unique value to verify other requests. The value only lasts for 30 minutes so keep that in mind. There are no inputs to this function.


## Get Account Data
   This method will return a json dictionary full of account details. It requires no input values but be sure to have authorized the account within 30 minutes of calling this function.

   Example
   ```
   account = td.accountEndpoint()
   ```
   See [TD Documentation](https://developer.tdameritrade.com/account-access/apis/get/accounts-0) for sample output.(Too long to include here)

## Get Current Positions
   This method will return a dictionary of the stocks held in your portfolio paired with the quantity. The first position listed will be named MMDA1. This is a name TD Ameritrade gives to the account they use to invest your free money. Feel free to ignore it. This method returns a dictionary.

   Example
   ```
   positions = td.getPositions()

   #Sample Output
   {'MMDA1': 600.00, 'BABA' : 2, 'TSLA' : 5}
   ```

## Get Account ID
   The Account ID is commonly used in other methods within the class. TD Ameritrade uses it as a verifier. This is seperate from the client_id specified in config. Returns and int.

   Example
   ```
   account_id = td.getAccountID()

   #Sample Output
   12345678
   ```

## Get Current Buying Power
   The buying power is a measure of spendable cash on new stocks. This is an essential number to know when going to buy positions. Returns and float

   Example
   ```
   buying_power = td.getBuyingPower()

   #Sample Output
   123.00
   ```

## Get Current Account Value
   This number is the liquidation value of your account. It is the sum of the values of your positions and your current buying power. Returns a float

   Example
   ```
   account_value = td.getAccountValue()

   # Sample Output
   1000.00
   ```

## Get Data on a Specific Position Held in Your Portfolio
   This method will return a dictionary of values that pertain to a specific position in your portfolio. It takes an optional argument for the ticker symbol you like to see information on. If no ticker symbol is given, it will return the information on every position of your portfolio

   Example
   ```
   data = td.getPositionValue(ticker='TSLA')
   ```

   Sample output can be found at the [TD Ameritrade](https://developer.tdameritrade.com/account-access/apis/get/accounts-0) documentation.

# Attributes

Quick Warning: *Due to frequency of change to the data used in this class, these value may not always be 100% accurate*

1. td.headers
   - This is the value returned from authorizing the account
3. td.accountID
4. td.currentPositions
5. td.buyingPower

# Example Script

Below is an example of this class authorizing a TD account and getting the long quantitiy of a position if it held in the portfolio. Hopefully this will give you a better understanding on how to use this class.

```
from resources.TD.td import TD

api = TD()
ticker = 'FB'
currentPositions = api.getPositions()

if ticker in currentPositions:
   print(api.getPositionValue(ticker = ticker))
else:
   print(ticker + "is not in your current positions")

```







   

