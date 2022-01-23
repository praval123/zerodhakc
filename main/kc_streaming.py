from kiteconnect import KiteTicker
import pandas as pd
import global_variables as gb
# get dump of a;; NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)


def tokenLookup(instrument_df, symbol_list):
    """"""
    token_list = []
    for symbol in symbol_list:
        token_list.append(int(instrument_df[instrument_df.tradingsymbol == symbol].instrument_token.value[0]))
    return token_list


tickers = ["ACC", "ICICIBANK", "HDFC"]

# create kite ticker object

kws = KiteTicker(key_secret[0], kite.access_token)
tokens = tokenLookup(instrument_df, tickers)


def on_ticks(ws, ticks):
    # callback to recieve ticks
    print(ticks)


def on_connection(ws, response):
    # callback on successful connect
    ws.subscribe


kws.on_ticks = on_ticks
