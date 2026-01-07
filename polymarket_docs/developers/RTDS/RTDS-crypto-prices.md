# RTDS Crypto Prices - Polymarket Documentation

Source: https://docs.polymarket.com/developers/RTDS/RTDS-crypto-prices

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Real Time Data Stream

RTDS Crypto Prices

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

  * Overview
  * Binance Source (crypto_prices)
  * Subscription Details
  * Subscription Message
  * With Symbol Filter
  * Chainlink Source (crypto_prices_chainlink)
  * Subscription Details
  * Subscription Message
  * With Symbol Filter
  * Message Format
  * Binance Source Message Format
  * Chainlink Source Message Format
  * Payload Fields
  * Example Messages
  * Binance Source Examples
  * Solana Price Update (Binance)
  * Bitcoin Price Update (Binance)
  * Chainlink Source Examples
  * Ethereum Price Update (Chainlink)
  * Bitcoin Price Update (Chainlink)
  * Supported Symbols
  * Binance Source Symbols
  * Chainlink Source Symbols
  * Notes
  * General



Real Time Data Stream

# RTDS Crypto Prices

Polymarket provides a Typescript client for interacting with this streaming service. [Download and view it’s documentation here](https://github.com/Polymarket/real-time-data-client)

## 

​

Overview

The crypto prices subscription provides real-time updates for cryptocurrency price data from two different sources:

  * **Binance Source** (`crypto_prices`): Real-time price data from Binance exchange
  * **Chainlink Source** (`crypto_prices_chainlink`): Price data from Chainlink oracle networks

Both streams deliver current market prices for various cryptocurrency trading pairs, but use different symbol formats and subscription structures.

## 

​

Binance Source (`crypto_prices`)

### 

​

Subscription Details

  * **Topic** : `crypto_prices`
  * **Type** : `update`
  * **Authentication** : Not required
  * **Filters** : Optional (specific symbols can be filtered)
  * **Symbol Format** : Lowercase concatenated pairs (e.g., `solusdt`, `btcusdt`)



### 

​

Subscription Message

Copy

Ask AI
    
    
    {
      "action": "subscribe",
      "subscriptions": [
        {
          "topic": "crypto_prices",
          "type": "update"
        }
      ]
    }
    

### 

​

With Symbol Filter

To subscribe to specific cryptocurrency symbols, include a filters parameter:

Copy

Ask AI
    
    
    {
      "action": "subscribe", 
      "subscriptions": [
        {
          "topic": "crypto_prices",
          "type": "update",
          "filters": "solusdt,btcusdt,ethusdt"
        }
      ]
    }
    

## 

​

Chainlink Source (`crypto_prices_chainlink`)

### 

​

Subscription Details

  * **Topic** : `crypto_prices_chainlink`
  * **Type** : `*` (all types)
  * **Authentication** : Not required
  * **Filters** : Optional (JSON object with symbol specification)
  * **Symbol Format** : Slash-separated pairs (e.g., `eth/usd`, `btc/usd`)



### 

​

Subscription Message

Copy

Ask AI
    
    
    {
      "action": "subscribe",
      "subscriptions": [
        {
          "topic": "crypto_prices_chainlink",
          "type": "*",
          "filters": ""
        }
      ]
    }
    

### 

​

With Symbol Filter

To subscribe to specific cryptocurrency symbols, include a JSON filters parameter:

Copy

Ask AI
    
    
    {
      "action": "subscribe",
      "subscriptions": [
        {
          "topic": "crypto_prices_chainlink",
          "type": "*",
          "filters": "{\"symbol\":\"eth/usd\"}"
        }
      ]
    }
    

## 

​

Message Format

### 

​

Binance Source Message Format

When subscribed to Binance crypto prices (`crypto_prices`), you’ll receive messages with the following structure:

Copy

Ask AI
    
    
    {
      "topic": "crypto_prices",
      "type": "update", 
      "timestamp": 1753314064237,
      "payload": {
        "symbol": "solusdt",
        "timestamp": 1753314064213,
        "value": 189.55
      }
    }
    

### 

​

Chainlink Source Message Format

When subscribed to Chainlink crypto prices (`crypto_prices_chainlink`), you’ll receive messages with the following structure:

Copy

Ask AI
    
    
    {
      "topic": "crypto_prices_chainlink",
      "type": "update", 
      "timestamp": 1753314064237,
      "payload": {
        "symbol": "eth/usd",
        "timestamp": 1753314064213,
        "value": 3456.78
      }
    }
    

## 

​

Payload Fields

Field| Type| Description  
---|---|---  
`symbol`| string| Trading pair symbol  
**Binance** : lowercase concatenated (e.g., “solusdt”, “btcusdt”)  
**Chainlink** : slash-separated (e.g., “eth/usd”, “btc/usd”)  
`timestamp`| number| Price timestamp in Unix milliseconds  
`value`| number| Current price value in the quote currency  
  
## 

​

Example Messages

### 

​

Binance Source Examples

#### 

​

Solana Price Update (Binance)

Copy

Ask AI
    
    
    {
      "topic": "crypto_prices",
      "type": "update",
      "timestamp": 1753314064237,
      "payload": {
        "symbol": "solusdt", 
        "timestamp": 1753314064213,
        "value": 189.55
      }
    }
    

#### 

​

Bitcoin Price Update (Binance)

Copy

Ask AI
    
    
    {
      "topic": "crypto_prices",
      "type": "update", 
      "timestamp": 1753314088421,
      "payload": {
        "symbol": "btcusdt",
        "timestamp": 1753314088395,
        "value": 67234.50
      }
    }
    

### 

​

Chainlink Source Examples

#### 

​

Ethereum Price Update (Chainlink)

Copy

Ask AI
    
    
    {
      "topic": "crypto_prices_chainlink",
      "type": "update",
      "timestamp": 1753314064237,
      "payload": {
        "symbol": "eth/usd", 
        "timestamp": 1753314064213,
        "value": 3456.78
      }
    }
    

#### 

​

Bitcoin Price Update (Chainlink)

Copy

Ask AI
    
    
    {
      "topic": "crypto_prices_chainlink",
      "type": "update", 
      "timestamp": 1753314088421,
      "payload": {
        "symbol": "btc/usd",
        "timestamp": 1753314088395,
        "value": 67234.50
      }
    }
    

## 

​

Supported Symbols

### 

​

Binance Source Symbols

The Binance source supports various cryptocurrency trading pairs using lowercase concatenated format:

  * `btcusdt` \- Bitcoin to USDT
  * `ethusdt` \- Ethereum to USDT
  * `solusdt` \- Solana to USDT
  * `xrpusdt` \- XRP to USDT



### 

​

Chainlink Source Symbols

The Chainlink source supports cryptocurrency trading pairs using slash-separated format:

  * `btc/usd` \- Bitcoin to USD
  * `eth/usd` \- Ethereum to USD
  * `sol/usd` \- Solana to USD
  * `xrp/usd` \- XRP to USD



## 

​

Notes

### 

​

General

  * Price updates are sent as market prices change
  * The timestamp in the payload represents when the price was recorded
  * The outer timestamp represents when the message was sent via WebSocket
  * No authentication is required for crypto price data



[RTDS Overview](/developers/RTDS/RTDS-overview)[RTDS Comments](/developers/RTDS/RTDS-comments)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
