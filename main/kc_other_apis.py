import logging
import global_variables


def get_quote(symbol):
    global_variables.logger.critical("fetch quote details ... ")
    quote = global_variables.kite.quote(symbol)
    return quote


def get_ltp(symbol):
    global_variables.logger.info("fetch last trading price of an instrument")
    ltp = global_variables.kite.ltp("NSE:" + symbol)
    logging.debug("LTP Strike Price of " + symbol + " is :" + ltp)
    return ltp


def get_ltp_options(symbol):
    global_variables.logger.info("fetch last trading price of an instrument")
    ohlc = global_variables.kite.ohlc('NSE:{}'.format(symbol))
    ltp = ohlc['NSE:{}'.format(symbol)]['last_price']
    return ltp


def get_orders():
    global_variables.logger.info("fetch order details")
    orders = global_variables.kite.orders()
    return orders


def get_positions():
    # fetch position details
    positions = global_variables.kite.positions()
    return positions


def get_holdings():
    # fetch holding details
    holdings = global_variables.kite.holdings()
    return holdings
