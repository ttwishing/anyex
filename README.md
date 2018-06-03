# anyex – ANY EXchange trading library

This library is originated from the famous [CCXT](https://github.com/ccxt/ccxt). The main reason to create this new package is due to the high maintenance cost of the original one, as it is written and maintained in three different languages, which makes it inconvenient for pythoners.

This library is under heavily development, use at your own risk!

Contribution is welcomed!

## Install

Before our auto CI is set up and ready to go, it is recommended to use this repo as your installation's primary source.

```shell
git clone https://github.com/anyexchange/anyex
cd anyex
python setup.py install
```



Until further notice, the `pip` install will ONLY help you set up the original code copied from CCXT.

```shell
pip install anyex
```



## Quickstart

### Exchanges

1. find out whether the desired exchange platform is supported,

   ```python
   >>> python
   >>> import anyex
   >>> anyex.exchanges  # will give you a list of supported exchanges
   ['_1broker', '_1btcxe', 'acx', 'allcoin', 'anxpro', 'bibox', 'binance', 'bit2c', 'bitbank', 'bitbay', 'bitfinex', 'bitfinex2', 'bitflyer', 'bithumb', 'bitkk', 'bitlish', 'bitmarket', 'bitmex', 'bitso', 'bitstamp', 'bitstamp1', 'bittrex', 'bitz', 'bl3p', 'bleutrade', 'braziliex', 'btcbox', 'btcchina', 'btcexchange', 'btcmarkets', 'btctradeim', 'btctradeua', 'btcturk', 'btcx', 'bxinth', 'ccex', 'cex', 'chbtc', 'chilebit', 'cobinhood', 'coincheck', 'coinegg', 'coinex', 'coinexchange', 'coinfloor', 'coingi', 'coinmarketcap', 'coinmate', 'coinnest', 'coinone', 'coinsecure', 'coinspot', 'coolcoin', 'cryptopia', 'dsx', 'ethfinex', 'exmo', 'exx', 'flowbtc', 'foxbit', 'fybse', 'fybsg', 'gatecoin', 'gateio', 'gdax', 'gemini', 'getbtc', 'hadax', 'hitbtc', 'hitbtc2', 'huobi', 'huobicny', 'huobipro', 'ice3x', 'independentreserve', 'indodax', 'itbit', 'jubi', 'kkex', 'kraken', 'kucoin', 'kuna', 'lakebtc', 'lbank', 'liqui', 'livecoin', 'luno', 'lykke', 'mercado', 'mixcoins', 'negociecoins', 'nova', 'okcoincny', 'okcoinusd', 'okex', 'paymium', 'poloniex', 'qryptos', 'quadrigacx', 'quoinex', 'southxchange', 'surbitcoin', 'therock', 'tidebit', 'tidex', 'urdubit', 'vaultoro', 'vbtc', 'virwox', 'wex', 'xbtce', 'yobit', 'yunbi', 'zaif', 'zb']
   ```

2. initialize an exchange platform instance

   ```python
   >>> gdax = anyex.gdax()
   ```



3. if needed, use  `load_markets` to fetch information about this exchange platform,

   ```python
   >>> gdax.load_markets()  # this method will give out A LOT data!
   {u'LTC/USD': {'quote': u'USD', 'symbol': u'LTC/USD', 'precision': {'amount': 8, 'price': 2}, 'fee_loaded': False, 'base': u'LTC', 'active': True, 'id': u'LTC-USD', 'info': {u'quote_currency': u'USD', u'status': u'online', u'post_only': False, u'display_name': u'LTC/USD', u'margin_enabled': False, u'cancel_only': False, u'quote_increment': u'0.01', u'limit_only': False, u'base_max_size': u'4000', u'max_market_funds': u'1000000', u'min_market_funds': u'10', u'base_currency': u'LTC', u'status_message': None, u'id': u'LTC-USD', u'base_min_size': u'0.1'}, 'taker': 0.003, 'limits': {'amount': {'max': 4000.0, 'min': 0.1}, 'cost': {'max': 1000000.0, 'min': 10.0}, 'price': {'max': None, 'min': 0.01}}, 'tierBased': True, 'percentage': True, 'maker': 0.0}, ...
   ```



4. if you need to use the private methods, such as making orders or fetching balances, then api key and api secret are needed, as in the following,

   ```python
   >>> gdax.apiKey = 'your api key'
   >>> gdax.secret = 'your secret'
   ```

   

### Symbols

Symbols in anyex are formatted as `quote asset symbol/base asset symbol`, all uppercased.

For example, if you want to do anything (get tickers, make orders, etc.) with bitcoin quoted in USD, then the symbol is `BTC/USD`, if you are interested in a trading pair, say EOS valued in bitcoin, then the symbol is `EOS/BTC` .



### Tickers

To fetch a ticker, simply do,

```python
>>> import anyex
>>> bitfinex = anyex.bitfinex()
>>> bitfinex.fetch_ticker('BTC/USD')  # get trading pair btc/usd
{'info': {u'volume': u'14963.14256026', u'timestamp': u'1528022227.0895257', u'bid': u'7728.6', u'last_price': u'7728.6', u'mid': u'7728.65', u'high': u'7779.0', u'low': u'7590.0', u'ask': u'7728.7'}, 'askVolume': None, 'last': 7728.6, 'timestamp': 1528022227089.5256, 'symbol': u'BTC/USD', 'previousClose': None, 'bidVolume': None, 'datetime': '2018-06-03T10:37:07.890Z', 'high': 7779.0, 'average': 7728.65, 'low': 7590.0, 'quoteVolume': None, 'ask': 7728.7, 'close': 7728.6, 'percentage': None, 'vwap': None, 'open': None, 'bid': 7728.6, 'change': None, 'baseVolume': 14963.14256026}

>>> bitfinex.fetch_ticker('EOS/BTC')  # get trading pair eos/btc
{'info': {u'volume': u'2446839.03769225', u'timestamp': u'1528022245.0409648', u'bid': u'0.0019', u'last_price': u'0.0019', u'mid': u'0.00190045', u'high': u'0.0020357', u'low': u'0.001794', u'ask': u'0.0019009'}, 'askVolume': None, 'last': 0.0019, 'timestamp': 1528022245040.9648, 'symbol': u'EOS/BTC', 'previousClose': None, 'bidVolume': None, 'datetime': '2018-06-03T10:37:25.400Z', 'high': 0.0020357, 'average': 0.00190045, 'low': 0.001794, 'quoteVolume': None, 'ask': 0.0019009, 'close': 0.0019, 'percentage': None, 'vwap': None, 'open': None, 'bid': 0.0019, 'change': None, 'baseVolume': 2446839.03769225}
```



### Orderbooks

To fetch the orderbooks, simply do,

```python
>>> import anyex
>>> bitfinex = anyex.bitfinex()
>>> bitfinex.fetch_order_book('EOS/BTC')
{'nonce': None, 'timestamp': None, 'bids': [[0.0019023, 200.0], [0.0019019, 60.0], [0.0019012, 30.0], [0.0019011, 130.0], [0.001901, 100.0], [0.0019009, 10.0], [0.0019, 812.85605091], [0.0018996, 30.0], [0.0018993, 68.21809585], [0.0018985, 200.0], [0.0018984, 33.27991993], [0.0018982, 265.29494411], [0.0018964, 5.497759], [0.0018955, 2117.55503198], [0.0018954, 1706.4733], [0.0018953, 2554.61576186], [0.0018952, 2483.5504428], [0.0018951, 649.074083], [0.0018943, 105.15804858], [0.001894, 69.94478043], [0.0018932, 6.0], [0.001893, 12.0], [0.0018929, 6.0], [0.0018927, 6.0], [0.0018923, 34.06226582]], 'asks': [[0.0019044, 23.84358608], [0.0019046, 65.83158608], [0.0019049, 4.0], [0.0019053, 4.0], [0.0019054, 26.0], [0.0019055, 105.080164], [0.0019062, 400.0], [0.0019063, 577.57368702], [0.0019076, 398.1], [0.0019079, 200.0], [0.001908, 154.86488615], [0.0019089, 226.05028102], [0.0019091, 33.14801328], [0.0019096, 3055.4006], [0.0019097, 110.0], [0.0019098, 210.06906354], [0.00191, 15.0], [0.0019104, 2000.0], [0.0019105, 100.0], [0.0019128, 1955.47586163], [0.0019129, 4583.2343], [0.001913, 1574.84], [0.0019135, 130.0], [0.0019136, 6.0], [0.0019152, 3.7]], 'datetime': None}
```



### Orders

To create an order,

```python
# create market sell order
# require positional arguments, symbol and amount
bitfinex.create_market_sell_order('EOS/BTC', 100)

# create market buy order
# require positional arguments, symbol and amount
bitfinex.create_market_buy_order('EOS/BTC', 100)

# create limit sell order
# require positional arguments, symbol, amount, and price
bitfinex.create_limit_sell_order('EOS/BTC', 100, 0.09)

# create limit buy order
# require positional arguments, symbol, amount, and price
bitfinex.create_limit_buy_order('EOS/BTC', 100, 0.08)
```



To cancel an order,

```python
# need positional arguments, order_id and symbol
bitfinex.cancel_order(10898, 'EOS/BTC')
```



To fetch an order,

```python
# need positional arguments, order_id and symbol
bitfinex.fetch_order(10898, 'EOS/BTC')
```



### Futures

Currently, future trading is supported on the following exchange platforms,

1. okex, for more information, chech their [API docs](https://github.com/okcoin-okex/API-docs-OKEx.com) (it is a huge mass though :(, especially compared to bitmex's).

```python
# create a long position
okex.create_future_long_position_limit(
    symbol,
    size,
    price,
    {
        'contract_type': your_contract_type,  # this_week, next_week, quarter
        'leverage_rate': your leverage_rate  # 10 or 20
   	}
)

# create a short position
okex.create_future_long_position_limit(
    symbol,
    size,
    price,
    {
        'contract_type': your_contract_type,  # this_week, next_week, quarter
        'leverage_rate': your leverage_rate  # 10 or 20
   	}
)

# fetch a position
okex.fetch_future_position(
	symbol,
    {
        'contract_type': your_contract_type,  # this_week, next_week, quarter
    }
)
```
2. bitmex, for more information, chech their [API docs](https://www.bitmex.com/app/apiOverview).

```python
# create a long position
bitmex.create_future_long_position_limit(
    symbol,
    size,
    price
)

# create a short position
bitnex.create_future_long_position_limit(
    symbol,
    size,
    price
)

# fetch a position
bitmex.fetch_future_position(
	symbol
)

# edit a position
bitmex.edit_position_leverage(
    symbol,
    leverage
)
```





### More methods

While the above methods may be enough to get you going, there are a HELL lot more methods available, to see it, simply typing,

```python
>>> import anyex
>>> bitfinex = anyex.bitfinex()
>>> dir(bitfinex)
['__class__', '__del__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'account', 'aggregate', 'aiohttpProxy', 'aiohttp_proxy', 'amountToLots', 'amountToPrecision', 'amountToString', 'amount_to_lots', 'amount_to_precision', 'amount_to_string', 'api', 'apiKey', 'apiSecret', 'arrayConcat', 'array_concat', 'asyncioLoop', 'asyncio_loop', 'balance', 'base64urlencode', 'binaryConcat', 'binaryToString', 'binary_concat', 'binary_to_string', 'buildOhlcv', 'build_ohlcv', 'calculateFee', 'calculate_fee', 'cancelOrder', 'cancel_order', 'capitalize', 'checkAddress', 'checkRequiredCredentials', 'check_address', 'check_required_credentials', 'closeFutureLongPositionLimit', 'closeFutureLongPositionMarket', 'closeFutureShortPositionLimit', 'closeFutureShortPositionMarket', 'closePosition', 'close_future_long_position_limit', 'close_future_long_position_market', 'close_future_short_position_limit', 'close_future_short_position_market', 'close_position', 'commonCurrencies', 'commonCurrencyCode', 'common_currency_code', 'convertOhlcvToTradingView', 'convertTradingViewToOhlcv', 'convert_ohlcv_to_trading_view', 'convert_trading_view_to_ohlcv', 'costToPrecision', 'cost_to_precision', 'countries', 'createDepositAddress', 'createFutureLongPositionLimit', 'createFutureLongPositionMarket', 'createFutureShortPositionLimit', 'createFutureShortPositionMarket', 'createLimitBuyOrder', 'createLimitOrder', 'createLimitSellOrder', 'createMarketBuyOrder', 'createMarketOrder', 'createMarketSellOrder', 'createOrder', 'createPosition', 'create_deposit_address', 'create_future_long_position_limit', 'create_future_long_position_market', 'create_future_short_position_limit', 'create_future_short_position_market', 'create_limit_buy_order', 'create_limit_order', 'create_limit_sell_order', 'create_market_buy_order', 'create_market_order', 'create_market_sell_order', 'create_order', 'create_position', 'currencies', 'currenciesById', 'currencies_by_id', 'currency', 'currencyId', 'currency_id', 'decode', 'deepExtend', 'deep_extend', 'defineRestApi', 'define_rest_api', 'describe', 'editLimitBuyOrder', 'editLimitOrder', 'editLimitSellOrder', 'editOrder', 'edit_limit_buy_order', 'edit_limit_order', 'edit_limit_sell_order', 'edit_order', 'enableRateLimit', 'encode', 'encodeUriComponent', 'encode_uri_component', 'exceptions', 'extend', 'extractParams', 'extract_params', 'feeToPrecision', 'fee_to_precision', 'fees', 'fetch', 'fetch2', 'fetchBalance', 'fetchBidsAsks', 'fetchClosedOrders', 'fetchDepositAddress', 'fetchFees', 'fetchFreeBalance', 'fetchFundingFees', 'fetchFuturePosition', 'fetchFuturePositions', 'fetchL2OrderBook', 'fetchMarkets', 'fetchMyTrades', 'fetchOhlcv', 'fetchOpenOrders', 'fetchOrder', 'fetchOrderBook', 'fetchOrderStatus', 'fetchOrderTrades', 'fetchOrders', 'fetchPartialBalance', 'fetchTicker', 'fetchTickers', 'fetchTotalBalance', 'fetchTrades', 'fetchTradingFees', 'fetchUsedBalance', 'fetch_balance', 'fetch_bids_asks', 'fetch_closed_orders', 'fetch_deposit_address', 'fetch_fees', 'fetch_free_balance', 'fetch_funding_fees', 'fetch_future_position', 'fetch_future_positions', 'fetch_l2_order_book', 'fetch_markets', 'fetch_my_trades', 'fetch_ohlcv', 'fetch_open_orders', 'fetch_order', 'fetch_order_book', 'fetch_order_status', 'fetch_order_trades', 'fetch_orders', 'fetch_partial_balance', 'fetch_ticker', 'fetch_tickers', 'fetch_total_balance', 'fetch_trades', 'fetch_trading_fees', 'fetch_used_balance', 'filterBy', 'filterByArray', 'filterBySinceLimit', 'filterBySymbol', 'filterBySymbolSinceLimit', 'filter_by', 'filter_by_array', 'filter_by_since_limit', 'filter_by_symbol', 'filter_by_symbol_since_limit', 'findBroadlyMatchedKey', 'findMarket', 'findSymbol', 'find_broadly_matched_key', 'find_market', 'find_symbol', 'getCurrencyName', 'get_currency_name', 'groupBy', 'group_by', 'gzipDeflate', 'gzip_deflate', 'handleErrors', 'handleRestErrors', 'handleRestResponse', 'handle_errors', 'handle_rest_errors', 'handle_rest_response', 'has', 'hash', 'headers', 'hmac', 'id', 'ids', 'implodeParams', 'implode_params', 'inArray', 'in_array', 'indexBy', 'index_by', 'iso8601', 'json', 'jwt', 'keysort', 'lastHttpResponse', 'lastJsonResponse', 'lastResponseHeaders', 'lastRestPollTimestamp', 'lastRestRequestTimestamp', 'last_http_response', 'last_json_response', 'last_response_headers', 'limits', 'loadFees', 'loadMarkets', 'load_fees', 'load_markets', 'logger', 'market', 'marketId', 'marketIds', 'market_id', 'market_ids', 'markets', 'marketsById', 'markets_by_id', 'microseconds', 'milliseconds', 'minFundingAddressLength', 'msec', 'name', 'nonce', 'omit', 'options', 'orderbooks', 'ordered', 'orders', 'origin', 'parse8601', 'parseBalance', 'parseBidAsk', 'parseBidsAsks', 'parseDate', 'parseJsonResponse', 'parseOhlcv', 'parseOhlcvs', 'parseOrder', 'parseOrderBook', 'parseOrders', 'parsePosition', 'parsePositions', 'parseTicker', 'parseTimeframe', 'parseTrade', 'parseTrades', 'parse_balance', 'parse_bid_ask', 'parse_bids_asks', 'parse_date', 'parse_ohlcv', 'parse_ohlcvs', 'parse_order', 'parse_order_book', 'parse_orders', 'parse_position', 'parse_positions', 'parse_ticker', 'parse_timeframe', 'parse_trade', 'parse_trades', 'password', 'pluck', 'populateFees', 'populate_fees', 'precision', 'precisionFromString', 'precisionMode', 'precision_from_string', 'prepareRequestHeaders', 'prepare_request_headers', 'priceToPrecision', 'price_to_precision', 'privatePostAccountFees', 'privatePostAccountInfos', 'privatePostBalances', 'privatePostBasketManage', 'privatePostCredits', 'privatePostDepositNew', 'privatePostFundingClose', 'privatePostHistory', 'privatePostHistoryMovements', 'privatePostKeyInfo', 'privatePostMarginInfos', 'privatePostMytrades', 'privatePostMytradesFunding', 'privatePostOfferCancel', 'privatePostOfferNew', 'privatePostOfferStatus', 'privatePostOffers', 'privatePostOffersHist', 'privatePostOrderCancel', 'privatePostOrderCancelAll', 'privatePostOrderCancelMulti', 'privatePostOrderCancelReplace', 'privatePostOrderNew', 'privatePostOrderNewMulti', 'privatePostOrderStatus', 'privatePostOrders', 'privatePostOrdersHist', 'privatePostPositionClaim', 'privatePostPositionClose', 'privatePostPositions', 'privatePostSummary', 'privatePostTakenFunds', 'privatePostTotalTakenFunds', 'privatePostTransfer', 'privatePostUnusedTakenFunds', 'privatePostWithdraw', 'private_post_account_fees', 'private_post_account_infos', 'private_post_balances', 'private_post_basket_manage', 'private_post_credits', 'private_post_deposit_new', 'private_post_funding_close', 'private_post_history', 'private_post_history_movements', 'private_post_key_info', 'private_post_margin_infos', 'private_post_mytrades', 'private_post_mytrades_funding', 'private_post_offer_cancel', 'private_post_offer_new', 'private_post_offer_status', 'private_post_offers', 'private_post_offers_hist', 'private_post_order_cancel', 'private_post_order_cancel_all', 'private_post_order_cancel_multi', 'private_post_order_cancel_replace', 'private_post_order_new', 'private_post_order_new_multi', 'private_post_order_status', 'private_post_orders', 'private_post_orders_hist', 'private_post_position_claim', 'private_post_position_close', 'private_post_positions', 'private_post_summary', 'private_post_taken_funds', 'private_post_total_taken_funds', 'private_post_transfer', 'private_post_unused_taken_funds', 'private_post_withdraw', 'proxies', 'proxy', 'publicGetBookSymbol', 'publicGetLendbookCurrency', 'publicGetLendsCurrency', 'publicGetPubtickerSymbol', 'publicGetStatsSymbol', 'publicGetSymbols', 'publicGetSymbolsDetails', 'publicGetTickers', 'publicGetToday', 'publicGetTradesSymbol', 'public_get_book_symbol', 'public_get_lendbook_currency', 'public_get_lends_currency', 'public_get_pubticker_symbol', 'public_get_stats_symbol', 'public_get_symbols', 'public_get_symbols_details', 'public_get_tickers', 'public_get_today', 'public_get_trades_symbol', 'purgeCachedOrders', 'purge_cached_orders', 'raiseError', 'raise_error', 'rateLimit', 'rateLimitMaxTokens', 'rateLimitTokens', 'rateLimitUpdateTime', 'rawencode', 'request', 'requiredCredentials', 'restPollerLoopIsRunning', 'restRequestQueue', 'safeFloat', 'safeInteger', 'safeString', 'safeValue', 'safe_float', 'safe_integer', 'safe_string', 'safe_value', 'sec', 'seconds', 'secret', 'session', 'setMarkets', 'set_markets', 'sign', 'sortBy', 'sort_by', 'substituteCommonCurrencyCodes', 'sum', 'symbols', 'throttle', 'tickers', 'timeframes', 'timeout', 'toArray', 'to_array', 'tokenBucket', 'trades', 'truncate', 'truncateToString', 'truncate_to_string', 'twofa', 'uid', 'unique', 'unjson', 'url', 'urlencode', 'urls', 'usec', 'userAgent', 'userAgents', 'uuid', 'v2GetCandlesTradeTimeframeSymbolHist', 'v2GetCandlesTradeTimeframeSymbolLast', 'v2GetCandlesTradeTimeframeSymbolSection', 'v2_get_candles_trade_timeframe_symbol_hist', 'v2_get_candles_trade_timeframe_symbol_last', 'v2_get_candles_trade_timeframe_symbol_section', 'verbose', 'version', 'withdraw', 'ymd', 'ymdhms']
```

We will work on explaining these, later :)



### Documentation

A more detailed methodology and documentation is under development.

