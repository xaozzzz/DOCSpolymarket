# Order Attribution - Polymarket Documentation

Source: https://docs.polymarket.com/developers/builders/order-attribution

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Polymarket Builders Program

Order Attribution

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
  * Builder API Credentials
  * Signing Methods
  * Authentication Headers
  * Next Steps



Polymarket Builders Program

# Order Attribution

Learn how to attribute orders to your builder account

## 

​

Overview

The [CLOB (Central Limit Order Book)](/developers/CLOB/introduction) is Polymarket’s order matching system. Order attribution adds builder authentication headers when placing orders through the CLOB Client, enabling Polymarket to credit trades to your builder account. This allows you to:

  * Track volume on the [Builder Leaderboard](https://builders.polymarket.com/)
  * Compete for grants based on trading activity
  * Monitor performance via the Data API



* * *

## 

​

Builder API Credentials

Each builder receives API credentials from their [Builder Profile](/developers/builders/builder-profile):

Credential| Description  
---|---  
`key`| Your builder API key identifier  
`secret`| Secret key for signing requests  
`passphrase`| Additional authentication passphrase  
  
**Security Notice** : Your Builder API keys must be kept secure. Never expose them in client-side code.

* * *

## 

​

Signing Methods

  * Remote Signing (Recommended)

  * Local Signing




Remote signing keeps your credentials secure on a server you control.**How it works:**

  1. User signs an order payload
  2. Payload is sent to your builder signing server
  3. Your server adds builder authentication headers
  4. Complete order is sent to the CLOB



### 

​

Server Implementation

Your signing server receives request details and returns the authentication headers. Use the `buildHmacSignature` function from the SDK:

TypeScript

Python

Copy

Ask AI
    
    
    import { 
      buildHmacSignature, 
      BuilderApiKeyCreds 
    } from "@polymarket/builder-signing-sdk";
    
    const BUILDER_CREDENTIALS: BuilderApiKeyCreds = {
      key: process.env.POLY_BUILDER_API_KEY!,
      secret: process.env.POLY_BUILDER_SECRET!,
      passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
    };
    
    // POST /sign - receives { method, path, body } from the client SDK
    export async function handleSignRequest(request) {
      const { method, path, body } = await request.json();
      
      const timestamp = Date.now().toString();
      
      const signature = buildHmacSignature(
        BUILDER_CREDENTIALS.secret,
        parseInt(timestamp),
        method,
        path,
        body
      );
    
      return {
        POLY_BUILDER_SIGNATURE: signature,
        POLY_BUILDER_TIMESTAMP: timestamp,
        POLY_BUILDER_API_KEY: BUILDER_CREDENTIALS.key,
        POLY_BUILDER_PASSPHRASE: BUILDER_CREDENTIALS.passphrase,
      };
    }
    

Never commit credentials to version control. Use environment variables or a secrets manager.

### 

​

Client Configuration

Point your client to your signing server:

TypeScript

Python

Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { BuilderConfig } from "@polymarket/builder-signing-sdk";
    
    // Point to your signing server
    const builderConfig = new BuilderConfig({
      remoteBuilderConfig: { 
        url: "https://your-server.com/sign"
      }
    });
    
    // Or with optional authorization token
    const builderConfigWithAuth = new BuilderConfig({
      remoteBuilderConfig: { 
        url: "https://your-server.com/sign", 
        token: "your-auth-token" 
      }
    });
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer, // ethers v5.x EOA signer
      creds, // User's API Credentials
      2, // signatureType for the Safe proxy wallet
      funderAddress, // Safe proxy wallet address
      undefined, 
      false,
      builderConfig
    );
    
    // Orders automatically use the signing server
    const order = await client.createOrder({
      price: 0.40,
      side: Side.BUY,
      size: 5,
      tokenID: "YOUR_TOKEN_ID"
    });
    
    const response = await client.postOrder(order);
    

### 

​

Troubleshooting

Invalid Signature Errors

**Error:** Client receives invalid signature errors**Solution:**

  1. Verify the request body is passed correctly as JSON
  2. Check that `path`, `body`, and `method` match what the client sends
  3. Ensure your server and client use the same Builder API credentials



Missing Credentials

**Error:** `Builder credentials not configured` or undefined values**Solution:** Ensure your environment variables are set:

  * `POLY_BUILDER_API_KEY`
  * `POLY_BUILDER_SECRET`
  * `POLY_BUILDER_PASSPHRASE`



Sign orders locally when you control the entire order placement flow.**How it works:**

  1. Your system creates and signs orders on behalf of users
  2. Your system uses Builder API credentials locally to add headers
  3. Complete signed order is sent directly to the CLOB



TypeScript

Python

Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";
    
    // Configure with local builder credentials
    const builderCreds: BuilderApiKeyCreds = {
      key: process.env.POLY_BUILDER_API_KEY!,
      secret: process.env.POLY_BUILDER_SECRET!,
      passphrase: process.env.POLY_BUILDER_PASSPHRASE!
    };
    
    const builderConfig = new BuilderConfig({
      localBuilderCreds: builderCreds
    });
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer, // ethers v5.x EOA signer
      creds, // User's API Credentials
      2, // signatureType for the Safe proxy wallet
      funderAddress, // Safe proxy wallet address
      undefined, 
      false,
      builderConfig
    );
    
    // Orders automatically include builder headers
    const order = await client.createOrder({
      price: 0.40,
      side: Side.BUY,
      size: 5,
      tokenID: "YOUR_TOKEN_ID"
    });
    
    const response = await client.postOrder(order);
    

Never commit credentials to version control. Use environment variables or a secrets manager.

* * *

## 

​

Authentication Headers

The SDK automatically generates and attaches these headers to each request:

Header| Description  
---|---  
`POLY_BUILDER_API_KEY`| Your builder API key  
`POLY_BUILDER_TIMESTAMP`| Unix timestamp of signature creation  
`POLY_BUILDER_PASSPHRASE`| Your builder passphrase  
`POLY_BUILDER_SIGNATURE`| HMAC signature of the request  
  
With **local signing** , the SDK constructs and attaches these headers automatically. With **remote signing** , your server must return these headers (see Server Implementation above), and the SDK attaches them to the request.

* * *

## 

​

Next Steps

## [Relayer ClientLearn how to configure and use the Relay Client too!](/developers/builders/relayer-client)## [CLOB Client MethodsExplore the complete CLOB client reference](/developers/CLOB/clients/methods-overview)

[Builder Profile & Keys](/developers/builders/builder-profile)[Relayer Client](/developers/builders/relayer-client)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
