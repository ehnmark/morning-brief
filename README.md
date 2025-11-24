# Morning brief generator

This is a simple Python application that uses an Agent Framework to generate a morning brief about Japanese equities. It sources data from the Bank of Japan (BOJ), Japan Exchange Group (JPX), and NHK in a fan-out fashion, collates the results, and produces a Markdown report.

## How to run

- Make a Python 3.12 virtual environment and install PIP packages in `dependencies.txt`
- Copy `example.env` to `.env` and input your own project and deployment details
- Run `python main.py` inside the virtual environment


## Example

```bash
$ python main.py
2025-11-24T16:31:54 INFO Fetching RSS from https://news.web.nhk/n-data/conf/na/rss/cat5.xml
2025-11-24T16:31:55 INFO Fetching RSS from https://www.jpx.co.jp/rss/markets_news.xml
2025-11-24T16:31:56 INFO Fetching RSS from https://www.boj.or.jp/rss/whatsnew.xml
2025-11-24T16:31:56 INFO Will fetch https://www.jpx.co.jp/news/2040/20251121-01.html
2025-11-24T16:31:56 INFO Will fetch https://www.jpx.co.jp/equities/products/tpm/issues/index.html
2025-11-24T16:31:56 INFO Will fetch https://www.jpx.co.jp/equities/products/tpm/issues/index.html
2025-11-24T16:31:56 INFO Will fetch https://www.jpx.co.jp/listing/stocks/new/index.html
2025-11-24T16:31:56 INFO Will fetch https://www.jpx.co.jp/listing/stocks/new/index.html
2025-11-24T16:31:57 INFO Will fetch https://news.web.nhk/newsweb/na/na-k10014984571000
2025-11-24T16:31:57 INFO Will fetch https://news.web.nhk/newsweb/na/na-k10014983951000
2025-11-24T16:31:57 INFO Will fetch https://news.web.nhk/newsweb/na/na-k10014983651000
2025-11-24T16:31:57 INFO Will fetch https://news.web.nhk/newsweb/na/na-k10014983561000
2025-11-24T16:31:57 INFO Will fetch https://news.web.nhk/newsweb/na/na-k10014983571000
2025-11-24T16:31:57 INFO Will fetch http://www.boj.or.jp/mopo/mpmdeci/transparency/tra251121a.htm
2025-11-24T16:31:57 INFO Will fetch http://www.boj.or.jp/research/research_data/reri/index.htm
2025-11-24T16:31:57 INFO Will fetch http://www.boj.or.jp/research/imes/mes/mes_251120.htm
2025-11-24T16:31:57 INFO Will fetch http://www.boj.or.jp/about/press/koen_2025/ko251120a.htm
2025-11-24T16:31:57 INFO Will fetch http://www.boj.or.jp/about/services/tame/tame_rate/syorei/hou2512.htm
```

# Morning Brief: Japanese Equities – 24 November 2025

## Overall Summary
Today’s session hinges on policy communication clarity from Japan’s authorities, real trade data as a gauge of domestic and external demand, and near-term policy expectations. Key drivers to monitor include:

- How the government-Bank of Japan joint statement language may shift inflation-growth framing and influence market expectations for policy guidance.
- Real exports and imports trends as a forward-looking read on domestic demand and external demand, with implications for exporters and import-intensive sectors.
- A BoJ Policy Board member’s remarks on the economy and price trends, shaping near-term inflation expectations and monetary policy stance.
- Access to BoJ-endorsed macro insights from the English-language Monetary and Economic Studies to inform models and scenario planning.
- December rate signaling and related monetary operations, which can affect short-term money-market dynamics and policy transmission.
- Regulatory developments at CITES regarding Japanese eel, potentially affecting seafood/agribusiness equities and consumer-staples exposure.
- Derivative market activity on a holiday trading day (Nov 24), which can impact liquidity and hedging behavior.

Key takeaway: stay attuned to BoJ communications and data releases for any shifts in policy path, and adjust risk hedges around the session start and potential sector sensitivities (seafood, agribusiness, exporters).

## Key Points and Readings

- Policy coordination language corrections in the government-Bank of Japan joint statement: Signals how policymakers want to frame alignment on inflation and growth goals, potentially shaping market expectations for policy guidance. [Policy coordination language corrections in the government-Bank of Japan joint statement](http://www.boj.or.jp/mopo/mpmdeci/transparency/tra251121a.htm)

- Real exports and imports trends: Real exports and imports trends—key gauge of domestic demand and external demand. A sharper/weaker trend can influence growth prospects and the outlook for exporters and import-intensive sectors. [Real exports and imports trends](http://www.boj.or.jp/research/research_data/reri/index.htm)

- 【挨拶】小枝審議委員「わが国の経済・物価情勢と金融政策」(新潟): Speech by a BoJ Policy Board member on Japan’s economy and price trends and implications for monetary policy. May shape near-term expectations for inflation trajectory and policy stance. [Remarks by BoJ Policy Board Member Koeda on Japan’s Economy, Prices, and Monetary Policy (Niigata)](http://www.boj.or.jp/about/press/koen_2025/ko251120a.htm)

- 金融研究所 英文機関誌 Monetary and Economic Studies （第43巻）: BoJ Research Institute English-language journal issue. Provides macro insights and policy discussion that analysts may incorporate into models and scenario analyses. [Monetary and Economic Studies (Vol. 43)](http://www.boj.or.jp/research/imes/mes/mes_251120.htm)

- 報告省令レート（12月分）: December rate report/order reference—relevant for monetary operations and rate signaling. Could affect short-term money markets and policy transmission expectations. [December rate report](http://www.boj.or.jp/about/services/tame/tame_rate/syorei/hou2512.htm)

- ニホンウナギも輸出規制に？ワシントン条約 日本への影響は…: NHK reports that the Washington Convention (CITES) meeting opens on 24 Nov, with proposals to regulate species including the Japanese eel. Japan is lobbying to oppose these proposals. If adopted, eel prices could rise, impacting seafood/agribusiness equities and related consumer-staples stocks, making this a potential market-moving risk for Japanese equities on the session opening. (Date: 2025-11-24) [Japanese eel export restrictions under CITES: Japan’s position](https://news.web.nhk.jp/newsweb/na/na-k10014984571000)

- [OSE,TOCOM]デリバティブの祝日取引の実施について（2025年11月24日）: JPXが2025年11月24日にデリバティブ市場で祝日取引を実施することを発表。OSEとTOCOMの市場に影響を与え、流動性・清算スケジュール・ヘッジング動向に留意が必要。朝のブリーフ用に、取引時間の変動や価格動向の可能性を確認しておくと良い。 [Derivative holiday trading on November 24, 2025 (OSE/TOCOM)](https://www.jpx.co.jp/news/2040/20251121-01.html)
