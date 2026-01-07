# Builder Profile & Keys - Polymarket Documentation

Source: https://docs.polymarket.com/developers/builders/builder-profile

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Polymarket Builders Program

Builder Profile & Keys

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

  * Accessing Your Builder Profile
  * Builder Profile Settings
  * Customize Your Builder Identity
  * View Your Builder Information
  * Builder API Keys
  * Creating API Keys
  * Managing API Keys
  * Next Steps



Polymarket Builders Program

# Builder Profile & Keys

Learn how to access your builder profile and obtain API credentials

## 

​

Accessing Your Builder Profile

## Direct Link

Go to [polymarket.com/settings?tab=builder](https://polymarket.com/settings?tab=builder)

## From Profile Menu

Click your profile image and Select “Builders”

* * *

## 

​

Builder Profile Settings

![Builder Settings Page](https://mintcdn.com/polymarket-292d1b1b/Quu9lXyXHL-5rjVX/images/builder-profile-image.png?fit=max&auto=format&n=Quu9lXyXHL-5rjVX&q=85&s=67176050b411016e3bfea47bc6fd8fbb)

### 

​

Customize Your Builder Identity

  * **Profile Picture** : Upload a custom image for the [Builder Leaderboard](https://builders.polymarket.com/)
  * **Builder Name** : Set the name displayed publicly on the leaderboard



### 

​

View Your Builder Information

  * **Builder Address** : Your unique builder address for identification
  * **Creation Date** : When your builder account was created
  * **Current Tier** : Your rate limit tier (Unverified or Verified)



* * *

## 

​

Builder API Keys

Builder API keys are required to access the relayer and for CLOB order attribution.

### 

​

Creating API Keys

In the **Builder Keys** section of your profile’s **Builder Settings** :

  1. View existing API keys with their creation dates and status
  2. Click **”+ Create New”** to generate a new API key

Each API key includes:

Credential| Description  
---|---  
`apiKey`| Your builder API key identifier  
`secret`| Secret key for signing requests  
`passphrase`| Additional authentication passphrase  
  
### 

​

Managing API Keys

  * **Multiple Keys** : Create separate keys for different environments
  * **Active Status** : Keys show “ACTIVE” when operational



* * *

## 

​

Next Steps

## [Order AttributionStart attributing customer orders to your account](/developers/builders/order-attribution)## [Builder LeaderboardView your public profile and stats](https://builders.polymarket.com/)

[Builder Tiers](/developers/builders/builder-tiers)[Order Attribution](/developers/builders/order-attribution)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
