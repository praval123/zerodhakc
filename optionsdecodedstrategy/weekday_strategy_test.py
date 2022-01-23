from main import kc_other_apis, utility, global_variables, kc_orders, kc_connect

global_variables.kite = kc_connect.login_with_access_token()


def execute_weekday_strategy(ltp_symbol, expiry, instrument):
    current_price = kc_other_apis.get_ltp_options(ltp_symbol)

    instrument_symbol_one = utility.generate_symbol(current_price, -300, "PE",
                                                    instrument, expiry)
    kc_orders.placeMarketOrder(instrument_symbol_one, "sell", 50)

    instrument_symbol_two = utility.generate_symbol(current_price, -500, "PE",
                                                    instrument, expiry)
    kc_orders.placeMarketOrder(instrument_symbol_two, "sell", 100)

    instrument_symbol_three = utility.generate_symbol(current_price, 500, "PE",
                                                      instrument, expiry)
    kc_orders.placeMarketOrder(instrument_symbol_three, "sell", 50)

    instrument_symbol_four = utility.generate_symbol(current_price, 200, "CE",
                                                     instrument, expiry)
    kc_orders.placeMarketOrder(instrument_symbol_four, "sell", 25)


execute_weekday_strategy("NIFTY BANK", "22JAN", "BANKNIFTY")
