# Cancel Orders(s) - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/orders/cancel-orders

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Order Management

Cancel Orders(s)

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



On this page

  * Cancel an single Order
  * Request Payload Parameters
  * Response Format
  * Cancel Multiple Orders
  * Request Payload Parameters
  * Response Format
  * Cancel ALL Orders
  * Response Format
  * Cancel orders from market
  * Request Payload Parameters
  * Response Format



Order Management

# Cancel Orders(s)

Multiple endpoints to cancel a single order, multiple orders, all orders or all orders from a single market.

# 

​

Cancel an single Order

This endpoint requires a L2 Header. 

Cancel an order. **HTTP REQUEST** `DELETE /<clob-endpoint>/order`

### 

​

Request Payload Parameters

Name| Required| Type| Description  
---|---|---|---  
orderID| yes| string| ID of order to cancel  
  
### 

​

Response Format

Name| Type| Description  
---|---|---  
canceled| string[]| list of canceled orders  
not_canceled| a order id -> reason map that explains why that order couldn’t be canceled|   
  
Python

Typescript

Copy

Ask AI
    
    
    resp = client.cancel(order_id="0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88")
    print(resp)
    

# 

​

Cancel Multiple Orders

This endpoint requires a L2 Header. 

**HTTP REQUEST** `DELETE /<clob-endpoint>/orders`

### 

​

Request Payload Parameters

Name| Required| Type| Description  
---|---|---|---  
null| yes| string[]| IDs of the orders to cancel  
  
### 

​

Response Format

Name| Type| Description  
---|---|---  
canceled| string[]| list of canceled orders  
not_canceled| a order id -> reason map that explains why that order couldn’t be canceled|   
  
Python

Typescript

Copy

Ask AI
    
    
    resp = client.cancel_orders(["0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88", "0xaaaa..."])
    print(resp)
    

# 

​

Cancel ALL Orders

This endpoint requires a L2 Header. 

Cancel all open orders posted by a user. **HTTP REQUEST** `DELETE /<clob-endpoint>/cancel-all`

### 

​

Response Format

Name| Type| Description  
---|---|---  
canceled| string[]| list of canceled orders  
not_canceled| a order id -> reason map that explains why that order couldn’t be canceled|   
  
Python

Typescript

Copy

Ask AI
    
    
    resp = client.cancel_all()
    print(resp)
    print("Done!")
    

# 

​

Cancel orders from market

This endpoint requires a L2 Header. 

Cancel orders from market. **HTTP REQUEST** `DELETE /<clob-endpoint>/cancel-market-orders`

### 

​

Request Payload Parameters

Name| Required| Type| Description  
---|---|---|---  
market| no| string| condition id of the market  
asset_id| no| string| id of the asset/token  
  
### 

​

Response Format

Name| Type| Description  
---|---|---  
canceled| string[]| list of canceled orders  
not_canceled| a order id -> reason map that explains why that order couldn’t be canceled|   
  
Python

Typescript

Copy

Ask AI
    
    
    resp = client.cancel_market_orders(market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af", asset_id="52114319501245915516055106046884209969926127482827954674443846427813813222426")
    print(resp)
    
    

[Check Order Reward Scoring](/developers/CLOB/orders/check-scoring)[Onchain Order Info](/developers/CLOB/orders/onchain-order-info)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
