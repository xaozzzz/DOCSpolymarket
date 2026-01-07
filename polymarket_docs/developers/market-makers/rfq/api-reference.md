# RFQ API Reference - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/rfq/api-reference

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

RFQ API Reference

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

  * Base URL
  * Request Endpoints
  * Create Request
  * Cancel Request
  * Get Requests
  * Quote Endpoints
  * Create Quote
  * Cancel Quote
  * Get Quotes
  * Execution Endpoints
  * Accept Quote
  * Approve Order
  * See Also



# RFQ API Reference

Complete API documentation for the Request for Quote system

## 

​

Base URL

Copy

Ask AI
    
    
    https://clob.polymarket.com
    

All endpoints require **L2 Authentication**. See [CLOB Authentication](/developers/CLOB/authentication) for details.

* * *

## 

​

Request Endpoints

### 

​

Create Request

`POST /rfq/request` Creates an RFQ Request to buy or sell outcome tokens. This initiates the RFQ flow. **Request Body**

Copy

Ask AI
    
    
    {
      "assetIn": "104173557214744537570424345347209544585775842950109756851652855913015295701992",
      "assetOut": "0",
      "amountIn": "50000000",
      "amountOut": "3000000",
      "userType": 1
    }
    

Field| Type| Description  
---|---|---  
`assetIn`| string| Token ID the Requester wants to receive. `"0"` indicates USDC  
`assetOut`| string| Token ID the Requester wants to give. `"0"` indicates USDC  
`amountIn`| string| Amount of asset to receive (in base units)  
`amountOut`| string| Amount of asset to give (in base units)  
`userType`| number| `0` = EOA, `1` = POLY_PROXY, `2` = POLY_GNOSIS_SAFE  
  
**Response**

Copy

Ask AI
    
    
    {
      "requestId": "0196464a-a1fa-75e6-821e-31aa0794f7ad",
      "expiry": 1744936318
    }
    

* * *

### 

​

Cancel Request

`DELETE /rfq/request` Cancels a request. The Request must be in `STATE_ACCEPTING_QUOTES`. **Request Body**

Copy

Ask AI
    
    
    {
      "requestId": "019689a4-0efa-77ca-8b31-c4505de38078"
    }
    

**Response**

Copy

Ask AI
    
    
    OK
    

* * *

### 

​

Get Requests

`GET /rfq/request` Gets RFQ Requests. Requesters can only view their own requests. Quoters can only see their own quotes and requests that they quoted. **Query Parameters**

Parameter| Type| Description  
---|---|---  
`offset`| string| Cursor offset for pagination (base64 encoded). Defaults to 0  
`limit`| number| Max requests to return. Defaults to 50, max 1000  
`state`| string| `active` or `inactive`. Defaults to `active`  
`requestIds`| string[]| Filter by request IDs (e.g., `requestIds=ID1&requestIds=ID2`)  
`markets`| string[]| Filter by condition IDs  
`sizeMin`| number| Minimum size in tokens  
`sizeMax`| number| Maximum size in tokens  
`sizeUsdcMin`| number| Minimum size in USDC  
`sizeUsdcMax`| number| Maximum size in USDC  
`priceMin`| number| Minimum price  
`priceMax`| number| Maximum price  
`sortBy`| string| `price`, `expiry`, `size`, or `created` (default)  
`sortDir`| string| `asc` (default) or `desc`  
  
**Response**

Copy

Ask AI
    
    
    {
      "data": [
        {
          "requestId": "01968f1e-1182-71c4-9d40-172db9be82af",
          "user": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",
          "proxy": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",
          "market": "0x37a6a2dd9f3469495d9ec2467b0a764c5905371a294ce544bc3b2c944eb3e84a",
          "token": "34097058504275310827233323421517291090691602969494795225921954353603704046623",
          "complement": "32868290514114487320702931554221558599637733115139769311383916145370132125101",
          "side": "BUY",
          "sizeIn": 100,
          "sizeOut": 50,
          "price": 0.5,
          "expiry": 1746159634
        }
      ],
      "next_cursor": "LTE=",
      "limit": 100,
      "count": 1
    }
    

* * *

## 

​

Quote Endpoints

### 

​

Create Quote

`POST /rfq/quote` Creates an RFQ Quote in response to a Request. **Request Body**

Copy

Ask AI
    
    
    {
      "requestId": "01968f1e-1182-71c4-9d40-172db9be82af",
      "assetIn": "0",
      "assetOut": "34097058504275310827233323421517291090691602969494795225921954353603704046623",
      "amountIn": "50000000",
      "amountOut": "100000000",
      "userType": 0
    }
    

Field| Type| Description  
---|---|---  
`requestId`| string| ID of the Request to quote  
`assetIn`| string| Token ID the Quoter wants to receive. `"0"` indicates USDC  
`assetOut`| string| Token ID the Quoter wants to give. `"0"` indicates USDC  
`amountIn`| string| Amount of asset to receive (in base units)  
`amountOut`| string| Amount of asset to give (in base units)  
`userType`| number| `0` = EOA, `1` = POLY_PROXY, `2` = POLY_GNOSIS_SAFE  
  
**Response**

Copy

Ask AI
    
    
    {
      "quoteId": "0196464a-a1fa-75e6-821e-31aa0794f7ad"
    }
    

* * *

### 

​

Cancel Quote

`DELETE /rfq/quote` Cancels an RFQ Quote. **Request Body**

Copy

Ask AI
    
    
    {
      "quoteId": "019689a4-0efa-77ca-8b31-c4505de38078"
    }
    

**Response**

Copy

Ask AI
    
    
    OK
    

* * *

### 

​

Get Quotes

`GET /rfq/quote` Gets RFQ Quotes. Requesters can view quotes for their requests. Quoters can view all quotes. **Query Parameters**

Parameter| Type| Description  
---|---|---  
`offset`| string| Cursor offset for pagination (base64 encoded). Defaults to 0  
`limit`| number| Max quotes to return. Defaults to 50, max 1000  
`state`| string| `active` or `inactive` (optional)  
`quoteIds`| string[]| Filter by quote IDs  
`requestIds`| string[]| Filter by request IDs  
`markets`| string[]| Filter by condition IDs  
`sizeMin`| number| Minimum size in tokens  
`sizeMax`| number| Maximum size in tokens  
`sizeUsdcMin`| number| Minimum size in USDC  
`sizeUsdcMax`| number| Maximum size in USDC  
`priceMin`| number| Minimum price  
`priceMax`| number| Maximum price  
`sortBy`| string| `price`, `expiry`, `size`, or `created` (default)  
`sortDir`| string| `asc` (default) or `desc`  
  
**Response**

Copy

Ask AI
    
    
    {
      "data": [
        {
          "quoteId": "0196f484-9fbd-74c1-bfc1-75ac21c1cf84",
          "requestId": "01968f1e-1182-71c4-9d40-172db9be82af",
          "user": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",
          "proxy": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",
          "market": "0x37a6a2dd9f3469495d9ec2467b0a764c5905371a294ce544bc3b2c944eb3e84a",
          "token": "34097058504275310827233323421517291090691602969494795225921954353603704046623",
          "complement": "32868290514114487320702931554221558599637733115139769311383916145370132125101",
          "side": "BUY",
          "sizeIn": 100,
          "sizeOut": 50,
          "price": 0.5
        }
      ],
      "next_cursor": "LTE=",
      "limit": 100,
      "count": 1
    }
    

* * *

## 

​

Execution Endpoints

### 

​

Accept Quote

`POST /rfq/request/accept` Requester accepts an RFQ Quote. This creates an Order that the Requester must sign. **Request Body**

Copy

Ask AI
    
    
    {
      "requestId": "0196a1be-8970-7a86-9324-febf0ad6f687",
      "quoteId": "0196a1be-8970-7a86-9324-febf0ad6f687",
      "makerAmount": "100000000",
      "takerAmount": "200000000",
      "tokenId": "34097058504275310827233323421517291090691602969494795225921954353603704046623",
      "maker": "0x08bba123175624693bd2c6bea754e8f1211accec",
      "signer": "0xb2e5677625a2d9fc6be4667da890acfd98167bd3",
      "taker": "0x25d7777e23e64e583bdc3172fedc636c13b0a1ff",
      "nonce": "1",
      "expiration": 1749149567,
      "side": "BUY",
      "feeRateBps": "0",
      "signature": "0x123123123123123123123123123123123123123123123123",
      "salt": "12312312312",
      "owner": "5d1c266a-ed39-b9bd-c1f5-f24ae3e14a7b"
    }
    

Field| Type| Description  
---|---|---  
`requestId`| string| ID of the Request  
`quoteId`| string| ID of the Quote being accepted  
`makerAmount`| string| Maker’s amount in base units  
`takerAmount`| string| Taker’s amount in base units  
`tokenId`| string| Outcome token ID  
`maker`| string| Maker’s address  
`signer`| string| Signer’s address  
`taker`| string| Taker’s address  
`nonce`| string| Order nonce  
`expiration`| number| Unix timestamp for order expiration  
`side`| string| `BUY` or `SELL`  
`feeRateBps`| string| Fee rate in basis points  
`signature`| string| EIP-712 signature  
`salt`| string| Random salt for order uniqueness  
`owner`| string| Owner identifier  
  
**Response**

Copy

Ask AI
    
    
    OK
    

* * *

### 

​

Approve Order

`POST /rfq/quote/approve` Quoter approves an RFQ order during the last look window. This queues the order for onchain execution. **Request Body**

Copy

Ask AI
    
    
    {
      "requestId": "0196a1be-8970-7a86-9324-febf0ad6f687",
      "quoteId": "0196a1be-8970-7a86-9324-febf0ad6f687",
      "makerAmount": "100000000",
      "takerAmount": "200000000",
      "tokenId": "34097058504275310827233323421517291090691602969494795225921954353603704046623",
      "maker": "0x08bba123175624693bd2c6bea754e8f1211accec",
      "signer": "0xb2e5677625a2d9fc6be4667da890acfd98167bd3",
      "taker": "0x25d7777e23e64e583bdc3172fedc636c13b0a1ff",
      "nonce": "1",
      "expiration": 1749149567,
      "side": "BUY",
      "feeRateBps": "0",
      "signature": "0x123123123123123123123123123123123123",
      "salt": "1231312313",
      "owner": "5d1c266a-ed39-b9bd-c1f5-f24ae3e14a7b"
    }
    

**Response**

Copy

Ask AI
    
    
    {
      "tradeIds": ["019af0f7-eb77-764f-b40f-6de8a3562e12"]
    }
    

* * *

## 

​

See Also

## [RFQ OverviewConcepts, lifecycle, and state transitions](/developers/market-makers/rfq/overview)## [CLOB AuthenticationSet up L2 API credentials](/developers/CLOB/authentication)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
