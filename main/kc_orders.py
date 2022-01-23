import global_variables


def placeMarketOrder(symbol, buy_sell, quantity):
    global_variables.logger.info("Placing order for " + symbol + " Type: " + buy_sell + " Quantity: " + str(quantity))
    if buy_sell == "buy":
        t_type = global_variables.kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "sell":
        t_type = global_variables.kite.TRANSACTION_TYPE_SELL
    global_variables.kite.place_order(tradingsymbol=symbol,
                                      exchange=global_variables.kite.EXCHANGE_NFO,
                                      transaction_type=t_type,
                                      quantity=quantity,
                                      order_type=global_variables.kite.ORDER_TYPE_MARKET,
                                      product=global_variables.kite.PRODUCT_NRML,
                                      variety=global_variables.kite.VARIETY_REGULAR)


#
def placeBracketOrder(symbol, buy_sell, quantity, atr, price, exchange):
    global_variables.logger.info("Placing order for " + symbol + " Type: " + buy_sell + " Quantity: " + quantity)
    if buy_sell == "buy":
        t_type = global_variables.kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "Sell":
        t_type = global_variables.kite.TRANSACTION_TYPE_SELL
    global_variables.kite.place_order(tradingsymbol=symbol,
                                      exchange=exchange,
                                      transaction_type=t_type,
                                      quantity=quantity,
                                      order_type=global_variables.kite.ORDER_TYPE_LIMIT,
                                      price=price,
                                      product=global_variables.kite.PRODUCT_MIS,
                                      variety=global_variables.kite.VARIETY_BO,
                                      squareoff=int(6 * atr),
                                      stoploss=int(3 * atr),
                                      trailing_stoploss=2)
