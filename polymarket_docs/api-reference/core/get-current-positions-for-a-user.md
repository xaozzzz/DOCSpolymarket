# Get current positions for a user - Polymarket Documentation

Source: https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Core

Get current positions for a user

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

    * [GETGet current positions for a user](/api-reference/core/get-current-positions-for-a-user)
    * [GETGet trades for a user or markets](/api-reference/core/get-trades-for-a-user-or-markets)
    * [GETGet user activity](/api-reference/core/get-user-activity)
    * [GETGet top holders for markets](/api-reference/core/get-top-holders-for-markets)
    * [GETGet total value of a user's positions](/api-reference/core/get-total-value-of-a-users-positions)
    * [GETGet closed positions for a user](/api-reference/core/get-closed-positions-for-a-user)
    * [GETGet trader leaderboard rankings](/api-reference/core/get-trader-leaderboard-rankings)
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



Get current positions for a user

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://data-api.polymarket.com/positions

200

400

401

500

Copy

Ask AI
    
    
    [
      {
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
        "asset": "<string>",
        "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
        "size": 123,
        "avgPrice": 123,
        "initialValue": 123,
        "currentValue": 123,
        "cashPnl": 123,
        "percentPnl": 123,
        "totalBought": 123,
        "realizedPnl": 123,
        "percentRealizedPnl": 123,
        "curPrice": 123,
        "redeemable": true,
        "mergeable": true,
        "title": "<string>",
        "slug": "<string>",
        "icon": "<string>",
        "eventSlug": "<string>",
        "outcome": "<string>",
        "outcomeIndex": 123,
        "oppositeOutcome": "<string>",
        "oppositeAsset": "<string>",
        "endDate": "<string>",
        "negativeRisk": true
      }
    ]

Core

# Get current positions for a user

Returns positions filtered by user and optional filters.

GET

/

positions

Try it

Get current positions for a user

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://data-api.polymarket.com/positions

200

400

401

500

Copy

Ask AI
    
    
    [
      {
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
        "asset": "<string>",
        "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
        "size": 123,
        "avgPrice": 123,
        "initialValue": 123,
        "currentValue": 123,
        "cashPnl": 123,
        "percentPnl": 123,
        "totalBought": 123,
        "realizedPnl": 123,
        "percentRealizedPnl": 123,
        "curPrice": 123,
        "redeemable": true,
        "mergeable": true,
        "title": "<string>",
        "slug": "<string>",
        "icon": "<string>",
        "eventSlug": "<string>",
        "outcome": "<string>",
        "outcomeIndex": 123,
        "oppositeOutcome": "<string>",
        "oppositeAsset": "<string>",
        "endDate": "<string>",
        "negativeRisk": true
      }
    ]

#### Query Parameters

​

user

string

required

User address (required) User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

​

market

string[]

Comma-separated list of condition IDs. Mutually exclusive with eventId.

0x-prefixed 64-hex string

​

eventId

integer[]

Comma-separated list of event IDs. Mutually exclusive with market.

Required range: `x >= 1`

​

sizeThreshold

number

default:1

Required range: `x >= 0`

​

redeemable

boolean

default:false

​

mergeable

boolean

default:false

​

limit

integer

default:100

Required range: `0 <= x <= 500`

​

offset

integer

default:0

Required range: `0 <= x <= 10000`

​

sortBy

enum<string>

default:TOKENS

Available options:

`CURRENT`,

`INITIAL`,

`TOKENS`,

`CASHPNL`,

`PERCENTPNL`,

`TITLE`,

`RESOLVING`,

`PRICE`,

`AVGPRICE`

​

sortDirection

enum<string>

default:DESC

Available options:

`ASC`,

`DESC`

​

title

string

Maximum string length: `100`

#### Response

200

application/json

Success

​

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

​

asset

string

​

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

​

size

number

​

avgPrice

number

​

initialValue

number

​

currentValue

number

​

cashPnl

number

​

percentPnl

number

​

totalBought

number

​

realizedPnl

number

​

percentRealizedPnl

number

​

curPrice

number

​

redeemable

boolean

​

mergeable

boolean

​

title

string

​

slug

string

​

icon

string

​

eventSlug

string

​

outcome

string

​

outcomeIndex

integer

​

oppositeOutcome

string

​

oppositeAsset

string

​

endDate

string

​

negativeRisk

boolean

[Data API Health check](/api-reference/data-api-status/data-api-health-check)[Get trades for a user or markets](/api-reference/core/get-trades-for-a-user-or-markets)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
