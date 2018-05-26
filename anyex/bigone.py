from anyex.base.exchange import Exchange
import base64
import hashlib
import math
import json
from anyex.base.errors import ExchangeError
from anyex.base.errors import NotSupported
from anyex.base.errors import AuthenticationError
from anyex.base.errors import InsufficientFunds
from anyex.base.errors import InvalidOrder
from anyex.base.errors import OrderNotFound
from anyex.base.errors import DDoSProtection
from anyex.base.errors import ExchangeNotAvailable
from anyex.base.errors import InvalidNonce
from anyex.base.decimal_to_precision import ROUND
from anyex.base.decimal_to_precision import TRUNCATE
from anyex.base.decimal_to_precision import SIGNIFICANT_DIGITS


class bigone (Exchange):

    def describe(self):
        return self.deep_extend(super(bigone, self).describe(), {
            'id': 'bigone',
            'name': 'BigONE',
            'countries': 'CN',
            'urls': {
                'logo': 'https://big.one/assets/icons-49607d33ce9fc8cdcf62d9f51a73ddc7-favicon.ico',
                'api': 'https://api.big.one',
                'www': 'https://big.one',
                'doc': [
                    'https://developer.big.one/',
                ],
            },
            'requiredCredentials': {
                'apiKey': True,
                'secret': False,
            },
            'api': {
                'public': {
                    'get': [
                        'markets',
                        'markets/{symbol}/book'
                    ],
                },
                'private': {
                    'post': [
                    ],
                },
            },
            'fees': {
            },
            'commonCurrencies': {
            },
            'exceptions': {
            },
        })

    def sign(self, path, api, method, params, headers, body):
        request = '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        url = self.urls['api'] + request
        if api == 'public':
            if query:
                suffix = '?' + self.urlencode(query)
                url += suffix
                request += suffix
        if api == 'private':
            self.check_required_credentials()
            query = self.json(query)
            headers = {'Accept': 'application/json',
                       'Big-Device-Id': self.uuid(),
                       'Authorization': 'Bearer {}'.format(self.apiKey)}

        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def fetch_markets(self):
        markets = self.publicGetMarkets()
        markets = markets.get('data', [])
        result = []
        for p in range(0, len(markets)):
            market = markets[p]
            id = market['symbol']
            baseId = market['base']
            quoteId = market['quote']
            symbol = quoteId + '/' + baseId
            precision = {
                'price': 8,
                'amount': market['quote_increment'],
            }
            limits = {
                'amount': {
                    'min': float(market['total_min']),
                    'max': None,
                },
                'price': {
                    'min': math.pow(10, -precision['price']),
                    'max': math.pow(10, precision['price']),
                },
            }
            limits['cost'] = {
                'min': market['base_min'],
                'max': market['base_max'],
            }
            market.pop('metrics')
            result.append({
                'id': id,
                'symbol': symbol,
                'base': baseId,
                'quote': quoteId,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': True,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
        }
        orderbook = self.publicGetMarketsSymbolBook(self.extend(request, params))
        orderbook = orderbook.get('data', {})
        return self.parse_order_book(orderbook, None, 'bids', 'asks', 'price', 'amount')
