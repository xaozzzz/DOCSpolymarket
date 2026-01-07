# Maker Rebates Program - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/maker-rebates-program

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Market Makers

Maker Rebates Program

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

  * Fee Handling by Implementation Type
  * Option 1: Official CLOB Clients (Recommended)
  * Option 2: REST API / Custom Implementations
  * Step 1: Fetch the Fee Rate
  * Step 2: Include in Your Signed Order
  * Step 3: Sign and Submit
  * Fee Behavior
  * Fee Denomination
  * Effective Rates: Buying (100 shares)
  * Effective Rates: Selling (100 shares)
  * Maker Rebates
  * How Rebates Work
  * Rebate Pool
  * Which Markets Have Fees?
  * Related Documentation



Market Makers

# Maker Rebates Program

Technical guide for handling taker fees and earning maker rebates on Polymarket

Polymarket has enabled **taker fees** on **15-minute crypto markets**. These fees fund a **Maker Rebates** program that pays daily USDC rebates to liquidity providers.

## 

​

Fee Handling by Implementation Type

### 

​

Option 1: Official CLOB Clients (Recommended)

The official CLOB clients **automatically handle fees** for you. Update to the latest version:

## [TypeScript Clientnpm install @polymarket/clob-client@latest](https://github.com/Polymarket/clob-client)## [Python Clientpip install —upgrade py-clob-client](https://github.com/Polymarket/py-clob-client)

**What the client does automatically:**

  1. Fetches the fee rate for the market’s token ID
  2. Includes `feeRateBps` in the order structure
  3. Signs the order with the fee rate included

**You don’t need to do anything extra**. Just update your client and your orders will work on fee-enabled markets.

* * *

### 

​

Option 2: REST API / Custom Implementations

If you’re calling the REST API directly or building your own order signing, you must manually include the fee rate in your **signed order payload**.

#### 

​

Step 1: Fetch the Fee Rate

Query the fee rate for the token ID before creating your order:

Copy

Ask AI
    
    
    GET https://clob.polymarket.com/fee-rate?token_id={token_id}
    

**Response:**

Copy

Ask AI
    
    
    {
      "fee_rate_bps": 1000
    }
    

  * **Fee-enabled markets** return a value like `1000`
  * **Fee-free markets** return `0`



#### 

​

Step 2: Include in Your Signed Order

Add the `feeRateBps` field to your order object. This value is **part of the signed payload** , the CLOB validates your signature against it.

Copy

Ask AI
    
    
    {
      "salt": "12345",
      "maker": "0x...",
      "signer": "0x...",
      "taker": "0x...",
      "tokenId": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
      "makerAmount": "50000000",
      "takerAmount": "100000000",
      "expiration": "0",
      "nonce": "0",
      "feeRateBps": "1000",
      "side": "0",
      "signatureType": 2,
      "signature": "0x..."
    }
    

#### 

​

Step 3: Sign and Submit

  1. Include `feeRateBps` in the order object **before signing**
  2. Sign the complete order
  3. POST to `/order` endpoint



**Important:** Always fetch `fee_rate_bps` dynamically, do not hardcode. The fee rate may vary by market or change over time. You only need to pass `feeRateBps`

See the [Create Order documentation](/developers/CLOB/orders/create-order) for full signing details.

* * *

## 

​

Fee Behavior

### 

​

Fee Denomination

Fees are deducted from the **proceeds** of your trade:

Order Type| You Receive| Fee Denomination  
---|---|---  
**BUY**|  Tokens| Fee in tokens  
**SELL**|  USDC| Fee in USDC  
  
Because fees are denominated differently, the **effective fee rate differs** between buying and selling.

### 

​

Effective Rates: Buying (100 shares)

When buying, the fee is in tokens. Effective rate peaks at 50%.

Price| Fee (tokens)| Fee ($)| Effective Rate  
---|---|---|---  
$0.10| 0.20| $0.02| 0.2%  
$0.30| 1.10| $0.33| 1.1%  
$0.50| 1.56| $0.78| 1.6%  
$0.70| 1.10| $0.77| 1.1%  
$0.90| 0.20| $0.18| 0.2%  
  
### 

​

Effective Rates: Selling (100 shares)

When selling, the fee is in USDC. Effective rate peaks around 30%.

Price| Proceeds| Fee ($)| Effective Rate  
---|---|---|---  
$0.10| $10| $0.20| 2.0%  
$0.30| $30| $1.10| 3.7%  
$0.50| $50| $1.56| 3.1%  
$0.70| $70| $1.10| 1.6%  
$0.90| $90| $0.20| 0.2%  
  
* * *

## 

​

Maker Rebates

### 

​

How Rebates Work

  * **Eligibility:** Your orders must add liquidity (maker orders) and get filled
  * **Calculation:** Proportional to your share of executed maker volume in each eligible market
  * **Payment:** Daily in USDC, paid directly to your wallet



### 

​

Rebate Pool

The rebate pool for each market is funded by taker fees collected in that market. Currently, 100% of collected fees are redistributed as maker rebates.

Since taker fees are lower at price extremes, trades filled at those prices contribute less to the rebate pool.

* * *

## 

​

Which Markets Have Fees?

Currently, only **15-minute crypto markets** have fees enabled. Query the fee-rate endpoint to check:

Copy

Ask AI
    
    
    GET https://clob.polymarket.com/fee-rate?token_id={token_id}
    
    # Fee-enabled: { "fee_rate_bps": 1000 }
    # Fee-free:    { "fee_rate_bps": 0 }
    

* * *

## 

​

Related Documentation

## [Maker Rebates ProgramUser-facing overview with full fee tables](/polymarket-learn/trading/maker-rebates-program)## [Create CLOB Order via REST APIFull order structure and signing documentation](/developers/CLOB/orders/create-order)

[Liquidity Rewards](/developers/market-makers/liquidity-rewards)[Data Feeds](/developers/market-makers/data-feeds)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
