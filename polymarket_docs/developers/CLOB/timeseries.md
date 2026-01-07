# Historical Timeseries Data - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/timeseries

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Historical Timeseries Data

Historical Timeseries Data

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

    * [GETHistorical Timeseries Data](/developers/CLOB/timeseries)
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



Get price history for a traded token

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://clob.polymarket.com/prices-history

200

400

404

500

Copy

Ask AI
    
    
    {
      "history": [
        {
          "t": 1697875200,
          "p": 1800.75
        }
      ]
    }

Historical Timeseries Data

# Historical Timeseries Data

Fetches historical price data for a specified market token.

GET

/

prices-history

Try it

Get price history for a traded token

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://clob.polymarket.com/prices-history

200

400

404

500

Copy

Ask AI
    
    
    {
      "history": [
        {
          "t": 1697875200,
          "p": 1800.75
        }
      ]
    }

The CLOB provides detailed price history for each traded token. **HTTP REQUEST** `GET /<clob-endpoint>/prices-history`

We also have a Interactive Notebook to visualize the data from this endpoint available [here](https://colab.research.google.com/drive/1s4TCOR4K7fRP7EwAH1YmOactMakx24Cs?usp=sharing#scrollTo=mYCJBcfB9Zu4).

#### Query Parameters

​

market

string

required

The CLOB token ID for which to fetch price history

​

startTs

number

The start time, a Unix timestamp in UTC

​

endTs

number

The end time, a Unix timestamp in UTC

​

interval

enum<string>

A string representing a duration ending at the current time. Mutually exclusive with startTs and endTs

Available options:

`1m`,

`1w`,

`1d`,

`6h`,

`1h`,

`max`

​

fidelity

number

The resolution of the data, in minutes

#### Response

200

application/json

A list of timestamp/price pairs

​

history

object[]

required

Show child attributes

[Get bid-ask spreads](/api-reference/spreads/get-bid-ask-spreads)[Orders Overview](/developers/CLOB/orders/orders)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
