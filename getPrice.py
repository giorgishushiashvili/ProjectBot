import pandas as pd


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
        Price =  amountOther / amount 
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

        Price =  amountOther / amount 
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
        Price =  amountOther / amount 
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

        Price =  amountOther / amount 
        return Price