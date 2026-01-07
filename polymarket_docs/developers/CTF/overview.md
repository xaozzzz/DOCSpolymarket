# Overview - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CTF/overview

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Conditional Token Frameworks

Overview

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



Conditional Token Frameworks

# Overview

All outcomes on Polymarket are tokenized on the Polygon network. Specifically, Polymarket outcomes shares are binary outcomes (ie “YES” and “NO”) using Gnosis’ Conditional Token Framework (CTF). They are distinct ERC1155 tokens related to a parent condition and backed by the same collateral. More technically, the binary outcome tokens are referred to as “positionIds” in Gnosis’s documentation. “PositionIds” are derived from a collateral token and distinct “collectionIds”. “CollectionIds” are derived from a “parentCollectionId”, (always bytes32(0) in our case) a “conditionId”, and a unique “indexSet”. The “indexSet” is a 256 bit array denoting which outcome slots are in an outcome collection; it MUST be a nonempty proper subset of a condition’s outcome slots. In the binary case, which we are interested in, there are two “indexSets”, one for the first outcome and one for the second. The first outcome’s “indexSet” is 0b01 = 1 and the second’s is 0b10 = 2. The parent “conditionId” (shared by both “collectionIds” and therefore “positionIds”) is derived from a “questionId” (a hash of the UMA ancillary data), an “oracle” (the UMA adapter V2), and an “outcomeSlotCount” (always 2 in the binary case). The steps for calculating the ERC1155 token ids (positionIds) is as follows:

  1. Get the conditionId
     1. Function:
        1. `getConditionId(oracle, questionId, outcomeSlotCount)`
     2. Inputs:
        1. `oracle`: address - UMA adapter V2
        2. `questionId`: bytes32 - hash of the UMA ancillary data
        3. `outcomeSlotCount`: uint - 2 for binary markets
  2. Get the two collectionIds
     1. Function:
        1. `getCollectionId(parentCollectionId, conditionId, indexSet)`
     2. Inputs:
        1. `parentCollectionId`: bytes32 - bytes32(0)
        2. `conditionId`: bytes32 - the conditionId derived from (1)
        3. `indexSet`: uint - 1 (0b01) for the first and 2 (0b10) for the second.
  3. Get the two positionIds
     1. Function:
        1. `getPositionId(collateralToken, collectionId)`
     2. Inputs:
        1. `collateralToken`: IERC20 - address of ERC20 token collateral (USDC)
        2. `collectionId`: bytes32 - the two collectionIds derived from (3)

Leveraging the relations above, specifically “conditionIds” -> “positionIds” the Gnosis CTF contract allows for “splitting” and “merging” full outcome sets. We explore these actions and provide code examples below.

[Resolution](/developers/resolution/UMA)[Splitting USDC](/developers/CTF/split)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
