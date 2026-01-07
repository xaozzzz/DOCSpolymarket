# RFQ Overview - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/rfq/overview

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

RFQ Overview

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

  * Overview
  * Roles
  * Requesters
  * Quoters (Market Makers)
  * High-Level Lifecycle
  * System Parameters
  * State Transitions
  * Request States
  * Quote States
  * Authentication
  * Next Steps



# RFQ Overview

Request for Quote (RFQ) system that enables market makers to respond to user-initiated quote requests

## 

​

Overview

The RFQ (Request for Quote) system enables quote-based trade execution by allowing users to request prices from market makers.

The RFQ system is currently in early alpha and requires onboarding. Contact [[email protected]](/cdn-cgi/l/email-protection#36454346465944427646595a4f5b57445d53421855595b) to request access.

## 

​

Roles

### 

​

Requesters

  * Create **Requests** : unsigned intents to buy or sell outcome tokens
  * Anyone may originate Requests from the Polymarket site or API



### 

​

Quoters (Market Makers)

  * Respond to Requests with **Quotes** : unsigned intents to fill those Requests
  * Must be onboarded into the RFQ system by address
  * Compete to offer the best price



## 

​

High-Level Lifecycle

![RFQ Lifecycle](https://mintcdn.com/polymarket-292d1b1b/0G4fHewnXJ-4lGTN/images/rfq-overview.png?fit=max&auto=format&n=0G4fHewnXJ-4lGTN&q=85&s=7bbea7326967df8cb04b189758dcf6a5)

  1. **Requester creates a Request** to BUY or SELL outcome tokens
     * This initiates an auction to the community of Quoters
  2. **Quoter A creates a Quote** responding to the Request
  3. **Quoter B submits a better Quote** (e.g., cheaper price)
  4. **Requester selects and accepts a Quote**
     * An Order is automatically created, which the Requester signs
     * A timer begins: the Quoter must approve within the defined window
  5. **Selected Quoter has last look**
     * If approved: another Order is created, which the Quoter signs
     * If not approved within timeframe: RFQ is rejected
  6. **If approved** : RFQ is executed onchain



## 

​

System Parameters

The RFQ API is live at `https://clob.polymarket.com/rfq`

Parameter| Value| Description  
---|---|---  
**Last Look**|  Enabled| Quoters have a final decision window before committing  
**RequestTTL**|  10 minutes| How long a Request is live before auto-expiration  
**QuoteAcceptTTL**|  10 seconds| Time for Quoter to approve after Requester accepts  
**MultiRequestEnabled**|  false| Requester can only have 1 active Request at a time  
**QuoteRestrictionMode**|  OneQuotePerRequestPerMarket| Quoter can only have 1 active Quote per market  
  
These parameters may change as the system progresses out of alpha.

## 

​

State Transitions

### 

​

Request States

![Request State Transitions](https://mintcdn.com/polymarket-292d1b1b/0G4fHewnXJ-4lGTN/images/rfq-request-states.png?fit=max&auto=format&n=0G4fHewnXJ-4lGTN&q=85&s=cacf3fc16b590a18c0da80b6e69bb0ba)

State| Description  
---|---  
`STATE_ACCEPTING_QUOTES`| Request is live, accepting quotes from market makers  
`STATE_QUOTE_ACCEPTED`| Requester accepted a quote, waiting for Quoter approval  
`STATE_MAKER_ORDER_APPROVED`| Quoter approved, pending onchain execution  
`STATE_COMPLETED`| Successfully executed onchain  
`STATE_USER_CANCELED`| Requester canceled the request  
`STATE_INTERNAL_CANCELED`| System canceled the request  
`STATE_REQUEST_EXPIRED`| Request TTL expired  
`STATE_REQUEST_EXECUTION_FAILED`| Onchain execution failed  
  
### 

​

Quote States

![Quote State Transitions](https://mintcdn.com/polymarket-292d1b1b/0G4fHewnXJ-4lGTN/images/rfq-quote-states.png?fit=max&auto=format&n=0G4fHewnXJ-4lGTN&q=85&s=fe60137b22ea0a849f931d0fc35ee0d1)

State| Description  
---|---  
`STATE_REQUEST_QUOTED`| Quote submitted, waiting for Requester decision  
`STATE_REQUEST_ACCEPTED_QUOTE`| Requester accepted this quote, last look timer started  
`STATE_MAKER_APPROVED`| Quoter approved, pending execution  
`STATE_COMPLETED`| Successfully executed  
`STATE_MAKER_CANCELED`| Quoter canceled their quote  
`STATE_REQUEST_CANCELED`| Parent request was canceled  
`STATE_REQUEST_EXPIRED`| Parent request expired  
`STATE_EXECUTION_FAILED`| Onchain execution failed  
`STATE_MAKER_REJECTED_CANCELED`| Quoter rejected during last look  
`STATE_MAKER_REJECTED_EXPIRED`| Quoter did not respond during last look window  
  
## 

​

Authentication

All RFQ endpoints use **L2 Auth** from the Polymarket CLOB API. See [CLOB Authentication](/developers/CLOB/authentication) for details on generating and using API credentials.

## 

​

Next Steps

## [RFQ API ReferenceComplete endpoint documentation](/developers/market-makers/rfq/api-reference)## [CLOB AuthenticationSet up API credentials for RFQ access](/developers/CLOB/authentication)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
