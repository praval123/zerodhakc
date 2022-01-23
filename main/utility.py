import math


def calculate_strike_price(base_price, final):
    val = base_price + 100
    val2 = math.fmod(val, 100)
    x = val - val2
    # to remove .0 string.
    abs_val = "{:.0f}".format(x)
    # PE_PRICE = "{}".format("{:.0f}".format(x + 0))
    PE_PRICE_2 = "{}".format("{:.0f}".format(x + final))
    return PE_PRICE_2


def generate_symbol(ltp_or_strike, final_strike_price_difference, CE_or_PE, instrument, expiry):
    strike_price = calculate_strike_price(ltp_or_strike, final_strike_price_difference)
    symbol = instrument + expiry + strike_price + CE_or_PE
    return symbol
