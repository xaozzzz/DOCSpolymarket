# Quickstart - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/quickstart

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Central Limit Order Book

Quickstart

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
  * Quick Start
  * 1\. Setup Client
  * 2\. Place an Order
  * 3\. Check Your Orders
  * Complete Example
  * Troubleshooting
  * Next Steps



Central Limit Order Book

# Quickstart

Initialize the CLOB and place your first order.

## 

​

Installation

TypeScript

Python

Copy

Ask AI
    
    
    npm install @polymarket/clob-client ethers
    

* * *

## 

​

Quick Start

### 

​

1\. Setup Client

TypeScript

Python

Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers"; // v5.8.0
    
    const HOST = "https://clob.polymarket.com";
    const CHAIN_ID = 137; // Polygon mainnet
    const signer = new Wallet(process.env.PRIVATE_KEY);
    
    // Create or derive user API credentials
    const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
    const apiCreds = await tempClient.createOrDeriveApiKey();
    
    // See 'Signature Types' note below
    const signatureType = 0;
    
    // Initialize trading client
    const client = new ClobClient(
      HOST, 
      CHAIN_ID, 
      signer, 
      apiCreds, 
      signatureType
    );
    

This quick start sets your EOA as the trading account. You’ll need to fund this wallet to trade and pay for gas on transactions. Gas-less transactions are only available by deploying a proxy wallet and using Polymarket’s Polygon relayer infrastructure.

Signature Types

Wallet Type| ID| When to Use  
---|---|---  
EOA| `0`| Standard Ethereum wallet (MetaMask)  
Custom Proxy| `1`| Specific to Magic Link users from Polymarket only  
Gnosis Safe| `2`| Injected providers (Metamask, Rabby, embedded wallets)  
  
* * *

### 

​

2\. Place an Order

TypeScript

Python

Copy

Ask AI
    
    
    import { Side } from "@polymarket/clob-client";
    
    // Place a limit order in one step
    const response = await client.createAndPostOrder({
      tokenID: "YOUR_TOKEN_ID", // Get from Gamma API
      price: 0.65, // Price per share
      size: 10, // Number of shares
      side: Side.BUY, // or SELL
    });
    
    console.log(`Order placed! ID: ${response.orderID}`);
    

* * *

### 

​

3\. Check Your Orders

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
    

* * *

## 

​

Complete Example

TypeScript

Python

Copy

Ask AI
    
    
    import { ClobClient, Side } from "@polymarket/clob-client";
    import { Wallet } from "ethers";
    
    async function trade() {
      const HOST = "https://clob.polymarket.com";
      const CHAIN_ID = 137; // Polygon mainnet
      const signer = new Wallet(process.env.PRIVATE_KEY);
    
      const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
      const apiCreds = await tempClient.createOrDeriveApiKey();
    
      const signatureType = 0;
    
      const client = new ClobClient(
        HOST,
        CHAIN_ID,
        signer,
        apiCreds,
        signatureType
      );
    
      const response = await client.createAndPostOrder({
        tokenID: "YOUR_TOKEN_ID",
        price: 0.65,
        size: 10,
        side: Side.BUY,
      });
    
      console.log(`Order placed! ID: ${response.orderID}`);
    }
    
    trade();
    

* * *

## 

​

Troubleshooting

Error: L2_AUTH_NOT_AVAILABLE

You forgot to call `createOrDeriveApiKey()`. Make sure you initialize the client with API credentials:

Copy

Ask AI
    
    
    const creds = await clobClient.createOrDeriveApiKey();
    const client = new ClobClient(host, chainId, wallet, creds);
    

Order rejected: insufficient balance

Ensure you have:

  * **USDC** in your funder address for BUY orders
  * **Outcome tokens** in your funder address for SELL orders

Check your balance at [polymarket.com/portfolio](https://polymarket.com/portfolio).

Order rejected: insufficient allowance

You need to approve the Exchange contract to spend your tokens. This is typically done through the Polymarket UI on your first trade. Or use the CTF contract’s `setApprovalForAll()` method.

What's my funder address?

Your funder address is the Polymarket proxy wallet where you deposit funds. Find it:

  1. Go to [polymarket.com/settings](https://polymarket.com/settings)
  2. Look for “Wallet Address” or “Profile Address”
  3. This is your `FUNDER_ADDRESS`



* * *

## 

​

Next Steps

## [Full Example ImplementationsComplete Next.js examples demonstrating integration of embedded wallets (Privy, Magic, Turnkey, wagmi) and the CLOB and Builder Relay clients](/developers/builders/examples)

## [Understand CLOB AuthenticationDeep dive into L1 and L2 authentication](/developers/CLOB/authentication)## [Browse Client MethodsExplore the complete client reference](/developers/CLOB/clients/methods-overview)## [Find Markets to TradeUse Gamma API to discover markets](/developers/gamma-markets-api/get-markets)## [Monitor with WebSocketGet real-time order updates](/developers/CLOB/websocket/wss-overview)

[Status](/developers/CLOB/status)[Authentication](/developers/CLOB/authentication)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
