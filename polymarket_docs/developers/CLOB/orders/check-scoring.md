# Check Order Reward Scoring - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/orders/check-scoring

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Order Management

Check Order Reward Scoring

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

    * [Orders Overview](/developers/CLOB/orders/orders)
    * [Place Single Order](/developers/CLOB/orders/create-order)
    * [Place Multiple Orders (Batching)](/developers/CLOB/orders/create-order-batch)
    * [Get Order](/developers/CLOB/orders/get-order)
    * [Get Active Orders](/developers/CLOB/orders/get-active-order)
    * [Check Order Reward Scoring](/developers/CLOB/orders/check-scoring)
    * [Cancel Orders(s)](/developers/CLOB/orders/cancel-orders)
    * [Onchain Order Info](/developers/CLOB/orders/onchain-order-info)
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



Python

Typescript

Copy

Ask AI
    
    
    scoring = client.is_order_scoring(
        OrderScoringParams(
            orderId="0x..."
        )
    )
    print(scoring)
    
    scoring = client.are_orders_scoring(
        OrdersScoringParams(
            orderIds=["0x..."]
        )
    )
    print(scoring)
    

Order Management

# Check Order Reward Scoring

Check if an order is eligble or scoring for Rewards purposes

This endpoint requires a L2 Header. 

Returns a boolean value where it is indicated if an order is scoring or not. **HTTP REQUEST** `GET /<clob-endpoint>/order-scoring?order_id={...}`

### 

​

Request Parameters

Name| Required| Type| Description  
---|---|---|---  
orderId| yes| string| id of order to get information about  
  
### 

​

Response Format

Name| Type| Description  
---|---|---  
null| OrdersScoring| order scoring data  
  
An `OrdersScoring` object is of the form:

Name| Type| Description  
---|---|---  
scoring| boolean| indicates if the order is scoring or not  
  
# 

​

Check if some orders are scoring

> This endpoint requires a L2 Header.

Returns to a dictionary with boolean value where it is indicated if an order is scoring or not. **HTTP REQUEST** `POST /<clob-endpoint>/orders-scoring`

### 

​

Request Parameters

Name| Required| Type| Description  
---|---|---|---  
orderIds| yes| string[]| ids of the orders to get information about  
  
### 

​

Response Format

Name| Type| Description  
---|---|---  
null| OrdersScoring| orders scoring data  
  
An `OrdersScoring` object is a dictionary that indicates the order by if it score.

Python

Typescript

Copy

Ask AI
    
    
    scoring = client.is_order_scoring(
        OrderScoringParams(
            orderId="0x..."
        )
    )
    print(scoring)
    
    scoring = client.are_orders_scoring(
        OrdersScoringParams(
            orderIds=["0x..."]
        )
    )
    print(scoring)
    

[Get Active Orders](/developers/CLOB/orders/get-active-order)[Cancel Orders(s)](/developers/CLOB/orders/cancel-orders)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
