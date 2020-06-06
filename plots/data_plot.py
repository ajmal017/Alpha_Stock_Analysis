import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

def line_plot(df, symbol, col='Close', figsize=(18,8)):
    plt.plot('Datetime',col, data=df)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(symbol)
    plt.grid()
    plt.show()

def candlestick_plot(df, symbol, ohlc_col=['Datetime', 'Open', 'High', 'Low', 'Close'],figsize=(18,8)):
    ohlc_df = df[ohlc_col]
    # Converting dates column to float values
    ohlc_df['Datetime'] = ohlc_df['Datetime'].map(mdates.date2num)
    # Making plot
    fig, ax = plt.subplots(figsize=figsize)
    # Converts raw mdate numbers to dates
    ax.xaxis_date()
    plt.xlabel("Date")
    # Making candlestick plot
    candlestick_ohlc(ax, ohlc_df.values, width=0.4,
                     colorup='g', colordown='r', alpha=0.8)
    plt.ylabel("Price")
    plt.title(symbol)
    plt.grid()
    plt.show()