#imports
#from binance.client import Client
import time
#My Libraries
import commands
import getPrice
import program
import Exemptions




def main():
    Trading = False
    while True:
        try:
            print("                         ")
            print(time.strftime("%H:%M:%S", time.localtime()))
            ticker = "ETHUSDT"
            #connect to the client
            client = commands.connect()
            if Trading == False:
                program.Searching(client,ticker)
            print("_________________________")

            time.sleep(1)

        except Exception as e:
            Exemptions.handlingProcess(e)
            time.sleep(1)

if __name__ == '__main__':
    main()