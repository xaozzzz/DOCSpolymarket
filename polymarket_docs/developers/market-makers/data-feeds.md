# Data Feeds - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/data-feeds

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Market Makers

Data Feeds

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
  * WebSocket Feeds
  * Connecting
  * Available Channels
  * User Channel (Authenticated)
  * Best Practices
  * Gamma API
  * Get Markets
  * Get Events
  * Key Fields for MMs
  * Onchain Data
  * Data Sources
  * RPC Providers
  * UMA Oracle
  * Related Documentation



Market Makers

# Data Feeds

Real-time and historical data sources for market makers

## 

​

Overview

Market makers need fast, reliable data to price markets and manage inventory. Polymarket provides several data feeds at different latency and detail levels.

Feed| Latency| Use Case| Access  
---|---|---|---  
WebSocket| ~100ms| Standard MM operations| Public  
Gamma API| ~1s| Market metadata, indexing| Public  
Onchain| Block time| Settlement, resolution| Public  
  
## 

​

WebSocket Feeds

The WebSocket API provides real-time market data with low latency. This is sufficient for most market making strategies.

### 

​

Connecting

Copy

Ask AI
    
    
    const ws = new WebSocket("wss://ws-subscriptions-clob.polymarket.com/ws/market");
    
    ws.onopen = () => {
      // Subscribe to orderbook updates
      ws.send(JSON.stringify({
        type: "market",
        assets_ids: [tokenId]
      }));
    };
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      // Handle orderbook update
    };
    

### 

​

Available Channels

Channel| Message Types| Documentation  
---|---|---  
`market`| `book`, `price_change`, `last_trade_price`| [Market Channel](/developers/CLOB/websocket/market-channel)  
`user`| Order fills, cancellations| [User Channel](/developers/CLOB/websocket/user-channel)  
  
### 

​

User Channel (Authenticated)

Monitor your order activity in real-time:

Copy

Ask AI
    
    
    // Requires authentication
    const userWs = new WebSocket("wss://ws-subscriptions-clob.polymarket.com/ws/user");
    
    userWs.onopen = () => {
      userWs.send(JSON.stringify({
        type: "user",
        auth: {
          apiKey: "your-api-key",
          secret: "your-secret",
          passphrase: "your-passphrase"
        },
        markets: [conditionId] // Optional: filter to specific markets
      }));
    };
    
    userWs.onmessage = (event) => {
      const data = JSON.parse(event.data);
      // Handle order fills, cancellations, etc.
    };
    

See [WebSocket Authentication](/developers/CLOB/websocket/wss-auth) for auth details.

### 

​

Best Practices

  1. **Reconnection logic** \- Implement automatic reconnection with exponential backoff
  2. **Heartbeats** \- Respond to ping messages to maintain connection
  3. **Local orderbook** \- Maintain a local copy and apply incremental updates
  4. **Sequence numbers** \- Track sequence to detect missed messages

See [WebSocket Overview](/developers/CLOB/websocket/wss-overview) for complete documentation.

## 

​

Gamma API

The Gamma API provides market metadata and indexing. Use it for:

  * Market titles, slugs, categories
  * Event/condition mapping
  * Volume and liquidity data
  * Outcome token metadata



### 

​

Get Markets

Copy

Ask AI
    
    
    const response = await fetch(
      "https://gamma-api.polymarket.com/markets?active=true"
    );
    const markets = await response.json();
    

### 

​

Get Events

Copy

Ask AI
    
    
    const response = await fetch(
      "https://gamma-api.polymarket.com/events?slug=us-presidential-election"
    );
    const event = await response.json();
    

### 

​

Key Fields for MMs

Field| Description  
---|---  
`conditionId`| Unique market identifier  
`clobTokenIds`| Outcome token IDs  
`outcomes`| Outcome names  
`outcomePrices`| Current outcome prices  
`volume`| Trading volume  
`liquidity`| Current liquidity  
`rfqEnabled`| Whether RFQ is enabled for this market  
  
See [Gamma API Overview](/developers/gamma-markets-api/overview) for complete documentation.

## 

​

Onchain Data

For settlement, resolution, and position tracking, market makers may query onchain data directly.

### 

​

Data Sources

Data| Source| Use Case  
---|---|---  
Token balances| ERC1155 `balanceOf`| Position tracking  
Resolution| UMA Oracle events| Pre-resolution risk modeling  
Condition resolution| CTF contract| Post-resolution redemption  
  
### 

​

RPC Providers

Common providers for Polygon:

  * Alchemy
  * QuickNode
  * Infura



### 

​

UMA Oracle

Markets are resolved via UMA’s Optimistic Oracle. Monitor resolution events for risk management. See [Resolution](/developers/resolution/UMA) for details on the resolution process.

## 

​

Related Documentation

## [WebSocket OverviewComplete WebSocket documentation](/developers/CLOB/websocket/wss-overview)## [Gamma APIMarket metadata and indexing](/developers/gamma-markets-api/overview)## [ResolutionUMA Oracle resolution process](/developers/resolution/UMA)

[Maker Rebates Program](/developers/market-makers/maker-rebates-program)[Inventory Management](/developers/market-makers/inventory)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
