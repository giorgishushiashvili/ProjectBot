#imports
from binance.client import Client
import time
#My Libraries
import API
import getPrice
import commands
import Exemptions

#wow
#TODO Make sure that I will be screening multiple assets
#TODO Make sure that my strategy will be refined
#TODO Strategy should be 

def main():
    while True:
        try:
            print("                         ")
            ticker = "ETHUSDT"
            #connect to the client
            client = Client(API.API, API.SECRET)
            depth = commands.orderBook(client,ticker)
            print("_________________________")
            time.sleep(1)

        except Exception as e:
            Exemptions.handlingProcess(e)
            time.sleep(1)

if __name__ == '__main__':
    main()