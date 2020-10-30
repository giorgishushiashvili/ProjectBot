#imports
#from binance.client import Client
import time
#My Libraries
import commands
import program
import Exemptions


#TODO make an paper trading bot

def main():
    Trading = False
    while True:
        try:
            print("                         ")
            print(time.strftime("%H:%M:%S", time.localtime()))
            ticker = "ETHUSDT"
            #connect to the client
            client = commands.connect()
            #TODO complate if statement finishing all edge cases
            #TODO time.sleep(3) should be part of the if statement 
            '''
            if Trading == False:
                if program.Searching(client,ticker):
                    Trading = True
            '''
            #TODO when I will complate if statement delete this line of code
            program.Searching(client,ticker)
            print("_________________________")

            time.sleep(3)

        except Exception as e:
            Exemptions.handlingProcess(e)
            time.sleep(1)

if __name__ == '__main__':
    main()