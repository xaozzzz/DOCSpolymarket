# Trading - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/trading

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Market Makers

Trading

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
  * Order Entry
  * Posting Limit Orders
  * Batch Orders
  * Order Types
  * When to Use Each
  * Order Management
  * Cancel Orders
  * Get Active Orders
  * Best Practices
  * Quote Management
  * Latency Optimization
  * Risk Management
  * Tick Sizes
  * Fee Structure
  * Related Documentation



Market Makers

# Trading

CLOB order entry and management for market makers

## 

​

Overview

Market makers primarily interact with Polymarket through the CLOB (Central Limit Order Book) API to post and manage limit orders.

## 

​

Order Entry

### 

​

Posting Limit Orders

Use the CLOB client to create and post limit orders:

Copy

Ask AI
    
    
    import { ClobClient, Side, OrderType } from "@polymarket/clob-client";
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      wallet,
      credentials,
      signatureType,
      funder
    );
    
    // Post a bid (buy order)
    const bidOrder = await client.createAndPostOrder({
      tokenID: "34097058504275310827233323421517291090691602969494795225921954353603704046623",
      side: Side.BUY,
      price: 0.48,
      size: 1000,
      orderType: OrderType.GTC
    });
    
    // Post an ask (sell order)
    const askOrder = await client.createAndPostOrder({
      tokenID: "34097058504275310827233323421517291090691602969494795225921954353603704046623",
      side: Side.SELL,
      price: 0.52,
      size: 1000,
      orderType: OrderType.GTC
    });
    

See [Create Order](/developers/CLOB/clients/methods-l1#createandpostorder) for full documentation.

### 

​

Batch Orders

For efficiency, post multiple orders in a single request:

Copy

Ask AI
    
    
    const orders = await Promise.all([
      client.createOrder({ tokenID, side: Side.BUY, price: 0.48, size: 500 }),
      client.createOrder({ tokenID, side: Side.BUY, price: 0.47, size: 500 }),
      client.createOrder({ tokenID, side: Side.SELL, price: 0.52, size: 500 }),
      client.createOrder({ tokenID, side: Side.SELL, price: 0.53, size: 500 })
    ]);
    
    const response = await client.postOrders(
      orders.map(order => ({ order, orderType: OrderType.GTC }))
    );
    

See [Post Orders Batch](/developers/CLOB/clients/methods-l2#postorders) for details.

## 

​

Order Types

Type| Behavior| MM Use Case  
---|---|---  
**GTC** (Good Till Cancelled)| Rests on book until filled or cancelled| Default for passive quoting  
**GTD** (Good Till Date)| Auto-expires at specified time| Auto-expire before events  
**FOK** (Fill or Kill)| Fill entirely immediately or cancel| Aggressive rebalancing (all or nothing)  
**FAK** (Fill and Kill)| Fill available immediately, cancel rest| Partial rebalancing acceptable  
  
### 

​

When to Use Each

**For passive market making (maker orders):**

  * **GTC** \- Standard quotes that sit on the book
  * **GTD** \- Time-limited quotes (e.g., expire before market close)

**For rebalancing (taker orders):**

  * **FOK** \- When you need exact size or nothing
  * **FAK** \- When partial fills are acceptable



Copy

Ask AI
    
    
    // GTD example: expire in 1 hour
    const expiringOrder = await client.createOrder({
      tokenID,
      side: Side.BUY,
      price: 0.50,
      size: 1000,
      orderType: OrderType.GTD,
      expiration: Math.floor(Date.now() / 1000) + 3600 // 1 hour from now
    });
    

## 

​

Order Management

### 

​

Cancel Orders

Cancel individual orders or all orders:

Copy

Ask AI
    
    
    // Cancel single order
    await client.cancelOrder(orderId);
    
    // Cancel multiple orders in a single calls
    await client.cancelOrders(orderIds: string[]);
    
    // Cancel all orders for a market
    await client.cancelMarketOrders(conditionId);
    
    // Cancel all orders
    await client.cancelAll();
    

See [Cancel Orders](/developers/CLOB/clients/methods-l2#cancelorder) for full documentation.

### 

​

Get Active Orders

Monitor your open orders:

Copy

Ask AI
    
    
    // Get active order
    const order = await client.getOrder(orderId);
    
    // Get active orders optionally filtered
    const orders = await client.getOpenOrders({
      id?: string; // Order ID (hash)
      market?: string; // Market condition ID
      asset_id?: string; // Token ID
    });
    

See [Get Active Orders](/developers/CLOB/clients/methods-l2#getorder) for details.

## 

​

Best Practices

### 

​

Quote Management

  1. **Two-sided quoting** \- Post both bids and asks to earn maximum [liquidity rewards](/developers/market-makers/liquidity-rewards)
  2. **Monitor inventory** \- Skew quotes based on your position
  3. **Cancel stale quotes** \- Remove orders when market conditions change
  4. **Use GTD for events** \- Auto-expire quotes before known events



### 

​

Latency Optimization

  1. **Batch orders** \- Use `postOrders()` instead of multiple `createAndPostOrder()` calls
  2. **WebSocket for data** \- Use WebSocket feeds instead of polling REST endpoints



### 

​

Risk Management

  1. **Size limits** \- Check token balances before quoting; don’t exceed inventory
  2. **Price guards** \- Validate against book midpoint; reject outlier prices
  3. **Kill switch** \- Use `cancelAll()` on error or position breach
  4. **Monitor fills** \- Subscribe to WebSocket user channel for real-time fill updates



## 

​

Tick Sizes

Markets have different minimum price increments:

Copy

Ask AI
    
    
    const tickSize = await client.getTickSize(tokenID);
    // Returns: "0.1" | "0.01" | "0.001" | "0.0001"
    

Ensure your prices conform to the market’s tick size.

## 

​

Fee Structure

Role| Fee  
---|---  
Maker| 0 bps  
Taker| 0 bps  
  
Current fees are 0% for both makers and takers. See [CLOB Introduction](/developers/CLOB/introduction) for fee calculation details.

## 

​

Related Documentation

## [CLOB Client OverviewComplete client method reference](/developers/CLOB/clients/methods-overview)## [L2 MethodsAuthenticated order management methods](/developers/CLOB/clients/methods-l2)## [WebSocket FeedsReal-time order and market data](/developers/CLOB/websocket/wss-overview)## [Liquidity RewardsEarn rewards for providing liquidity](/developers/market-makers/liquidity-rewards)

[Setup](/developers/market-makers/setup)[Liquidity Rewards](/developers/market-makers/liquidity-rewards)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
