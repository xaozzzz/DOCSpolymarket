# Market Maker Introduction - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/introduction

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Market Makers

Market Maker Introduction

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

  * What is a Market Maker?
  * Getting Started
  * Available Tools
  * By Action Type
  * Quick Reference
  * Support



Market Makers

# Market Maker Introduction

Overview of market making on Polymarket and available tools for liquidity providers

## 

​

What is a Market Maker?

A Market Maker (MM) on Polymarket is a sophisticated trader who provides liquidity to prediction markets by continuously posting bid and ask orders. By “laying the spread,” market makers enable other users to trade efficiently while earning the spread as compensation for the risk they take. Market makers are essential to Polymarket’s ecosystem:

  * **Provide liquidity** across all markets
  * **Tighten spreads** for better user experience
  * **Enable price discovery** through continuous quoting
  * **Absorb trading flow** from retail and institutional users

**Not a Market Maker?** If you’re building an application that routes orders for your users, see the [Builders Program](/developers/builders/builder-intro) instead. Builders get access to gasless transactions via the Relayer Client and can earn grants through order attribution.

## 

​

Getting Started

To become a market maker on Polymarket:

  1. **Contact Polymarket** \- Email [[email protected]](/cdn-cgi/l/email-protection#eb989e9b9b84999fab9b848792868a99808e9fc5888486) to request acces to RFQ API
  2. **Complete setup** \- Deploy wallets, fund with USDCe, set token approvals
  3. **Connect to data feeds** \- WebSocket for orderbook, RTDS for low-latency data
  4. **Start quoting** \- Post orders via CLOB REST API or respond to RFQ requests



## 

​

Available Tools

### 

​

By Action Type

## [SetupDeposits, token approvals, wallet deployment, API keys](/developers/market-makers/setup)## [TradingCLOB order entry, order types, quoting best practices](/developers/market-makers/trading)## [RFQ APIRequest for Quote system for responding to large orders](/developers/market-makers/rfq/overview)## [Data FeedsWebSocket, RTDS, Gamma API, on-chain data](/developers/market-makers/data-feeds)## [Inventory ManagementSplit, merge, and redeem outcome tokens](/developers/market-makers/inventory)## [Liquidity RewardsEarn rewards for providing liquidity](/developers/market-makers/liquidity-rewards)

## 

​

Quick Reference

Action| Tool| Documentation  
---|---|---  
Deposit USDCe| Bridge API| [Bridge Overview](/developers/misc-endpoints/bridge-overview)  
Approve tokens| Relayer Client| [Setup Guide](/developers/market-makers/setup)  
Post limit orders| CLOB REST API| [CLOB Client](/developers/CLOB/clients/methods-l2)  
Respond to RFQ| RFQ API| [RFQ Overview](/developers/market-makers/rfq/overview)  
Monitor orderbook| WebSocket| [WebSocket Overview](/developers/CLOB/websocket/wss-overview)  
Low-latency data| RTDS| [Data Feeds](/developers/market-makers/data-feeds)  
Split USDCe to tokens| CTF / Relayer| [Inventory](/developers/market-makers/inventory)  
Merge tokens to USDCe| CTF / Relayer| [Inventory](/developers/market-makers/inventory)  
  
## 

​

Support

For market maker onboarding and support, contact [[email protected]](/cdn-cgi/l/email-protection#ed9e989d9d829f99ad9d828194808c9f868899c38e8280).

[Endpoints](/quickstart/reference/endpoints)[Setup](/developers/market-makers/setup)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
