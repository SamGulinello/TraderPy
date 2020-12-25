# TraderPY TD Class
#
# Written By Sam Gulinello
# MIT Licensed
#
# For More Information About This Project Go to 
# https://github.com/SamGulinello/TraderPY

from splinter import *
#from selenium import *
from operator import attrgetter
from urllib.parse import urlparse
from config.config import config
import requests
import urllib
import time

# Valuable Account Information Necessary for API
client_id = config["client_id"]
account_number = config["account_number"]
username = config["username"]
password = config["password"]
executable_path = {'executable_path':config["chrome_driver"]}

# Class that will be called once and used to control the TD Ameritrade api
class TD():

    def __init__(self):
        self.headers = self.authorizeAccount()
        self.accountID = self.getAccountID()
        self.positions = self.getPositions()
        self.buyingPower = self.getBuyingPower()

    # Method to authorize the accout before a trade. It will return an authorization code
    def authorizeAccount(self):
        print('authorizing account')

        # create a new instance of the chrome browser
        print("opening browser")
        browser = Browser('chrome',**executable_path, headless = True)
        
        # delay time to allow browser to load properly
        time.sleep(2)

        # components of the URL
        print("building auth url")
        method = 'GET'
        url = 'https://auth.tdameritrade.com/auth?'
        client_code = client_id + '@AMER.OAUTHAP'
        paylaod = {
            'response_type':'code',
            'redirect_uri':'http://localhost/test',
            'client_id': client_code
        }

        # build the url
        built_url = requests.Request(method, url, params = paylaod).prepare()
        built_url = built_url.url

        print('visiting url')
        # go to our url
        browser.visit(built_url)
        
        time.sleep(5)

        # define payload
        payload = {'username': username, 'password':password}

        print('entering username and password')
        # fill out each element in the form
        browser.find_by_id("username0").first.fill(payload['username'])
        browser.find_by_id("password").first.fill(payload['password'])
        browser.find_by_id("accept").first.click()
        time.sleep(1)

        # Get the Text Message Box
        browser.find_by_text('Can\'t get the text message?').first.click()

        # Get the Answer Box
        browser.find_by_value("Answer a security question").first.click()

        print('answering security question')
        
        # Answer the Security Questions.
        question_one = "What is your paternal grandfather's first name?"
        question_two = "In what city were you born? (Enter full name of city only.)"
        question_three = "What was the name of your first pet?"
        question_four = "What is your father\'s middle name?"
        question_five = "In what city was your high school? (Enter full name of city only.)"
        question_six = "In what city was your father born? (Enter full name of city only.)"
        
        if browser.is_text_present(question_one):
            browser.find_by_id('secretquestion0').first.fill(config["security_questions"][question_one])
            
        elif browser.is_text_present(question_two):
            browser.find_by_id('secretquestion0').first.fill(config["security_questions"][question_two])
        
        elif browser.is_text_present(question_three):
            browser.find_by_id('secretquestion0').first.fill(config["security_questions"][question_three])

        elif browser.is_text_present(question_four):
            browser.find_by_id('secretquestion0').first.fill(config["security_questions"][question_four])

        elif browser.is_text_present(question_five):
            browser.find_by_id('secretquestion0').first.fill(config["security_questions"][question_five])
        
        elif browser.is_text_present(question_six):
            browser.find_by_id('secretquestion0').first.fill(config["security_questions"][question_six])
        
        # Submit results
        browser.find_by_id('accept').first.click()

        # Remember Device
        time.sleep(2)
        remember = browser.find_by_xpath('//*[@id="stepup_trustthisdevice0"]/div[1]')
        remember.click()

        # Submit results
        browser.find_by_id('accept').first.click()

        # Sleep and click Accept Terms.
        time.sleep(2)
        browser.find_by_id('accept').first.click()

        # Give it a second to load
        time.sleep(2)
        new_url = browser.url

        print('grabbing auth code')
        # grab the part we need, and decode it.
        parse_url = urllib.parse.unquote(new_url.split('code=')[1])
        print(new_url)
        #parse_url = urlparse(new_url.split('code=')[1])
        #parse_url= urllib.unquote(parse_url.path)
        print(parse_url)
        # Close the browser
        browser.quit()

        # define the endpoint
        url = r"https://api.tdameritrade.com/v1/oauth2/token"

        # define the headers
        headers = {"Content-Type":"application/x-www-form-urlencoded"}

        # define the payload
        payload = {'grant_type': 'authorization_code', 
                'access_type': 'offline', 
                'code': parse_url, 
                'client_id':client_id, 
                'redirect_uri':'http://localhost/test'}

        # post the data to get the token
        authReply = requests.post(r'https://api.tdameritrade.com/v1/oauth2/token', headers = headers, data=payload)

        print('sending for headers')
        # convert it to a dictionary and grab access token
        decoded_content = authReply.json()
        print(decoded_content)
        access_token = decoded_content['access_token']
        headers = {'Authorization': "Bearer {}".format(access_token)}

        return(headers)

    # Method to return a list of the current positions held along with the quantity of those positions
    def getPositions(self):

        print("grabing current positions")

        # Define Accounts Headpoints
        endpoint = r"https://api.tdameritrade.com/v1/accounts"

        # Make a Request
        content = requests.get(url = endpoint, headers = self.headers, params={'fields':'positions'})

        # Convert it to a dictionary Method
        data = content.json()

        # Empty list to be populated with current positions
        currentPositions = {}

        time.sleep(2)

        # Grab account positions
        for i in range(len(data[0]['securitiesAccount']['positions'])):
            symbol = data[0]['securitiesAccount']['positions'][i]['instrument']['symbol']
            quantity = data[0]['securitiesAccount']['positions'][i]['longQuantity']
            currentPositions.update({symbol:quantity})
            
        for i in currentPositions:
            print(i)

        return(currentPositions)

    # Method to return the account id
    def getAccountID(self):

        print("grabbing account ID")

        # Define Accounts Headpoints
        endpoint = r"https://api.tdameritrade.com/v1/accounts"

        # Make a Request
        content = requests.get(url = endpoint, headers = self.headers)

        # Convert it to a dictionary Method
        data = content.json()
        
        # Grab account ID
        account_id = data[0]['securitiesAccount']['accountId']
        print("account id: " + account_id)
        return (account_id)

    # Method to return the buying power
    def getBuyingPower(self):

        print("grabbing buying power")

        # Define Accounts Headpoints
        endpoint = r"https://api.tdameritrade.com/v1/accounts"

        # Make a Request
        content = requests.get(url = endpoint, headers = self.headers)

        # Convert it to a dictionary Method
        data = content.json()
        
        # Grab account ID
        buyingPower = data[0]['securitiesAccount']['currentBalances']['buyingPower']
        print("buying power: " + str(buyingPower))
        return (buyingPower)