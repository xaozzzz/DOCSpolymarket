# How to Fetch Markets - Polymarket Documentation

Source: https://docs.polymarket.com/developers/gamma-markets-api/fetch-markets-guide

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Gamma Structure

How to Fetch Markets

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
  * 1\. Fetch by Slug
  * How to Extract the Slug
  * API Endpoints
  * Examples
  * 2\. Fetch by Tags
  * Discover Available Tags
  * Using Tags in Market Requests
  * Additional Tag Filtering
  * 3\. Fetch All Active Markets
  * Key Parameters
  * Examples
  * Pagination
  * Best Practices
  * Related Endpoints



Gamma Structure

# How to Fetch Markets

Both the getEvents and getMarkets are paginated. See pagination section for details.

This guide covers the three recommended approaches for fetching market data from the Gamma API, each optimized for different use cases.

## 

​

Overview

There are three main strategies for retrieving market data:

  1. **By Slug** \- Best for fetching specific individual markets or events
  2. **By Tags** \- Ideal for filtering markets by category or sport
  3. **Via Events Endpoint** \- Most efficient for retrieving all active markets



* * *

## 

​

1\. Fetch by Slug

**Use Case:** When you need to retrieve a specific market or event that you already know about. Individual markets and events are best fetched using their unique slug identifier. The slug can be found directly in the Polymarket frontend URL.

### 

​

How to Extract the Slug

From any Polymarket URL, the slug is the path segment after `/event/` or `/market/`:

Copy

Ask AI
    
    
    https://polymarket.com/event/fed-decision-in-october?tid=1758818660485
                                ↑
                      Slug: fed-decision-in-october
    

### 

​

API Endpoints

**For Events:** [GET /events/slug/](/api-reference/events/list-events) **For Markets:** [GET /markets/slug/](/api-reference/markets/list-markets)

### 

​

Examples

Copy

Ask AI
    
    
    curl "https://gamma-api.polymarket.com/events/slug/fed-decision-in-october"
    

* * *

## 

​

2\. Fetch by Tags

**Use Case:** When you want to filter markets by category, sport, or topic. Tags provide a powerful way to categorize and filter markets. You can discover available tags and then use them to filter your market requests.

### 

​

Discover Available Tags

**General Tags:** [GET /tags](/api-reference/tags/list-tags) **Sports Tags & Metadata:** [GET /sports](/api-reference/sports/get-sports-metadata-information) The `/sports` endpoint returns comprehensive metadata for sports including tag IDs, images, resolution sources, and series information.

### 

​

Using Tags in Market Requests

Once you have tag IDs, you can use them with the `tag_id` parameter in both markets and events endpoints. **Markets with Tags:** [GET /markets](/api-reference/markets/list-markets) **Events with Tags:** [GET /events](/api-reference/events/list-events)

Copy

Ask AI
    
    
    curl "https://gamma-api.polymarket.com/events?tag_id=100381&limit=1&closed=false"
    
    

### 

​

Additional Tag Filtering

You can also:

  * Use `related_tags=true` to include related tag markets
  * Exclude specific tags with `exclude_tag_id`



* * *

## 

​

3\. Fetch All Active Markets

**Use Case:** When you need to retrieve all available active markets, typically for broader analysis or market discovery. The most efficient approach is to use the `/events` endpoint and work backwards, as events contain their associated markets. **Events Endpoint:** [GET /events](/api-reference/events/list-events) **Markets Endpoint:** [GET /markets](/api-reference/markets/list-markets)

### 

​

Key Parameters

  * `order=id` \- Order by event ID
  * `ascending=false` \- Get newest events first
  * `closed=false` \- Only active markets
  * `limit` \- Control response size
  * `offset` \- For pagination



### 

​

Examples

Copy

Ask AI
    
    
    curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=100"
    

This approach gives you all active markets ordered from newest to oldest, allowing you to systematically process all available trading opportunities.

### 

​

Pagination

For large datasets, use pagination with `limit` and `offset` parameters:

  * `limit=50` \- Return 50 results per page
  * `offset=0` \- Start from the beginning (increment by limit for subsequent pages)

**Pagination Examples:**

Copy

Ask AI
    
    
    # Page 1: First 50 results (offset=0)
    curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=0"
    

Copy

Ask AI
    
    
    # Page 2: Next 50 results (offset=50)
    curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=50"
    

Copy

Ask AI
    
    
    # Page 3: Next 50 results (offset=100)
    curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=100"
    

Copy

Ask AI
    
    
    # Paginating through markets with tag filtering
    curl "https://gamma-api.polymarket.com/markets?tag_id=100381&closed=false&limit=25&offset=0"
    

Copy

Ask AI
    
    
    # Next page of markets with tag filtering
    curl "https://gamma-api.polymarket.com/markets?tag_id=100381&closed=false&limit=25&offset=25"
    

* * *

## 

​

Best Practices

  1. **For Individual Markets:** Always use the slug method for best performance
  2. **For Category Browsing:** Use tag filtering to reduce API calls
  3. **For Complete Market Discovery:** Use the events endpoint with pagination
  4. **Always Include`closed=false`:** Unless you specifically need historical data
  5. **Implement Rate Limiting:** Respect API limits for production applications



## 

​

Related Endpoints

  * [Get Markets](/developers/gamma-markets-api/get-markets) \- Full markets endpoint documentation
  * [Get Events](/developers/gamma-markets-api/get-events) \- Full events endpoint documentation
  * [Search Markets](/developers/gamma-markets-api/get-public-search) \- Search functionality



[Gamma Structure](/developers/gamma-markets-api/gamma-structure)[Gamma API Health check](/api-reference/gamma-status/gamma-api-health-check)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
