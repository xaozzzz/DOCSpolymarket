# L1 Methods - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/clients/methods-l1

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Client

L1 Methods

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
  * API Key Management
  * createApiKey()
  * deriveApiKey()
  * createOrDeriveApiKey()
  * Order Signing
  * createOrder()
  * createMarketOrder()
  * Troubleshooting
  * See Also



Client

# L1 Methods

These methods require a wallet signer (private key) but do not require user API credentials. Use these for initial setup.

## 

​

Client Initialization

L1 methods require the client to initialize with a signer.

  * TypeScript

  * Python




Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers";
    
    const signer = new Wallet(process.env.PRIVATE_KEY);
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer // Signer required for L1 methods
    );
    
    // Ready to create user API credentials
    const apiKey = await client.createApiKey();
    

Copy

Ask AI
    
    
    from py_clob_client.client import ClobClient
    import os
    
    private_key = os.getenv("PRIVATE_KEY")
    
    client = ClobClient(
        host="https://clob.polymarket.com",
        chain_id=137,
        key=private_key  # Signer required for L1 methods
    )
    
    # Ready to create user API credentials
    api_key = await client.create_api_key()
    

**Security:** Never commit private keys to version control. Always use environment variables or secure key management systems.

* * *

## 

​

API Key Management

* * *

### 

​

createApiKey()

Creates a new API key (L2 credentials) for the wallet signer. This generates a new set of credentials that can be used for L2 authenticated requests. Each wallet can only have one active API key at a time. Creating a new key invalidates the previous one.

Signature

Copy

Ask AI
    
    
    async createApiKey(nonce?: number): Promise<ApiKeyCreds>
    

Params

Copy

Ask AI
    
    
    `nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
    

Response

Copy

Ask AI
    
    
    interface ApiKeyCreds {
      apiKey: string;
      secret: string;
      passphrase: string;
    }
    

* * *

### 

​

deriveApiKey()

Derives an existing API key (L2 credentials) using a specific nonce. If you’ve already created API credentials with a particular nonce, this method will return the same credentials again.

Signature

Copy

Ask AI
    
    
    async deriveApiKey(nonce?: number): Promise<ApiKeyCreds>
    

Params

Copy

Ask AI
    
    
    `nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
    

Response

Copy

Ask AI
    
    
    interface ApiKeyCreds {
      apiKey: string;
      secret: string;
      passphrase: string;
    }
    

* * *

### 

​

createOrDeriveApiKey()

Convenience method that attempts to derive an API key with the default nonce, or creates a new one if it doesn’t exist. This is the recommended method for initial setup if you’re unsure if credentials already exist.

Signature

Copy

Ask AI
    
    
    async createOrDeriveApiKey(nonce?: number): Promise<ApiKeyCreds>
    

Params

Copy

Ask AI
    
    
    `nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
    

Response

Copy

Ask AI
    
    
    interface ApiKeyCreds {
      apiKey: string;
      secret: string;
      passphrase: string;
    }
    

* * *

## 

​

Order Signing

### 

​

createOrder()

Create and sign a limit order locally without posting it to the CLOB. Use this when you want to sign orders in advance or implement custom order submission logic. Place order via L2 methods postOrder or postOrders.

Signature

Copy

Ask AI
    
    
    async createOrder(
      userOrder: UserOrder,
      options?: Partial<CreateOrderOptions>
    ): Promise<SignedOrder>
    

Params

Copy

Ask AI
    
    
    interface UserOrder {
      tokenID: string;
      price: number;
      size: number;
      side: Side;
      feeRateBps?: number;
      nonce?: number;
      expiration?: number;
      taker?: string;
    }
    
    interface CreateOrderOptions {
      tickSize: TickSize;
      negRisk?: boolean;
    }
    

Response

Copy

Ask AI
    
    
    interface SignedOrder {
      salt: string;
      maker: string;
      signer: string;
      taker: string;
      tokenId: string;
      makerAmount: string;
      takerAmount: string;
      side: number;  // 0 = BUY, 1 = SELL
      expiration: string;
      nonce: string;
      feeRateBps: string;
      signatureType: number;
      signature: string;
    }
    

* * *

### 

​

createMarketOrder()

Create and sign a market order locally without posting it to the CLOB. Use this when you want to sign orders in advance or implement custom order submission logic. Place orders via L2 methods postOrder or postOrders.

Signature

Copy

Ask AI
    
    
    async createMarketOrder(
      userMarketOrder: UserMarketOrder,
      options?: Partial<CreateOrderOptions>
    ): Promise<SignedOrder>
    

Params

Copy

Ask AI
    
    
    interface UserMarketOrder {
      tokenID: string;
      amount: number;  // BUY: dollar amount, SELL: number of shares
      side: Side;
      price?: number;  // Optional price limit
      feeRateBps?: number;
      nonce?: number;
      taker?: string;
      orderType?: OrderType.FOK | OrderType.FAK;
    }
    

Response

Copy

Ask AI
    
    
    interface SignedOrder {
      salt: string;
      maker: string;
      signer: string;
      taker: string;
      tokenId: string;
      makerAmount: string;
      takerAmount: string;
      side: number;  // 0 = BUY, 1 = SELL
      expiration: string;
      nonce: string;
      feeRateBps: string;
      signatureType: number;
      signature: string;
    }
    

* * *

## 

​

Troubleshooting

Error: INVALID_SIGNATURE

Your wallet’s private key is incorrect or improperly formatted.**Solution:**

  * Verify your private key is a valid hex string (starts with “0x”)
  * Ensure you’re using the correct key for the intended address
  * Check that the key has proper permissions



Error: NONCE_ALREADY_USED

The nonce you provided has already been used to create an API key.**Solution:**

  * Use `deriveApiKey()` with the same nonce to retrieve existing credentials
  * Or use a different nonce with `createApiKey()`



Error: Invalid Funder Address

Your funder address is incorrect or doesn’t match your wallet.**Solution:** Check your Polymarket profile address at [polymarket.com/settings](https://polymarket.com/settings).If it does not exist or user has never logged into Polymarket.com, deploy it first before creating L2 authentication.

Lost API credentials but have nonce

Copy

Ask AI
    
    
    // Use deriveApiKey with the original nonce
    const recovered = await client.deriveApiKey(originalNonce);
    

Lost both credentials and nonce

Unfortunately, there’s no way to recover lost API credentials without the nonce. You’ll need to create new credentials:

Copy

Ask AI
    
    
    // Create fresh credentials with a new nonce
    const newCreds = await client.createApiKey();
    // Save the nonce this time!
    

* * *

## 

​

See Also

## [Understand CLOB AuthenticationDeep dive into L1 and L2 authentication](/developers/CLOB/authentication)## [CLOB Quickstart GuideInitialize the CLOB quickly and place your first order.](/developers/CLOB/quickstart)## [Public MethodsAccess market data, orderbooks, and prices.](/developers/CLOB/clients/methods-l2)## [L2 MethodsManage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)

[Public Methods](/developers/CLOB/clients/methods-public)[L2 Methods](/developers/CLOB/clients/methods-l2)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
