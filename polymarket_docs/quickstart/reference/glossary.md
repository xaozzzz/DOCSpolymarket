# Glossary - Polymarket Documentation

Source: https://docs.polymarket.com/quickstart/reference/glossary

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Developer Quickstart

Glossary

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

  * Markets & Events
  * Trading
  * Order Types
  * Market Types
  * Wallets
  * Token Operations (CTF)
  * Infrastructure



Developer Quickstart

# Glossary

Key terms and concepts for Polymarket developers

## 

​

Markets & Events

Term| Definition  
---|---  
**Event**|  A collection of related markets grouped under a common topic. Example: “2024 US Presidential Election” contains markets for each candidate.  
**Market**|  A single tradeable outcome within an event. Each market has a Yes and No side. Corresponds to a condition ID, question ID, and pair of token IDs.  
**Token**|  Represents a position in a specific outcome (Yes or No). Prices range from 0.00 to 1.00. Winning tokens redeem for $1 USDCe. Also called _outcome token_ or referenced by _token ID_.  
**Token ID**|  The unique identifier for a specific outcome token. Required when placing orders or querying prices.  
**Condition ID**|  Onchain identifier for a market’s resolution condition. Used in CTF operations.  
**Question ID**|  Identifier linking a market to its resolution oracle (UMA).  
**Slug**|  Human-readable URL identifier for a market or event. Found in Polymarket URLs: `polymarket.com/event/[slug]`  
  
* * *

## 

​

Trading

Term| Definition  
---|---  
**CLOB**|  Central Limit Order Book. Polymarket’s off-chain order matching system. Orders are matched here before onchain settlement.  
**Tick Size**|  The minimum price increment for a market. Usually `0.01` (1 cent) or `0.001` (0.1 cent).  
**Fill**|  When an order is matched and executed. Orders can be partially or fully filled.  
  
* * *

## 

​

Order Types

Term| Definition  
---|---  
**GTC**|  Good-Til-Cancelled. An order that remains open until filled or manually cancelled.  
**GTD**|  Good-Til-Date. An order that expires at a specified time if not filled.  
**FOK**|  Fill-Or-Kill. An order that must be filled entirely and immediately, or it’s cancelled. No partial fills.  
**FAK**|  Fill-And-Kill. An order that fills as much as possible immediately, then cancels any remaining unfilled portion.  
  
* * *

## 

​

Market Types

Term| Definition  
---|---  
**Binary Market**|  A market with exactly two outcomes: Yes and No. The prices always sum to approximately $1.  
**Negative Risk (NegRisk)**|  A multi-outcome event where only one outcome can resolve Yes. Requires `negRisk: true` in order parameters. [Details](/developers/neg-risk/overview)  
  
* * *

## 

​

Wallets

Term| Definition  
---|---  
**EOA**|  Externally Owned Account. A standard Ethereum wallet controlled by a private key.  
**Funder Address**|  The wallet address that holds funds and tokens for trading.  
**Signature Type**|  Identifies wallet type when trading. `0` = EOA, `1` = Magic Link proxy, `2` = Gnosis Safe proxy.  
  
* * *

## 

​

Token Operations (CTF)

Term| Definition  
---|---  
**CTF**|  Conditional Token Framework. The onchain smart contracts that manage outcome tokens.  
**Split**|  Convert USDCe into a complete set of outcome tokens (one Yes + one No).  
**Merge**|  Convert a complete set of outcome tokens back into USDCe.  
**Redeem**|  After resolution, exchange winning tokens for $1 USDCe each.  
  
* * *

## 

​

Infrastructure

Term| Definition  
---|---  
**Polygon**|  The blockchain network where Polymarket operates. Chain ID: `137`.  
**USDCe**|  The stablecoin used as collateral on Polymarket. Bridged USDC on Polygon.  
  
[Placing Your First Order](/quickstart/first-order)[API Rate Limits](/quickstart/introduction/rate-limits)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
