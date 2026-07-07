# utils/stocks.py  ->  a module inside the 'utils' package

# A tiny fake price table to keep the demo offline.
_PRICES = {"AAPL": 195, "GOOG": 175, "TSLA": 250}


def get_todays_price(stock_name):
    """Return today's price for a ticker, or 0 if unknown."""
    return _PRICES.get(stock_name.upper(), 0)
