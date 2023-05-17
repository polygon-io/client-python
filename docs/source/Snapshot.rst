.. _snapshot_header:

Snapshot
=================================

=================================
Get all snapshots
=================================

- `Stocks snapshot all tickers`_
- `Options snapshot all tickers`_
- `Forex snapshot all tickers`_
- `Crypto snapshot all tickers`_

.. automethod:: polygon.RESTClient.list_asset_snapshots

=================================
Get all snapshots
=================================

- `Stocks snapshot all tickers (deprecated)`_
- `Forex snapshot all tickers (deprecated)`_
- `Crypto snapshot all tickers (deprecated)`_

.. automethod:: polygon.RESTClient.get_snapshot_all

=================================
Get gainers/losers snapshot
=================================

- `Stocks snapshot gainers/losers`_
- `Forex snapshot gainers/losers`_
- `Crypto snapshot gainers/losers`_

.. automethod:: polygon.RESTClient.get_snapshot_direction

=================================
Get ticker snapshot
=================================

- `Stocks snapshot ticker`_
- `Forex snapshot ticker`_
- `Crypto snapshot ticker`_

.. automethod:: polygon.RESTClient.get_snapshot_ticker

=================================
Get options snapshot
=================================

- `Options snapshot option contract`_

.. automethod:: polygon.RESTClient.get_snapshot_option

=================================
Get crypto L2 book snapshot
=================================

- `Crypto snapshot ticker full book (L2)`_

.. automethod:: polygon.RESTClient.get_snapshot_crypto_book

.. _Stocks snapshot all tickers: https://polygon.io/docs/stocks/get_v3_snapshot
.. _Options snapshot all tickers: https://polygon.io/docs/options/get_v3_snapshot
.. _Forex snapshot all tickers: https://polygon.io/docs/forex/get_v3_snapshot
.. _Crypto snapshot all tickers:: https://polygon.io/docs/crypto/get_v3_snapshot
.. _Stocks snapshot all tickers (deprecated): https://polygon.io/docs/stocks/get_v2_snapshot_locale_us_markets_stocks_tickers
.. _Options snapshot all tickers (deprecated): https://polygon.io/docs/options/get_v2_snapshot_locale_us_markets_stocks_tickers
.. _Forex snapshot all tickers (deprecated): https://polygon.io/docs/forex/get_v2_snapshot_locale_global_markets_forex_tickers
.. _Crypto snapshot all tickers (deprecated):: https://polygon.io/docs/crypto/get_v2_snapshot_locale_global_markets_crypto_tickers
.. _Stocks snapshot gainers/losers: https://polygon.io/docs/stocks/get_v2_snapshot_locale_us_markets_stocks__direction
.. _Forex snapshot gainers/losers: https://polygon.io/docs/forex/get_v2_snapshot_locale_global_markets_forex__direction
.. _Crypto snapshot gainers/losers: https://polygon.io/docs/crypto/get_v2_snapshot_locale_global_markets_crypto__direction
.. _Stocks snapshot ticker: https://polygon.io/docs/stocks/get_v2_snapshot_locale_us_markets_stocks_tickers__stocksticker
.. _Forex snapshot ticker: https://polygon.io/docs/forex/get_v2_snapshot_locale_global_markets_forex_tickers__ticker
.. _Crypto snapshot ticker: https://polygon.io/docs/crypto/get_v2_snapshot_locale_global_markets_crypto_tickers__ticker
.. _Options snapshot option contract: https://polygon.io/docs/options/get_v3_snapshot_options__underlyingasset___optioncontract
.. _Crypto snapshot ticker full book (L2): https://polygon.io/docs/crypto/get_v2_snapshot_locale_global_markets_crypto_tickers__ticker__book