#imports
from binance.client import Client
import time
#My Libraries
import API
import getPrice
import program
import Exemptions




def main():
    Trading = False
    while True:
        try:
            print("                         ")
            ticker = "ETHUSDT"
            #connect to the client
            client = Client(API.API, API.SECRET)
            if Trading == False:
                program.Searching(client,ticker)
            print("_________________________")
            time.sleep(1)

        except Exception as e:
            Exemptions.handlingProcess(e)
            time.sleep(1)

if __name__ == '__main__':
    main()