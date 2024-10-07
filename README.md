```python
import tvscreener as tvs
from tvscreener.filter import Country
from tvscreener import TimeInterval
import pandas as pd

%load_ext autoreload
%autoreload 2

```


```python
# Initialize the StockScreener with your session credentials
screener = tvs.StockScreener(sessionid="YOUR SESSION ID", sessionid_sign="YOUR SESSION ID SIGN")

if screener.is_authenticated():
    print("Successfully authenticated with TradingView")
else:
    print("Failed to authenticate with TradingView")

# Set the country filter to China
screener.set_countries(Country.CHINA)

df = screener.get()

if df.empty:
    print("No data found")
else:
    desired_columns = {
        'Symbol': 'Symbol',
        'Name': 'Name',
        'close': 'Price',
        'Change from Open %' : 'Change from Open %',
        'Country' : 'Country'
    }

    # Format the data for columns that exist
    for col in df_selected.columns:
        if col == 'Price' or col == 'Change %':
            df_selected[col] = df_selected[col].round(2)

        # we're not pulling volume or market cap but eh its here
        elif col == 'Volume':
            df_selected[col] = df_selected[col].apply(lambda x: f'{x:,.0f}' if pd.notnull(x) else '')
        elif col == 'Market Cap':
            df_selected[col] = df_selected[col].apply(lambda x: f'${x/1e9:.2f}B' if x >= 1e9 else f'${x/1e6:.2f}M' if pd.notnull(x) else '')

    # Sort by Changre from Open % if available, otherwise by the first column
    sort_column = 'Change from Open %' if 'Change from Open %' in df_selected.columns else df_selected.columns[0]
    df_sorted = df_selected.sort_values(sort_column, ascending=False)

    # Display results
    print("\nTop Chinese Stocks:")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(df_sorted)

    # Check if valid
    print(f"\nTotal number of Chinese stocks: {len(df_sorted)}")
```

    Successfully authenticated with TradingView
    
    Top Chinese Stocks:
               Symbol   Name  Change from Open % Country
    245   NASDAQ:CHSN   CHSN          428.928571   China
    430      OTC:YBCN   YBCN          222.580645   China
    461     OTC:SECOY  SECOY          100.000000   China
    ...
    27     NASDAQ:DUO    DUO          -34.455959   China
    446     OTC:JPPYY  JPPYY          -50.247934   China
    178     OTC:CTRYF  CTRYF          -52.380952   China
    
    Total number of Chinese stocks: 477



```python
# Print available columns and data shape
print("Available columns:")
print(df.columns.tolist())
```

    Available columns:
    ['Symbol', 'Name', 'Description', 'All Time High', 'All Time Low', 'All Time Performance', 'Aroon Down (14)', 'Aroon Up (14)', 'Average Day Range (14)', 'Average Directional Index (14)', 'Average True Range (14)', 'Average Volume (10 day)', 'Average Volume (30 day)', 'Average Volume (60 day)', 'Average Volume (90 day)', 'Awesome Oscillator', 'Basic EPS (FY)', 'Basic EPS (TTM)', 'Bollinger Lower Band (20)', 'Bollinger Upper Band (20)', 'Bull Bear Power', 'Candle.3BlackCrows', 'Candle.3WhiteSoldiers', 'Candle.AbandonedBaby.Bearish', 'Candle.AbandonedBaby.Bullish', 'Candle.Doji', 'Candle.Doji.Dragonfly', 'Candle.Doji.Gravestone', 'Candle.Engulfing.Bearish', 'Candle.Engulfing.Bullish', 'Candle.EveningStar', 'Candle.Hammer', 'Candle.HangingMan', 'Candle.Harami.Bearish', 'Candle.Harami.Bullish', 'Candle.InvertedHammer', 'Candle.Kicking.Bearish', 'Candle.Kicking.Bullish', 'Candle.LongShadow.Lower', 'Candle.LongShadow.Upper', 'Candle.Marubozu.Black', 'Candle.Marubozu.White', 'Candle.MorningStar', 'Candle.ShootingStar', 'Candle.SpinningTop.Black', 'Candle.SpinningTop.White', 'Candle.TriStar.Bearish', 'Candle.TriStar.Bullish', 'Cash & Equivalents (FY)', 'Cash & Equivalents (MRQ)', 'Cash and short term investments (FY)', 'Cash and short term investments (MRQ)', 'Chaikin Money Flow (20)', 'Change', 'Change 15m', 'Change 15m, %', 'Change 1h', 'Change 1h, %', 'Change 1m', 'Change 1M', 'Change 1m, %', 'Change 1M, %', 'Change 1W', 'Change 1W, %', 'Change 4h', 'Change 4h, %', 'Change 5m', 'Change 5m, %', 'Change from Open', 'Change from Open %', 'Change %', 'Commodity Channel Index (20)', 'Country', 'Currency', 'Current Ratio (MRQ)', 'Debt to Equity Ratio (MRQ)', 'Dividends Paid (FY)', 'Dividends per share (Annual YoY Growth)', 'Dividends per Share (FY)', 'Dividends per Share (MRQ)', 'Dividend Yield Forward', 'Donchian Channels Lower Band (20)', 'Donchian Channels Upper Band (20)', 'EBITDA (Annual YoY Growth)', 'EBITDA (Quarterly QoQ Growth)', 'EBITDA (Quarterly YoY Growth)', 'EBITDA (TTM)', 'EBITDA (TTM YoY Growth)', 'Enterprise Value/EBITDA (TTM)', 'Enterprise Value (MRQ)', 'EPS Diluted (Annual YoY Growth)', 'EPS Diluted (FY)', 'EPS Diluted (MRQ)', 'EPS Diluted (Quarterly QoQ Growth)', 'EPS Diluted (Quarterly YoY Growth)', 'EPS Diluted (TTM)', 'EPS Diluted (TTM YoY Growth)', 'EPS Forecast (MRQ)', 'Exchange', 'Exponential Moving Average (10)', 'Exponential Moving Average (100)', 'Exponential Moving Average (20)', 'Exponential Moving Average (200)', 'Exponential Moving Average (30)', 'Exponential Moving Average (5)', 'Exponential Moving Average (50)', 'Free Cash Flow (Annual YoY Growth)', 'Free Cash Flow Margin (FY)', 'Free Cash Flow Margin (TTM)', 'Free Cash Flow (Quarterly QoQ Growth)', 'Free Cash Flow (Quarterly YoY Growth)', 'Free Cash Flow (TTM YoY Growth)', 'Fundamental Currency Code', 'Gap %', 'Goodwill', 'Gross Margin (FY)', 'Gross Margin (TTM)', 'Gross Profit (Annual YoY Growth)', 'Gross Profit (FY)', 'Gross Profit (MRQ)', 'Gross Profit (Quarterly QoQ Growth)', 'Gross Profit (Quarterly YoY Growth)', 'Gross Profit (TTM YoY Growth)', 'High', 'Hull Moving Average (9)', 'Ichimoku Base Line (9, 26, 52, 26)', 'Ichimoku Conversion Line (9, 26, 52, 26)', 'Ichimoku Leading Span A (9, 26, 52, 26)', 'Ichimoku Leading Span B (9, 26, 52, 26)', 'Industry', 'Keltner Channels Lower Band (20)', 'Keltner Channels Upper Band (20)', 'Last Year Revenue (FY)', 'Logoid', 'Low', 'MACD Level (12, 26)', 'MACD Signal (12, 26)', 'Market Capitalization', 'Momentum (10)', 'Money Flow (14)', 'Monthly Performance', '1-Month High', '3-Month High', '6-Month High', '1-Month Low', '3-Month Low', '6-Month Low', '3-Month Performance', '6-Month Performance', 'Moving Averages Rating', 'Negative Directional Indicator (14)', 'Net Debt (MRQ)', 'Net Income (Annual YoY Growth)', 'Net Income (FY)', 'Net Income (Quarterly QoQ Growth)', 'Net Income (Quarterly YoY Growth)', 'Net Income (TTM YoY Growth)', 'Net Margin (FY)', 'Net Margin (TTM)', 'Number of Employees', 'Number of Shareholders', 'Open', 'Operating Margin (FY)', 'Operating Margin (TTM)', 'Oscillators Rating', 'Parabolic SAR', 'Pivot Camarilla P', 'Pivot Camarilla R1', 'Pivot Camarilla R2', 'Pivot Camarilla R3', 'Pivot Camarilla S1', 'Pivot Camarilla S2', 'Pivot Camarilla S3', 'Pivot Classic P', 'Pivot Classic R1', 'Pivot Classic R2', 'Pivot Classic R3', 'Pivot Classic S1', 'Pivot Classic S2', 'Pivot Classic S3', 'Pivot DM P', 'Pivot DM R1', 'Pivot DM S1', 'Pivot Fibonacci P', 'Pivot Fibonacci R1', 'Pivot Fibonacci R2', 'Pivot Fibonacci R3', 'Pivot Fibonacci S1', 'Pivot Fibonacci S2', 'Pivot Fibonacci S3', 'Pivot Woodie P', 'Pivot Woodie R1', 'Pivot Woodie R2', 'Pivot Woodie R3', 'Pivot Woodie S1', 'Pivot Woodie S2', 'Pivot Woodie S3', 'Positive Directional Indicator (14)', 'Post-market Change', 'Post-market Change %', 'Post-market Close', 'Post-market High', 'Post-market Low', 'Post-market Open', 'Post-market Volume', 'Pre-market Change', 'Pre-market Change from Open', 'Pre-market Change from Open %', 'Pre-market Change %', 'Pre-market Close', 'Pre-market Gap %', 'Pre-market High', 'Pre-market Low', 'Pre-market Open', 'Pre-market Volume', 'Pretax Margin (TTM)', 'Price', 'Price to Book (FY)', 'Price to Book (MRQ)', 'Price to Earnings Ratio (TTM)', 'Price to Free Cash Flow (TTM)', 'Price to Revenue Ratio (TTM)', 'Price to Sales (FY)', 'Quick Ratio (MRQ)', 'Rate Of Change (9)', 'Recent Earnings Date', 'Relative Strength Index (14)', 'Relative Strength Index (7)', 'Relative Volume', 'Relative Volume at Time', 'Research & development Ratio (FY)', 'Research & development Ratio (TTM)', 'Return on Assets (TTM)', 'Return on Equity (TTM)', 'Return on Invested Capital (TTM)', 'Revenue (Annual YoY Growth)', 'Revenue per Employee (FY)', 'Revenue (Quarterly QoQ Growth)', 'Revenue (Quarterly YoY Growth)', 'Revenue (TTM YoY Growth)', 'Sector', 'Selling General & Admin expenses Ratio (FY)', 'Selling General & Admin expenses Ratio (TTM)', 'Shares Float', 'Simple Moving Average (10)', 'Simple Moving Average (100)', 'Simple Moving Average (20)', 'Simple Moving Average (200)', 'Simple Moving Average (30)', 'Simple Moving Average (5)', 'Simple Moving Average (50)', 'Stochastic %D (14, 3, 3)', 'Stochastic %K (14, 3, 3)', 'Stochastic RSI Fast (3, 3, 14, 14)', 'Stochastic RSI Slow (3, 3, 14, 14)', 'Submarket', 'Subtype', 'Technical Rating', 'Total Assets (Annual YoY Growth)', 'Total Assets (MRQ)', 'Total Assets (Quarterly QoQ Growth)', 'Total Assets (Quarterly YoY Growth)', 'Total Current Assets (MRQ)', 'Total Debt (Annual YoY Growth)', 'Total Debt (MRQ)', 'Total Debt (Quarterly QoQ Growth)', 'Total Debt (Quarterly YoY Growth)', 'Total Liabilities (FY)', 'Total Liabilities (MRQ)', 'Total Revenue (FY)', 'Total Shares Outstanding', 'Type', 'Ultimate Oscillator (7, 14, 28)', 'Upcoming Earnings Date', 'Volatility', 'Volatility Month', 'Volatility Week', 'Volume', 'Volume*Price', 'Volume Weighted Average Price', 'Volume Weighted Moving Average (20)', 'Weekly Performance', '52 Week High', '52 Week Low', 'Williams Percent Range (14)', 'Yearly Performance', '1-Year Beta', 'YTD Performance', '5Y Performance', 'Reco. BBPower', 'Reco. HullMA9', 'Reco. UO', 'Reco. VWMA', 'Prev. Awesome Oscillator', 'Prev. Commodity Channel Index (20)', 'Prev. Momentum (10)', 'Prev. Negative Directional Indicator (14)', 'Prev. Positive Directional Indicator (14)', 'Prev. Relative Strength Index (14)', 'Prev. Relative Strength Index (7)', 'Prev. Stochastic %D (14, 3, 3)', 'Prev. Stochastic %K (14, 3, 3)']


