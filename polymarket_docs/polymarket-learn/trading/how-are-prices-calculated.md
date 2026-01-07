# How Are Prices Calculated? - Polymarket Documentation

Source: https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated

Skip to main content

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](/)

Search...

⌘KAsk AI

  * [Main Site](https://polymarket.com)
  * [Main Site](https://polymarket.com)



Search...

Navigation

Markets

How Are Prices Calculated?

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

  * Initial Price
  * Future Price
  * Prices = Probabilities



Markets

# How Are Prices Calculated?

The prices probabilities displayed on Polymarket are the midpoint of the bid-ask spread in the orderbook.

## 

​

Initial Price

  * When a market is created, there are initially zero shares and no pre-defined prices or odds.
  * Market makers (a fancy term for traders placing limit orders) interested in buying YES or NO shares can place [Limit Orders](../trading/limit-orders) at the price they’re willing to pay
  * When offers for the YES and NO side equal $1.00, the order is “matched” and that $1.00 is converted into 1 YES and 1 NO share, each going to their respective buyers.

For example, if you place a limit order at $0.60 for YES, that order is matched when someone places a NO order at $0.40. _This becomes the initial market price._

## 

​

Future Price

The prices displayed on Polymarket are the midpoint of the bid-ask spread in the orderbook — unless that spread is over $0.10, in which case the last traded price is used. Like the stock market, prices on Polymarket are a function of realtime supply & demand.

### 

​

Prices = Probabilities

In the market below, the probability of 37% is the midpoint between the 34¢ bid and 40¢ ask. If the bid-ask spread is wider than 10¢, the probability is shown as the last traded price.

![](https://polymarket-upload.s3.us-east-2.amazonaws.com/how_are_prices_calculated.png)

You may not be able to buy shares at the displayed probability / price because there is a bid-ask spread. In the above example, a trader wanting to buy shares would pay 40¢ for up to 4,200 shares, after which the price would rise to 43¢.

[How Are Markets Created?](/polymarket-learn/markets/how-are-markets-created)[How Are Prediction Markets Resolved?](/polymarket-learn/markets/how-are-markets-resolved)

⌘I

[github](https://github.com/polymarket)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=polymarket-292d1b1b)
