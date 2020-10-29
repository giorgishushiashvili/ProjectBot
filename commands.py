from binance.client import Client
import API
def connect():
    print(0)
    return Client(API.API, API.SECRET)

#Market orders
def orderBook(client,ticker, maxlimit=1000):
    depth = client.get_order_book(symbol=ticker,limit=maxlimit)
    print(1)
    return depth

def getServerTime(client):
    time_res = float(client.get_server_time()['serverTime'])
    print(2)
    return round((time_res/1000)%60,0)

def BUY(client,ticker,AMOUNT):
    client.order_market_buy(
            symbol=ticker,
            quantity=AMOUNT
        )
    print(3)


def SELL(client,ticker,AMOUNT):
    client.order_market_sell(
                symbol=ticker,
                quantity=AMOUNT
        )
    print(4)


def getPrice(client,ticker):
    print(5)
    return float(client.get_ticker(symbol=ticker)['lastPrice'])


#TODO change the code and adjust for different cryptos or at lease make sure that I can change the request from the app.py
def getBalance_ETH(client):
    print(6)
    return float(client.get_asset_balance(asset='ETH')['free'])

def getBalance_USDT(client):
    print(7)
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
    print(8)