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
            #TODO complate if statement finishing all edge cases
            #TODO time.sleep(3) should be part of the if statement 
            
            if Trading == False:
                if program.Searching(client,ticker):
                    #TODO after the testing phase add Market Buy/Sell for the trades
                    Trading = True
                    depth = commands.orderBook(client,ticker,500)
                    amount = round(commands.getBalance_USDT(client),0)
                    price = commands.BuyPrice(depth,amount)
                    data = [CurrentTime,price,price*1.02,price*0.993]
                    log.additlog("data.csv",data)
                
                #I do not need fast updates when searching for trades
                time.sleep(3)
            else:
                if program.WaitingForTrade(client,price,ticker,amount):
                    Trading = False
                    amount = 0
                    price = commands.SellPrice(depth,amount,USDT=False)
                    data = [CurrentTime,price]
                    log.additlog("data.csv",data)
                #I will need updates as fast as possible when I will be waiting for trades to close
                #TODO change time to 1 second when done
                time.sleep(3)
            print("_________________________")

            

        except Exception as e:
            Exemptions.handlingProcess(e)
            time.sleep(1)

if __name__ == '__main__':
    main()