# Place Multiple Orders (Batching) - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/orders/create-order-batch

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Order Management

Place Multiple Orders (Batching)

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

    * [Orders Overview](/developers/CLOB/orders/orders)
    * [Place Single Order](/developers/CLOB/orders/create-order)
    * [Place Multiple Orders (Batching)](/developers/CLOB/orders/create-order-batch)
    * [Get Order](/developers/CLOB/orders/get-order)
    * [Get Active Orders](/developers/CLOB/orders/get-active-order)
    * [Check Order Reward Scoring](/developers/CLOB/orders/check-scoring)
    * [Cancel Orders(s)](/developers/CLOB/orders/cancel-orders)
    * [Onchain Order Info](/developers/CLOB/orders/onchain-order-info)
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



Python

typescript

Example Payload

Copy

Ask AI
    
    
    from py_clob_client.client import ClobClient
    from py_clob_client.clob_types import OrderArgs, OrderType, PostOrdersArgs
    from py_clob_client.order_builder.constants import BUY
    
    
    host: str = "https://clob.polymarket.com"
    key: str = "" ##This is your Private Key. Export from https://reveal.magic.link/polymarket or from your Web3 Application
    chain_id: int = 137 #No need to adjust this
    POLYMARKET_PROXY_ADDRESS: str = '' #This is the address listed below your profile picture when using the Polymarket site.
    
    #Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.
    
    
    ### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)
    
    ### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)
    
    ### Initialization of a client that trades directly from an EOA. 
    client = ClobClient(host, key=key, chain_id=chain_id)
    
    ## Create and sign a limit order buying 100 YES tokens for 0.50c each
    #Refer to the Markets API documentation to locate a tokenID: https://docs.polymarket.com/developers/gamma-markets-api/get-markets
    
    client.set_api_creds(client.create_or_derive_api_creds()) 
    
    resp = client.post_orders([
        PostOrdersArgs(
            # Create and sign a limit order buying 100 YES tokens for 0.50 each
            order=client.create_order(OrderArgs(
                price=0.01,
                size=5,
                side=BUY,
                token_id="88613172803544318200496156596909968959424174365708473463931555296257475886634",
            )),
            orderType=OrderType.GTC,  # Good 'Til Cancelled
        ),
        PostOrdersArgs(
            # Create and sign a limit order selling 200 NO tokens for 0.25 each
            order=client.create_order(OrderArgs(
                price=0.01,
                size=5,
                side=BUY,
                token_id="93025177978745967226369398316375153283719303181694312089956059680730874301533",
            )),
            orderType=OrderType.GTC,  # Good 'Til Cancelled
        )
    ])
    print(resp)
    print("Done!")
    

Order Management

# Place Multiple Orders (Batching)

Instructions for placing multiple orders(Batch)

This endpoint requires a L2 Header 

Polymarket’s CLOB supports batch orders, allowing you to place up to `15` orders in a single request. Before using this feature, make sure you’re comfortable placing a single order first. You can find the documentation for that [here.](/developers/CLOB/orders/create-order) **HTTP REQUEST** `POST /<clob-endpoint>/orders`

### 

​

Request Payload Parameters

Name| Required| Type| Description  
---|---|---|---  
PostOrder| yes| PostOrders[]| list of signed order objects (Signed Order + Order Type + Owner)  
  
A `PostOrder` object is the form:

Name| Required| Type| Description  
---|---|---|---  
order| yes| order| See below table for details on crafting this object  
orderType| yes| string| order type (“FOK”, “GTC”, “GTD”, “FAK”)  
owner| yes| string| api key of order owner  
  
An `order` object is the form:

Name| Required| Type| Description  
---|---|---|---  
salt| yes| integer| random salt used to create unique order  
maker| yes| string| maker address (funder)  
signer| yes| string| signing address  
taker| yes| string| taker address (operator)  
tokenId| yes| string| ERC1155 token ID of conditional token being traded  
makerAmount| yes| string| maximum amount maker is willing to spend  
takerAmount| yes| string| minimum amount taker will pay the maker in return  
expiration| yes| string| unix expiration timestamp  
nonce| yes| string| maker’s exchange nonce of the order is associated  
feeRateBps| yes| string| fee rate basis points as required by the operator  
side| yes| string| buy or sell enum index  
signatureType| yes| integer| signature type enum index  
signature| yes| string| hex encoded signature  
  
### 

​

Order types

  * **FOK** : A Fill-Or-Kill order is an market order to buy (in dollars) or sell (in shares) shares that must be executed immediately in its entirety; otherwise, the entire order will be cancelled.
  * **FAK** : A Fill-And-Kill order is a market order to buy (in dollars) or sell (in shares) that will be executed immediately for as many shares as are available; any portion not filled at once is cancelled.
  * **GTC** : A Good-Til-Cancelled order is a limit order that is active until it is fulfilled or cancelled.
  * **GTD** : A Good-Til-Date order is a type of order that is active until its specified date (UTC seconds timestamp), unless it has already been fulfilled or cancelled. There is a security threshold of one minute. If the order needs to expire in 90 seconds the correct expiration value is: now + 1 minute + 30 seconds



### 

​

Response Format

Name| Type| Description  
---|---|---  
success| boolean| boolean indicating if server-side err (`success = false`) -> server-side error  
errorMsg| string| error message in case of unsuccessful placement (in case `success = false`, e.g. `client-side error`, the reason is in `errorMsg`)  
orderId| string| id of order  
orderHashes| string[]| hash of settlement transaction order was marketable and triggered a match  
  
### 

​

Insert Error Messages

If the `errorMsg` field of the response object from placement is not an empty string, the order was not able to be immediately placed. This might be because of a delay or because of a failure. If the `success` is not `true`, then there was an issue placing the order. The following `errorMessages` are possible:

#### 

​

Error

Error| Success| Message| Description  
---|---|---|---  
INVALID_ORDER_MIN_TICK_SIZE| yes| order is invalid. Price breaks minimum tick size rules| order price isn’t accurate to correct tick sizing  
INVALID_ORDER_MIN_SIZE| yes| order is invalid. Size lower than the minimum| order size must meet min size threshold requirement  
INVALID_ORDER_DUPLICATED| yes| order is invalid. Duplicated. Same order has already been placed, can’t be placed again|   
INVALID_ORDER_NOT_ENOUGH_BALANCE| yes| not enough balance / allowance| funder address doesn’t have sufficient balance or allowance for order  
INVALID_ORDER_EXPIRATION| yes| invalid expiration| expiration field expresses a time before now  
INVALID_ORDER_ERROR| yes| could not insert order| system error while inserting order  
EXECUTION_ERROR| yes| could not run the execution| system error while attempting to execute trade  
ORDER_DELAYED| no| order match delayed due to market conditions| order placement delayed  
DELAYING_ORDER_ERROR| yes| error delaying the order| system error while delaying order  
FOK_ORDER_NOT_FILLED_ERROR| yes| order couldn’t be fully filled, FOK orders are fully filled/killed| FOK order not fully filled so can’t be placed  
MARKET_NOT_READY| no| the market is not yet ready to process new orders| system not accepting orders for market yet  
  
### 

​

Insert Statuses

When placing an order, a status field is included. The status field provides additional information regarding the order’s state as a result of the placement. Possible values include:

#### 

​

Status

Status| Description  
---|---  
matched| order placed and matched with an existing resting order  
live| order placed and resting on the book  
delayed| order marketable, but subject to matching delay  
unmatched| order marketable, but failure delaying, placement successful  
  
Python

typescript

Example Payload

Copy

Ask AI
    
    
    from py_clob_client.client import ClobClient
    from py_clob_client.clob_types import OrderArgs, OrderType, PostOrdersArgs
    from py_clob_client.order_builder.constants import BUY
    
    
    host: str = "https://clob.polymarket.com"
    key: str = "" ##This is your Private Key. Export from https://reveal.magic.link/polymarket or from your Web3 Application
    chain_id: int = 137 #No need to adjust this
    POLYMARKET_PROXY_ADDRESS: str = '' #This is the address listed below your profile picture when using the Polymarket site.
    
    #Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.
    
    
    ### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)
    
    ### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)
    
    ### Initialization of a client that trades directly from an EOA. 
    client = ClobClient(host, key=key, chain_id=chain_id)
    
    ## Create and sign a limit order buying 100 YES tokens for 0.50c each
    #Refer to the Markets API documentation to locate a tokenID: https://docs.polymarket.com/developers/gamma-markets-api/get-markets
    
    client.set_api_creds(client.create_or_derive_api_creds()) 
    
    resp = client.post_orders([
        PostOrdersArgs(
            # Create and sign a limit order buying 100 YES tokens for 0.50 each
            order=client.create_order(OrderArgs(
                price=0.01,
                size=5,
                side=BUY,
                token_id="88613172803544318200496156596909968959424174365708473463931555296257475886634",
            )),
            orderType=OrderType.GTC,  # Good 'Til Cancelled
        ),
        PostOrdersArgs(
            # Create and sign a limit order selling 200 NO tokens for 0.25 each
            order=client.create_order(OrderArgs(
                price=0.01,
                size=5,
                side=BUY,
                token_id="93025177978745967226369398316375153283719303181694312089956059680730874301533",
            )),
            orderType=OrderType.GTC,  # Good 'Til Cancelled
        )
    ])
    print(resp)
    print("Done!")
    

[Place Single Order](/developers/CLOB/orders/create-order)[Get Order](/developers/CLOB/orders/get-order)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
