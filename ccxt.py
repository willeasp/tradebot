import ccxt

hitbtc = ccxt.hitbtc()

print(hitbtc)

print(hitbtc.load_markets())
ticker_data = []

""" 
# fetch the BTC/USDT ticker for use in converting assets to price in USDT
bitcoin_ticker = hitbtc.fetch_ticker('BTC/USDT')

i = 1
for x in bitcoin_ticker:
    print(i)
    i += 1
    print(str(x) + " : " + str(bitcoin_ticker[x]))

while 1:
    print(hitbtc.fetch_ticker('BTC/USDT')["high"])
     """