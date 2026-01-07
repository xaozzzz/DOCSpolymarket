# Public Methods - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/clients/methods-public

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Client

Public Methods

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
  * Health Check
  * getOk()
  * Markets
  * getMarket()
  * getMarkets()
  * getSimplifiedMarkets()
  * getSamplingMarkets()
  * getSamplingSimplifiedMarkets()
  * Order Books and Prices
  * calculateMarketPrice()
  * getOrderBook()
  * getOrderBooks()
  * getPrice()
  * getPrices()
  * getMidpoint()
  * getMidpoints()
  * getSpread()
  * getSpreads()
  * getPricesHistory()
  * Trades
  * getLastTradePrice()
  * getLastTradesPrices()
  * getMarketTradesEvents
  * Market Parameters
  * getFeeRateBps()
  * getTickSize()
  * getNegRisk()
  * Time & Server Info
  * getServerTime()
  * See Also



Client

# Public Methods

These methods can be called without a signer or user credentials. Use these for reading market data, prices, and order books.

## 

​

Client Initialization

Public methods require the client to initialize with the host URL and Polygon chain ID.

  * TypeScript

  * Python




Copy

Ask AI
    
    
    import { ClobClient } from "@polymarket/clob-client";
    
    const client = new ClobClient(
      "https://clob.polymarket.com",
      137
    );
    
    // Ready to call public methods
    const markets = await client.getMarkets();
    

Copy

Ask AI
    
    
    from py_clob_client.client import ClobClient
    
    client = ClobClient(
        host="https://clob.polymarket.com",
        chain_id=137
    )
    
    # Ready to call public methods
    markets = await client.get_markets()
    

* * *

## 

​

Health Check

* * *

### 

​

getOk()

Health check endpoint to verify the CLOB service is operational.

Signature

Copy

Ask AI
    
    
    async getOk(): Promise<any>
    

* * *

## 

​

Markets

* * *

### 

​

getMarket()

Get details for a single market by condition ID.

Signature

Copy

Ask AI
    
    
    async getMarket(conditionId: string): Promise<Market>
    

Response

Copy

Ask AI
    
    
    interface MarketToken {
      outcome: string;
      price: number;
      token_id: string;
      winner: boolean;
    }
    
    interface Market {
      accepting_order_timestamp: string | null;
      accepting_orders: boolean;
      active: boolean;
      archived: boolean;
      closed: boolean;
      condition_id: string;
      description: string;
      enable_order_book: boolean;
      end_date_iso: string;
      fpmm: string;
      game_start_time: string;
      icon: string;
      image: string;
      is_50_50_outcome: boolean;
      maker_base_fee: number;
      market_slug: string;
      minimum_order_size: number;
      minimum_tick_size: number;
      neg_risk: boolean;
      neg_risk_market_id: string;
      neg_risk_request_id: string;
      notifications_enabled: boolean;
      question: string;
      question_id: string;
      rewards: {
        max_spread: number;
        min_size: number;
        rates: any | null;
      };
      seconds_delay: number;
      tags: string[];
      taker_base_fee: number;
      tokens: MarketToken[];
    }
    

* * *

### 

​

getMarkets()

Get details for multiple markets paginated.

Signature

Copy

Ask AI
    
    
    async getMarkets(): Promise<PaginationPayload>
    

Response

Copy

Ask AI
    
    
    interface PaginationPayload {
      limit: number;
      count: number;
      data: Market[];
    }
    
    interface Market {
      accepting_order_timestamp: string | null;
      accepting_orders: boolean;
      active: boolean;
      archived: boolean;
      closed: boolean;
      condition_id: string;
      description: string;
      enable_order_book: boolean;
      end_date_iso: string;
      fpmm: string;
      game_start_time: string;
      icon: string;
      image: string;
      is_50_50_outcome: boolean;
      maker_base_fee: number;
      market_slug: string;
      minimum_order_size: number;
      minimum_tick_size: number;
      neg_risk: boolean;
      neg_risk_market_id: string;
      neg_risk_request_id: string;
      notifications_enabled: boolean;
      question: string;
      question_id: string;
      rewards: {
        max_spread: number;
        min_size: number;
        rates: any | null;
      };
      seconds_delay: number;
      tags: string[];
      taker_base_fee: number;
      tokens: MarketToken[];
    }
    
    interface MarketToken {
      outcome: string;
      price: number;
      token_id: string;
      winner: boolean;
    }
    

* * *

### 

​

getSimplifiedMarkets()

Get simplified market data paginated for faster loading.

Signature

Copy

Ask AI
    
    
    async getSimplifiedMarkets(): Promise<PaginationPayload>
    

Response

Copy

Ask AI
    
    
    interface PaginationPayload {
      limit: number;
      count: number;
      data: SimplifiedMarket[];
    }
    
    interface SimplifiedMarket {
      accepting_orders: boolean;
      active: boolean;
      archived: boolean;
      closed: boolean;
      condition_id: string;
      rewards: {
        rates: any | null;
        min_size: number;
        max_spread: number;
      };
        tokens: SimplifiedToken[];
    }
    
    interface SimplifiedToken {
      outcome: string;
      price: number;
      token_id: string;
    }
    

* * *

### 

​

getSamplingMarkets()

Signature

Copy

Ask AI
    
    
    async getSamplingMarkets(): Promise<PaginationPayload>
    

Response

Copy

Ask AI
    
    
    interface PaginationPayload {
      limit: number;
      count: number;
      data: Market[];
    }
    
    interface Market {
      accepting_order_timestamp: string | null;
      accepting_orders: boolean;
      active: boolean;
      archived: boolean;
      closed: boolean;
      condition_id: string;
      description: string;
      enable_order_book: boolean;
      end_date_iso: string;
      fpmm: string;
      game_start_time: string;
      icon: string;
      image: string;
      is_50_50_outcome: boolean;
      maker_base_fee: number;
      market_slug: string;
      minimum_order_size: number;
      minimum_tick_size: number;
      neg_risk: boolean;
      neg_risk_market_id: string;
      neg_risk_request_id: string;
      notifications_enabled: boolean;
      question: string;
      question_id: string;
      rewards: {
        max_spread: number;
        min_size: number;
        rates: any | null;
      };
      seconds_delay: number;
      tags: string[];
      taker_base_fee: number;
      tokens: MarketToken[];
    }
    
    interface MarketToken {
      outcome: string;
      price: number;
      token_id: string;
      winner: boolean;
    }
    

* * *

### 

​

getSamplingSimplifiedMarkets()

Signature

Copy

Ask AI
    
    
    async getSamplingSimplifiedMarkets(): Promise<PaginationPayload>
    

Response

Copy

Ask AI
    
    
    interface PaginationPayload {
      limit: number;
      count: number;
      data: SimplifiedMarket[];
    }
    
    interface SimplifiedMarket {
      accepting_orders: boolean;
      active: boolean;
      archived: boolean;
      closed: boolean;
      condition_id: string;
      rewards: {
        rates: any | null;
        min_size: number;
        max_spread: number;
      };
        tokens: SimplifiedToken[];
    }
    
    interface SimplifiedToken {
      outcome: string;
      price: number;
      token_id: string;
    }
    

* * *

## 

​

Order Books and Prices

* * *

### 

​

calculateMarketPrice()

Signature

Copy

Ask AI
    
    
    async calculateMarketPrice(
      tokenID: string,
      side: Side,
      amount: number,
      orderType: OrderType = OrderType.FOK
    ): Promise<number>
    

Params

Copy

Ask AI
    
    
    enum OrderType {
      GTC = "GTC",  // Good Till Cancelled
      FOK = "FOK",  // Fill or Kill
      GTD = "GTD",  // Good Till Date
      FAK = "FAK",  // Fill and Kill
    }
    
    enum Side {
      BUY = "BUY",
      SELL = "SELL",
    }
    

Response

Copy

Ask AI
    
    
    number // calculated market price
    

* * *

### 

​

getOrderBook()

Get the order book for a specific token ID.

Signature

Copy

Ask AI
    
    
    async getOrderBook(tokenID: string): Promise<OrderBookSummary>
    

Response

Copy

Ask AI
    
    
    interface OrderBookSummary {
      market: string;
      asset_id: string;
      timestamp: string;
      bids: OrderSummary[];
      asks: OrderSummary[];
      min_order_size: string;
      tick_size: string;
      neg_risk: boolean;
      hash: string;
    }
    
    interface OrderSummary {
      price: string;
      size: string;
    }
    

* * *

### 

​

getOrderBooks()

Get order books for multiple token IDs.

Signature

Copy

Ask AI
    
    
    async getOrderBooks(params: BookParams[]): Promise<OrderBookSummary[]>
    

Params

Copy

Ask AI
    
    
    interface BookParams {
      token_id: string;
      side: Side;  // Side.BUY or Side.SELL
    }
    

Response

Copy

Ask AI
    
    
    OrderBookSummary[]
    

* * *

### 

​

getPrice()

Get the current best price for buying or selling a token ID.

Signature

Copy

Ask AI
    
    
    async getPrice(
      tokenID: string,
      side: "BUY" | "SELL"
    ): Promise<any>
    

Response

Copy

Ask AI
    
    
    {
      price: string;
    }
    

* * *

### 

​

getPrices()

Get the current best prices for multiple token IDs.

Signature

Copy

Ask AI
    
    
    async getPrices(params: BookParams[]): Promise<PricesResponse>
    

Params

Copy

Ask AI
    
    
    interface BookParams {
      token_id: string;
      side: Side;  // Side.BUY or Side.SELL
    }
    

Response

Copy

Ask AI
    
    
    interface TokenPrices {
      BUY?: string;
      SELL?: string;
    }
    
    type PricesResponse = {
      [tokenId: string]: TokenPrices;
    }
    

* * *

### 

​

getMidpoint()

Get the midpoint price (average of best bid and best ask) for a token ID.

Signature

Copy

Ask AI
    
    
    async getMidpoint(tokenID: string): Promise<any>
    

Response

Copy

Ask AI
    
    
    {
      mid: string;
    }
    

* * *

### 

​

getMidpoints()

Get the midpoint prices (average of best bid and best ask) for multiple token IDs.

Signature

Copy

Ask AI
    
    
    async getMidpoints(params: BookParams[]): Promise<any>
    

Params

Copy

Ask AI
    
    
    interface BookParams {
      token_id: string;
      side: Side;  // Side is ignored
    }
    

Response

Copy

Ask AI
    
    
    {
      [tokenId: string]: string;
    }
    

* * *

### 

​

getSpread()

Get the spread (difference between best ask and best bid) for a token ID.

Signature

Copy

Ask AI
    
    
    async getSpread(tokenID: string): Promise<SpreadResponse>
    

Response

Copy

Ask AI
    
    
    interface SpreadResponse {
      spread: string;
    }
    

* * *

### 

​

getSpreads()

Get the spreads (difference between best ask and best bid) for multiple token IDs.

Signature

Copy

Ask AI
    
    
    async getSpreads(params: BookParams[]): Promise<SpreadsResponse>
    

Params

Copy

Ask AI
    
    
    interface BookParams {
      token_id: string;
      side: Side;
    }
    

Response

Copy

Ask AI
    
    
    type SpreadsResponse = {
      [tokenId: string]: string;
    }
    

* * *

### 

​

getPricesHistory()

Get historical price data for a token.

Signature

Copy

Ask AI
    
    
    async getPricesHistory(params: PriceHistoryFilterParams): Promise<MarketPrice[]>
    

Params

Copy

Ask AI
    
    
    interface PriceHistoryFilterParams {
      market: string; // tokenID
      startTs?: number;
      endTs?: number;
      fidelity?: number;
      interval: PriceHistoryInterval;
    }
    
    enum PriceHistoryInterval {
      MAX = "max",
      ONE_WEEK = "1w",
      ONE_DAY = "1d",
      SIX_HOURS = "6h",
      ONE_HOUR = "1h",
    }
    

Response

Copy

Ask AI
    
    
    interface MarketPrice {
      t: number;  // timestamp
      p: number;  // price
    }
    

* * *

## 

​

Trades

* * *

### 

​

getLastTradePrice()

Get the price of the most recent trade for a token.

Signature

Copy

Ask AI
    
    
    async getLastTradePrice(tokenID: string): Promise<LastTradePrice>
    

Response

Copy

Ask AI
    
    
    interface LastTradePrice {
      price: string;
      side: string;
    }
    

* * *

### 

​

getLastTradesPrices()

Get the price of the most recent trade for a token.

Signature

Copy

Ask AI
    
    
    async getLastTradesPrices(params: BookParams[]): Promise<LastTradePriceWithToken[]>
    

Params

Copy

Ask AI
    
    
    interface BookParams {
      token_id: string;
      side: Side;
    }
    

Response

Copy

Ask AI
    
    
    interface LastTradePriceWithToken {
      price: string;
      side: string;
      token_id: string;
    }
    

* * *

### 

​

getMarketTradesEvents

Signature

Copy

Ask AI
    
    
    async getMarketTradesEvents(conditionID: string): Promise<MarketTradeEvent[]>
    

Response

Copy

Ask AI
    
    
    interface MarketTradeEvent {
      event_type: string;
      market: {
        condition_id: string;
        asset_id: string;
        question: string;
        icon: string;
        slug: string;
      };
      user: {
        address: string;
        username: string;
        profile_picture: string;
        optimized_profile_picture: string;
        pseudonym: string;
      };
      side: Side;
      size: string;
      fee_rate_bps: string;
      price: string;
      outcome: string;
      outcome_index: number;
      transaction_hash: string;
      timestamp: string;
    }
    

## 

​

Market Parameters

* * *

### 

​

getFeeRateBps()

Get the fee rate in basis points for a token.

Signature

Copy

Ask AI
    
    
    async getFeeRateBps(tokenID: string): Promise<number>
    

Response

Copy

Ask AI
    
    
    number
    

* * *

### 

​

getTickSize()

Get the tick size (minimum price increment) for a market.

Signature

Copy

Ask AI
    
    
    async getTickSize(tokenID: string): Promise<TickSize>
    

Response

Copy

Ask AI
    
    
    type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
    

* * *

### 

​

getNegRisk()

Check if a market uses negative risk (binary complementary tokens).

Signature

Copy

Ask AI
    
    
    async getNegRisk(tokenID: string): Promise<boolean>
    

Response

Copy

Ask AI
    
    
    boolean
    

* * *

## 

​

Time & Server Info

### 

​

getServerTime()

Get the current server timestamp.

Signature

Copy

Ask AI
    
    
    async getServerTime(): Promise<number>
    

Response

Copy

Ask AI
    
    
    number // Unix timestamp in seconds
    

* * *

## 

​

See Also

## [L1 MethodsPrivate key authentication to create or derive API keys (L2 headers).](/developers/CLOB/clients/methods-l1)## [L2 MethodsManage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)## [CLOB Rest API ReferenceComplete REST endpoint documentation](/api-reference/orderbook/get-order-book-summary)## [Web Socket APIReal-time market data streaming](/developers/CLOB/websocket/wss-overview)

[Methods Overview](/developers/CLOB/clients/methods-overview)[L1 Methods](/developers/CLOB/clients/methods-l1)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
