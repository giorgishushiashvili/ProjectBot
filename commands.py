from binance.client import Client
import API
import pandas as pd

def connect():
    return Client(API.API, API.SECRET)

#Market orders
def orderBook(client,ticker, maxlimit=1000):
    depth = client.get_order_book(symbol=ticker,limit=maxlimit)
    return depth

def getServerTime(client):
    time_res = float(client.get_server_time()['serverTime'])
    return round((time_res/1000)%60,0)

def BUY(client,ticker,AMOUNT):
    client.order_market_buy(
            symbol=ticker,
            quantity=AMOUNT
        )


def SELL(client,ticker,AMOUNT):
    client.order_market_sell(
                symbol=ticker,
                quantity=AMOUNT
        )

#TODO delete this entry I do not believe I will need it
def getPrice(client,ticker):
    return float(client.get_ticker(symbol=ticker)['lastPrice'])


#TODO change the code and adjust for different cryptos or at lease make sure that I can change the request from the app.py
def getBalance_ETH(client):
    return float(client.get_asset_balance(asset='ETH')['free'])

def getBalance_USDT(client):
    return float(client.get_asset_balance(asset='USDT')['free'])

def getMyTrades(client,side):
    if side == "ETH":
        trades = client.get_my_trades(symbol='ETHUSDT')
        trade_p = float(trades[len(trades) - 1]['qty'])
        return trade_p
    if side == "USDT":
        trades = client.get_my_trades(symbol='ETHUSDT')
        trade_p = float(trades[len(trades) - 1]['quoteQty'])
        return trade_p

#Depth is data from order book, FinalAmount is on which amount i will be calculating the price, and USDT=True means FinalAmount is USDT 
def BuyPrice(depth, FinalAmount, USDT=True):
    asks = pd.DataFrame(data=depth['asks'])
    asks.columns = ['Price','Quantity']
    asks['Price'] = asks['Price'].astype(float)
    asks['Quantity'] = asks['Quantity'].astype(float)
    asks['USDT'] = asks['Price'] * asks['Quantity']
    asks['cumsum'] = round(asks['USDT'].cumsum(),2)

    if USDT:
        amount = 0
        amountOther = 0
        for index, row in asks.iterrows():
            if amountOther >= FinalAmount:
                break
            else:
                if FinalAmount - amountOther > row['USDT']:
                    amountOther = row['USDT'] + amountOther
                    amount = row['Quantity'] + amount
                else:
                    helperAmount = FinalAmount - amountOther
                    amount = amount + (helperAmount / row['Price'])
                    amountOther = FinalAmount
                    break
        Price =  round(amountOther / amount ,2)
        return Price

    else:
        amount = 0
        amountOther = 0
        for index, row in asks.iterrows():
            if amount >= FinalAmount:
                break
            else:
                if FinalAmount - amount > row['Quantity']:
                    amountOther = row['USDT'] + amountOther
                    amount = row['Quantity'] + amount
                    
                else:
                    helperAmount = FinalAmount - amount
                    amountOther = amountOther + (helperAmount * row['Price'])
                    amount = FinalAmount
                    break

        Price =  round(amountOther / amount ,2)
        return Price


def SellPrice(depth, FinalAmount, USDT=True):
    bids = pd.DataFrame(data=depth['bids'])
    bids.columns = ['Price','Quantity']
    bids['Price'] = bids['Price'].astype(float)
    bids['Quantity'] = bids['Quantity'].astype(float)
    bids['USDT'] = bids['Price'] * bids['Quantity']
    bids['cumsum'] = round(bids['USDT'].cumsum(),2)
    print(bids)
    if USDT:
        amount = 0
        amountOther = 0
        for index, row in bids.iterrows():
            if amountOther >= FinalAmount:
                break
            else:
                if FinalAmount - amountOther > row['USDT']:
                    amountOther = row['USDT'] + amountOther
                    amount = row['Quantity'] + amount
                else:
                    helperAmount = FinalAmount - amountOther
                    amount = amount + (helperAmount / row['Price'])
                    amountOther = FinalAmount
                    break
        Price =  round(amountOther / amount ,2)
        return Price

    else:
        amount = 0
        amountOther = 0
        for index, row in bids.iterrows():
            if amount >= FinalAmount:
                break
            else:
                if FinalAmount - amount > row['Quantity']:
                    amountOther = row['USDT'] + amountOther
                    amount = row['Quantity'] + amount
                    
                else:
                    helperAmount = FinalAmount - amount
                    amountOther = amountOther + (helperAmount * row['Price'])
                    amount = FinalAmount
                    break

        Price =  round(amountOther / amount ,2)
        return Price