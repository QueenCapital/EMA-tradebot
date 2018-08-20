import bitfinex_v1

def getTicker(exchange, coin_pair):
        if exchange == 'bitfinexv1':
                ticker = bitfinex_v1.getTicker(coin_pair)
        return ticker['bid']

def getWalletBalances(exchange, wallet_type, currency):
        if exchange == 'bitfinexv1':
                wallets = bitfinex_v1.BitfinexClient().getWalletBalances()
        for wallet in wallets:
                if wallet_type == 'all' and currency == 'all':
                        wallet_balance = wallets
                elif wallet['type'] == wallet_type and wallet['currency'] == currency:
                        wallet_balance = wallet['available']
        return wallet_balance

def getActivePositions(exchange):
        if exchange == 'bitfinexv1':
                active_positions = bitfinex_v1.BitfinexClient().getActivePositions()
        return active_positions

def newOrder(exchange, symbol, amount, price, side, order_type):
        if exchange == 'bitfinexv1':
                #price is arbitrary for market orders
                order = bitfinex_v1.BitfinexClient().newOrder(symbol, amount, price, side, order_type)
        return order

def getOrderStatus(exchange, trade_id):
        if exchange == 'bitfinexv1':
                status = bitfinex_v1.BitfinexClient().getOrderStatus(trade_id)
        return status

def transferWallet(exchange, from_type, to_type, amount, currency):
        if exchange == 'bitfinexv1':
                transfer = bitfinex_v1.BitfinexClient().transferWallet(from_type, to_type, amount, currency)
        return transfer

#returns BTC to Exchange wallet, closes position
def claimPosition(exchange, xchangeID, amount):
        if exchange == 'bitfinexv1':
                claim = bitfinex_v1.BitfinexClient().claimPosition(xchangeID, amount)
        return claim

def getPastTrades(exchange, symbol):
        if exchange == 'bitfinexv1':
                past_trades  = bitfinex_v1.BitfinexClient().getPastTrades(symbol)
        return past_trades


