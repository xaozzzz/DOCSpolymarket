# Real Time Data Socket - Polymarket Documentation

Source: https://docs.polymarket.com/developers/RTDS/RTDS-overview

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Real Time Data Stream

Real Time Data Socket

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
  * Connection Details
  * Authentication
  * Connection Management
  * Available Subscription Types
  * Message Structure
  * Subscription Management
  * Subscribe to Topics
  * Unsubscribe from Topics
  * Error Handling



Real Time Data Stream

# Real Time Data Socket

## 

​

Overview

The Polymarket Real-Time Data Socket (RTDS) is a WebSocket-based streaming service that provides real-time updates for various Polymarket data streams. The service allows clients to subscribe to multiple data feeds simultaneously and receive live updates as events occur on the platform.

Polymarket provides a Typescript client for interacting with this streaming service. [Download and view it’s documentation here](https://github.com/Polymarket/real-time-data-client)

### 

​

Connection Details

  * **WebSocket URL** : `wss://ws-live-data.polymarket.com`
  * **Protocol** : WebSocket
  * **Data Format** : JSON



### 

​

Authentication

The RTDS supports two types of authentication depending on the subscription type:

  1. **CLOB Authentication** : Required for certain trading-related subscriptions
     * `key`: API key
     * `secret`: API secret
     * `passphrase`: API passphrase
  2. **Gamma Authentication** : Required for user-specific data
     * `address`: User wallet address



### 

​

Connection Management

The WebSocket connection supports:

  * **Dynamic Subscriptions** : Without disconnecting from the socket users can add, remove and modify topics and filters they are subscribed to.
  * **Ping/Pong** : You should send PING messages (every 5 seconds ideally) to maintain connection



## 

​

Available Subscription Types

Although this connection technically supports additional activity and subscription types, they are not fully supported at this time. Users are free to use them but there may be some unexpected behavior.

The RTDS currently supports the following subscription types:

  1. **[Crypto Prices](/developers/RTDS/RTDS-crypto-prices)** \- Real-time cryptocurrency price updates
  2. **[Comments](/developers/RTDS/RTDS-comments)** \- Comment-related events including reactions



## 

​

Message Structure

All messages received from the WebSocket follow this structure:

Copy

Ask AI
    
    
    {
      "topic": "string",
      "type": "string", 
      "timestamp": "number",
      "payload": "object"
    }
    

  * `topic`: The subscription topic (e.g., “crypto_prices”, “comments”, “activity”)
  * `type`: The message type/event (e.g., “update”, “reaction_created”, “orders_matched”)
  * `timestamp`: Unix timestamp in milliseconds
  * `payload`: Event-specific data object



## 

​

Subscription Management

### 

​

Subscribe to Topics

To subscribe to data streams, send a JSON message with this structure:

Copy

Ask AI
    
    
    {
      "action": "subscribe",
      "subscriptions": [
        {
          "topic": "topic_name",
          "type": "message_type",
          "filters": "optional_filter_string",
          "clob_auth": {
            "key": "api_key",
            "secret": "api_secret", 
            "passphrase": "api_passphrase"
          },
          "gamma_auth": {
            "address": "wallet_address"
          }
        }
      ]
    }
    

### 

​

Unsubscribe from Topics

To unsubscribe from data streams, send a similar message with `"action": "unsubscribe"`.

## 

​

Error Handling

  * Connection errors will trigger automatic reconnection attempts
  * Invalid subscription messages may result in connection closure
  * Authentication failures will prevent successful subscription to protected topics



[Market Channel](/developers/CLOB/websocket/market-channel)[RTDS Crypto Prices](/developers/RTDS/RTDS-crypto-prices)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
