import datetime as dt
import pandas as pd
import global_variables as gb


# get dump of all NSE instruments
def get_instrument_dump():
    instrument_dump = gb.kite.instruments()
    return pd.DataFrame(instrument_dump)


def instrument_lookup(instrument_df, symbol):
    """Looks up instrument token for a given script from instrument dump"""
    try:
        return instrument_df[instrument_df.tradingsymbol == symbol].instrument_token.values[0]
    except:
        return -1


def fetch_OHLC(ticker, interval, duration, instrument_df):
    """extracts historical data and outputs in the form of data frame"""
    instrument = instrument_lookup(instrument_df, ticker)
    data = pd.DataFrame(
        gb.kite.historical_data(instrument, dt.date.today() - dt.timedelta(duration), dt.date.today(), interval))
    data.set_index("date", inplace=True)
    return data


def fetchOHLCExtended(ticker, inception_date, interval, instrument_df):
    """extracts historical data and outputs in the form of data frame inception date string format - dd-mm-yyyy"""
    instrument = instrument_lookup(instrument_df, ticker)
    from_date = dt.datetime.strptime(inception_date, '%d-%m-%y')
    to_date = dt.date.today()
    data = pd.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume'])
    while True:
        if from_date.date() >= (dt.date.today() - dt.timedelta(100)):
            data = data.append(pd.DataFrame(gb.kite.historical_data(instrument, from_date, dt.date.today(), interval)),
                               ignore_index=True)
            break
        else:
            to_date = from_date + dt.timedelta(100)
            data = data.append(pd.DataFrame(gb.kite.historical_data(instrument, from_date, to_date, interval)),
                               ignore_index=True)
            from_date = to_date
    data.set_index("date", inplace=True)
    return data
