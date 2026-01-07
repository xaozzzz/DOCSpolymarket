# Maker Rebates Program - Polymarket Documentation

Source: https://docs.polymarket.com/polymarket-learn/trading/maker-rebates-program

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Trading

Maker Rebates Program

[User Guide](/polymarket-learn/get-started/what-is-polymarket)[For Developers](/quickstart/overview)[Changelog](/changelog/changelog)

  * [Polymarket](https://polymarket.com)
  * [Discord Community](https://discord.gg/polymarket)
  * [Twitter](https://x.com/polymarket)



##### Get Started

  * [What is Polymarket?](/polymarket-learn/get-started/what-is-polymarket)
  * [How to Sign-Up](/polymarket-learn/get-started/how-to-signup)
  * [How to Deposit](/polymarket-learn/get-started/how-to-deposit)
  * [Making Your First Trade](/polymarket-learn/get-started/making-your-first-trade)



##### Deposits and Withdrawals

  * [Deposit by Transfering Crypto](/polymarket-learn/deposits/supported-tokens)
  * [Deposit with Coinbase](/polymarket-learn/deposits/coinbase)
  * [Deposit Using Your Card](/polymarket-learn/deposits/moonpay)
  * [Deposit USDC on Ethereum](/polymarket-learn/deposits/usdc-on-eth)
  * [Large Cross Chain Deposits](/polymarket-learn/deposits/large-cross-chain-deposits)
  * [How to Withdraw](/polymarket-learn/deposits/how-to-withdraw)



##### Markets

  * [How Are Markets Created?](/polymarket-learn/markets/how-are-markets-created)
  * [How Are Prices Calculated?](/polymarket-learn/trading/how-are-prices-calculated)
  * [How Are Prediction Markets Resolved?](/polymarket-learn/markets/how-are-markets-resolved)
  * [How Are Markets Clarified?](/polymarket-learn/markets/how-are-markets-clarified)
  * [How Are Markets Disputed?](/polymarket-learn/markets/dispute)



##### Trading

  * [Limit Orders](/polymarket-learn/trading/limit-orders)
  * [Market Orders](/polymarket-learn/trading/market-orders)
  * [Holding Rewards](/polymarket-learn/trading/holding-rewards)
  * [Liquidity Rewards](/polymarket-learn/trading/liquidity-rewards)
  * [Fees](/polymarket-learn/trading/fees)
  * [Maker Rebates Program](/polymarket-learn/trading/maker-rebates-program)
  * [Does Polymarket Have Trading Limits?](/polymarket-learn/trading/no-limits)
  * [Using the Order Book](/polymarket-learn/trading/using-the-orderbook)



##### FAQs

  * [Geographic Restrictions](/polymarket-learn/FAQ/geoblocking)
  * [How To Use Embeds](/polymarket-learn/FAQ/embeds)
  * [Polymarket vs. Polling](/polymarket-learn/FAQ/polling)
  * [Recover Missing Deposit](/polymarket-learn/FAQ/recover-missing-deposit)
  * [Can I Sell Early?](/polymarket-learn/FAQ/sell-early)
  * [Does Polymarket Have a Token?](/polymarket-learn/FAQ/wen-token)
  * [Does Polymarket have an API?](/polymarket-learn/FAQ/does-polymarket-have-an-api)
  * [How Do I Contact Support?](/polymarket-learn/FAQ/support)
  * [How Do I Export My Key?](/polymarket-learn/FAQ/how-to-export-private-key)
  * [Is My Money Safe?](/polymarket-learn/FAQ/is-my-money-safe)
  * [Is Polymarket The House?](/polymarket-learn/FAQ/is-polymarket-the-house)
  * [Why Crypto?](/polymarket-learn/FAQ/why-do-i-need-crypto)
  * [What is a Prediction Market?](/polymarket-learn/FAQ/what-are-prediction-markets)



On this page

  * Why Maker Rebates?
  * How Maker Rebates Work
  * Funding
  * Taker Fee Structure
  * How Fees Are Charged
  * Fee Amount vs Effective Rate
  * Buying Fees (100 shares)
  * Selling Fees (100 shares)
  * Fee Precision
  * FAQ
  * For API Users



Trading

# Maker Rebates Program

We’re rolling out **Maker Rebates** for **15-minute crypto markets** ; a program designed to make these fast-moving markets deeper, tighter, and easier to trade. Market makers who provide **active liquidity** (orders that get filled) earn **daily USDC rebates** , proportional to the liquidity they provide.

## 

​

Why Maker Rebates?

15-minute markets move quickly. When liquidity is deeper:

  * Spreads tend to be tighter
  * Price impact is lower
  * Fills are more reliable
  * Markets are more resilient during volatility

Maker Rebates incentivize **consistent, competitive quoting** so everyone gets a better trading experience.

## 

​

How Maker Rebates Work

  * **Paid daily in USDC:** Rebates are calculated and distributed every day.
  * **Performance-based:** You earn based on the share of liquidity you provided that actually got taken.



### 

​

Funding

Maker Rebates are funded by **taker fees collected in 15-minute crypto markets**. These fees are redistributed to makers who keep the markets liquid.

Polymarket collects taker fees **only** in 15-minute crypto markets. These fees are distributed as maker rebates.

## 

​

Taker Fee Structure

### 

​

How Fees Are Charged

Fees are deducted from the **proceeds** of your trade (what you receive):

Action| You Pay| You Receive| Fee Taken From  
---|---|---|---  
**BUY**|  USDC| Tokens| Tokens  
**SELL**|  Tokens| USDC| USDC  
  
Because fees are denominated differently for buys vs sells, **the effective fee percentage differs** even at the same price.

### 

​

Fee Amount vs Effective Rate

There’s an important distinction:

  * **Fee amount** (in units): Highest at 50% probability, lowest at extremes
  * **Effective fee rate** (as % of trade): Depends on whether you’re buying or selling

![Fee Curve](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/polymarket-learn/media/fee_image.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=5a4bdaf810ad1dafafd7c6f2be20719e)

The graph above shows the **fee amount** curve, which peaks at 50%. But the **effective percentage you pay** depends on whether you’re buying or selling — see the tables below.

### 

​

Buying Fees (100 shares)

When you **buy** , the fee is deducted in tokens. The effective rate peaks at 50% probability.

Price| Trade Cost| Fee (tokens)| Fee Value| Effective Rate  
---|---|---|---|---  
$0.10| $10| 0.20| $0.02| **0.2%**  
$0.20| $20| 0.64| $0.13| **0.6%**  
$0.30| $30| 1.10| $0.33| **1.1%**  
$0.40| $40| 1.44| $0.58| **1.4%**  
$0.50| $50| 1.56| $0.78| **1.6%**  
$0.60| $60| 1.44| $0.86| **1.4%**  
$0.70| $70| 1.10| $0.77| **1.1%**  
$0.80| $80| 0.64| $0.51| **0.6%**  
$0.90| $90| 0.20| $0.18| **0.2%**  
  
### 

​

Selling Fees (100 shares)

When you **sell** , the fee is deducted in USDC. The effective rate peaks around 30% probability.

Price| Proceeds| Fee (USDC)| Effective Rate  
---|---|---|---  
$0.10| $10| $0.20| **2.0%**  
$0.20| $20| $0.64| **3.2%**  
$0.30| $30| $1.10| **3.7%**  
$0.40| $40| $1.44| **3.6%**  
$0.50| $50| $1.56| **3.1%**  
$0.60| $60| $1.44| **2.4%**  
$0.70| $70| $1.10| **1.6%**  
$0.80| $80| $0.64| **0.8%**  
$0.90| $90| $0.20| **0.2%**  
  
**Why is selling more expensive?** When buying, the fee is valued at the token price (e.g., 1.56 tokens × 0.50=0.50 = 0.50=0.78). When selling, the fee is taken directly in USDC ($1.56). Same fee units, different dollar impact.

### 

​

Fee Precision

Fees are rounded to 4 decimal places. The smallest fee charged is **0.0001 USDC**. Anything smaller rounds to zero, so very small trades near the extremes may incur no fee at all.

## 

​

FAQ

How do I qualify for maker rebates?

Place orders that add liquidity to the book and get filled (i.e., your liquidity is taken by another trader).

When are rebates paid?

Daily, in USDC.

How are rebates calculated?

Rebates are proportional to your share of executed maker liquidity in each eligible market.

Where does the rebate pool come from?

Taker fees collected in eligible markets are allocated to the maker rebate pool and distributed daily.

Which markets have fees enabled?

Currently, only 15-minute crypto markets have taker fees enabled.

Is Polymarket charging fees on all markets?

No. Polymarket is collecting taker fees **only** on 15-minute crypto markets. All other markets remain fee-free.

Do makers earn less for trades at price extremes?

Yes. The rebate pool is funded by taker fees collected. Since taker fees are lower at price extremes, the rebate pool is smaller for those trades.

## 

​

For API Users

If you trade programmatically, you’ll need to update your client to handle fees correctly. ## [Developer Guide: Maker RebatesTechnical documentation for handling fees in your trading code](/developers/market-makers/maker-rebates-program)

[Fees](/polymarket-learn/trading/fees)[Does Polymarket Have Trading Limits?](/polymarket-learn/trading/no-limits)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
