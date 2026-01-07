# Endpoints - Polymarket Documentation

Source: https://docs.polymarket.com/quickstart/reference/endpoints

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Developer Quickstart

Endpoints

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

  * REST APIs
  * WebSocket Endpoints
  * Quick Reference
  * CLOB API
  * Gamma API
  * Data API
  * CLOB WebSocket
  * RTDS (Real-Time Data Stream)



Developer Quickstart

# Endpoints

All Polymarket API URLs and base endpoints

All base URLs for Polymarket APIs. See individual API documentation for available routes and parameters.

* * *

## 

​

REST APIs

API| Base URL| Description  
---|---|---  
**CLOB API**| `https://clob.polymarket.com`| Order management, prices, orderbooks  
**Gamma API**| `https://gamma-api.polymarket.com`| Market discovery, metadata, events  
**Data API**| `https://data-api.polymarket.com`| User positions, activity, history  
  
* * *

## 

​

WebSocket Endpoints

Service| URL| Description  
---|---|---  
**CLOB WebSocket**| `wss://ws-subscriptions-clob.polymarket.com/ws/`| Orderbook updates, order status  
**RTDS**| `wss://ws-live-data.polymarket.com`| Low-latency crypto prices, comments  
  
* * *

## 

​

Quick Reference

### 

​

CLOB API

Copy

Ask AI
    
    
    https://clob.polymarket.com
    

Common endpoints:

  * `GET /price` — Get current price for a token
  * `GET /book` — Get orderbook for a token
  * `GET /midpoint` — Get midpoint price
  * `POST /order` — Place an order (auth required)
  * `DELETE /order` — Cancel an order (auth required)

[Full CLOB documentation →](/developers/CLOB/introduction)

### 

​

Gamma API

Copy

Ask AI
    
    
    https://gamma-api.polymarket.com
    

Common endpoints:

  * `GET /events` — List events
  * `GET /markets` — List markets
  * `GET /events/{id}` — Get event details

[Full Gamma documentation →](/developers/gamma-markets-api/overview)

### 

​

Data API

Copy

Ask AI
    
    
    https://data-api.polymarket.com
    

Common endpoints:

  * `GET /positions` — Get user positions
  * `GET /activity` — Get user activity
  * `GET /trades` — Get trade history

[Full Data API documentation →](/developers/misc-endpoints/data-api-get-positions)

### 

​

CLOB WebSocket

Copy

Ask AI
    
    
    wss://ws-subscriptions-clob.polymarket.com/ws/
    

Channels:

  * `market` — Orderbook and price updates (public)
  * `user` — Order status updates (authenticated)

[Full WebSocket documentation →](/developers/CLOB/websocket/wss-overview)

### 

​

RTDS (Real-Time Data Stream)

Copy

Ask AI
    
    
    wss://ws-live-data.polymarket.com
    

Channels:

  * Crypto price feeds
  * Comment streams

[Full RTDS documentation →](/developers/RTDS/RTDS-overview)

[API Rate Limits](/quickstart/introduction/rate-limits)[Market Maker Introduction](/developers/market-makers/introduction)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
