# User Channel - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/websocket/user-channel

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Websocket

User Channel

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



On this page

  * Trade Message
  * Structure
  * Order Message
  * Structure



Websocket

# User Channel

Authenticated channel for updates related to user activities (orders, trades), filtered for authenticated user by apikey. **SUBSCRIBE** `<wss-channel> user`

## 

​

Trade Message

Emitted when:

  * when a market order is matched (“MATCHED”)
  * when a limit order for the user is included in a trade (“MATCHED”)
  * subsequent status changes for trade (“MINED”, “CONFIRMED”, “RETRYING”, “FAILED”)



### 

​

Structure

Name| Type| Description  
---|---|---  
asset_id| string| asset id (token ID) of order (market order)  
event_type| string| ”trade”  
id| string| trade id  
last_update| string| time of last update to trade  
maker_orders| MakerOrder[]| array of maker order details  
market| string| market identifier (condition ID)  
matchtime| string| time trade was matched  
outcome| string| outcome  
owner| string| api key of event owner  
price| string| price  
side| string| BUY/SELL  
size| string| size  
status| string| trade status  
taker_order_id| string| id of taker order  
timestamp| string| time of event  
trade_owner| string| api key of trade owner  
type| string| ”TRADE”  
  
Where a `MakerOrder` object is of the form:

Name| Type| Description  
---|---|---  
asset_id| string| asset of the maker order  
matched_amount| string| amount of maker order matched in trade  
order_id| string| maker order ID  
outcome| string| outcome  
owner| string| owner of maker order  
price| string| price of maker order  
  
Response

Copy

Ask AI
    
    
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "event_type": "trade",
      "id": "28c4d2eb-bbea-40e7-a9f0-b2fdb56b2c2e",
      "last_update": "1672290701",
      "maker_orders": [
        {
          "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
          "matched_amount": "10",
          "order_id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
          "outcome": "YES",
          "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
          "price": "0.57"
        }
      ],
      "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      "matchtime": "1672290701",
      "outcome": "YES",
      "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "price": "0.57",
      "side": "BUY",
      "size": "10",
      "status": "MATCHED",
      "taker_order_id": "0x06bc63e346ed4ceddce9efd6b3af37c8f8f440c92fe7da6b2d0f9e4ccbc50c42",
      "timestamp": "1672290701",
      "trade_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "type": "TRADE"
    }
    

## 

​

Order Message

Emitted when:

  * When an order is placed (PLACEMENT)
  * When an order is updated (some of it is matched) (UPDATE)
  * When an order is canceled (CANCELLATION)



### 

​

Structure

Name| Type| Description  
---|---|---  
asset_id| string| asset ID (token ID) of order  
associate_trades| string[]| array of ids referencing trades that the order has been included in  
event_type| string| ”order”  
id| string| order id  
market| string| condition ID of market  
order_owner| string| owner of order  
original_size| string| original order size  
outcome| string| outcome  
owner| string| owner of orders  
price| string| price of order  
side| string| BUY/SELL  
size_matched| string| size of order that has been matched  
timestamp| string| time of event  
type| string| PLACEMENT/UPDATE/CANCELLATION  
  
Response

Copy

Ask AI
    
    
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "associate_trades": null,
      "event_type": "order",
      "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
      "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      "order_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "original_size": "10",
      "outcome": "YES",
      "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "price": "0.57",
      "side": "SELL",
      "size_matched": "0",
      "timestamp": "1672290687",
      "type": "PLACEMENT"
    }
    

[WSS Authentication](/developers/CLOB/websocket/wss-auth)[Market Channel](/developers/CLOB/websocket/market-channel)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
