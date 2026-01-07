# Builder Program Introduction - Polymarket Documentation

Source: https://docs.polymarket.com/developers/builders/builder-intro

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Polymarket Builders Program

Builder Program Introduction

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

  * What is a Builder?
  * Program Benefits
  * Relayer Access
  * Trading Attribution
  * Getting Started
  * SDKs & Libraries



Polymarket Builders Program

# Builder Program Introduction

Learn about Polymarket’s Builder Program and how to integrate

## 

​

What is a Builder?

A “builder” is a person, group, or organization that routes orders from their users to Polymarket. If you’ve created a platform that allows users to trade on Polymarket via your system, this program is for you.

* * *

## 

​

Program Benefits

## Relayer Access

All onchain operations are gasless through our relayer

## Order Attribution

Get credited for orders and compete for grants on the Builder Leaderboard

## Fee Share

Earn a share of fees on routed orders

### 

​

Relayer Access

We expose our relayer to builders, providing gasless transactions for users with Polymarket’s Proxy Wallets deployed via [Relayer Client](/developers/builders/relayer-client). When transactions are routed through proxy wallets, Polymarket pays all gas fees for:

  * Deploying Gnosis Safe Wallets or Custom Proxy (Magic Link users) Wallets
  * Token approvals (USDC, outcome tokens)
  * CTF operations (split, merge, redeem)
  * Order execution (via [CLOB API](/developers/CLOB/introduction))



EOA wallets do not have relayer access. Users trading directly from an EOA pay their own gas fees.

### 

​

Trading Attribution

Attach custom headers to orders to identify your builder account:

  * Orders attributed to your builder account
  * Compete on the [Builder Leaderboard](https://builders.polymarket.com/) for grants
  * Track performance via the Data API
    * [Leaderboard API](/api-reference/builders/get-aggregated-builder-leaderboard): Get aggregated builder rankings for a time period
    * [Volume API](/api-reference/builders/get-daily-builder-volume-time-series): Get daily time-series volume data for trend analysis



* * *

## 

​

Getting Started

  1. **Get Builder Credentials** : Generate API keys from your [Builder Profile](/developers/builders/builder-profile)
  2. **Configure Order Attribution** : Set up CLOB client to credit trades to your account ([guide](/developers/builders/order-attribution))
  3. **Enable Gasless Transactions** : Use the Relayer for gas-free wallet deployment and trading ([guide](/developers/builders/relayer-client))



See [Example Apps](/developers/builders/examples) for complete Next.js reference implementations.

* * *

## 

​

SDKs & Libraries

## [CLOB Client (TypeScript)Place orders with builder attribution](https://github.com/Polymarket/clob-client)## [CLOB Client (Python)Place orders with builder attribution](https://github.com/Polymarket/py-clob-client)## [Relayer Client (TypeScript)Gasless onchain transactions for your users](https://github.com/Polymarket/builder-relayer-client)## [Relayer Client (Python)Gasless onchain transactions for your users](https://github.com/Polymarket/py-builder-relayer-client)## [Signing SDK (TypeScript)Sign builder authentication headers](https://github.com/Polymarket/builder-signing-sdk)## [Signing SDK (Python)Sign builder authentication headers](https://github.com/Polymarket/py-builder-signing-sdk)

[Inventory Management](/developers/market-makers/inventory)[Builder Tiers](/developers/builders/builder-tiers)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
