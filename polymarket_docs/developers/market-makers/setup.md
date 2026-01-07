# Setup - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/setup

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Market Makers

Setup

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
  * Deposit USDCe
  * Options
  * Using the Bridge API
  * Wallet Options
  * EOA (Externally Owned Account)
  * Safe Wallet (Recommended)
  * Token Approvals
  * Required Approvals
  * Contract Addresses (Polygon Mainnet)
  * Approve via Relayer Client
  * API Key Generation
  * Generate API Key
  * Using Credentials
  * Next Steps



Market Makers

# Setup

One-time setup for market making on Polymarket: deposits, approvals, wallets, and API keys

## 

​

Overview

Before you can start market making on Polymarket, you need to complete these one-time setup steps:

  1. Deposit bridged USDCe to Polygon
  2. Deploy a wallet (EOA or Safe)
  3. Approve tokens for trading
  4. Generate API credentials



## 

​

Deposit USDCe

Market makers need USDCe on Polygon to fund their trading operations.

### 

​

Options

Method| Best For| Documentation  
---|---|---  
Bridge API| Automated deposits from other chains| [Bridge Overview](/developers/misc-endpoints/bridge-overview)  
Direct Polygon transfer| Already have USDCe on Polygon| N/A  
Cross-chain bridge| Large deposits from Ethereum| [Large Deposits](/polymarket-learn/deposits/large-cross-chain-deposits)  
  
### 

​

Using the Bridge API

Copy

Ask AI
    
    
    // Deposit USDCe from Ethereum to Polygon
    const deposit = await fetch("https://clob.polymarket.com/deposit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chainId: "1",
        fromChain: "ethereum",
        toChain: "polygon",
        asset: "USDCe",
        amount: "100000000000" // $100,000 in USDCe (6 decimals)
      })
    });
    

See [Bridge Deposit](/developers/misc-endpoints/bridge-deposit) for full API details.

## 

​

Wallet Options

### 

​

EOA (Externally Owned Account)

Standard Ethereum wallet. You pay for all onchain transactions (approvals, splits, merges, trade exedcution).

### 

​

Safe Wallet (Recommended)

Gnosis Safe-based wallet deployed via Polymarket’s relayer. Benefits:

  * **Gasless transactions** \- Polymarket pays gas fees for onchain operations
  * **Contract wallet** \- Enables advanced features like batched transactions.

Deploy a Safe wallet using the [Relayer Client](/developers/builders/relayer-client):

Copy

Ask AI
    
    
    import { RelayClient, RelayerTxType } from "@polymarket/builder-relayer-client";
    
    const client = new RelayClient(
      "https://relayer-v2.polymarket.com/",
      137, // Polygon mainnet
      signer,
      builderConfig,
      RelayerTxType.SAFE
    );
    
    // Deploy the Safe wallet
    const response = await client.deploy();
    const result = await response.wait();
    console.log("Safe Address:", result?.proxyAddress);
    

## 

​

Token Approvals

Before trading, you must approve the exchange contracts to spend your tokens.

### 

​

Required Approvals

Token| Spender| Purpose  
---|---|---  
USDCe| CTF Contract| Split USDCe into outcome tokens  
CTF (outcome tokens)| CTF Exchange| Trade outcome tokens  
CTF (outcome tokens)| Neg Risk CTF Exchange| Trade neg-risk market tokens  
  
### 

​

Contract Addresses (Polygon Mainnet)

Copy

Ask AI
    
    
    const ADDRESSES = {
      USDCe: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      CTF: "0x4d97dcd97ec945f40cf65f87097ace5ea0476045",
      CTF_EXCHANGE: "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
      NEG_RISK_CTF_EXCHANGE: "0xC5d563A36AE78145C45a50134d48A1215220f80a",
      NEG_RISK_ADAPTER: "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296"
    };
    

### 

​

Approve via Relayer Client

Copy

Ask AI
    
    
    import { ethers } from "ethers";
    import { Interface } from "ethers/lib/utils";
    
    const erc20Interface = new Interface([
      "function approve(address spender, uint256 amount) returns (bool)"
    ]);
    
    // Approve USDCe for CTF contract
    const approveTx = {
      to: ADDRESSES.USDCe,
      data: erc20Interface.encodeFunctionData("approve", [
        ADDRESSES.CTF,
        ethers.constants.MaxUint256
      ]),
      value: "0"
    };
    
    const response = await client.execute([approveTx], "Approve USDCe for CTF");
    await response.wait();
    

See [Relayer Client](/developers/builders/relayer-client) for complete examples.

## 

​

API Key Generation

To place orders and access authenticated endpoints, you need L2 API credentials.

### 

​

Generate API Key

Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer
    );
    
    // Derive API credentials from your wallet
    const credentials = await client.deriveApiKey();
    console.log("API Key:", credentials.key);
    console.log("Secret:", credentials.secret);
    console.log("Passphrase:", credentials.passphrase);
    

### 

​

Using Credentials

Once you have credentials, initialize the client for authenticated operations:

Copy

Ask AI
    
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      wallet,
      credentials
    );
    

See [CLOB Authentication](/developers/CLOB/authentication) for full details.

## 

​

Next Steps

Once setup is complete:

## [Start TradingPost limit orders and manage quotes](/developers/market-makers/trading)## [Connect to RFQRespond to Request for Quote requests](/developers/market-makers/rfq/overview)

[Market Maker Introduction](/developers/market-makers/introduction)[Trading](/developers/market-makers/trading)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
