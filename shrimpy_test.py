""" Just testing out the shrimpy api """

from api_keys import public_key, secret_key
import shrimpy
import json

def prettyprint(res):
    print(json.dumps(res, indent=4, sort_keys=True))


client = shrimpy.ShrimpyApiClient(public_key, secret_key)

prettyprint(client.get_ticker('binance'))

# prettyprint(client.get_supported_exchanges())

# prettyprint(client.get_trading_pairs('binance'))

