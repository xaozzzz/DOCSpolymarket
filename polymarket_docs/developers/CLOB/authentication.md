# Authentication - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/authentication

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Central Limit Order Book

Authentication

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

  * Authentication Levels
  * L1 Authentication
  * What is L1?
  * What This Enables
  * CLOB Client
  * REST API
  * L2 Authentication
  * What is L2?
  * What This Enables
  * CLOB Client
  * REST API
  * Signature Types and Funder
  * Troubleshooting
  * See Client Methods



Central Limit Order Book

# Authentication

Understanding authentication using Polymarket’s CLOB

The CLOB uses two levels of authentication: **L1 (Private Key)** and **L2 (API Key)**. Either can be accomplished using the CLOB client or REST API. Authentication is not required to access client public methods and public endpoints.

## 

​

Authentication Levels

L1 AuthenticationUse the private key of the user’s account to sign messagesL2 AuthenticationUse API credentials (key, secret, passphrase) to authenticate requests to the CLOB

* * *

## 

​

L1 Authentication

### 

​

What is L1?

L1 authentication uses the wallet’s private key to sign an EIP-712 message used in the request header. It proves ownership and control over the private key. The private key stays in control of the user and all trading activity remains non-custodial.

### 

​

What This Enables

Access to L1 methods that create or derive L2 authentication headers.

  * Create user API credentials
  * Derive existing user API credentials
  * Sign/create user’s orders locally



### 

​

CLOB Client

  * TypeScript

  * Python




Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers"; // v5.8.0
    
    const HOST = "https://clob.polymarket.com";
    const CHAIN_ID = 137; // Polygon mainnet
    const signer = new Wallet(process.env.PRIVATE_KEY);
    
    const client = new ClobClient(
      HOST,
      CHAIN_ID,
      signer // Signer enables L1 methods
    );
    
    // Gets API key, or else creates
    const apiCreds = await client.createOrDeriveApiKey();
    
    /*
    apiCreds = {
      "apiKey": "550e8400-e29b-41d4-a716-446655440000",
      "secret": "base64EncodedSecretString",
      "passphrase": "randomPassphraseString"
    }
    */
    

Copy

Ask AI
    
    
    from py_clob_client.client import ClobClient
    import os
    
    host = "https://clob.polymarket.com"
    chain_id = 137 # Polygon mainnet
    private_key = os.getenv("PRIVATE_KEY")
    
    client = ClobClient(
        host=host,
        chain_id=chaind_id,
        key=private_key  # Signer enables L1 methods
    )
    
    # Gets API key, or else creates
    api_creds = await client.create_or_derive_api_key()
    
    # api_creds = {
    #     "apiKey": "550e8400-e29b-41d4-a716-446655440000",
    #     "secret": "base64EncodedSecretString",
    #     "passphrase": "randomPassphraseString"
    # }
    

**Never commit private keys to version control.** Always use environment variables or secure key management systems.

* * *

### 

​

REST API

While we highly recommend using our provided clients to handle signing and authentication, the following is for developers who choose NOT to use our [Python](https://github.com/Polymarket/py-clob-client) or [TypeScript](https://github.com/Polymarket/clob-client) clients. When making direct REST API calls with L1 authentication, include these headers:

Header| Required?| Description  
---|---|---  
`POLY_ADDRESS`| yes| Polygon signer address  
`POLY_SIGNATURE`| yes| CLOB EIP 712 signature  
`POLY_TIMESTAMP`| yes| Current UNIX timestamp  
`POLY_NONCE`| yes| Nonce. Default 0  
  
The `POLY_SIGNATURE` is generated by signing the following EIP-712 struct.

EIP-712 Signing Example

Typescript

Python

Copy

Ask AI
    
    
    const domain = {
      name: "ClobAuthDomain",
      version: "1",
      chainId: chainId, // Polygon Chain ID 137
    };
    
    const types = {
      ClobAuth: [
        { name: "address", type: "address" },
        { name: "timestamp", type: "string" },
        { name: "nonce", type: "uint256" },
        { name: "message", type: "string" },
      ],
    };
    
    const value = {
      address: signingAddress, // The Signing address
      timestamp: ts,            // The CLOB API server timestamp
      nonce: nonce,             // The nonce used
      message: "This message attests that I control the given wallet",
    };
    
    const sig = await signer._signTypedData(domain, types, value);
    

Reference implementations:

  * [TypeScript](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts)
  * [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py)



* * *

**Create API Credentials** Create new API credentials for user.

Copy

Ask AI
    
    
    POST {clob-endpoint}/auth/api-key
    

**Derive API Credentials** Derive API credentials for user.

Copy

Ask AI
    
    
    GET {clob-endpoint}/auth/derive-api-key
    

**Response**

Copy

Ask AI
    
    
    {
      "apiKey": "550e8400-e29b-41d4-a716-446655440000",
      "secret": "base64EncodedSecretString",
      "passphrase": "randomPassphraseString"
    }
    

**You’ll need all three values for L2 authentication.**

* * *

## 

​

L2 Authentication

### 

​

What is L2?

The next level of authentication is called L2, and it consists of the user’s API credentials (apiKey, secret, passphrase) generated from L1 authentication. These are used solely to authenticate requests made to the CLOB API. Requests are signed using HMAC-SHA256.

### 

​

What This Enables

Access to L2 methods such as posting signed/created orders, viewing open orders, cancelling open orders, getting trades

  * Cancel or get user’s open orders
  * Check user’s balances and allowances
  * Post user’s signed orders



### 

​

CLOB Client

  * TypeScript

  * Python




Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers"; // v5.8.0
    
    const HOST = "https://clob.polymarket.com";
    const CHAIN_ID = 137; // Polygon mainnet
    const signer = new Wallet(process.env.PRIVATE_KEY);
    
    const client = new ClobClient(
      HOST,
      CHAIN_ID,
      signer,
      apiCreds, // Generated from L1 auth, API credentials enable L2 methods
      1, // signatureType explained below
      FUNDER // funder explained below
    );
    
    // Now you can trade!*
    const order = await client.createAndPostOrder(
      { tokenID: "123456", price: 0.65, size: 100, side: "BUY" },
      { tickSize: "0.01", negRisk: false }
    );
    

Copy

Ask AI
    
    
    from py_clob_client.client import ClobClient
    import os
    
    host = "https://clob.polymarket.com"
    chain_id = 137 # Polygon mainnet
    private_key = os.getenv("PRIVATE_KEY")
    
    client = ClobClient(
        host="https://clob.polymarket.com",
        chain_id=137,
        key=os.getenv("PRIVATE_KEY"),
        creds=api_creds,  # Generated from L1 auth, API credentials enable L2 methods
        signature_type=1,  # signatureType explained below
        funder=os.getenv("FUNDER_ADDRESS") # funder explained below
    )
    
    # Now you can trade!*
    order = await client.create_and_post_order(
        {"token_id": "123456", "price": 0.65, "size": 100, "side": "BUY"},
        {"tick_size": "0.01", "neg_risk": False}
    )
    

Even with L2 authentication headers, methods that create user orders still require the user to sign the order payload.

* * *

### 

​

REST API

While we highly recommend using our provided clients to handle signing and authentication, the following is for developers who choose NOT to use our [Python](https://github.com/Polymarket/py-clob-client) or [TypeScript](https://github.com/Polymarket/clob-client) clients. When making direct REST API calls with L2 authentication, include these headers:

Header| Required?| Description  
---|---|---  
`POLY_ADDRESS`| yes| Polygon signer address  
`POLY_SIGNATURE`| yes| HMAC signature for request  
`POLY_TIMESTAMP`| yes| Current UNIX timestamp  
`POLY_API_KEY`| yes| User’s API `apiKey` value  
`POLY_PASSPHRASE`| yes| User’s API `passphrase` value  
  
The `POLY_SIGNATURE` for L2 is an HMAC-SHA256 signature created using the user’s API credentials `secret` value. Reference implementations can be found in the [Typescript](https://github.com/Polymarket/clob-client/blob/main/src/signing/hmac.ts) and [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/hmac.py) clients.

* * *

## 

​

Signature Types and Funder

When initializing the L2 client, you must specify your wallet **signatureType** and the **funder** address which holds the funds:

Signature Type| Value| Description  
---|---|---  
EOA| 0| Standard Ethereum wallet (MetaMask). Funder is the EOA address and will need POL to pay gas on transactions.  
POLY_PROXY| 1| A custom proxy wallet only used with users who logged in via Magic Link email/Google. Using this requires the user to have exported their PK from Polymarket.com and imported into your app.  
GNOSIS_SAFE| 2| Gnosis Safe multisig proxy wallet (most common). Use this for any new or returning user who does not fit the other 2 types.  
  
The wallet addresses displayed to the user on Polymarket.com is the proxy wallet and should be used as the funder. These can be deterministically derived or you can deploy them on behalf of the user. These proxy wallets are automatically deployed for the user on their first login to Polymarket.com.

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

See Client Methods

## [Public MethodsAccess market data, orderbooks, and prices.](/developers/CLOB/clients/methods-public)## [L1 MethodsPrivate key authentication to create or derive API keys (L2 headers).](/developers/CLOB/clients/methods-l1)## [L2 MethodsManage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)## [Builder Program MethodsBuilder-specific operations for those in the Builders Program.](/developers/CLOB/clients/methods-builder)

[Quickstart](/developers/CLOB/quickstart)[Geographic Restrictions](/developers/CLOB/geoblock)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
