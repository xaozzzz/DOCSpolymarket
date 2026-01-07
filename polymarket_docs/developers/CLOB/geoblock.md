# Geographic Restrictions - Polymarket Documentation

Source: https://docs.polymarket.com/developers/CLOB/geoblock

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Central Limit Order Book

Geographic Restrictions

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
  * Server Infrastructure
  * Geoblock Endpoint
  * Response
  * Blocked Countries
  * Blocked Regions
  * Usage Examples



Central Limit Order Book

# Geographic Restrictions

Check geographic restrictions before placing orders on Polymarket’s CLOB

## 

​

Overview

Polymarket restricts order placement from certain geographic locations due to regulatory requirements and compliance with international sanctions. Before placing orders, builders should verify the location.

Orders submitted from blocked regions will be rejected. Implement geoblock checks in your application to provide users with appropriate feedback before they attempt to trade.

* * *

## 

​

Server Infrastructure

  * **Primary Servers** : eu-west-2
  * **Closest Non-Georestricted Region** : eu-west-1



* * *

## 

​

Geoblock Endpoint

Check the geographic eligibility of the requesting IP address:

Copy

Ask AI
    
    
    GET https://polymarket.com/api/geoblock
    

### 

​

Response

Copy

Ask AI
    
    
    {
      "blocked": boolean;
      "ip": string;
      "country": string;
      "region": string;
    }
    

Field| Type| Description  
---|---|---  
`blocked`| boolean| Whether the user is blocked from placing orders  
`ip`| string| Detected IP address  
`country`| string| ISO 3166-1 alpha-2 country code  
`region`| string| Region/state code  
  
* * *

## 

​

Blocked Countries

The following **33 countries** are completely restricted from placing orders on Polymarket:

Country Code| Country Name  
---|---  
AU| Australia  
BE| Belgium  
BY| Belarus  
BI| Burundi  
CF| Central African Republic  
CD| Congo (Kinshasa)  
CU| Cuba  
DE| Germany  
ET| Ethiopia  
FR| France  
GB| United Kingdom  
IR| Iran  
IQ| Iraq  
IT| Italy  
KP| North Korea  
LB| Lebanon  
LY| Libya  
MM| Myanmar  
NI| Nicaragua  
PL| Poland  
RU| Russia  
SG| Singapore  
SO| Somalia  
SS| South Sudan  
SD| Sudan  
SY| Syria  
TH| Thailand  
TW| Taiwan  
UM| United States Minor Outlying Islands  
US| United States  
VE| Venezuela  
YE| Yemen  
ZW| Zimbabwe  
  
* * *

## 

​

Blocked Regions

In addition to fully blocked countries, the following specific regions within otherwise accessible countries are also restricted:

Country| Region| Region Code  
---|---|---  
Canada (CA)| Ontario| ON  
Ukraine (UA)| Crimea| 43  
Ukraine (UA)| Donetsk| 14  
Ukraine (UA)| Luhansk| 09  
  
* * *

## 

​

Usage Examples

  * TypeScript

  * Python




Copy

Ask AI
    
    
    interface GeoblockResponse {
      blocked: boolean;
      ip: string;
      country: string;
      region: string;
    }
    
    async function checkGeoblock(): Promise<GeoblockResponse> {
      const response = await fetch("https://polymarket.com/api/geoblock");
      return response.json();
    }
    
    // Usage
    const geo = await checkGeoblock();
    
    if (geo.blocked) {
      console.log(`Trading not available in ${geo.country}`);
    } else {
      console.log("Trading available");
    }
    

Copy

Ask AI
    
    
    import requests
    
    def check_geoblock() -> dict:
        response = requests.get("https://polymarket.com/api/geoblock")
        return response.json()
    
    # Usage
    geo = check_geoblock()
    
    if geo["blocked"]:
        print(f"Trading not available in {geo['country']}")
    else:
        print("Trading available")
    

[Authentication](/developers/CLOB/authentication)[Methods Overview](/developers/CLOB/clients/methods-overview)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
