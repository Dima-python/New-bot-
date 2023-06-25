import requests

symbols_market = {}
def binance_bybit(symbol):
	try:
		get_binance = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}" )
		symbol_binance = get_binance.json()
		result_binance =  symbol_binance['symbol'] + " " + symbol_binance['price'] + "$"

		get_bybit = requests.get(f'https://api-testnet.bybit.com/derivatives/v3/public/tickers?category=linear&symbol={symbol}')
		symbol_bybit = get_bybit.json()
		result_bybit = symbol_bybit['result']['list'][0]['symbol'] + " " +  symbol_bybit['result']['list'][0]['indexPrice'] + "$"
		
		symbols_market["Binance"] = "Binance: " + result_binance
		symbols_market["Bybit"] = "Bybit: " + result_bybit
		
		return symbols_market

	except (IndexError, KeyError, ValueError):
		return "Такая пара отсутствует на одной из бирж"



#указывать пару через "-"
#get_kycoin = requests.get(f'https://api.kucoin.com/api/v1/mark-price/{symbol}/current')
#symbol_kycoin = get_kycoin.json() IndexError, KeyError