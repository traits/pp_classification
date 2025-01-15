# pp_classification

Classification handling in [Portfolio Performance](https://github.com/buchen/portfolio). See also:
  - [Forum Discussion (deutsch)](https://forum.portfolio-performance.info/t/automatische-erstellung-von-klassifizierungen/2969)
  - [Similar PP issue](https://github.com/buchen/portfolio/issues/1665)
  - [etf-classification-pp (github)](https://github.com/fbuchinger/etf-classification-pp)


## Dependencies
- pandas
- matplotlib


## Data Sources
- [GICS vs. ICB Stock Classification: What's the Difference?](https://www.investopedia.com/articles/stocks/08/global-industry-classification-industrial-classification-benchmark.asp)

### Classifications

#### ICB
  - [Wikipedia](https://en.wikipedia.org/wiki/Industry_Classification_Benchmark) 
  - [FTSE Russell - Industry Classification Benchmark](https://www.ftserussell.com/data/industry-classification-benchmark-icb)
    - [Codes (Excel File)](https://www.ftserussell.com/files/support-document/icb-codes-descriptions)
    - [Structure (Excel File)](https://www.ftserussell.com/files/support-document/icb-structure-definitions)
#### GICS
  - [Wikipedia](https://en.wikipedia.org/wiki/Global_Industry_Classification_Standard) 
  - [MSCI - The Global Industry Classification Standard](https://www.msci.com/our-solutions/indexes/gics)
    - [GICS structure & sub-industry definitions (Excel File)](https://www.msci.com/documents/1296102/11185224/GICS_map+2018.xlsx/)
    - The site also hosts Excelified translations (e.g in [German](https://www.msci.com/documents/1296102/11185315/GICS_map+2018_German.xlsx))

### Indexes & Derived Instruments

#### Indexes
- MSCI
  - [Where to get MSCI World Index constituents](https://quant.stackexchange.com/questions/47142/where-to-get-msci-world-index-constituents-weights)
  - [Equity Index Constituents (msci.com)](https://www.msci.com/constituents)

#### ETF Examples
- IE00BK5BQT80 - Vanguard FTSE All-World
  - [deutsch](https://www.de.vanguard/professionell/anlageprodukte/etf/aktien/9679/ftse-all-world-ucits-etf-usd-accumulating)
  - [eng.](https://www.vanguard.co.uk/professional/product/etf/equity/9679/ftse-all-world-ucits-etf-usd-accumulating)
- IE00B4L5YC18 - iShares MSCI EM UCITS ETF USD (Acc)
  - [deutsch](https://www.ishares.com/de/privatanleger/de/produkte/251858/?switchLocale=y&siteEntryPassthrough=true) [[CSV]](https://www.ishares.com/de/privatanleger/de/produkte/251858/ishares-msci-emerging-markets-ucits-etf-acc-fund/1478358465952.ajax?fileType=csv&fileName=EUNM_holdings&dataType=fund)
  - [eng. (UK)](https://www.ishares.com/uk/individual/en/products/251858/ishares-msci-emerging-markets-ucits-etf-acc-fund) [[CSV]](https://www.ishares.com/uk/individual/en/products/251858/ishares-msci-emerging-markets-ucits-etf-acc-fund/1506575576011.ajax?fileType=csv&fileName=SEMA_holdings&dataType=fund)
- IE00B4L5Y983 - iShares Core MSCI World UCITS ETF
  - [deutsch](https://www.ishares.com/de/privatanleger/de/produkte/251882/ishares-msci-world-ucits-etf-acc-fund) [[CSV]](https://www.ishares.com/de/privatanleger/de/produkte/251882/ishares-msci-world-ucits-etf-acc-fund/1478358465952.ajax?fileType=csv&fileName=EUNL_holdings&dataType=fund)
  - [eng. (UK)](https://www.ishares.com/uk/individual/en/products/251882/ishares-msci-world-ucits-etf-acc-fund) [[CSV]](https://www.ishares.com/uk/individual/en/products/251882/ishares-msci-world-ucits-etf-acc-fund/1506575576011.ajax?fileType=csv&fileName=SWDA_holdings&dataType=fund)

It is possible to obtain computer-processable crossovers between different standards, but this is [somewhat expensive](https://classification.codes/store/selection/).


