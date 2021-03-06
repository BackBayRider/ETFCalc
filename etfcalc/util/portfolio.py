class Portfolio(object):

    def __init__(self):
        self.holdings = {}
        self.prices = {}

    def get_holdings(self):
        return self.holdings

    def get_tickers(self):
        return list(self.holdings.keys())

    def set_amount(self, ticker, amount):
        self.holdings[ticker] = amount

    def get_price(self, ticker):
        return self.prices[ticker]

    def set_price(self, ticker, price):
        self.prices[ticker] = price
