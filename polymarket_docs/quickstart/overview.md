# Developer Quickstart - Polymarket Documentation

Source: https://docs.polymarket.com/quickstart/overview

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Developer Quickstart

Developer Quickstart

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

  * What Can You Build?
  * APIs at a Glance
  * Markets & Data
  * Additional Data Sources
  * Trading Infrastructure
  * SDKs & Libraries



Developer Quickstart

# Developer Quickstart

Get started building with Polymarket APIs

Polymarket provides a suite of APIs and SDKs for building prediction market applications. This guide will help you understand what’s available and where to find it.

* * *

## 

​

What Can You Build?

If you want to…| Start here  
---|---  
Fetch markets & prices| [Fetching Market Data](/quickstart/fetching-data)  
Place orders for yourself| [Placing Your First Order](/quickstart/first-order)  
Build a trading app for users| [Builders Program Introduction](/developers/builders/builder-intro)  
Provide liquidity| [Market Makers](/developers/market-makers/introduction)  
  
* * *

## 

​

APIs at a Glance

### 

​

Markets & Data

## [Gamma API**Market discovery & metadata**Fetch events, markets, categories, and resolution data. This is where you discover what’s tradeable.`https://gamma-api.polymarket.com`](/developers/gamma-markets-api/overview)## [CLOB API**Prices, orderbooks & trading**Get real-time prices, orderbook depth, and place orders. The core trading API.`https://clob.polymarket.com`](/developers/CLOB/introduction)## [Data API**Positions, activity & history**Query user positions, trade history, and portfolio data.`https://data-api.polymarket.com`](/developers/misc-endpoints/data-api-get-positions)## [WebSocket**Real-time updates** Subscribe to orderbook changes, price updates, and order status.`wss://ws-subscriptions-clob.polymarket.com`](/developers/CLOB/websocket/wss-overview)

### 

​

Additional Data Sources

## [RTDS**Low-latency data stream** Real-time crypto prices and comments. Optimized for market makers.](/developers/RTDS/RTDS-overview)## [Subgraph**Onchain queries** Query blockchain state directly via GraphQL.](/developers/subgraph/overview)

### 

​

Trading Infrastructure

## [CTF Operations**Token split/merge/redeem** Convert between USDC and outcome tokens. Essential for inventory management.](/developers/CTF/overview)## [Relayer Client**Gasless transactions** Builders can offer gasfree transactions via Polymarket’s relayer.](/developers/builders/relayer-client)

* * *

## 

​

SDKs & Libraries

## [CLOB Client (TypeScript)`npm install @polymarket/clob-client`](https://github.com/Polymarket/clob-client)## [CLOB Client (Python)`pip install py-clob-client`](https://github.com/Polymarket/py-clob-client)

For builders routing orders for users:

## [Relayer ClientGasless wallet operations](https://github.com/Polymarket/builder-relayer-client)## [Signing SDKBuilder authentication headers](https://github.com/Polymarket/builder-signing-sdk)

[Fetching Market Data](/quickstart/fetching-data)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
