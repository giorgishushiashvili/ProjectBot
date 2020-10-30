#Commond libraries
import pandas as pd
#my Libraries
import commands

#TODO here I will have main logic of the program

def ShareTotal(depth,portion=500):
    #get bids data
    bids = pd.DataFrame(data=depth['bids'])
    bids.columns = ['Price','Quantity']
    bids['Price'] = bids['Price'].astype(float)
    bids['Quantity'] = bids['Quantity'].astype(float)
    #Calculate average price and total quantity of 250 entries of bids.
    bids['USDT'] = round(bids['Price'] * bids['Quantity'],2)
    bids = bids.groupby(bids.index // portion).sum()
    bids['Price'] = round(bids['USDT'] / bids['Quantity'],2)
    #get asks data
    asks = pd.DataFrame(data=depth['asks'])
    asks.columns = ['Price','Quantity']
    asks['Price'] = asks['Price'].astype(float)
    asks['Quantity'] = asks['Quantity'].astype(float)
    #Calculate average price and total quantity of 250 entries of asks.
    asks['USDT'] = round(asks['Price'] * asks['Quantity'],2)
    asks = asks.groupby(asks.index // portion).sum()
    asks['Price'] = round(asks['USDT'] / asks['Quantity'],2)
    
    ask = round(asks['Quantity'][0],2)
    bid = round(bids['Quantity'][0],2)
    
    return round(ask/(ask+bid) * 100, 0)

def Searching(client, ticker):
    depth = commands.orderBook(client,ticker,maxlimit=5000)
    shareTotal_5000 = ShareTotal(depth,portion=5000)
    shareTotal_1000 = ShareTotal(depth,portion=1000)
    # 500 changes too fast will not be able to make any profit with it.
    BuyPrice = commands.BuyPrice(depth,192)
    print("shareTotal_5000 " + str(shareTotal_5000) + " shareTotal_1000 " + str(shareTotal_1000) + " Price " + str(BuyPrice))
    if shareTotal_5000 > 52 and shareTotal_1000 > 52:
        return True
    else:
        return False
    