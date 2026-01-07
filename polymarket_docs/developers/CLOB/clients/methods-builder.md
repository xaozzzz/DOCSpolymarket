# Builder Methods - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/clients/methods-builder

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Client

Builder Methods

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

  * Client Initialization
  * Methods
  * getBuilderTrades()
  * revokeBuilderApiKey()
  * See Also



Client

# Builder Methods

These methods require builder API credentials and are only relevant for Builders Program order attribution.

## 

​

Client Initialization

Builder methods require the client to initialize with a separate authentication setup using builder configs acquired from [Polymarket.com](https://polymarket.com/settings?tab=builder) and the `@polymarket/builder-signing-sdk` package.

  * Local Builder Credentials

  * Remote Builder Signing




TypeScript

Python

Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";
    
    const builderConfig = new BuilderConfig({
      localBuilderCreds: new BuilderApiKeyCreds({
        key: process.env.BUILDER_API_KEY,
        secret: process.env.BUILDER_SECRET,
        passphrase: process.env.BUILDER_PASS_PHRASE,
      }),
    });
    
    const clobClient = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer,
      apiCreds, // The user's API credentials generated from L1 authentication
      signatureType,
      funderAddress,
      undefined,
      false,
      builderConfig
    );
    

TypeScript

Python

Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { BuilderConfig } from "@polymarket/builder-signing-sdk";
    
    const builderConfig = new BuilderConfig({
        remoteBuilderConfig: {url: "http://localhost:3000/sign"}
    });
    
    const clobClient = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer,
      apiCreds, // The user's API credentials generated from L1 authentication
      signatureType,
      funder,
      undefined,
      false,
      builderConfig
    );
    

[More information on builder signing](/developers/builders/order-attribution)

* * *

## 

​

Methods

* * *

### 

​

getBuilderTrades()

Retrieves all trades attributed to your builder account. This method allows builders to track which trades were routed through your platform.

Signature

Copy

Ask AI
    
    
    async getBuilderTrades(
      params?: TradeParams,
    ): Promise<BuilderTradesPaginatedResponse>
    

Params

Copy

Ask AI
    
    
    interface TradeParams {
      id?: string;
      maker_address?: string;
      market?: string;
      asset_id?: string;
      before?: string;
      after?: string;
    }
    

Response

Copy

Ask AI
    
    
    interface BuilderTradesPaginatedResponse {
      trades: BuilderTrade[];
      next_cursor: string;
      limit: number;
      count: number;
    }
    
    interface BuilderTrade {
      id: string;
      tradeType: string;
      takerOrderHash: string;
      builder: string;
      market: string;
      assetId: string;
      side: string;
      size: string;
      sizeUsdc: string;
      price: string;
      status: string;
      outcome: string;
      outcomeIndex: number;
      owner: string;
      maker: string;
      transactionHash: string;
      matchTime: string;
      bucketIndex: number;
      fee: string;
      feeUsdc: string;
      err_msg?: string | null;
      createdAt: string | null;
      updatedAt: string | null;
    }
    

* * *

### 

​

revokeBuilderApiKey()

Revokes the builder API key used to authenticate the current request. After revocation, the key can no longer be used to make builder-authenticated requests.

Signature

Copy

Ask AI
    
    
    async revokeBuilderApiKey(): Promise<any>
    

* * *

## 

​

See Also

## [Builders Program IntroductionLearn the benefits, how to implement, and more.](/developers/builders/builder-intro)## [Implement Builders SigningAttribute orders to you, and pre-requisite to using the Relayer Client.](/developers/builders/order-attribution)## [Relayer ClientThe relayer executes other gasless transactions for your users, on your app.](/developers/builders/relayer-client)## [Full Example ImplementationsComplete Next.js examples integrated with embedded wallets (Privy, Magic, Turnkey, wagmi)](/developers/builders/examples)

[L2 Methods](/developers/CLOB/clients/methods-l2)[Get order book summary](/api-reference/orderbook/get-order-book-summary)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
