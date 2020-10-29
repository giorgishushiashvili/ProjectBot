from binance.client import Client


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