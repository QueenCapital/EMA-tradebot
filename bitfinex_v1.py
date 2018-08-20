import requests
import hashlib
import hmac
import time #for nonce
import json
import base64
import init

# Implemented Endpoints
# getTicker(symbol)
# getStats(symbol)
# getLendbook()
# getFundbook(symbol)
# getTrades(symbol)
# getLends()
# getSymbols()
# getSymbolsDetails()
# getBalanceHistory(currency)
# getDepositWithdrawHistory(currency)
# getPastTrades(symbol)
# getActivePositions()
# getOrdersHistory()
# getActiveOrders()
# getOrderStatus(id)
# cancelOrderAll()
# cancelOrder(id)
# newOrder(symbol, amount, price, side, type)
# transferWallet(walletfrom, walletto, amount, currency)
# getWalletBalances()
# getMarginInfos()
# getKeyPermissions()
# getDepositAddress()
# getSummary()
# getAccountInfo()



base_url = 'https://api.bitfinex.com/v1/'

symbol = 'BTCUSD'
currency = 'usd'
candle = 3600

#Public Endpoints

def getTicker(symbol):
        url = base_url + "/pubticker/" + symbol
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''

def getStats(symbol):
        url = base_url +  "/stats/" + symbol
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''

def getLendbook():
        url = base_url +  "/lendbook/usd"
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''

def getFundbook(symbol):
        url = base_url +  "/book/" + symbol
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''

def getTrades(symbol):
        url = base_url +  "/trades/" + symbol
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''

def getLends():
        url = base_url +  "/lends/usd"
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''

def getSymbols():
        url = base_url +  "/symbols"
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''

def getSymbolsDetails():
        url = base_url +  "/symbols_details"
        response = requests.request("GET", url)
        if response.status_code == 200:
                return response.json()
        else:
                print response.status_code
                print response
                return ''



#Authenticated Endpoints

class BitfinexClient(object):
        BASE_URL = "https://api.bitfinex.com"
        KEY= init.getBFXKey()
        SECRET= init.getBFXSecret()

        def _nonce(self):
                return str(int(round(time.time() * 1000)))

        def _headers(self, payload_json, m):
            headers = {
                        'X-BFX-APIKEY':self.KEY,
                        'X-BFX-PAYLOAD':base64.b64encode(bytes(payload_json)),
                        'X-BFX-SIGNATURE': m
                }
            return headers

        def _m(self, payload):
            m = hmac.new(self.SECRET, payload, hashlib.sha384)
            m = m.hexdigest()
            return m

        def getAccountInfo(self):
                nonce = self._nonce()
                path = '/v1/balances'
                payloadObject = {
                        'request':'/v1/balances',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getSummary(self):
                nonce = self._nonce()
                path = '/v1/summary'
                payloadObject = {
                        'request':'/v1/summary',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getDepositAddress(self):
                nonce = self._nonce()
                path = '/v1/deposit/new'
                payloadObject = {
                        'request':'/v1/deposit/new',
                        'nonce':nonce,
                        'options':{
                        'method':'bitcoin',
                        'wallet':'trading'}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getKeyPermissions(self):
                nonce = self._nonce()
                path = '/v1/key_info'
                payloadObject = {
                        'request':'/v1/key_info',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getMarginInfos(self):
                nonce = self._nonce()
                path = '/v1/margin_infos'
                payloadObject = {
                        'request':'/v1/margin_infos',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getWalletBalances(self):
                nonce = self._nonce()
                path = '/v1/balances'
                payloadObject = {
                        'request':'/v1/balances',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def transferWallet(self, walletfrom, walletto, amount, currency):
                nonce = self._nonce()
                path = '/v1/transfer'
                payloadObject = {
                        'request':'/v1/transfer',
                        'nonce':nonce,
                        'options':{},
                        'amount':str(amount),
                        'walletfrom':walletfrom,
                        'walletto':walletto,
                        'currency':currency
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)

                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def newOrder(self, symbol, amount, price, side, order_type):
                nonce = self._nonce()
                path = '/v1/order/new'
                payloadObject = {
                        'request':'/v1/order/new',
                        'nonce':nonce,
                        'options':{},
                        'symbol':symbol,
                        'amount':str(amount),
                        'price':str(price),
                        'exchange':'bitfinex',
                        'side':side,
                        'type':order_type
                }
                payload_json = json.dumps(payloadObject)
                #payload = base64.b64encode(bytes(payload_json))
                payload = base64.standard_b64encode(payload_json.encode('utf8'))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                    print r.text
                    return r.json()
                else:
                        print r
                        print r.status_code
                        print r.text
                        return ''

        def cancelOrder(self, id):
                nonce = self._nonce()
                path = '/v1/order/cancel'
                payloadObject = {
                        'request':'/v1/order/cancel',
                        'nonce':nonce,
                        'options':{
                        'order_id':id}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def cancelOrderAll(self):
                nonce = self._nonce()
                path = '/v1/order/cancel/all'
                payloadObject = {
                        'request':'/v1/order/cancel/all',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getOrderStatus(self, id):
                nonce = self._nonce()
                path = '/v1/order/status'
                payloadObject = {
                        'request':'/v1/order/status',
                        'nonce':nonce,
                        'options':{
                        'order_id':id}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getActiveOrders(self):
                nonce = self._nonce()
                path = '/v1/orders'
                payloadObject = {
                        'request':'/v1/orders',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''


        def getOrdersHistory(self):
                nonce = self._nonce()
                path = '/v1/orders/hist'
                payloadObject = {
                        'request':'/v1/orders/hist',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''


        def getActivePositions(self):
                nonce = self._nonce()
                path = '/v1/positions'
                payloadObject = {
                        'request':'/v1/positions',
                        'nonce':nonce,
                        'options':{}
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def claimPosition(self, xchangeID, amount):
                nonce = self._nonce()
                path = '/v1/position/claim'
                payloadObject = {
                        'request':'/v1/position/claim',
                        'nonce':nonce,
                        'options':{},
                        'position_id':int(xchangeID),
                        'amount':str(amount)
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                    return r.json()
                    print r.text
                else:
                  print r.status_code
                  print r.text
                  return ''





        def getPastTrades(self, symbol):
                nonce = self._nonce()
                path = '/v1/mytrades'
                payloadObject = {
                        'request':'/v1/mytrades',
                        'nonce':nonce,
                        'options':{},
                        'symbol':symbol,
                        'timestamp':'1534348800'
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''


        def getDepositWithdrawHistory(self, currency):
                nonce = self._nonce()
                path = '/v1/history/movements'
                payloadObject = {
                        'request':'/v1/history/movements',
                        'nonce':nonce,
                        'options':{},
                        'currency':currency
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''

        def getBalanceHistory(self, currency):
                nonce = self._nonce()
                path = '/v1/history'
                payloadObject = {
                        'request':'/v1/history',
                        'nonce':nonce,
                        'options':{},
                        'currency':currency
                }
                payload_json = json.dumps(payloadObject)
                payload = base64.b64encode(bytes(payload_json))

                m = self._m(payload)
                headers = self._headers(payload_json, m)

                r = requests.post(self.BASE_URL + path, data={}, headers=headers)
                if r.status_code == 200:
                  return r.json()
                else:
                  print r.status_code
                  print r.text
                  return ''
