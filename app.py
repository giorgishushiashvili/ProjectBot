import time
#My Libraries
import commands
import program
import Exemptions
import log

#Global Variables
Trading = False
price = 0
amount = 0


def main():
    #Variables will be used in actual program
    global Trading
    global price
    global amount
    while True:
        try:
            print("                         ")
            CurrentTime = time.strftime("%H:%M:%S", time.localtime())
            print(CurrentTime)
            ticker = "ETHUSDT"
            #connect to the client
            client = commands.connect()
            #I deleted logic because I still need to test the data and do not need to overcomplecate my information stream.
            #TODO Rewrite the logic.
            program.Searching(client,ticker)

            time.sleep(3)
            print("_________________________")

            

        except Exception as e:
            Exemptions.handlingProcess(e)
            time.sleep(1)

if __name__ == '__main__':
    main()