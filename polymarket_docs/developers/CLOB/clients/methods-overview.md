# Methods Overview - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/clients/methods-overview

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Client

Methods Overview

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

    * [Methods Overview](/developers/CLOB/clients/methods-overview)
    * [Public Methods](/developers/CLOB/clients/methods-public)
    * [L1 Methods](/developers/CLOB/clients/methods-l1)
    * [L2 Methods](/developers/CLOB/clients/methods-l2)
    * [Builder Methods](/developers/CLOB/clients/methods-builder)
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

  * Client Initialization by Use Case
  * Resources



Client

# Methods Overview

CLOB client methods require different levels of authentication. This reference is organized by what credentials you need to call each method.

## [Public MethodsAccess market data, orderbooks, and prices.](/developers/CLOB/clients/methods-public)## [L1 MethodsPrivate key authentication to create or derive API keys (L2 headers).](/developers/CLOB/clients/methods-l1)## [L2 MethodsManage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)## [Builder Program MethodsBuilder-specific operations for those in the Builders Program.](/developers/CLOB/clients/methods-builder)

* * *

## 

​

Client Initialization by Use Case

  * Get Market Data

  * Generate User API Credentials

  * Create and Post Order

  * Get Builders Orders




TypeScript

Python

Copy

Ask AI
    
    
    // No signer or credentials needed
    const client = new ClobClient(
      "https://clob.polymarket.com", 
      137
    );
    
    // All public methods available
    const markets = await client.getMarkets();
    const book = await client.getOrderBook(tokenId);
    const price = await client.getPrice(tokenId, "BUY");
    

TypeScript

Python

Copy

Ask AI
    
    
    // Create client with signer
    const client = new ClobClient(
      "https://clob.polymarket.com", 
      137, 
      signer
    );
    
    // All public and L1 methods available
    const newCreds = createApiKey();
    const derivedCreds = deriveApiKey();
    const creds = createOrDeriveApiKey();
    

TypeScript

Python

Copy

Ask AI
    
    
    // Create client with signer and creds
    const client = new ClobClient(
      "https://clob.polymarket.com", 
      137, 
      signer,
      creds,
      2, // Indicates Gnosis Safe proxy
      funder // Safe wallet address holding funds
    );
    
    // All public, L1, and L2 methods available
    const order = await client.createOrder({ /* ... */ });
    const result = await client.postOrder(order);
    const trades = await client.getTrades();
    

TypeScript

Python

Copy

Ask AI
    
    
    // Create client with builder's authentication headers
    import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";
    
    const builderCreds: BuilderApiKeyCreds = {
      key: process.env.POLY_BUILDER_API_KEY!,
      secret: process.env.POLY_BUILDER_SECRET!,
      passphrase: process.env.POLY_BUILDER_PASSPHRASE!
    };
    
    const builderConfig: BuilderConfig = {
      localBuilderCreds: builderCreds
    };
    
    const client = new ClobClient(
      "https://clob.polymarket.com", 
      137, 
      signer,
      creds, // User's API credentials
      2,
      funder,
      undefined,
      false,
      builderConfig // Builder's API credentials
    );
    
    // You can call all methods including builder methods
    const builderTrades = await client.getBuilderTrades();
    

Learn more about the Builders Program and Relay Client here

* * *

## 

​

Resources

## [TypeScript ClientOpen source TypeScript client on GitHub](https://github.com/Polymarket/clob-client)## [Python ClientOpen source Python client for GitHub](https://github.com/Polymarket/py-clob-client)## [TypeScript ExamplesTypeScript client method examples](https://github.com/Polymarket/clob-client/tree/main/examples)## [Python ExamplesPython client method examples](https://github.com/Polymarket/py-clob-client/tree/main/examples)## [CLOB Rest API ReferenceComplete REST endpoint documentation](/api-reference/orderbook/get-order-book-summary)## [Web Socket APIReal-time market data streaming](/developers/CLOB/websocket/wss-overview)

[Geographic Restrictions](/developers/CLOB/geoblock)[Public Methods](/developers/CLOB/clients/methods-public)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
