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
            print(time.strftime("%H:%M:%S", time.localtime()))
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
                    data = [price]
                    log.additlog("data.csv",data)
                
                #I do not need fast updates when searching for trades
                time.sleep(3)
            else:
                PR = commands.SellPrice(depth,amount,USDT=False)
                print("Price " + str(PR) + " TAKE PROFIT " + str(price * 1.02) + " Cut Losses " + str(price * 0.993))
                if program.WaitingForTrade(client,price,ticker,amount):
                    Trading = False
                    amount = 0
                    price = PR
                    data = [PR]
                    log.additlog("data.csv",data)
                #I will need updates as fast as possible when I will be waiting for trades to close
                time.sleep(1)
            print("_________________________")

            

        except Exception as e:
            Exemptions.handlingProcess(e)
            time.sleep(1)

if __name__ == '__main__':
    main()