# TraderPY Config Sample
#
# Written By Sam Gulinello
# MIT Licensed
#
# For More Information About This Project Go to 
# https://github.com/SamGulinello/TraderPY

config = {

    # Account Information - Instruction on how to find this is in the README
    "client_id" : "INSERT CLIENT ID",           # Type: String
    "account_number" : "INSERT ACCOUNT_NUMBER", # Type: Int
    "username" : "*INSERT USERNAME*",           # Type: String
    "password" : "INSERT PASSWORD",             # Type: String

    #  Absolute Path to the chrome driver required for selenium
    "chrome_driver" : "INSERT PATH TO CHROME DRIVER EXECUTABLE",

    # TD Ameritrade requires a security question to be answered every time the account is logged in
    # These answers would have been provided when setting up a TD Ameritrade Account
    "security_questions" : {
        "What is your paternal grandfather's first name?" : 'INSERT ANSWER',
        "In what city were you born? (Enter full name of city only.)": 'INSERT ANSWER',
        "What was the name of your first pet?": 'INSERT ANSWER',
        "What is your father's middle name?": 'INSERT ANSWER',
        "In what city was your high school? (Enter full name of city only.)": 'INSERT ANSWER',
        "In what city was your father born? (Enter full name of city only.)": 'INSERT ANSWER'
    },

    "modules" : [
        {
            "module" : "MovingAverage",
            "buying_power_allocation": 30, # Percentage of available buying power
            "index" : "TEST"
        }
    ]
            
}