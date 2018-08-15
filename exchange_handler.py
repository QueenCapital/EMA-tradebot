import bitfinex_v1

def getTicker(exchange, coin_pair):
        if exchange == 'bitfinexv1':
                ticker = bitfinex_v1.getTicker(coin_pair)
        return ticker['bid']

def getWalletBalances(exchange, type, currency):
        if exchange == 'bitfinexv1':
                wallets = bitfinex_v1.BitfinexClient().getWalletBalances()
        for wallet in wallets:
                if wallet['type'] == type and wallet['currency'] == currency:
                        wallet_balance = wallet['available']
        return wallet_balance

def getActivePositions(exchange):
        if exchange == 'bitfinexv1':
                active_positions = bitfinex_v1.BitfinexClient().getActivePositions()
        return active_positions

def newOrder(exchange, symbol, amount, price, side, type):
        if exchange == 'bitfinexv1':
                #price is arbitrary for market orders
                order = bitfinex_v1.BitfinexClient().newOrder(symbol, amount, price, side, type)
        return order

def getOrderStatus(exchange, id):
        if exchange == 'bitfinexv1':
                status = bitfinex_v1.BitfinexClient().getOrderStatus(id)
        return status

def transferWallet(exchange, from_type, to_type, amount, currency):
        if exchange == 'bitfinexv1':
                transfer = bitfinex_v1.BitfinexClient().transferWallet(from_type, to_type, amount, currency)
        return transfer
