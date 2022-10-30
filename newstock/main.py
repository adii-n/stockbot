from re import T
from yahoo_fin.stock_info import *
import time
import os 
from twilio.rest import Client 
from credentials import account_sid, auth_token


client = Client(account_sid, auth_token)

tradinghours = False


tickers = ["AAPL", "MSFT"]

sendmessage = False

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

##create function to set trading hours to true when us market opens 
def tradinghours():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if current_time >= "08:30:00" and current_time <= "15:00:00":
        tradinghours = True
    else:
        tradinghours = False


##create function to get stock price
def stockprice():
    for i in range(len(tickers)):
        return(
            tickers[i] + ": " + str(get_live_price(tickers[i]))
            )


##create function to run def(stockprice) at 12:00:00, 12:30:00, 13:00:00, 13:30:00, 14:00:00, 14:30:00, 15:00:00
def runstockprice():
    if tradinghours == False:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if current_time == "12:00:00" or current_time == "12:30:00" or current_time == "16:25:00" or current_time == "13:30:00" or current_time == "14:00:00" or current_time == "14:30:00" or current_time == "15:00:00":
            sendmessage = True


 
##create infinite loop to run functions
while True:
    if sendmessage == True:
        message = client.messages \
                .create(
                     body=str(stockprice()),
                     from_='+12058824151',
                     to='+14088194119',
                 )
        print(message.sid)
        sendmessage = False

        
        
        
        
        
    
