# Price Change Message Migration Guide - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/websocket/market-channel-migration-guide

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Price Change Message Migration Guide

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
  * What’s Changed
  * Key Differences
  * Handle New Fields
  * Benefits of the New Schema
  * Timeline
  * Testing Your Migration
  * Support



# Price Change Message Migration Guide

**🚨 Breaking Change:** This change goes live on **September 15, 2025 at 11PM UTC**. Please upgrade your implementation as soon as possible to avoid service disruption.

## 

​

Overview

  * The `price_change` message schema in the Market Channel WebSocket has been updated to improve websocket performance and reliability.
  * Messages now come in the form of objects as opposed to lists of fields.



## 

​

What’s Changed

**Before (Legacy Schema):**

Copy

Ask AI
    
    
    {
      "asset_id": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
      "changes": [
        {
          "price": "0.4",
          "side": "SELL", 
          "size": "3300"
        }
      ],
      "event_type": "price_change",
      "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
      "timestamp": "1729084877448",
      "hash": "3cd4d61e042c81560c9037ece0c61f3b1a8fbbdd"
    }
    

**After (New Schema):**

Copy

Ask AI
    
    
    {
        "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
        "price_changes": [
            {
                "asset_id": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
                "price": "0.5",
                "size": "200",
                "side": "BUY",
                "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
                "best_bid": "0.5",
                "best_ask": "1"
            },
            {
                "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
                "price": "0.5",
                "size": "200",
                "side": "SELL",
                "hash": "1895759e4df7a796bf4f1c5a5950b748306923e2",
                "best_bid": "0",
                "best_ask": "0.5"
            }
        ],
        "timestamp": "1757908892351",
        "event_type": "price_change"
    }
    

### 

​

Key Differences

Aspect| Legacy Schema| New Schema  
---|---|---  
**Root level asset_id**|  Present| Removed  
**Changes array**| `changes`| `price_changes`  
**Asset ID location**|  Root level| Inside each price change object  
**Hash location**|  Root level| Inside each price change object  
**Best bid/ask**|  Not included| Included in each change  
**Side values**|  ”SELL”, “BUY"| "SELL”, “BUY” (unchanged)  
  
## 

​

Handle New Fields

The new schema provides additional market data:

  * **`best_bid`** : Current best bid price for the asset
  * **`best_ask`** : Current best ask price for the asset
  * **`hash`** : Now provided per price change rather than per message



## 

​

Benefits of the New Schema

  * **Enhanced market data** : Best bid/ask prices are now included
  * **Granular change tracking** : Hash values are provided per change rather than per message
  * **Clearer structure** : The reorganized schema makes the relationship between market, assets, and changes more explicit



## 

​

Timeline

  * **Go-live** : **September 15, 2025 at 11PM UTC**
  * **Legacy support** : None, these changes are not backwards compatible



## 

​

Testing Your Migration

  1. **Update your parsing logic** following the examples above
  2. **Verify handling of new fields** like `best_bid` and `best_ask`
  3. **Check error handling** for the new structure



## 

​

Support

If you encounter issues during migration or have questions about the new schema, please reach out to `Fleming` on the #dev channel of our Discord.

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
