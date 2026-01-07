# Get order book summary - Polymarket Documentation

Source: https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Orderbook

Get order book summary

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

    * Orderbook

      * [GETGet order book summary](/api-reference/orderbook/get-order-book-summary)
      * [POSTGet multiple order books summaries by request](/api-reference/orderbook/get-multiple-order-books-summaries-by-request)
    * Pricing

    * Spreads

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



Get order book summary

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://clob.polymarket.com/book

200

400

404

500

Copy

Ask AI
    
    
    {
      "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
      "asset_id": "1234567890",
      "timestamp": "2023-10-01T12:00:00Z",
      "hash": "0xabc123def456...",
      "bids": [
        {
          "price": "1800.50",
          "size": "10.5"
        }
      ],
      "asks": [
        {
          "price": "1800.50",
          "size": "10.5"
        }
      ],
      "min_order_size": "0.001",
      "tick_size": "0.01",
      "neg_risk": false
    }

Orderbook

# Get order book summary

Retrieves the order book summary for a specific token

GET

/

book

Try it

Get order book summary

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://clob.polymarket.com/book

200

400

404

500

Copy

Ask AI
    
    
    {
      "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
      "asset_id": "1234567890",
      "timestamp": "2023-10-01T12:00:00Z",
      "hash": "0xabc123def456...",
      "bids": [
        {
          "price": "1800.50",
          "size": "10.5"
        }
      ],
      "asks": [
        {
          "price": "1800.50",
          "size": "10.5"
        }
      ],
      "min_order_size": "0.001",
      "tick_size": "0.01",
      "neg_risk": false
    }

#### Query Parameters

​

token_id

string

required

The unique identifier for the token

#### Response

200

application/json

Successful response

​

market

string

required

Market identifier

Example:

`"0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa"`

​

asset_id

string

required

Asset identifier

Example:

`"1234567890"`

​

timestamp

string<date-time>

required

Timestamp of the order book snapshot

Example:

`"2023-10-01T12:00:00Z"`

​

hash

string

required

Hash of the order book state

Example:

`"0xabc123def456..."`

​

bids

object[]

required

Array of bid levels

Show child attributes

​

asks

object[]

required

Array of ask levels

Show child attributes

​

min_order_size

string

required

Minimum order size for this market

Example:

`"0.001"`

​

tick_size

string

required

Minimum price increment

Example:

`"0.01"`

​

neg_risk

boolean

required

Whether negative risk is enabled

Example:

`false`

[Builder Methods](/developers/CLOB/clients/methods-builder)[Get multiple order books summaries by request](/api-reference/orderbook/get-multiple-order-books-summaries-by-request)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
