# Get Trades - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/trades/trades

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Trades

Get Trades

[User Guide](/polymarket-learn/get-started/what-is-polymarket)[For Developers](/quickstart/overview)[Changelog](/changelog/changelog)

  * [Polymarket](https://polymarket.com)
  * [Discord Community](https://discord.gg/polymarket)
  * [Twitter](https://x.com/polymarket)



##### Developer Quickstart

  * [Developer Quickstart](/quickstart/overview)
  * [Fetching Market Data](/quickstart/fetching-data)
  * [Placing Your First Order](/quickstart/first-order)
  * [Glossary](/quickstart/reference/glossary)
  * [API Rate Limits](/quickstart/introduction/rate-limits)
  * [Endpoints](/quickstart/reference/endpoints)



##### Market Makers

  * [Market Maker Introduction](/developers/market-makers/introduction)
  * [Setup](/developers/market-makers/setup)
  * [Trading](/developers/market-makers/trading)
  * [Liquidity Rewards](/developers/market-makers/liquidity-rewards)
  * [Maker Rebates Program](/developers/market-makers/maker-rebates-program)
  * [Data Feeds](/developers/market-makers/data-feeds)
  * [Inventory Management](/developers/market-makers/inventory)



##### Polymarket Builders Program

  * [Builder Program Introduction](/developers/builders/builder-intro)
  * [Builder Tiers](/developers/builders/builder-tiers)
  * [Builder Profile & Keys](/developers/builders/builder-profile)
  * [Order Attribution](/developers/builders/order-attribution)
  * [Relayer Client](/developers/builders/relayer-client)
  * [Examples](/developers/builders/examples)



##### Central Limit Order Book

  * [CLOB Introduction](/developers/CLOB/introduction)
  * [Status](/developers/CLOB/status)
  * [Quickstart](/developers/CLOB/quickstart)
  * [Authentication](/developers/CLOB/authentication)
  * [Geographic Restrictions](/developers/CLOB/geoblock)
  * Client

  * REST API

  * Historical Timeseries Data

  * Order Management

  * Trades

    * [Trades Overview](/developers/CLOB/trades/trades-overview)
    * [Get Trades](/developers/CLOB/trades/trades)



##### Websocket

  * [WSS Overview](/developers/CLOB/websocket/wss-overview)
  * [WSS Quickstart](/quickstart/websocket/WSS-Quickstart)
  * [WSS Authentication](/developers/CLOB/websocket/wss-auth)
  * [User Channel](/developers/CLOB/websocket/user-channel)
  * [Market Channel](/developers/CLOB/websocket/market-channel)



##### Real Time Data Stream

  * [RTDS Overview](/developers/RTDS/RTDS-overview)
  * [RTDS Crypto Prices](/developers/RTDS/RTDS-crypto-prices)
  * [RTDS Comments](/developers/RTDS/RTDS-comments)



##### Gamma Structure

  * [Overview](/developers/gamma-markets-api/overview)
  * [Gamma Structure](/developers/gamma-markets-api/gamma-structure)
  * [Fetching Markets](/developers/gamma-markets-api/fetch-markets-guide)



##### Gamma Endpoints

  * Gamma Status

  * Sports

  * Tags

  * Events

  * Markets

  * Series

  * Comments

  * Profiles

  * Search




##### Data-API

  * Data API Status

  * Core

  * Misc

  * Builders




##### Bridge & Swap

  * [Overview](/developers/misc-endpoints/bridge-overview)
  * Bridge




##### Subgraph

  * [Overview](/developers/subgraph/overview)



##### Resolution

  * [Resolution](/developers/resolution/UMA)



##### Conditional Token Frameworks

  * [Overview](/developers/CTF/overview)
  * [Splitting USDC](/developers/CTF/split)
  * [Merging Tokens](/developers/CTF/merge)
  * [Reedeeming Tokens](/developers/CTF/redeem)
  * [Deployment and Additional Information](/developers/CTF/deployment-resources)



##### Proxy Wallets

  * [Proxy wallet](/developers/proxy-wallet)



##### Negative Risk

  * [Overview](/developers/neg-risk/overview)



Python

Typescript

Copy

Ask AI
    
    
    from py_clob_client.clob_types import TradeParams
    
    resp = client.get_trades(
        TradeParams(
            maker_address=client.get_address(),
            market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        ),
    )
    print(resp)
    print("Done!")
    

Trades

# Get Trades

This endpoint requires a L2 Header. 

Get trades for the authenticated user based on the provided filters. **HTTP REQUEST** `GET /<clob-endpoint>/data/trades`

### 

​

Request Parameters

Name| Required| Type| Description  
---|---|---|---  
id| no| string| id of trade to fetch  
taker| no| string| address to get trades for where it is included as a taker  
maker| no| string| address to get trades for where it is included as a maker  
market| no| string| market for which to get the trades (condition ID)  
before| no| string| unix timestamp representing the cutoff up to which trades that happened before then can be included  
after| no| string| unix timestamp representing the cutoff for which trades that happened after can be included  
  
### 

​

Response Format

Name| Type| Description  
---|---|---  
null| Trade[]| list of trades filtered by query parameters  
  
A `Trade` object is of the form:

Name| Type| Description  
---|---|---  
id| string| trade id  
taker_order_id| string| hash of taker order (market order) that catalyzed the trade  
market| string| market id (condition id)  
asset_id| string| asset id (token id) of taker order (market order)  
side| string| buy or sell  
size| string| size  
fee_rate_bps| string| the fees paid for the taker order expressed in basic points  
price| string| limit price of taker order  
status| string| trade status (see above)  
match_time| string| time at which the trade was matched  
last_update| string| timestamp of last status update  
outcome| string| human readable outcome of the trade  
maker_address| string| funder address of the taker of the trade  
owner| string| api key of taker of the trade  
transaction_hash| string| hash of the transaction where the trade was executed  
bucket_index| integer| index of bucket for trade in case trade is executed in multiple transactions  
maker_orders| MakerOrder[]| list of the maker trades the taker trade was filled against  
type| string| side of the trade: TAKER or MAKER  
  
A `MakerOrder` object is of the form:

Name| Type| Description  
---|---|---  
order_id| string| id of maker order  
maker_address| string| maker address of the order  
owner| string| api key of the owner of the order  
matched_amount| string| size of maker order consumed with this trade  
fee_rate_bps| string| the fees paid for the taker order expressed in basic points  
price| string| price of maker order  
asset_id| string| token/asset id  
outcome| string| human readable outcome of the maker order  
side| string| the side of the maker order. Can be `buy` or `sell`  
  
Python

Typescript

Copy

Ask AI
    
    
    from py_clob_client.clob_types import TradeParams
    
    resp = client.get_trades(
        TradeParams(
            maker_address=client.get_address(),
            market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        ),
    )
    print(resp)
    print("Done!")
    

[Trades Overview](/developers/CLOB/trades/trades-overview)[WSS Overview](/developers/CLOB/websocket/wss-overview)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
