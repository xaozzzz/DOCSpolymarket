# L2 Methods - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/clients/methods-l2

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Client

L2 Methods

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
  * Order Creation and Management
  * createAndPostOrder()
  * createAndPostMarketOrder()
  * postOrder()
  * postOrders()
  * cancelOrder()
  * cancelOrders()
  * cancelAll()
  * cancelMarketOrders()
  * Order and Trade Queries
  * getOrder()
  * getOpenOrders()
  * getTrades()
  * getTradesPaginated()
  * Balance and Allowances
  * getBalanceAllowance()
  * updateBalanceAllowance()
  * API Key Management (L2)
  * getApiKeys()
  * deleteApiKey()
  * Notifications
  * getNotifications()
  * dropNotifications()
  * See Also



Client

# L2 Methods

These methods require user API credentials (L2 headers). Use these for placing trades and managing user’s positions.

* * *

## 

​

Client Initialization

L2 methods require the client to initialize with the signer, signatureType, user API credentials, and funder.

  * TypeScript

  * Python




Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers";
    
    const signer = new Wallet(process.env.PRIVATE_KEY)
    
    const apiCreds = {
      apiKey: process.env.API_KEY,
      secret: process.env.SECRET,
      passphrase: process.env.PASSPHRASE,
    };
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer,
      apiCreds,
      2, // Deployed Safe proxy wallet
      process.env.FUNDER_ADDRESS // Address of deployed Safe proxy wallet
    );
    
    // Ready to send authenticated requests to the CLOB API!
    const order = await client.postOrder(signedOrder);
    

Copy

Ask AI
    
    
    from py_clob_client.client import ClobClient
    from py_clob_client.clob_types import ApiCreds
    import os
    
    api_creds = ApiCreds(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("SECRET"),
        api_passphrase=os.getenv("PASSPHRASE")
    )
    
    client = ClobClient(
        host="https://clob.polymarket.com",
        chain_id=137,
        key=os.getenv("PRIVATE_KEY"),
        creds=api_creds,
        signature_type=2, # Deployed Safe proxy wallet
        funder=os.getenv("FUNDER_ADDRESS") # Address of deployed Safe proxy wallet
    )
    
    # Ready to send authenticated requests to the CLOB API!
    order = await client.post_order(signed_order)
    

* * *

## 

​

Order Creation and Management

* * *

### 

​

createAndPostOrder()

A convenience method that creates, prompts signature, and posts an order in a single call. Use when you want to buy/sell at a specific price and can wait.

Signature

Copy

Ask AI
    
    
    async createAndPostOrder(
      userOrder: UserOrder,
      options?: Partial<CreateOrderOptions>,
      orderType?: OrderType.GTC | OrderType.GTD, // Defaults to GTC
    ): Promise<OrderResponse>
    

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
    
    type CreateOrderOptions = {
      tickSize: TickSize;
      negRisk?: boolean;
    }
    
    type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
    

Response

Copy

Ask AI
    
    
    interface OrderResponse {
      success: boolean;
      errorMsg: string;
      orderID: string;
      transactionsHashes: string[];
      status: string;
      takingAmount: string;
      makingAmount: string;
    }
    

* * *

### 

​

createAndPostMarketOrder()

A convenience method that creates, prompts signature, and posts an order in a single call. Use when you want to buy/sell right now at whatever the market price is.

Signature

Copy

Ask AI
    
    
    async createAndPostMarketOrder(
      userMarketOrder: UserMarketOrder,
      options?: Partial<CreateOrderOptions>,
      orderType?: OrderType.FOK | OrderType.FAK, // Defaults to FOK
    ): Promise<OrderResponse>
    

Params

Copy

Ask AI
    
    
    interface UserMarketOrder {
      tokenID: string;
      amount: number;
      side: Side;
      price?: number;
      feeRateBps?: number;
      nonce?: number;
      taker?: string;
      orderType?: OrderType.FOK | OrderType.FAK;
    }
    
    type CreateOrderOptions = {
      tickSize: TickSize;
      negRisk?: boolean;
    }
    
    type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
    

Response

Copy

Ask AI
    
    
    interface OrderResponse {
      success: boolean;
      errorMsg: string;
      orderID: string;
      transactionsHashes: string[];
      status: string;
      takingAmount: string;
      makingAmount: string;
    }
    

* * *

### 

​

postOrder()

Posts a pre-signed and created order to the CLOB.

Signature

Copy

Ask AI
    
    
    async postOrder(
      order: SignedOrder,
      orderType?: OrderType, // Defaults to GTC
    ): Promise<OrderResponse>
    

Params

Copy

Ask AI
    
    
    order: SignedOrder  // Pre-signed order from createOrder() or createMarketOrder()
    orderType?: OrderType  // Optional, defaults to GTC
    

Response

Copy

Ask AI
    
    
    interface OrderResponse {
      success: boolean;
      errorMsg: string;
      orderID: string;
      transactionsHashes: string[];
      status: string;
      takingAmount: string;
      makingAmount: string;
    }
    

* * *

### 

​

postOrders()

Posts up to 15 pre-signed and created orders in a single batch.

Copy

Ask AI
    
    
    async postOrders(
      args: PostOrdersArgs[],
    ): Promise<OrderResponse[]>
    

Params

Copy

Ask AI
    
    
    interface PostOrdersArgs {
      order: SignedOrder;
      orderType: OrderType;
    }
    

Response

Copy

Ask AI
    
    
    OrderResponse[]  // Array of OrderResponse objects
    
    interface OrderResponse {
      success: boolean;
      errorMsg: string;
      orderID: string;
      transactionsHashes: string[];
      status: string;
      takingAmount: string;
      makingAmount: string;
    }
    

* * *

### 

​

cancelOrder()

Cancels a single open order.

Signature

Copy

Ask AI
    
    
    async cancelOrder(orderID: string): Promise<CancelOrdersResponse>
    

Response

Copy

Ask AI
    
    
    interface CancelOrdersResponse {
      canceled: string[];
      not_canceled: Record<string, any>;
    }
    

* * *

### 

​

cancelOrders()

Cancels multiple orders in a single batch.

Signature

Copy

Ask AI
    
    
    async cancelOrders(orderIDs: string[]): Promise<CancelOrdersResponse>
    

Params

Copy

Ask AI
    
    
    orderIDs: string[];
    

Response

Copy

Ask AI
    
    
    interface CancelOrdersResponse {
      canceled: string[];
      not_canceled: Record<string, any>;
    }
    

* * *

### 

​

cancelAll()

Cancels all open orders.

Signature

Copy

Ask AI
    
    
    async cancelAll(): Promise<CancelResponse>
    

Response

Copy

Ask AI
    
    
    interface CancelOrdersResponse {
      canceled: string[];
      not_canceled: Record<string, any>;
    }
    

* * *

### 

​

cancelMarketOrders()

Cancels all open orders for a specific market.

Signature

Copy

Ask AI
    
    
    async cancelMarketOrders(
      payload: OrderMarketCancelParams
    ): Promise<CancelOrdersResponse>
    

Parameters

Copy

Ask AI
    
    
    interface OrderMarketCancelParams {
      market?: string;
      asset_id?: string;
    }
    

Response

Copy

Ask AI
    
    
    interface CancelOrdersResponse {
      canceled: string[];
      not_canceled: Record<string, any>;
    }
    

* * *

## 

​

Order and Trade Queries

* * *

### 

​

getOrder()

Get details for a specific order.

Signature

Copy

Ask AI
    
    
    async getOrder(orderID: string): Promise<OpenOrder>
    

Response

Copy

Ask AI
    
    
    interface OpenOrder {
      id: string;
      status: string;
      owner: string;
      maker_address: string;
      market: string;
      asset_id: string;
      side: string;
      original_size: string;
      size_matched: string;
      price: string;
      associate_trades: string[];
      outcome: string;
      created_at: number;
      expiration: string;
      order_type: string;
    }
    

* * *

### 

​

getOpenOrders()

Get all your open orders.

Signature

Copy

Ask AI
    
    
    async getOpenOrders(
      params?: OpenOrderParams,
      only_first_page?: boolean,
    ): Promise<OpenOrdersResponse>
    

Params

Copy

Ask AI
    
    
    interface OpenOrderParams {
      id?: string; // Order ID
      market?: string; // Market condition ID
      asset_id?: string; // Token ID
    }
    
    only_first_page?: boolean  // Defaults to false
    

Response

Copy

Ask AI
    
    
    type OpenOrdersResponse = OpenOrder[];
    
    interface OpenOrder {
      id: string;
      status: string;
      owner: string;
      maker_address: string;
      market: string;
      asset_id: string;
      side: string;
      original_size: string;
      size_matched: string;
      price: string;
      associate_trades: string[];
      outcome: string;
      created_at: number;
      expiration: string;
      order_type: string;
    }
    

* * *

### 

​

getTrades()

Get your trade history (filled orders).

Signature

Copy

Ask AI
    
    
    async getTrades(
      params?: TradeParams,
      only_first_page?: boolean,
    ): Promise<Trade[]>
    

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
    
    only_first_page?: boolean  // Defaults to false
    

Response

Copy

Ask AI
    
    
    interface Trade {
      id: string;
      taker_order_id: string;
      market: string;
      asset_id: string;
      side: Side;
      size: string;
      fee_rate_bps: string;
      price: string;
      status: string;
      match_time: string;
      last_update: string;
      outcome: string;
      bucket_index: number;
      owner: string;
      maker_address: string;
      maker_orders: MakerOrder[];
      transaction_hash: string;
      trader_side: "TAKER" | "MAKER";
    }
    
    interface MakerOrder {
      order_id: string;
      owner: string;
      maker_address: string;
      matched_amount: string;
      price: string;
      fee_rate_bps: string;
      asset_id: string;
      outcome: string;
      side: Side;
    }
    

* * *

### 

​

getTradesPaginated()

Get trade history with pagination for large result sets.

Signature

Copy

Ask AI
    
    
    async getTradesPaginated(
      params?: TradeParams,
    ): Promise<TradesPaginatedResponse>
    

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
    
    
    interface TradesPaginatedResponse {
      trades: Trade[];
      limit: number;
      count: number;
    }
    

* * *

## 

​

Balance and Allowances

* * *

### 

​

getBalanceAllowance()

Get your balance and allowance for specific tokens.

Signature

Copy

Ask AI
    
    
    async getBalanceAllowance(
      params?: BalanceAllowanceParams
    ): Promise<BalanceAllowanceResponse>
    

Params

Copy

Ask AI
    
    
    interface BalanceAllowanceParams {
      asset_type: AssetType;
      token_id?: string;
    }
    
    enum AssetType {
      COLLATERAL = "COLLATERAL",
      CONDITIONAL = "CONDITIONAL",
    }
    

Response

Copy

Ask AI
    
    
    interface BalanceAllowanceResponse {
      balance: string;
      allowance: string;
    }
    

* * *

### 

​

updateBalanceAllowance()

Updates the cached balance and allowance for specific tokens.

Signature

Copy

Ask AI
    
    
    async updateBalanceAllowance(
      params?: BalanceAllowanceParams
    ): Promise<void>
    

Params

Copy

Ask AI
    
    
    interface BalanceAllowanceParams {
      asset_type: AssetType;
      token_id?: string;
    }
    
    enum AssetType {
      COLLATERAL = "COLLATERAL",
      CONDITIONAL = "CONDITIONAL",
    }
    

* * *

## 

​

API Key Management (L2)

### 

​

getApiKeys()

Get all API keys associated with your account.

Signature

Copy

Ask AI
    
    
    async getApiKeys(): Promise<ApiKeysResponse>
    

Response

Copy

Ask AI
    
    
    interface ApiKeysResponse {
      apiKeys: ApiKeyCreds[];
    }
    
    interface ApiKeyCreds {
      key: string;
      secret: string;
      passphrase: string;
    }
    

* * *

### 

​

deleteApiKey()

Deletes (revokes) the currently authenticated API key. **TypeScript Signature:**

Copy

Ask AI
    
    
    async deleteApiKey(): Promise<any>
    

* * *

## 

​

Notifications

* * *

### 

​

getNotifications()

Retrieves all event notifications for the L2 authenticated user. Records are removed automatically after 48 hours or if manually removed via dropNotifications().

Signature

Copy

Ask AI
    
    
    public async getNotifications(): Promise<Notification[]>
    

Response

Copy

Ask AI
    
    
    interface Notification {
        id: number;           // Unique notification ID
        owner: string;        // User's L2 credential apiKey or empty string for global notifications
        payload: any;         // Type-specific payload data
        timestamp?: number;   // Unix timestamp
        type: number;         // Notification type (see type mapping below)
    }
    

**Notification Type Mapping**

Name| Value| Description  
---|---|---  
Order Cancellation| 1| User’s order was canceled  
Order Fill| 2| User’s order was filled (maker or taker)  
Market Resolved| 4| Market was resolved  
  
* * *

### 

​

dropNotifications()

Mark notifications as read/dismissed.

Signature

Copy

Ask AI
    
    
    public async dropNotifications(params?: DropNotificationParams): Promise<void>
    

Params

Copy

Ask AI
    
    
    interface DropNotificationParams {
        ids: string[];  // Array of notification IDs to mark as read
    }
    

* * *

## 

​

See Also

## [Understand CLOB AuthenticationDeep dive into L1 and L2 authentication](/developers/CLOB/authentication)## [Public MethodsAccess market data, orderbooks, and prices.](/developers/CLOB/clients/methods-l2)## [L1 MethodsPrivate key authentication to create or derive API keys (L2 headers)](/developers/CLOB/clients/methods-l2)## [Web Socket APIReal-time market data streaming](/developers/CLOB/websocket/wss-overview)

[L1 Methods](/developers/CLOB/clients/methods-l1)[Builder Methods](/developers/CLOB/clients/methods-builder)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
