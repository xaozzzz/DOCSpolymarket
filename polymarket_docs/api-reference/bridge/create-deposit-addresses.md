# Create deposit addresses - Polymarket Documentation

Source: https://docs.polymarket.com/api-reference/bridge/create-deposit-addresses

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Bridge

Create deposit addresses

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

    * [POSTCreate deposit addresses](/api-reference/bridge/create-deposit-addresses)
    * [GETGet supported assets](/api-reference/bridge/get-supported-assets)



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



Create deposit addresses

cURL

Copy

Ask AI
    
    
    curl --request POST \
      --url https://bridge.polymarket.com/deposit \
      --header 'Content-Type: application/json' \
      --data '
    {
      "address": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
    }
    '

201

400

500

Copy

Ask AI
    
    
    {
      "address": {
        "evm": "0x23566f8b2E82aDfCf01846E54899d110e97AC053",
        "svm": "CrvTBvzryYxBHbWu2TiQpcqD5M7Le7iBKzVmEj3f36Jb",
        "btc": "bc1q8eau83qffxcj8ht4hsjdza3lha9r3egfqysj3g"
      },
      "note": "Only certain chains and tokens are supported. See /supported-assets for details."
    }

Bridge

# Create deposit addresses

Generate unique deposit addresses for bridging assets to Polymarket.

**How it works:**

  1. Request deposit addresses for your Polymarket wallet
  2. Receive deposit addresses for each blockchain type (EVM, Solana, Bitcoin)
  3. Send assets to the appropriate deposit address for your source chain
  4. Assets are automatically bridged and swapped to USDC.e on Polygon
  5. USDC.e is credited to your Polymarket wallet for trading



POST

/

deposit

Try it

Create deposit addresses

cURL

Copy

Ask AI
    
    
    curl --request POST \
      --url https://bridge.polymarket.com/deposit \
      --header 'Content-Type: application/json' \
      --data '
    {
      "address": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
    }
    '

201

400

500

Copy

Ask AI
    
    
    {
      "address": {
        "evm": "0x23566f8b2E82aDfCf01846E54899d110e97AC053",
        "svm": "CrvTBvzryYxBHbWu2TiQpcqD5M7Le7iBKzVmEj3f36Jb",
        "btc": "bc1q8eau83qffxcj8ht4hsjdza3lha9r3egfqysj3g"
      },
      "note": "Only certain chains and tokens are supported. See /supported-assets for details."
    }

#### Body

application/json

​

address

string

required

Your Polymarket wallet address

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

#### Response

201

application/json

Deposit addresses created successfully

​

address

object

Deposit addresses for different blockchain networks

Show child attributes

​

note

string

Additional information about supported chains

Example:

`"Only certain chains and tokens are supported. See /supported-assets for details."`

[Overview](/developers/misc-endpoints/bridge-overview)[Get supported assets](/api-reference/bridge/get-supported-assets)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
