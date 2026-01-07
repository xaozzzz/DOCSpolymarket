# CLOB Introduction - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/introduction

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Central Limit Order Book

CLOB Introduction

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

  * System
  * API
  * Security
  * Fees
  * Schedule
  * Overview
  * Additional Resources



Central Limit Order Book

# CLOB Introduction

Welcome to the Polymarket Order Book API! This documentation provides overviews, explanations, examples, and annotations to simplify interaction with the order book. The following sections detail the Polymarket Order Book and the API usage.

## 

​

System

Polymarket’s Order Book, or CLOB (Central Limit Order Book), is hybrid-decentralized. It includes an operator for off-chain matching/ordering, with settlement executed on-chain, non-custodially, via signed order messages. The exchange uses a custom Exchange contract facilitating atomic swaps between binary Outcome Tokens (CTF ERC1155 assets and ERC20 PToken assets) and collateral assets (ERC20), following signed limit orders. Designed for binary markets, the contract enables complementary tokens to match across a unified order book. Orders are EIP712-signed structured data. Matched orders have one maker and one or more takers, with price improvements benefiting the taker. The operator handles off-chain order management and submits matched trades to the blockchain for on-chain execution.

## 

​

API

The Polymarket Order Book API enables market makers and traders to programmatically manage market orders. Orders of any amount can be created, listed, fetched, or read from the market order books. Data includes all available markets, market prices, and order history via REST and WebSocket endpoints.

## 

​

Security

Polymarket’s Exchange contract has been audited by Chainsecurity ([View Audit](https://github.com/Polymarket/ctf-exchange/blob/main/audit/ChainSecurity_Polymarket_Exchange_audit.pdf)). The operator’s privileges are limited to order matching, non-censorship, and ensuring correct ordering. Operators can’t set prices or execute unauthorized trades. Users can cancel orders on-chain independently if trust issues arise.

## 

​

Fees

### 

​

Schedule

> Subject to change

Volume Level| Maker Fee Base Rate (bps)| Taker Fee Base Rate (bps)  
---|---|---  
>0 USDC| 0| 0  
  
### 

​

Overview

Fees apply symmetrically in output assets (proceeds). This symmetry ensures fairness and market integrity. Fees are calculated differently depending on whether you are buying or selling:

  * **Selling outcome tokens (base) for collateral (quote):**

feeQuote=baseRate×min⁡(price,1−price)×sizefeeQuote = baseRate \times \min(price, 1 - price) \times sizefeeQuote=baseRate×min(price,1−price)×size

  * **Buying outcome tokens (base) with collateral (quote):**

feeBase=baseRate×min⁡(price,1−price)×sizepricefeeBase = baseRate \times \min(price, 1 - price) \times \frac{size}{price}feeBase=baseRate×min(price,1−price)×pricesize​

## 

​

Additional Resources

  * [Exchange contract source code](https://github.com/Polymarket/ctf-exchange/tree/main/src)
  * [Exchange contract documentation](https://github.com/Polymarket/ctf-exchange/blob/main/docs/Overview.md)



[Examples](/developers/builders/examples)[Status](/developers/CLOB/status)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
