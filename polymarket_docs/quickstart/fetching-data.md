# Fetching Market Data - Polymarket Documentation

Source: https://docs.polymarket.com/quickstart/fetching-data

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Developer Quickstart

Fetching Market Data

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

  * Understanding the Data Model
  * Fetch Active Events
  * Market Discovery Best Practices
  * For Sports Events
  * For Non-Sports Topics
  * Get Market Details
  * Get Current Price
  * Get Orderbook Depth
  * More Data APIs



Developer Quickstart

# Fetching Market Data

Fetch Polymarket data in minutes with no authentication required

Get market data with zero setup. No API key, no authentication, no wallet required.

* * *

## 

​

Understanding the Data Model

Before fetching data, understand how Polymarket structures its markets:

1

Event

The top-level object representing a question like “Will X happen?”

2

Market

Each event contains one or more markets. Each market is a specific tradable binary outcome.

3

Outcomes & Prices

Markets have `outcomes` and `outcomePrices` arrays that map 1:1. These prices represent implied probabilities.

Copy

Ask AI
    
    
    {
      "outcomes": "[\"Yes\", \"No\"]",
      "outcomePrices": "[\"0.20\", \"0.80\"]"
    }
    // Index 0: "Yes" → 0.20 (20% probability)
    // Index 1: "No" → 0.80 (80% probability)
    

* * *

## 

​

Fetch Active Events

List all currently active events on Polymarket:

Copy

Ask AI
    
    
    curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=5"
    

Example Response

Copy

Ask AI
    
    
    [
      {
        "id": "123456",
        "slug": "will-bitcoin-reach-100k-by-2025",
        "title": "Will Bitcoin reach $100k by 2025?",
        "active": true,
        "closed": false,
        "tags": [
          { "id": "21", "label": "Crypto", "slug": "crypto" }
        ],
        "markets": [
          {
            "id": "789",
            "question": "Will Bitcoin reach $100k by 2025?",
            "clobTokenIds": ["TOKEN_YES_ID", "TOKEN_NO_ID"],
            "outcomes": "[\"Yes\", \"No\"]",
            "outcomePrices": "[\"0.65\", \"0.35\"]"
          }
        ]
      }
    ]
    

Always use `active=true&closed=false` to filter for live, tradable events.

* * *

## 

​

Market Discovery Best Practices

### 

​

For Sports Events

Use the `/sports` endpoint to discover leagues, then query by `series_id`:

Copy

Ask AI
    
    
    # Get all supported sports leagues
    curl "https://gamma-api.polymarket.com/sports"
    
    # Get events for a specific league (e.g., NBA series_id=10345)
    curl "https://gamma-api.polymarket.com/events?series_id=10345&active=true&closed=false"
    
    # Filter to just game bets (not futures) using tag_id=100639
    curl "https://gamma-api.polymarket.com/events?series_id=10345&tag_id=100639&active=true&closed=false&order=startTime&ascending=true"
    

`/sports` only returns automated leagues. For others (UFC, Boxing, F1, Golf, Chess), use tag IDs via `/events?tag_id=<tag_id>`.

### 

​

For Non-Sports Topics

Use `/tags` to discover all available categories, then filter events:

Copy

Ask AI
    
    
    # Get all available tags
    curl "https://gamma-api.polymarket.com/tags?limit=100"
    
    # Query events by topic
    curl "https://gamma-api.polymarket.com/events?tag_id=2&active=true&closed=false"
    

Each event response includes a `tags` array, useful for discovering categories from live data and building your own tag mapping.

* * *

## 

​

Get Market Details

Once you have an event, get details for a specific market using its ID or slug:

Copy

Ask AI
    
    
    curl "https://gamma-api.polymarket.com/markets?slug=will-bitcoin-reach-100k-by-2025"
    

The response includes `clobTokenIds`, you’ll need these to fetch prices and place orders.

* * *

## 

​

Get Current Price

Query the CLOB for the current price of any token:

Copy

Ask AI
    
    
    curl "https://clob.polymarket.com/price?token_id=YOUR_TOKEN_ID&side=buy"
    

Example Response

Copy

Ask AI
    
    
    {
      "price": "0.65"
    }
    

* * *

## 

​

Get Orderbook Depth

See all bids and asks for a market:

Copy

Ask AI
    
    
    curl "https://clob.polymarket.com/book?token_id=YOUR_TOKEN_ID"
    

Example Response

Copy

Ask AI
    
    
    {
      "market": "0x...",
      "asset_id": "YOUR_TOKEN_ID",
      "bids": [
        { "price": "0.64", "size": "500" },
        { "price": "0.63", "size": "1200" }
      ],
      "asks": [
        { "price": "0.66", "size": "300" },
        { "price": "0.67", "size": "800" }
      ]
    }
    

* * *

## 

​

More Data APIs

## [Gamma APIDeep dive into market discovery](/developers/gamma-markets-api/overview)## [Data APIPositions, activity, and holders data](/developers/misc-endpoints/data-api-get-positions)## [WebSocketReal-time orderbook updates](/developers/CLOB/websocket/wss-overview)## [RTDSReal-time data streaming service](/developers/RTDS/RTDS-overview)

[Developer Quickstart](/quickstart/overview)[Placing Your First Order](/quickstart/first-order)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
