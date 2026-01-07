# RTDS Comments - Polymarket Documentation

Source: https://docs.polymarket.com/developers/RTDS/RTDS-comments

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Real Time Data Stream

RTDS Comments

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
  * Subscription Details
  * Subscription Message
  * Message Format
  * Message Types
  * comment_created
  * comment_removed
  * reaction_created
  * reaction_removed
  * Payload Fields
  * Profile Object Fields
  * Parent Entity Types
  * Example Messages
  * New Comment Created
  * Reply to Existing Comment
  * Comment Hierarchy
  * Use Cases
  * Content
  * Notes



Real Time Data Stream

# RTDS Comments

Polymarket provides a Typescript client for interacting with this streaming service. [Download and view it’s documentation here](https://github.com/Polymarket/real-time-data-client)

## 

​

Overview

The comments subscription provides real-time updates for comment-related events on the Polymarket platform. This includes new comments being created, as well as other comment interactions like reactions and replies.

## 

​

Subscription Details

  * **Topic** : `comments`
  * **Type** : `comment_created` (and potentially other comment event types like `reaction_created`)
  * **Authentication** : May require Gamma authentication for user-specific data
  * **Filters** : Optional (can filter by specific comment IDs, users, or events)



## 

​

Subscription Message

Copy

Ask AI
    
    
    {
      "action": "subscribe",
      "subscriptions": [
        {
          "topic": "comments", 
          "type": "comment_created"
        }
      ]
    }
    

## 

​

Message Format

When subscribed to comments, you’ll receive messages with the following structure:

Copy

Ask AI
    
    
    {
      "topic": "comments",
      "type": "comment_created",
      "timestamp": 1753454975808,
      "payload": {
        "body": "do you know what the term encircle means? it means to surround from all sides, Russia has present on only 1 side, that's the opposite of an encirclement",
        "createdAt": "2025-07-25T14:49:35.801298Z",
        "id": "1763355",
        "parentCommentID": "1763325",
        "parentEntityID": 18396,
        "parentEntityType": "Event",
        "profile": {
          "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
          "displayUsernamePublic": true,
          "name": "salted.caramel",
          "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
          "pseudonym": "Adored-Disparity"
        },
        "reactionCount": 0,
        "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
        "reportCount": 0,
        "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
      }
    }
    

## 

​

Message Types

### 

​

comment_created

Triggered when a user creates a new comment on an event or in reply to another comment.

### 

​

comment_removed

Triggered when a comment is removed or deleted.

### 

​

reaction_created

Triggered when a user adds a reaction to an existing comment.

### 

​

reaction_removed

Triggered when a reaction is removed from a comment.

## 

​

Payload Fields

Field| Type| Description  
---|---|---  
`body`| string| The text content of the comment  
`createdAt`| string| ISO 8601 timestamp when the comment was created  
`id`| string| Unique identifier for this comment  
`parentCommentID`| string| ID of the parent comment if this is a reply (null for top-level comments)  
`parentEntityID`| number| ID of the parent entity (event, market, etc.)  
`parentEntityType`| string| Type of parent entity (e.g., “Event”, “Market”)  
`profile`| object| Profile information of the user who created the comment  
`reactionCount`| number| Current number of reactions on this comment  
`replyAddress`| string| Polygon address for replies (may be different from userAddress)  
`reportCount`| number| Current number of reports on this comment  
`userAddress`| string| Polygon address of the user who created the comment  
  
### 

​

Profile Object Fields

Field| Type| Description  
---|---|---  
`baseAddress`| string| User profile address  
`displayUsernamePublic`| boolean| Whether the username should be displayed publicly  
`name`| string| User’s display name  
`proxyWallet`| string| Proxy wallet address used for transactions  
`pseudonym`| string| Generated pseudonym for the user  
  
## 

​

Parent Entity Types

The following parent entity types are supported:

  * `Event` \- Comments on prediction events
  * `Market` \- Comments on specific markets
  * Additional entity types may be available



## 

​

Example Messages

### 

​

New Comment Created

Copy

Ask AI
    
    
    {
      "topic": "comments",
      "type": "comment_created",
      "timestamp": 1753454975808,
      "payload": {
        "body": "do you know what the term encircle means? it means to surround from all sides, Russia has present on only 1 side, that's the opposite of an encirclement",
        "createdAt": "2025-07-25T14:49:35.801298Z",
        "id": "1763355",
        "parentCommentID": "1763325",
        "parentEntityID": 18396,
        "parentEntityType": "Event",
        "profile": {
          "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
          "displayUsernamePublic": true,
          "name": "salted.caramel",
          "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
          "pseudonym": "Adored-Disparity"
        },
        "reactionCount": 0,
        "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
        "reportCount": 0,
        "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
      }
    }
    

### 

​

Reply to Existing Comment

Copy

Ask AI
    
    
    {
      "topic": "comments",
      "type": "comment_created",
      "timestamp": 1753454985123,
      "payload": {
        "body": "That's a good point about the definition of encirclement.",
        "createdAt": "2025-07-25T14:49:45.120000Z",
        "id": "1763356",
        "parentCommentID": "1763355",
        "parentEntityID": 18396,
        "parentEntityType": "Event",
        "profile": {
          "baseAddress": "0x1234567890abcdef1234567890abcdef12345678",
          "displayUsernamePublic": true,
          "name": "trader",
          "proxyWallet": "0x9876543210fedcba9876543210fedcba98765432",
          "pseudonym": "Bright-Analysis"
        },
        "reactionCount": 0,
        "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
        "reportCount": 0,
        "userAddress": "0x1234567890abcdef1234567890abcdef12345678"
      }
    }
    

## 

​

Comment Hierarchy

Comments support nested threading:

  * **Top-level comments** : `parentCommentID` is null or empty
  * **Reply comments** : `parentCommentID` contains the ID of the parent comment
  * All comments are associated with a `parentEntityID` and `parentEntityType`



## 

​

Use Cases

  * Real-time comment feed displays
  * Discussion thread monitoring
  * Community sentiment analysis



## 

​

Content

  * Comments include `reactionCount` and `reportCount`
  * Comment body contains the full text content



## 

​

Notes

  * The `createdAt` timestamp uses ISO 8601 format with timezone information
  * The outer `timestamp` field represents when the WebSocket message was sent
  * User profiles include both primary addresses and proxy wallet addresses



[RTDS Crypto Prices](/developers/RTDS/RTDS-crypto-prices)[Overview](/developers/gamma-markets-api/overview)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
