# API Rate Limits - Polymarket Documentation

Source: https://docs.polymarket.com/quickstart/introduction/rate-limits

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Developer Quickstart

API Rate Limits

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

  * How Rate Limiting Works
  * General Rate Limits
  * Data API Rate Limits
  * GAMMA API Rate Limits
  * CLOB API Rate Limits
  * General CLOB Endpoints
  * CLOB Market Data
  * CLOB Ledger Endpoints
  * CLOB Markets & Pricing
  * CLOB Authentication
  * CLOB Trading Endpoints
  * Other API Rate Limits



Developer Quickstart

# API Rate Limits

## 

​

How Rate Limiting Works

All rate limits are enforced using Cloudflare’s throttling system. When you exceed the maximum configured rate for any endpoint, requests are throttled rather than immediately rejected. This means:

  * **Throttling** : Requests over the limit are delayed/queued rather than dropped
  * **Burst Allowances** : Some endpoints allow short bursts above the sustained rate
  * **Time Windows** : Limits reset based on sliding time windows (e.g., per 10 seconds, per minute)



## 

​

General Rate Limits

Endpoint| Limit| Notes  
---|---|---  
General Rate Limiting| 15000 requests / 10s| Throttle requests over the maximum configured rate  
”OK” Endpoint| 100 requests / 10s| Throttle requests over the maximum configured rate  
  
## 

​

Data API Rate Limits

Endpoint| Limit| Notes  
---|---|---  
Data API (General)| 1000 requests / 10s| Throttle requests over the maximum configured rate  
Data API `/trades`| 200 requests / 10s| Throttle requests over the maximum configured rate  
Data API `/positions`| 150 requests / 10s| Throttle requests over the maximum configured rate  
Data API `/closed-positions`| 150 requests / 10s| Throttle requests over the maximum configured rate  
Data API “OK” Endpoint| 100 requests / 10s| Throttle requests over the maximum configured rate  
  
## 

​

GAMMA API Rate Limits

Endpoint| Limit| Notes  
---|---|---  
GAMMA (General)| 4000 requests / 10s| Throttle requests over the maximum configured rate  
GAMMA Get Comments| 200 requests / 10s| Throttle requests over the maximum configured rate  
GAMMA `/events`| 500 requests / 10s| Throttle requests over the maximum configured rate  
GAMMA `/markets`| 300 requests / 10s| Throttle requests over the maximum configured rate  
GAMMA `/markets` /events listing| 900 requests / 10s| Throttle requests over the maximum configured rate  
GAMMA Tags| 200 requests / 10s| Throttle requests over the maximum configured rate  
GAMMA Search| 350 requests / 10s| Throttle requests over the maximum configured rate  
  
## 

​

CLOB API Rate Limits

### 

​

General CLOB Endpoints

Endpoint| Limit| Notes  
---|---|---  
CLOB (General)| 9000 requests / 10s| Throttle requests over the maximum configured rate  
CLOB GET Balance Allowance| 200 requests / 10s| Throttle requests over the maximum configured rate  
CLOB UPDATE Balance Allowance| 50 requests / 10s| Throttle requests over the maximum configured rate  
  
### 

​

CLOB Market Data

Endpoint| Limit| Notes  
---|---|---  
CLOB `/book`| 1500 requests / 10s| Throttle requests over the maximum configured rate  
CLOB `/books`| 500 requests / 10s| Throttle requests over the maximum configured rate  
CLOB `/price`| 1500 requests / 10s| Throttle requests over the maximum configured rate  
CLOB `/prices`| 500 requests / 10s| Throttle requests over the maximum configured rate  
CLOB `/midprice`| 1500 requests / 10s| Throttle requests over the maximum configured rate  
CLOB `/midprices`| 500 requests / 10s| Throttle requests over the maximum configured rate  
  
### 

​

CLOB Ledger Endpoints

Endpoint| Limit| Notes  
---|---|---  
CLOB Ledger (`/trades` `/orders` `/notifications` `/order`)| 900 requests / 10s| Throttle requests over the maximum configured rate  
CLOB Ledger `/data/orders`| 500 requests / 10s| Throttle requests over the maximum configured rate  
CLOB Ledger `/data/trades`| 500 requests / 10s| Throttle requests over the maximum configured rate  
CLOB `/notifications`| 125 requests / 10s| Throttle requests over the maximum configured rate  
  
### 

​

CLOB Markets & Pricing

Endpoint| Limit| Notes  
---|---|---  
CLOB Price History| 1000 requests / 10s| Throttle requests over the maximum configured rate  
CLOB Market Tick Size| 200 requests / 10s| Throttle requests over the maximum configured rate  
  
### 

​

CLOB Authentication

Endpoint| Limit| Notes  
---|---|---  
CLOB API Keys| 100 requests / 10s| Throttle requests over the maximum configured rate  
  
### 

​

CLOB Trading Endpoints

Endpoint| Limit| Notes  
---|---|---  
CLOB POST `/order`| 3500 requests / 10s (500/s)| BURST - Throttle requests over the maximum configured rate  
CLOB POST `/order`| 36000 requests / 10 minutes (60/s)| Throttle requests over the maximum configured rate  
CLOB DELETE `/order`| 3000 requests / 10s (300/s)| BURST - Throttle requests over the maximum configured rate  
CLOB DELETE `/order`| 30000 requests / 10 minutes (50/s)| Throttle requests over the maximum configured rate  
CLOB POST `/orders`| 1000 requests / 10s (100/s)| BURST - Throttle requests over the maximum configured rate  
CLOB POST `/orders`| 15000 requests / 10 minutes (25/s)| Throttle requests over the maximum configured rate  
CLOB DELETE `/orders`| 1000 requests / 10s (100/s)| BURST - Throttle requests over the maximum configured rate  
CLOB DELETE `/orders`| 15000 requests / 10 minutes (25/s)| Throttle requests over the maximum configured rate  
CLOB DELETE `/cancel-all`| 250 requests / 10s (25/s)| BURST - Throttle requests over the maximum configured rate  
CLOB DELETE `/cancel-all`| 6000 requests / 10 minutes (10/s)| Throttle requests over the maximum configured rate  
CLOB DELETE `/cancel-market-orders`| 1000 requests / 10s (100/s)| BURST - Throttle requests over the maximum configured rate  
CLOB DELETE `/cancel-market-orders`| 1500 requests / 10 minutes (25/s)| Throttle requests over the maximum configured rate  
  
## 

​

Other API Rate Limits

Endpoint| Limit| Notes  
---|---|---  
RELAYER `/submit`| 25 requests / 1 minute| Throttle requests over the maximum configured rate  
User PNL API| 200 requests / 10s| Throttle requests over the maximum configured rate  
  
[Glossary](/quickstart/reference/glossary)[Endpoints](/quickstart/reference/endpoints)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
