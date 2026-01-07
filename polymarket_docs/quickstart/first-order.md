# Placing Your First Order - Polymarket Documentation

Source: https://docs.polymarket.com/quickstart/first-order

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Developer Quickstart

Placing Your First Order

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

  * Installation
  * Step 1: Initialize Client with Private Key
  * Step 2: Derive User API Credentials
  * Step 3: Configure Signature Type and Funder
  * Step 4: Reinitialize with Full Authentication
  * Step 5: Place an Order
  * Step 6: Check Your Orders
  * Troubleshooting
  * Adding Builder API Credentials



Developer Quickstart

# Placing Your First Order

Set up authentication and submit your first trade

This guide walks you through placing an order on Polymarket using your own wallet.

* * *

## 

​

Installation

TypeScript

Python

Copy

Ask AI
    
    
    npm install @polymarket/clob-client ethers@5
    

* * *

## 

​

Step 1: Initialize Client with Private Key

TypeScript

Python

Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers"; // v5.8.0
    
    const HOST = "https://clob.polymarket.com";
    const CHAIN_ID = 137; // Polygon mainnet
    const signer = new Wallet(process.env.PRIVATE_KEY);
    
    const client = new ClobClient(HOST, CHAIN_ID, signer);
    

* * *

## 

​

Step 2: Derive User API Credentials

Your private key is used once to derive API credentials. These credentials authenticate all subsequent requests.

TypeScript

Python

Copy

Ask AI
    
    
    // Get existing API key, or create one if none exists
    const userApiCreds = await client.createOrDeriveApiKey();
    
    console.log("API Key:", userApiCreds.apiKey);
    console.log("Secret:", userApiCreds.secret);
    console.log("Passphrase:", userApiCreds.passphrase);
    

* * *

## 

​

Step 3: Configure Signature Type and Funder

Before reinitializing the client, determine your **signature type** and **funder address** :

How do you want to trade?| Type| Value| Funder Address  
---|---|---|---  
I want to use an EOA wallet. It holds USDCe and position tokens, and I’ll pay my own gas.| EOA| `0`| Your EOA wallet address  
I want to trade through my Polymarket.com account (Magic Link email/Google login).| POLY_PROXY| `1`| Your proxy wallet address  
I want to trade through my Polymarket.com account (browser wallet connection).| GNOSIS_SAFE| `2`| Your proxy wallet address  
  
If you have a Polymarket.com account, your funds are in a proxy wallet (visible in the profile dropdown). Use type 1 or 2. Type 0 is for standalone EOA wallets only.

* * *

## 

​

Step 4: Reinitialize with Full Authentication

TypeScript

Python

Copy

Ask AI
    
    
    // Choose based on your wallet type (see table above)
    const SIGNATURE_TYPE = 0; // EOA example
    const FUNDER_ADDRESS = signer.address; // For EOA, funder is your wallet
    
    const client = new ClobClient(
      HOST,
      CHAIN_ID,
      signer,
      userApiCreds,
      SIGNATURE_TYPE,
      FUNDER_ADDRESS
    );
    

**Do not use Builder API credentials in place of User API credentials!** Builder credentials are for order attribution, not user authentication. See [Builder Order Attribution](/developers/builders/order-attribution).

* * *

## 

​

Step 5: Place an Order

Now you’re ready to trade! First, get a token ID from the [Gamma API](/developers/gamma-markets-api/get-markets).

TypeScript

Python

Copy

Ask AI
    
    
    import { Side, OrderType } from "@polymarket/clob-client";
    
    // Get market info first
    const market = await client.getMarket("TOKEN_ID");
    
    const response = await client.createAndPostOrder(
      {
        tokenID: "TOKEN_ID",
        price: 0.50,        // Price per share ($0.50)
        size: 10,           // Number of shares
        side: Side.BUY,     // BUY or SELL
      },
      {
        tickSize: market.tickSize,
        negRisk: market.negRisk,    // true for multi-outcome events
      },
      OrderType.GTC  // Good-Til-Cancelled
    );
    
    console.log("Order ID:", response.orderID);
    console.log("Status:", response.status);
    

* * *

## 

​

Step 6: Check Your Orders

TypeScript

Python

Copy

Ask AI
    
    
    // View all open orders
    const openOrders = await client.getOpenOrders();
    console.log(`You have ${openOrders.length} open orders`);
    
    // View your trade history
    const trades = await client.getTrades();
    console.log(`You've made ${trades.length} trades`);
    
    // Cancel an order
    await client.cancelOrder(response.orderID);
    

* * *

## 

​

Troubleshooting

Invalid Signature / L2 Auth Not Available

Wrong private key, signature type, or funder address for the derived User API credentials.Double check the following values when creating User API credentials via `createOrDeriveApiKey()`:

  * Do not use Builder API credentials in place of User API credentials
  * Check `signatureType` matches your account type (0, 1, or 2)
  * Ensure `funder` is correct for your wallet type



Unauthorized / Invalid API Key

Wrong API key, secret, or passphrase.Re-derive credentials with `createOrDeriveApiKey()` and update your config.

Not Enough Balance / Allowance

Either not enough USDCe / position tokens in your funder address, or you lack approvals to spend your tokens.

  * Deposit USDCe to your funder address.
  * Ensure you have more USDCe than what’s committed in open orders.
  * Check that you’ve set all necessary token approvals.



Blocked by Cloudflare / Geoblock

You’re trying to place a trade from a restricted region.See [Geographic Restrictions](/developers/CLOB/geoblock) for details.

* * *

## 

​

Adding Builder API Credentials

If you’re building an app that routes orders for your users, you can add builder credentials to get attribution on the [Builder Leaderboard](https://builders.polymarket.com/):

TypeScript

Copy

Ask AI
    
    
    import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";
    
    const builderCreds: BuilderApiKeyCreds = {
      key: process.env.POLY_BUILDER_API_KEY!,
      secret: process.env.POLY_BUILDER_SECRET!,
      passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
    };
    
    const builderConfig = new BuilderConfig({ localBuilderCreds: builderCreds });
    
    // Add builderConfig as the last parameter
    const client = new ClobClient(
      HOST, 
      CHAIN_ID, 
      signer, 
      userApiCreds, 
      signatureType, 
      funderAddress,
      undefined, 
      false, 
      builderConfig
    );
    

Builder credentials are **separate** from user credentials. You use your builder credentials to tag orders, but each user still needs their own L2 credentials to trade.

## [Full Builder GuideComplete documentation for order attribution and gasless transactions](/developers/builders/order-attribution)

[Fetching Market Data](/quickstart/fetching-data)[Glossary](/quickstart/reference/glossary)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
