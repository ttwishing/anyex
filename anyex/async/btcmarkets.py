# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/anyex/anyex/blob/master/CONTRIBUTING.md#how-to-contribute-code

from anyex.async.base.exchange import Exchange
import base64
import hashlib
import json
from anyex.base.errors import ExchangeError
from anyex.base.errors import NotSupported
from anyex.base.errors import InvalidOrder
from anyex.base.errors import OrderNotFound
from anyex.base.errors import DDoSProtection


class btcmarkets (Exchange):

    def describe(self):
        return self.deep_extend(super(btcmarkets, self).describe(), {
            'id': 'btcmarkets',
            'name': 'BTC Markets',
            'countries': 'AU',  # Australia
            'rateLimit': 1000,  # market data cached for 1 second(trades cached for 2 seconds)
            'has': {
                'CORS': False,
                'fetchOHLCV': True,
                'fetchOrder': True,
                'fetchOrders': True,
                'fetchClosedOrders': 'emulated',
                'fetchOpenOrders': True,
                'fetchMyTrades': True,
                'cancelOrders': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/29142911-0e1acfc2-7d5c-11e7-98c4-07d9532b29d7.jpg',
                'api': {
                    'public': 'https://api.btcmarkets.net',
                    'private': 'https://api.btcmarkets.net',
                    'web': 'https://btcmarkets.net/data',
                },
                'www': 'https://btcmarkets.net/',
                'doc': 'https://github.com/BTCMarkets/API',
            },
            'api': {
                'public': {
                    'get': [
                        'market/{id}/tick',
                        'market/{id}/orderbook',
                        'market/{id}/trades',
                    ],
                },
                'private': {
                    'get': [
                        'account/balance',
                        'account/{id}/tradingfee',
                    ],
                    'post': [
                        'fundtransfer/withdrawCrypto',
                        'fundtransfer/withdrawEFT',
                        'order/create',
                        'order/cancel',
                        'order/history',
                        'order/open',
                        'order/trade/history',
                        'order/createBatch',  # they promise it's coming soon...
                        'order/detail',
                    ],
                },
                'web': {
                    'get': [
                        'market/BTCMarkets/{id}/tickByTime',
                    ],
                },
            },
            'markets': {
                'BTC/AUD': {'id': 'BTC/AUD', 'symbol': 'BTC/AUD', 'base': 'BTC', 'quote': 'AUD', 'maker': 0.0085, 'taker': 0.0085, 'limits': {'amount': {'min': 0.001, 'max': None}}, 'precision': {'price': 2}},
                'LTC/AUD': {'id': 'LTC/AUD', 'symbol': 'LTC/AUD', 'base': 'LTC', 'quote': 'AUD', 'maker': 0.0085, 'taker': 0.0085, 'limits': {'amount': {'min': 0.001, 'max': None}}, 'precision': {'price': 2}},
                'ETH/AUD': {'id': 'ETH/AUD', 'symbol': 'ETH/AUD', 'base': 'ETH', 'quote': 'AUD', 'maker': 0.0085, 'taker': 0.0085, 'limits': {'amount': {'min': 0.001, 'max': None}}, 'precision': {'price': 2}},
                'ETC/AUD': {'id': 'ETC/AUD', 'symbol': 'ETC/AUD', 'base': 'ETC', 'quote': 'AUD', 'maker': 0.0085, 'taker': 0.0085, 'limits': {'amount': {'min': 0.001, 'max': None}}, 'precision': {'price': 2}},
                'XRP/AUD': {'id': 'XRP/AUD', 'symbol': 'XRP/AUD', 'base': 'XRP', 'quote': 'AUD', 'maker': 0.0085, 'taker': 0.0085, 'limits': {'amount': {'min': 0.001, 'max': None}}, 'precision': {'price': 2}},
                'BCH/AUD': {'id': 'BCH/AUD', 'symbol': 'BCH/AUD', 'base': 'BCH', 'quote': 'AUD', 'maker': 0.0085, 'taker': 0.0085, 'limits': {'amount': {'min': 0.001, 'max': None}}, 'precision': {'price': 2}},
                'LTC/BTC': {'id': 'LTC/BTC', 'symbol': 'LTC/BTC', 'base': 'LTC', 'quote': 'BTC', 'maker': 0.0022, 'taker': 0.0022, 'limits': {'amount': {'min': 0.001, 'max': None}}},
                'ETH/BTC': {'id': 'ETH/BTC', 'symbol': 'ETH/BTC', 'base': 'ETH', 'quote': 'BTC', 'maker': 0.0022, 'taker': 0.0022, 'limits': {'amount': {'min': 0.001, 'max': None}}},
                'ETC/BTC': {'id': 'ETC/BTC', 'symbol': 'ETC/BTC', 'base': 'ETC', 'quote': 'BTC', 'maker': 0.0022, 'taker': 0.0022, 'limits': {'amount': {'min': 0.001, 'max': None}}},
                'XRP/BTC': {'id': 'XRP/BTC', 'symbol': 'XRP/BTC', 'base': 'XRP', 'quote': 'BTC', 'maker': 0.0022, 'taker': 0.0022, 'limits': {'amount': {'min': 0.001, 'max': None}}},
                'BCH/BTC': {'id': 'BCH/BTC', 'symbol': 'BCH/BTC', 'base': 'BCH', 'quote': 'BTC', 'maker': 0.0022, 'taker': 0.0022, 'limits': {'amount': {'min': 0.001, 'max': None}}},
            },
            'timeframes': {
                '1m': 'minute',
                '1h': 'hour',
                '1d': 'day',
            },
            'exceptions': {
                '3': InvalidOrder,
                '6': DDoSProtection,
            },
        })

    async def fetch_balance(self, params={}):
        await self.load_markets()
        balances = await self.privateGetAccountBalance()
        result = {'info': balances}
        for b in range(0, len(balances)):
            balance = balances[b]
            currency = balance['currency']
            multiplier = 100000000
            total = float(balance['balance'] / multiplier)
            used = float(balance['pendingFunds'] / multiplier)
            free = total - used
            account = {
                'free': free,
                'used': used,
                'total': total,
            }
            result[currency] = account
        return self.parse_balance(result)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
        multiplier = 100000000  # for price and volume
        return [
            ohlcv[0],
            float(ohlcv[1]) / multiplier,
            float(ohlcv[2]) / multiplier,
            float(ohlcv[3]) / multiplier,
            float(ohlcv[4]) / multiplier,
            float(ohlcv[5]) / multiplier,
        ]

    async def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'id': market['id'],
            'timeWindow': self.timeframes[timeframe],
        }
        if since is not None:
            request['since'] = since
        response = await self.webGetMarketBTCMarketsIdTickByTime(self.extend(request, params))
        return self.parse_ohlcvs(response['ticks'], market, timeframe, since, limit)

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        orderbook = await self.publicGetMarketIdOrderbook(self.extend({
            'id': market['id'],
        }, params))
        timestamp = orderbook['timestamp'] * 1000
        return self.parse_order_book(orderbook, timestamp)

    def parse_ticker(self, ticker, market=None):
        timestamp = ticker['timestamp'] * 1000
        symbol = None
        if market:
            symbol = market['symbol']
        last = float(ticker['lastPrice'])
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': None,
            'low': None,
            'bid': float(ticker['bestBid']),
            'bidVolume': None,
            'ask': float(ticker['bestAsk']),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': float(ticker['volume24h']),
            'quoteVolume': None,
            'info': ticker,
        }

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        ticker = await self.publicGetMarketIdTick(self.extend({
            'id': market['id'],
        }, params))
        return self.parse_ticker(ticker, market)

    def parse_trade(self, trade, market):
        timestamp = trade['date'] * 1000
        return {
            'info': trade,
            'id': str(trade['tid']),
            'order': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'type': None,
            'side': None,
            'price': trade['price'],
            'amount': trade['amount'],
        }

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        response = await self.publicGetMarketIdTrades(self.extend({
            # 'since': 59868345231,
            'id': market['id'],
        }, params))
        return self.parse_trades(response, market, since, limit)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        multiplier = 100000000  # for price and volume
        orderSide = 'Bid' if (side == 'buy') else 'Ask'
        order = self.ordered({
            'currency': market['quote'],
        })
        order['currency'] = market['quote']
        order['instrument'] = market['base']
        order['price'] = int(price * multiplier)
        order['volume'] = int(amount * multiplier)
        order['orderSide'] = orderSide
        order['ordertype'] = self.capitalize(type)
        order['clientRequestId'] = str(self.nonce())
        response = await self.privatePostOrderCreate(order)
        return {
            'info': response,
            'id': str(response['id']),
        }

    async def cancel_orders(self, ids):
        await self.load_markets()
        for i in range(0, len(ids)):
            ids[i] = int(ids[i])
        return await self.privatePostOrderCancel({'orderIds': ids})

    async def cancel_order(self, id, symbol=None, params={}):
        await self.load_markets()
        return await self.cancel_orders([id])

    def parse_my_trade(self, trade, market):
        multiplier = 100000000
        timestamp = trade['creationTime']
        side = 'buy' if (trade['side'] == 'Bid') else 'sell'
        # BTCMarkets always charge in AUD for AUD-related transactions.
        currency = market['quote'] if (market['quote'] == 'AUD') else market['base']
        return {
            'info': trade,
            'id': str(trade['id']),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'type': None,
            'side': side,
            'price': trade['price'] / multiplier,
            'fee': {
                'currency': currency,
                'cost': trade['fee'] / multiplier,
            },
            'amount': trade['volume'] / multiplier,
            'order': self.safe_string(trade, 'orderId'),
        }

    def parse_my_trades(self, trades, market=None, since=None, limit=None):
        result = []
        for i in range(0, len(trades)):
            trade = self.parse_my_trade(trades[i], market)
            result.append(trade)
        return result

    def parse_order(self, order, market=None):
        multiplier = 100000000
        side = 'buy' if (order['orderSide'] == 'Bid') else 'sell'
        type = 'limit' if (order['ordertype'] == 'Limit') else 'market'
        timestamp = order['creationTime']
        if not market:
            market = self.market(order['instrument'] + '/' + order['currency'])
        status = 'open'
        if order['status'] == 'Failed' or order['status'] == 'Cancelled' or order['status'] == 'Partially Cancelled' or order['status'] == 'Error':
            status = 'canceled'
        elif order['status'] == 'Fully Matched' or order['status'] == 'Partially Matched':
            status = 'closed'
        price = self.safe_float(order, 'price') / multiplier
        amount = self.safe_float(order, 'volume') / multiplier
        remaining = self.safe_float(order, 'openVolume', 0.0) / multiplier
        filled = amount - remaining
        cost = price * amount
        trades = self.parse_my_trades(order['trades'], market)
        result = {
            'info': order,
            'id': str(order['id']),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': market['symbol'],
            'type': type,
            'side': side,
            'price': price,
            'cost': cost,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'trades': trades,
            'fee': None,
        }
        return result

    async def fetch_order(self, id, symbol=None, params={}):
        await self.load_markets()
        ids = [int(id)]
        response = await self.privatePostOrderDetail(self.extend({
            'orderIds': ids,
        }, params))
        numOrders = len(response['orders'])
        if numOrders < 1:
            raise OrderNotFound(self.id + ' No matching order found: ' + id)
        order = response['orders'][0]
        return self.parse_order(order)

    def prepare_history_request(self, market, since=None, limit=None):
        request = self.ordered({
            'currency': market['quote'],
            'instrument': market['base'],
        })
        if limit is not None:
            request['limit'] = limit
        else:
            request['limit'] = 100
        if since is not None:
            request['since'] = since
        else:
            request['since'] = 0
        return request

    async def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        if not symbol:
            raise NotSupported(self.id + ': fetchOrders requires a `symbol` parameter.')
        await self.load_markets()
        market = self.market(symbol)
        request = self.prepare_history_request(market, since, limit)
        response = await self.privatePostOrderHistory(self.extend(request, params))
        return self.parse_orders(response['orders'], market)

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        if not symbol:
            raise NotSupported(self.id + ': fetchOpenOrders requires a `symbol` parameter.')
        await self.load_markets()
        market = self.market(symbol)
        request = self.prepare_history_request(market, since, limit)
        response = await self.privatePostOrderOpen(self.extend(request, params))
        return self.parse_orders(response['orders'], market)

    async def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        orders = await self.fetch_orders(symbol, since, limit, params)
        return self.filter_by(orders, 'status', 'closed')

    async def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        if not symbol:
            raise NotSupported(self.id + ': fetchMyTrades requires a `symbol` parameter.')
        await self.load_markets()
        market = self.market(symbol)
        request = self.prepare_history_request(market, since, limit)
        response = await self.privatePostOrderTradeHistory(self.extend(request, params))
        return self.parse_my_trades(response['trades'], market)

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        uri = '/' + self.implode_params(path, params)
        url = self.urls['api'][api] + uri
        if api == 'private':
            self.check_required_credentials()
            nonce = str(self.nonce())
            # eslint-disable-next-line quotes
            auth = uri + "\n" + nonce + "\n"
            headers = {
                'Content-Type': 'application/json',
                'apikey': self.apiKey,
                'timestamp': nonce,
            }
            if method == 'POST':
                body = self.json(params)
                auth += body
            secret = base64.b64decode(self.secret)
            signature = self.hmac(self.encode(auth), secret, hashlib.sha512, 'base64')
            headers['signature'] = self.decode(signature)
        else:
            if params:
                url += '?' + self.urlencode(params)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body):
        if len(body) < 2:
            return  # fallback to default error handler
        if body[0] == '{':
            response = json.loads(body)
            if 'success' in response:
                if not response['success']:
                    error = self.safe_string(response, 'errorCode')
                    message = self.id + ' ' + self.json(response)
                    if error in self.exceptions:
                        ExceptionClass = self.exceptions[error]
                        raise ExceptionClass(message)
                    else:
                        raise ExchangeError(message)

    async def request(self, path, api='public', method='GET', params={}, headers=None, body=None):
        response = await self.fetch2(path, api, method, params, headers, body)
        return response
