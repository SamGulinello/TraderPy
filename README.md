# **TraderPy**
TraderPy is an open-source modular algorithmic trading platform. Through the use of interchangable modules it can take control of your TD Ameritrade portfolio. This Program uses the TD Ameritrade api to get real time market data and control a TD Ameritrade trading account.

## Installation

---

1. In the command line clone this repository
```
git clone https://github.com/SamGulinello/TraderPY
```
2. CD into the repository
```
cd TraderPy
```
3. Install the application
```
pip3 install requirements.txt
```
4. To use this application you need to sign up for a TD Ameritrade developer account. This can be done [here](https://developer.tdameritrade.com/).
    - **This is seperate from your actual TD Ameritrade trading account.** 
    - To set up a Trading account, if you don't already have one, go to [their official website](https://www.tdameritrade.com/home.page)
5. Once an account has been created, you will need to create an application [here](https://developer.tdameritrade.com/user/me/apps/add) to be approved for the api.
    - Fill out the required fields in the Add App screen. Select **Create App**. 
    - Field details are as follows:
        - **App Name:** A unique application name.
        - **Callback URL:** The URL to receive the auth code (used to retrieve a token from the Authentication API) after successful authentication. Separate URLs with a comma for multiple URLs. Localhost can be used here, as well.
        - **What is the purpose of your application?:** Use cases of the application, trading strategy, number of orders sent per day, etc.
    - The new application will be displayed in [My Apps](https://developer.tdameritrade.com/user/me/apps) once it is successfully registered
    - For more information on this process, they provide good [guides](https://developer.tdameritrade.com/guides).
6. This project uses a python library called selenium. It is used to for web scraping and is essentail for some of the methods to work. This  library requires a chrome driver to be installed on your machine and the path to the executable needs to be included in the config file. This needs to be the absolute path not the relative one (Google will tell you how to find this if you don't know). The resources directory has an empty folder waiting for you to install the chrome driver into it. 
7. Finally make a copy of the sample config file and name it config.py. Fill out the required information (*indicated in all caps text*)
    - Required information is as follows:
        - client_id: This is the **Consumer Key** of the successfully registered app on your TD Ameritrade developer account
        - account_number: This can be found in the **My Profile** page on TD Ameritrades Trading Website
        - username: This is your TD Ameritrade *Trading* Account Username
        - password: This is your TD Ameritrade *Trading* Account Password
        - chrome_driver: This is the absolute path to the chrome driver executable
        - security_questions: The answers would have been determined when setting up the TD Ameritrade account.
8. To run this project open up your command line and go to the root directory of this project. Once in the root directory just type
```
python3 main.py
```

## Creating a module

---

To create a module you will first want to import the config file. The main function of this program sets the root directory to make an import of the config file look like this.
```
from config.config import config
```
In the config file you need to include the name of the module and set it the the key "module". An example of a module specific config looks like this. It is used for a module that compares the 10 and 30 moving averages of the S&P 500 and trades stocks accordingly. 
```
{
    "module" : "MovingAverage",
    "buying_power_allocation": 30, # Percentage of available buying power
    "index" : "TEST"
}
```
Your module will also need to include which index will be used for any analysis. The index options are located in the resource directory. A user can create their own custom index they will just need to specify it in the config.\
\
The main function is designed to run a module and expects it to return both a buy list and sell list. These will be added to a master list which will then be used by the main function to know what to buy and sell at the end of the day (duh). If for some reason the module does not need to add to these list please return two empyt lists or else an error will get thrown (ooh).\
\
Finally, the module must be located in it's own directory named the same as the file which as a main function in it. This program is set up to run a function called main in the file named the module. I am bad at describing this and it may sound confusing but look at the MovingAverage module. Do that.\
\
To submit a module for review please fork this repository and submit a pull request when done. I will review the code and make sure it works. 

## What's Next

---

The next deployment should include a few new things. First, I would like to add more methods to both the TD and Stock classes. The TD api has a lot to offer but the request system can be confusing at times. I would like to have these classes make getting data from TD Ameritrade as easy as possible. Next, I plan on documenting both those classes. There are already a number of cool things they can do but there is no way of knowing it without looking at the code. Documentation will either come in the form of another README or I have toyed with the idea of making a documentation website to accompany this project (will probably start with a README). Finally, I hope to develop a 'trailing stop' module. This will ensure the program doesn't hold a stock until the bitter end and will instead lock in a loss percentage value that will change as the stock hopefully goes up in value.

## Support

---

If you have any question or feedback please let me know. You can contact me at sgulinello12@gmail.com. I will try my best to respond promptly. I hope to contribute to this project regularly because there is so much I would like to do with it. I am a full time college student so I can't promise anything. 

## Legal Things ... I'm assuming

---

I just want it on record that I am not personally responsible for the funds in your trading account. What you do with your money is completely seperate from the programs I write. This project is honestly just an exercise in a lot of programming practices I wanted to learn more about. This should in no way be your primary decision maker with large quantities of your financials. I also assume bugs will occur as they have before when developing this. I try to program in safe guards though that will protect your funds. Also please be aware of any personal information you use with this. **When pushing something to githup please add your specific config file to a .gitignore.** That file with contain sensitive information which I am assuming you don't want on the internet. Thank you and enjoy :)

