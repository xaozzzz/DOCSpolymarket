# Get market by id - Polymarket Documentation

Source: https://docs.polymarket.com/api-reference/markets/get-market-by-id

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Markets

Get market by id

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

    * [GETList markets](/api-reference/markets/list-markets)
    * [GETGet market by id](/api-reference/markets/get-market-by-id)
    * [GETGet market tags by id](/api-reference/markets/get-market-tags-by-id)
    * [GETGet market by slug](/api-reference/markets/get-market-by-slug)
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



Get market by id

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://gamma-api.polymarket.com/markets/{id}

200

Copy

Ask AI
    
    
    {
      "id": "<string>",
      "question": "<string>",
      "conditionId": "<string>",
      "slug": "<string>",
      "twitterCardImage": "<string>",
      "resolutionSource": "<string>",
      "endDate": "2023-11-07T05:31:56Z",
      "category": "<string>",
      "ammType": "<string>",
      "liquidity": "<string>",
      "sponsorName": "<string>",
      "sponsorImage": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "xAxisValue": "<string>",
      "yAxisValue": "<string>",
      "denominationToken": "<string>",
      "fee": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "lowerBound": "<string>",
      "upperBound": "<string>",
      "description": "<string>",
      "outcomes": "<string>",
      "outcomePrices": "<string>",
      "volume": "<string>",
      "active": true,
      "marketType": "<string>",
      "formatType": "<string>",
      "lowerBoundDate": "<string>",
      "upperBoundDate": "<string>",
      "closed": true,
      "marketMakerAddress": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "closedTime": "<string>",
      "wideFormat": true,
      "new": true,
      "mailchimpTag": "<string>",
      "featured": true,
      "archived": true,
      "resolvedBy": "<string>",
      "restricted": true,
      "marketGroup": 123,
      "groupItemTitle": "<string>",
      "groupItemThreshold": "<string>",
      "questionID": "<string>",
      "umaEndDate": "<string>",
      "enableOrderBook": true,
      "orderPriceMinTickSize": 123,
      "orderMinSize": 123,
      "umaResolutionStatus": "<string>",
      "curationOrder": 123,
      "volumeNum": 123,
      "liquidityNum": 123,
      "endDateIso": "<string>",
      "startDateIso": "<string>",
      "umaEndDateIso": "<string>",
      "hasReviewedDates": true,
      "readyForCron": true,
      "commentsEnabled": true,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "gameStartTime": "<string>",
      "secondsDelay": 123,
      "clobTokenIds": "<string>",
      "disqusThread": "<string>",
      "shortOutcomes": "<string>",
      "teamAID": "<string>",
      "teamBID": "<string>",
      "umaBond": "<string>",
      "umaReward": "<string>",
      "fpmmLive": true,
      "volume24hrAmm": 123,
      "volume1wkAmm": 123,
      "volume1moAmm": 123,
      "volume1yrAmm": 123,
      "volume24hrClob": 123,
      "volume1wkClob": 123,
      "volume1moClob": 123,
      "volume1yrClob": 123,
      "volumeAmm": 123,
      "volumeClob": 123,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "makerBaseFee": 123,
      "takerBaseFee": 123,
      "customLiveness": 123,
      "acceptingOrders": true,
      "notificationsEnabled": true,
      "score": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "events": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "startDate": "2023-11-07T05:31:56Z",
          "creationDate": "2023-11-07T05:31:56Z",
          "endDate": "2023-11-07T05:31:56Z",
          "image": "<string>",
          "icon": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "liquidity": 123,
          "volume": 123,
          "openInterest": 123,
          "sortBy": "<string>",
          "category": "<string>",
          "subcategory": "<string>",
          "isTemplate": true,
          "templateVariables": "<string>",
          "published_at": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "competitive": 123,
          "volume24hr": 123,
          "volume1wk": 123,
          "volume1mo": 123,
          "volume1yr": 123,
          "featuredImage": "<string>",
          "disqusThread": "<string>",
          "parentEvent": "<string>",
          "enableOrderBook": true,
          "liquidityAmm": 123,
          "liquidityClob": 123,
          "negRisk": true,
          "negRiskMarketID": "<string>",
          "negRiskFeeBips": 123,
          "commentCount": 123,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "featuredImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "subEvents": [
            "<string>"
          ],
          "markets": "<array>",
          "series": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "seriesType": "<string>",
              "recurrence": "<string>",
              "description": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": true,
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "competitive": "<string>",
              "volume24hr": 123,
              "volume": 123,
              "liquidity": 123,
              "startDate": "2023-11-07T05:31:56Z",
              "pythTokenID": "<string>",
              "cgAssetName": "<string>",
              "score": 123,
              "events": "<array>",
              "collections": [
                {
                  "id": "<string>",
                  "ticker": "<string>",
                  "slug": "<string>",
                  "title": "<string>",
                  "subtitle": "<string>",
                  "collectionType": "<string>",
                  "description": "<string>",
                  "tags": "<string>",
                  "image": "<string>",
                  "icon": "<string>",
                  "headerImage": "<string>",
                  "layout": "<string>",
                  "active": true,
                  "closed": true,
                  "archived": true,
                  "new": true,
                  "featured": true,
                  "restricted": true,
                  "isTemplate": true,
                  "templateVariables": "<string>",
                  "publishedAt": "<string>",
                  "createdBy": "<string>",
                  "updatedBy": "<string>",
                  "createdAt": "2023-11-07T05:31:56Z",
                  "updatedAt": "2023-11-07T05:31:56Z",
                  "commentsEnabled": true,
                  "imageOptimized": {
                    "id": "<string>",
                    "imageUrlSource": "<string>",
                    "imageUrlOptimized": "<string>",
                    "imageSizeKbSource": 123,
                    "imageSizeKbOptimized": 123,
                    "imageOptimizedComplete": true,
                    "imageOptimizedLastUpdated": "<string>",
                    "relID": 123,
                    "field": "<string>",
                    "relname": "<string>"
                  },
                  "iconOptimized": {
                    "id": "<string>",
                    "imageUrlSource": "<string>",
                    "imageUrlOptimized": "<string>",
                    "imageSizeKbSource": 123,
                    "imageSizeKbOptimized": 123,
                    "imageOptimizedComplete": true,
                    "imageOptimizedLastUpdated": "<string>",
                    "relID": 123,
                    "field": "<string>",
                    "relname": "<string>"
                  },
                  "headerImageOptimized": {
                    "id": "<string>",
                    "imageUrlSource": "<string>",
                    "imageUrlOptimized": "<string>",
                    "imageSizeKbSource": 123,
                    "imageSizeKbOptimized": 123,
                    "imageOptimizedComplete": true,
                    "imageOptimizedLastUpdated": "<string>",
                    "relID": 123,
                    "field": "<string>",
                    "relname": "<string>"
                  }
                }
              ],
              "categories": [
                {
                  "id": "<string>",
                  "label": "<string>",
                  "parentCategory": "<string>",
                  "slug": "<string>",
                  "publishedAt": "<string>",
                  "createdBy": "<string>",
                  "updatedBy": "<string>",
                  "createdAt": "2023-11-07T05:31:56Z",
                  "updatedAt": "2023-11-07T05:31:56Z"
                }
              ],
              "tags": [
                {
                  "id": "<string>",
                  "label": "<string>",
                  "slug": "<string>",
                  "forceShow": true,
                  "publishedAt": "<string>",
                  "createdBy": 123,
                  "updatedBy": 123,
                  "createdAt": "2023-11-07T05:31:56Z",
                  "updatedAt": "2023-11-07T05:31:56Z",
                  "forceHide": true,
                  "isCarousel": true
                }
              ],
              "commentCount": 123,
              "chats": [
                {
                  "id": "<string>",
                  "channelId": "<string>",
                  "channelName": "<string>",
                  "channelImage": "<string>",
                  "live": true,
                  "startTime": "2023-11-07T05:31:56Z",
                  "endTime": "2023-11-07T05:31:56Z"
                }
              ]
            }
          ],
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "collections": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "collectionType": "<string>",
              "description": "<string>",
              "tags": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "headerImage": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "imageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "iconOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "headerImageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              }
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "cyom": true,
          "closedTime": "2023-11-07T05:31:56Z",
          "showAllOutcomes": true,
          "showMarketImages": true,
          "automaticallyResolved": true,
          "enableNegRisk": true,
          "automaticallyActive": true,
          "eventDate": "<string>",
          "startTime": "2023-11-07T05:31:56Z",
          "eventWeek": 123,
          "seriesSlug": "<string>",
          "score": "<string>",
          "elapsed": "<string>",
          "period": "<string>",
          "live": true,
          "ended": true,
          "finishedTimestamp": "2023-11-07T05:31:56Z",
          "gmpChartMode": "<string>",
          "eventCreators": [
            {
              "id": "<string>",
              "creatorName": "<string>",
              "creatorHandle": "<string>",
              "creatorUrl": "<string>",
              "creatorImage": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tweetCount": 123,
          "chats": [
            {
              "id": "<string>",
              "channelId": "<string>",
              "channelName": "<string>",
              "channelImage": "<string>",
              "live": true,
              "startTime": "2023-11-07T05:31:56Z",
              "endTime": "2023-11-07T05:31:56Z"
            }
          ],
          "featuredOrder": 123,
          "estimateValue": true,
          "cantEstimate": true,
          "estimatedValue": "<string>",
          "templates": [
            {
              "id": "<string>",
              "eventTitle": "<string>",
              "eventSlug": "<string>",
              "eventImage": "<string>",
              "marketTitle": "<string>",
              "description": "<string>",
              "resolutionSource": "<string>",
              "negRisk": true,
              "sortBy": "<string>",
              "showMarketImages": true,
              "seriesSlug": "<string>",
              "outcomes": "<string>"
            }
          ],
          "spreadsMainLine": 123,
          "totalsMainLine": 123,
          "carouselMap": "<string>",
          "pendingDeployment": true,
          "deploying": true,
          "deployingTimestamp": "2023-11-07T05:31:56Z",
          "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
          "gameStatus": "<string>"
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "creator": "<string>",
      "ready": true,
      "funded": true,
      "pastSlugs": "<string>",
      "readyTimestamp": "2023-11-07T05:31:56Z",
      "fundedTimestamp": "2023-11-07T05:31:56Z",
      "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
      "competitive": 123,
      "rewardsMinSize": 123,
      "rewardsMaxSpread": 123,
      "spread": 123,
      "automaticallyResolved": true,
      "oneDayPriceChange": 123,
      "oneHourPriceChange": 123,
      "oneWeekPriceChange": 123,
      "oneMonthPriceChange": 123,
      "oneYearPriceChange": 123,
      "lastTradePrice": 123,
      "bestBid": 123,
      "bestAsk": 123,
      "automaticallyActive": true,
      "clearBookOnStart": true,
      "chartColor": "<string>",
      "seriesColor": "<string>",
      "showGmpSeries": true,
      "showGmpOutcome": true,
      "manualActivation": true,
      "negRiskOther": true,
      "gameId": "<string>",
      "groupItemRange": "<string>",
      "sportsMarketType": "<string>",
      "line": 123,
      "umaResolutionStatuses": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "rfqEnabled": true,
      "eventStartTime": "2023-11-07T05:31:56Z"
    }

Markets

# Get market by id

GET

/

markets

/

{id}

Try it

Get market by id

cURL

Copy

Ask AI
    
    
    curl --request GET \
      --url https://gamma-api.polymarket.com/markets/{id}

200

Copy

Ask AI
    
    
    {
      "id": "<string>",
      "question": "<string>",
      "conditionId": "<string>",
      "slug": "<string>",
      "twitterCardImage": "<string>",
      "resolutionSource": "<string>",
      "endDate": "2023-11-07T05:31:56Z",
      "category": "<string>",
      "ammType": "<string>",
      "liquidity": "<string>",
      "sponsorName": "<string>",
      "sponsorImage": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "xAxisValue": "<string>",
      "yAxisValue": "<string>",
      "denominationToken": "<string>",
      "fee": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "lowerBound": "<string>",
      "upperBound": "<string>",
      "description": "<string>",
      "outcomes": "<string>",
      "outcomePrices": "<string>",
      "volume": "<string>",
      "active": true,
      "marketType": "<string>",
      "formatType": "<string>",
      "lowerBoundDate": "<string>",
      "upperBoundDate": "<string>",
      "closed": true,
      "marketMakerAddress": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "closedTime": "<string>",
      "wideFormat": true,
      "new": true,
      "mailchimpTag": "<string>",
      "featured": true,
      "archived": true,
      "resolvedBy": "<string>",
      "restricted": true,
      "marketGroup": 123,
      "groupItemTitle": "<string>",
      "groupItemThreshold": "<string>",
      "questionID": "<string>",
      "umaEndDate": "<string>",
      "enableOrderBook": true,
      "orderPriceMinTickSize": 123,
      "orderMinSize": 123,
      "umaResolutionStatus": "<string>",
      "curationOrder": 123,
      "volumeNum": 123,
      "liquidityNum": 123,
      "endDateIso": "<string>",
      "startDateIso": "<string>",
      "umaEndDateIso": "<string>",
      "hasReviewedDates": true,
      "readyForCron": true,
      "commentsEnabled": true,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "gameStartTime": "<string>",
      "secondsDelay": 123,
      "clobTokenIds": "<string>",
      "disqusThread": "<string>",
      "shortOutcomes": "<string>",
      "teamAID": "<string>",
      "teamBID": "<string>",
      "umaBond": "<string>",
      "umaReward": "<string>",
      "fpmmLive": true,
      "volume24hrAmm": 123,
      "volume1wkAmm": 123,
      "volume1moAmm": 123,
      "volume1yrAmm": 123,
      "volume24hrClob": 123,
      "volume1wkClob": 123,
      "volume1moClob": 123,
      "volume1yrClob": 123,
      "volumeAmm": 123,
      "volumeClob": 123,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "makerBaseFee": 123,
      "takerBaseFee": 123,
      "customLiveness": 123,
      "acceptingOrders": true,
      "notificationsEnabled": true,
      "score": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "events": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "startDate": "2023-11-07T05:31:56Z",
          "creationDate": "2023-11-07T05:31:56Z",
          "endDate": "2023-11-07T05:31:56Z",
          "image": "<string>",
          "icon": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "liquidity": 123,
          "volume": 123,
          "openInterest": 123,
          "sortBy": "<string>",
          "category": "<string>",
          "subcategory": "<string>",
          "isTemplate": true,
          "templateVariables": "<string>",
          "published_at": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "competitive": 123,
          "volume24hr": 123,
          "volume1wk": 123,
          "volume1mo": 123,
          "volume1yr": 123,
          "featuredImage": "<string>",
          "disqusThread": "<string>",
          "parentEvent": "<string>",
          "enableOrderBook": true,
          "liquidityAmm": 123,
          "liquidityClob": 123,
          "negRisk": true,
          "negRiskMarketID": "<string>",
          "negRiskFeeBips": 123,
          "commentCount": 123,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "featuredImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "subEvents": [
            "<string>"
          ],
          "markets": "<array>",
          "series": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "seriesType": "<string>",
              "recurrence": "<string>",
              "description": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": true,
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "competitive": "<string>",
              "volume24hr": 123,
              "volume": 123,
              "liquidity": 123,
              "startDate": "2023-11-07T05:31:56Z",
              "pythTokenID": "<string>",
              "cgAssetName": "<string>",
              "score": 123,
              "events": "<array>",
              "collections": [
                {
                  "id": "<string>",
                  "ticker": "<string>",
                  "slug": "<string>",
                  "title": "<string>",
                  "subtitle": "<string>",
                  "collectionType": "<string>",
                  "description": "<string>",
                  "tags": "<string>",
                  "image": "<string>",
                  "icon": "<string>",
                  "headerImage": "<string>",
                  "layout": "<string>",
                  "active": true,
                  "closed": true,
                  "archived": true,
                  "new": true,
                  "featured": true,
                  "restricted": true,
                  "isTemplate": true,
                  "templateVariables": "<string>",
                  "publishedAt": "<string>",
                  "createdBy": "<string>",
                  "updatedBy": "<string>",
                  "createdAt": "2023-11-07T05:31:56Z",
                  "updatedAt": "2023-11-07T05:31:56Z",
                  "commentsEnabled": true,
                  "imageOptimized": {
                    "id": "<string>",
                    "imageUrlSource": "<string>",
                    "imageUrlOptimized": "<string>",
                    "imageSizeKbSource": 123,
                    "imageSizeKbOptimized": 123,
                    "imageOptimizedComplete": true,
                    "imageOptimizedLastUpdated": "<string>",
                    "relID": 123,
                    "field": "<string>",
                    "relname": "<string>"
                  },
                  "iconOptimized": {
                    "id": "<string>",
                    "imageUrlSource": "<string>",
                    "imageUrlOptimized": "<string>",
                    "imageSizeKbSource": 123,
                    "imageSizeKbOptimized": 123,
                    "imageOptimizedComplete": true,
                    "imageOptimizedLastUpdated": "<string>",
                    "relID": 123,
                    "field": "<string>",
                    "relname": "<string>"
                  },
                  "headerImageOptimized": {
                    "id": "<string>",
                    "imageUrlSource": "<string>",
                    "imageUrlOptimized": "<string>",
                    "imageSizeKbSource": 123,
                    "imageSizeKbOptimized": 123,
                    "imageOptimizedComplete": true,
                    "imageOptimizedLastUpdated": "<string>",
                    "relID": 123,
                    "field": "<string>",
                    "relname": "<string>"
                  }
                }
              ],
              "categories": [
                {
                  "id": "<string>",
                  "label": "<string>",
                  "parentCategory": "<string>",
                  "slug": "<string>",
                  "publishedAt": "<string>",
                  "createdBy": "<string>",
                  "updatedBy": "<string>",
                  "createdAt": "2023-11-07T05:31:56Z",
                  "updatedAt": "2023-11-07T05:31:56Z"
                }
              ],
              "tags": [
                {
                  "id": "<string>",
                  "label": "<string>",
                  "slug": "<string>",
                  "forceShow": true,
                  "publishedAt": "<string>",
                  "createdBy": 123,
                  "updatedBy": 123,
                  "createdAt": "2023-11-07T05:31:56Z",
                  "updatedAt": "2023-11-07T05:31:56Z",
                  "forceHide": true,
                  "isCarousel": true
                }
              ],
              "commentCount": 123,
              "chats": [
                {
                  "id": "<string>",
                  "channelId": "<string>",
                  "channelName": "<string>",
                  "channelImage": "<string>",
                  "live": true,
                  "startTime": "2023-11-07T05:31:56Z",
                  "endTime": "2023-11-07T05:31:56Z"
                }
              ]
            }
          ],
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "collections": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "collectionType": "<string>",
              "description": "<string>",
              "tags": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "headerImage": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "imageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "iconOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "headerImageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              }
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "cyom": true,
          "closedTime": "2023-11-07T05:31:56Z",
          "showAllOutcomes": true,
          "showMarketImages": true,
          "automaticallyResolved": true,
          "enableNegRisk": true,
          "automaticallyActive": true,
          "eventDate": "<string>",
          "startTime": "2023-11-07T05:31:56Z",
          "eventWeek": 123,
          "seriesSlug": "<string>",
          "score": "<string>",
          "elapsed": "<string>",
          "period": "<string>",
          "live": true,
          "ended": true,
          "finishedTimestamp": "2023-11-07T05:31:56Z",
          "gmpChartMode": "<string>",
          "eventCreators": [
            {
              "id": "<string>",
              "creatorName": "<string>",
              "creatorHandle": "<string>",
              "creatorUrl": "<string>",
              "creatorImage": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tweetCount": 123,
          "chats": [
            {
              "id": "<string>",
              "channelId": "<string>",
              "channelName": "<string>",
              "channelImage": "<string>",
              "live": true,
              "startTime": "2023-11-07T05:31:56Z",
              "endTime": "2023-11-07T05:31:56Z"
            }
          ],
          "featuredOrder": 123,
          "estimateValue": true,
          "cantEstimate": true,
          "estimatedValue": "<string>",
          "templates": [
            {
              "id": "<string>",
              "eventTitle": "<string>",
              "eventSlug": "<string>",
              "eventImage": "<string>",
              "marketTitle": "<string>",
              "description": "<string>",
              "resolutionSource": "<string>",
              "negRisk": true,
              "sortBy": "<string>",
              "showMarketImages": true,
              "seriesSlug": "<string>",
              "outcomes": "<string>"
            }
          ],
          "spreadsMainLine": 123,
          "totalsMainLine": 123,
          "carouselMap": "<string>",
          "pendingDeployment": true,
          "deploying": true,
          "deployingTimestamp": "2023-11-07T05:31:56Z",
          "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
          "gameStatus": "<string>"
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "creator": "<string>",
      "ready": true,
      "funded": true,
      "pastSlugs": "<string>",
      "readyTimestamp": "2023-11-07T05:31:56Z",
      "fundedTimestamp": "2023-11-07T05:31:56Z",
      "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
      "competitive": 123,
      "rewardsMinSize": 123,
      "rewardsMaxSpread": 123,
      "spread": 123,
      "automaticallyResolved": true,
      "oneDayPriceChange": 123,
      "oneHourPriceChange": 123,
      "oneWeekPriceChange": 123,
      "oneMonthPriceChange": 123,
      "oneYearPriceChange": 123,
      "lastTradePrice": 123,
      "bestBid": 123,
      "bestAsk": 123,
      "automaticallyActive": true,
      "clearBookOnStart": true,
      "chartColor": "<string>",
      "seriesColor": "<string>",
      "showGmpSeries": true,
      "showGmpOutcome": true,
      "manualActivation": true,
      "negRiskOther": true,
      "gameId": "<string>",
      "groupItemRange": "<string>",
      "sportsMarketType": "<string>",
      "line": 123,
      "umaResolutionStatuses": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "rfqEnabled": true,
      "eventStartTime": "2023-11-07T05:31:56Z"
    }

#### Path Parameters

​

id

integer

required

#### Query Parameters

​

include_tag

boolean

#### Response

200

application/json

Market

​

id

string

​

question

string | null

​

conditionId

string

​

slug

string | null

​

twitterCardImage

string | null

​

resolutionSource

string | null

​

endDate

string<date-time> | null

​

category

string | null

​

ammType

string | null

​

liquidity

string | null

​

sponsorName

string | null

​

sponsorImage

string | null

​

startDate

string<date-time> | null

​

xAxisValue

string | null

​

yAxisValue

string | null

​

denominationToken

string | null

​

fee

string | null

​

image

string | null

​

icon

string | null

​

lowerBound

string | null

​

upperBound

string | null

​

description

string | null

​

outcomes

string | null

​

outcomePrices

string | null

​

volume

string | null

​

active

boolean | null

​

marketType

string | null

​

formatType

string | null

​

lowerBoundDate

string | null

​

upperBoundDate

string | null

​

closed

boolean | null

​

marketMakerAddress

string

​

createdBy

integer | null

​

updatedBy

integer | null

​

createdAt

string<date-time> | null

​

updatedAt

string<date-time> | null

​

closedTime

string | null

​

wideFormat

boolean | null

​

new

boolean | null

​

mailchimpTag

string | null

​

featured

boolean | null

​

archived

boolean | null

​

resolvedBy

string | null

​

restricted

boolean | null

​

marketGroup

integer | null

​

groupItemTitle

string | null

​

groupItemThreshold

string | null

​

questionID

string | null

​

umaEndDate

string | null

​

enableOrderBook

boolean | null

​

orderPriceMinTickSize

number | null

​

orderMinSize

number | null

​

umaResolutionStatus

string | null

​

curationOrder

integer | null

​

volumeNum

number | null

​

liquidityNum

number | null

​

endDateIso

string | null

​

startDateIso

string | null

​

umaEndDateIso

string | null

​

hasReviewedDates

boolean | null

​

readyForCron

boolean | null

​

commentsEnabled

boolean | null

​

volume24hr

number | null

​

volume1wk

number | null

​

volume1mo

number | null

​

volume1yr

number | null

​

gameStartTime

string | null

​

secondsDelay

integer | null

​

clobTokenIds

string | null

​

disqusThread

string | null

​

shortOutcomes

string | null

​

teamAID

string | null

​

teamBID

string | null

​

umaBond

string | null

​

umaReward

string | null

​

fpmmLive

boolean | null

​

volume24hrAmm

number | null

​

volume1wkAmm

number | null

​

volume1moAmm

number | null

​

volume1yrAmm

number | null

​

volume24hrClob

number | null

​

volume1wkClob

number | null

​

volume1moClob

number | null

​

volume1yrClob

number | null

​

volumeAmm

number | null

​

volumeClob

number | null

​

liquidityAmm

number | null

​

liquidityClob

number | null

​

makerBaseFee

integer | null

​

takerBaseFee

integer | null

​

customLiveness

integer | null

​

acceptingOrders

boolean | null

​

notificationsEnabled

boolean | null

​

score

integer | null

​

imageOptimized

object

Show child attributes

​

iconOptimized

object

Show child attributes

​

events

object[]

Show child attributes

​

categories

object[]

Show child attributes

​

tags

object[]

Show child attributes

​

creator

string | null

​

ready

boolean | null

​

funded

boolean | null

​

pastSlugs

string | null

​

readyTimestamp

string<date-time> | null

​

fundedTimestamp

string<date-time> | null

​

acceptingOrdersTimestamp

string<date-time> | null

​

competitive

number | null

​

rewardsMinSize

number | null

​

rewardsMaxSpread

number | null

​

spread

number | null

​

automaticallyResolved

boolean | null

​

oneDayPriceChange

number | null

​

oneHourPriceChange

number | null

​

oneWeekPriceChange

number | null

​

oneMonthPriceChange

number | null

​

oneYearPriceChange

number | null

​

lastTradePrice

number | null

​

bestBid

number | null

​

bestAsk

number | null

​

automaticallyActive

boolean | null

​

clearBookOnStart

boolean | null

​

chartColor

string | null

​

seriesColor

string | null

​

showGmpSeries

boolean | null

​

showGmpOutcome

boolean | null

​

manualActivation

boolean | null

​

negRiskOther

boolean | null

​

gameId

string | null

​

groupItemRange

string | null

​

sportsMarketType

string | null

​

line

number | null

​

umaResolutionStatuses

string | null

​

pendingDeployment

boolean | null

​

deploying

boolean | null

​

deployingTimestamp

string<date-time> | null

​

scheduledDeploymentTimestamp

string<date-time> | null

​

rfqEnabled

boolean | null

​

eventStartTime

string<date-time> | null

[List markets](/api-reference/markets/list-markets)[Get market tags by id](/api-reference/markets/get-market-tags-by-id)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
