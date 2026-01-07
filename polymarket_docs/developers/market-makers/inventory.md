# Inventory Management - Polymarket Documentation

Source: https://docs.polymarket.com/developers/market-makers/inventory

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Market Makers

Inventory Management

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
  * Splitting USDCe into Tokens
  * Via Relayer Client (Recommended)
  * Result
  * Merging Tokens to USDCe
  * Via Relayer Client
  * Result
  * Redeeming After Resolution
  * Check Resolution Status
  * Redeem Winning Tokens
  * Payout
  * Negative Risk Markets
  * Inventory Strategies
  * Pre-market Preparation
  * During Trading
  * Post-Resolution
  * Batch Operations
  * Related Documentation



Market Makers

# Inventory Management

Split, merge, and redeem outcome tokens for market making

## 

​

Overview

Market makers need to manage their inventory of outcome tokens. This involves:

  1. **Splitting** USDCe into YES/NO tokens to have inventory to quote
  2. **Merging** tokens back to USDCe to reduce exposure
  3. **Redeeming** winning tokens after market resolution

All these operations use the Conditional Token Framework (CTF) contract, typically via the Relayer Client for gasless execution.

These examples assume you have initialized a RelayClient. See [Setup](/developers/market-makers/setup) for client initialization.

## 

​

Splitting USDCe into Tokens

Split 1 USDCe into 1 YES + 1 NO token. This creates inventory for quoting both sides.

### 

​

Via Relayer Client (Recommended)

Copy

Ask AI
    
    
    import { ethers } from "ethers";
    import { Interface } from "ethers/lib/utils";
    import { RelayClient, Transaction } from "@polymarket/builder-relayer-client";
    
    const CTF_ADDRESS = "0x4d97dcd97ec945f40cf65f87097ace5ea0476045";
    const USDCe_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";
    
    const ctfInterface = new Interface([
      "function splitPosition(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"
    ]);
    
    // Split $1000 USDCe into YES/NO tokens
    const amount = ethers.utils.parseUnits("1000", 6); // USDCe has 6 decimals
    
    const splitTx: Transaction = {
      to: CTF_ADDRESS,
      data: ctfInterface.encodeFunctionData("splitPosition", [
        USDCe_ADDRESS,                                    // collateralToken
        ethers.constants.HashZero,                       // parentCollectionId (null for Polymarket)
        conditionId,                                     // conditionId from market
        [1, 2],                                          // partition: [YES, NO]
        amount
      ]),
      value: "0"
    };
    
    const response = await client.execute([splitTx], "Split USDCe into tokens");
    const result = await response.wait();
    console.log("Split completed:", result?.transactionHash);
    

### 

​

Result

After splitting 1000 USDCe:

  * Receive 1000 YES tokens
  * Receive 1000 NO tokens
  * USDCe balance decreases by 1000



## 

​

Merging Tokens to USDCe

Merge equal amounts of YES + NO tokens back into USDCe. Useful for:

  * Reducing inventory
  * Exiting a market
  * Converting profits to USDCe



### 

​

Via Relayer Client

Copy

Ask AI
    
    
    const ctfInterface = new Interface([
      "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"
    ]);
    
    // Merge 500 YES + 500 NO back to 500 USDCe
    const amount = ethers.utils.parseUnits("500", 6);
    
    const mergeTx: Transaction = {
      to: CTF_ADDRESS,
      data: ctfInterface.encodeFunctionData("mergePositions", [
        USDCe_ADDRESS,
        ethers.constants.HashZero,
        conditionId,
        [1, 2],
        amount
      ]),
      value: "0"
    };
    
    const response = await client.execute([mergeTx], "Merge tokens to USDCe");
    await response.wait();
    

### 

​

Result

After merging 500 of each:

  * YES tokens decrease by 500
  * NO tokens decrease by 500
  * USDCe balance increases by 500



## 

​

Redeeming After Resolution

After a market resolves, redeem winning tokens for USDCe.

### 

​

Check Resolution Status

Copy

Ask AI
    
    
    // Via CLOB API
    const market = await clobClient.getMarket(conditionId);
    if (market.closed) {
      // Market is resolved
      const winningToken = market.tokens.find(t => t.winner);
      console.log("Winning outcome:", winningToken?.outcome);
    }
    

### 

​

Redeem Winning Tokens

Copy

Ask AI
    
    
    const ctfInterface = new Interface([
      "function redeemPositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] indexSets)"
    ]);
    
    const redeemTx: Transaction = {
      to: CTF_ADDRESS,
      data: ctfInterface.encodeFunctionData("redeemPositions", [
        USDCe_ADDRESS,
        ethers.constants.HashZero,
        conditionId,
        [1, 2]  // Redeem both YES and NO (only winners pay out)
      ]),
      value: "0"
    };
    
    const response = await client.execute([redeemTx], "Redeem winning tokens");
    await response.wait();
    

### 

​

Payout

  * If YES wins: Each YES token redeems for $1 USDCe
  * If NO wins: Each NO token redeems for $1 USDCe
  * Losing tokens are worthless (redeem for $0)



## 

​

Negative Risk Markets

Multi-outcome markets use the Negative Risk CTF Exchange. The split/merge process is similar but uses different contract addresses.

Copy

Ask AI
    
    
    const NEG_RISK_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296";
    const NEG_RISK_CTF_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a";
    

See [Negative Risk Overview](/developers/neg-risk/overview) for details.

## 

​

Inventory Strategies

### 

​

Pre-market Preparation

Before quoting a market:

  1. Check market metadata via Gamma API
  2. Split sufficient USDCe to cover expected quoting size
  3. Set token approvals if not already done



### 

​

During Trading

Monitor inventory and adjust:

  * Skew quotes when inventory is imbalanced
  * Merge excess tokens to free up capital
  * Split more when inventory runs low



### 

​

Post-Resolution

After market closes:

  1. Cancel all open orders
  2. Wait for resolution
  3. Redeem winning tokens
  4. Merge any remaining pairs



## 

​

Batch Operations

For efficiency, batch multiple operations:

Copy

Ask AI
    
    
    const transactions: Transaction[] = [
      // Split on Market A
      {
        to: CTF_ADDRESS,
        data: ctfInterface.encodeFunctionData("splitPosition", [
          USDCe_ADDRESS,
          ethers.constants.HashZero,
          conditionIdA,
          [1, 2],
          ethers.utils.parseUnits("1000", 6)
        ]),
        value: "0"
      },
      // Split on Market B
      {
        to: CTF_ADDRESS,
        data: ctfInterface.encodeFunctionData("splitPosition", [
          USDCe_ADDRESS,
          ethers.constants.HashZero,
          conditionIdB,
          [1, 2],
          ethers.utils.parseUnits("1000", 6)
        ]),
        value: "0"
      }
    ];
    
    const response = await client.execute(transactions, "Batch inventory setup");
    await response.wait();
    

## 

​

Related Documentation

## [CTF OverviewConditional Token Framework basics](/developers/CTF/overview)## [Split PositionsDetailed split documentation](/developers/CTF/split)## [Merge PositionsDetailed merge documentation](/developers/CTF/merge)## [Relayer ClientGasless transaction execution](/developers/builders/relayer-client)

[Data Feeds](/developers/market-makers/data-feeds)[Builder Program Introduction](/developers/builders/builder-intro)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
