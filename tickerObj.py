class TickerObj():

    def __init__(self):
        pass

    def __init__(self, ticker, price, percentChange, volume, currency, high, low, dateDelay):
        self.ticker = ticker
        self.price = price
        self.percentChange = percentChange
        self.volume = volume
        self.currency = currency
        self.high = high
        self.low = low
        self.dateDelay = dateDelay

    def to_dict(self):
        return {"ticker": self.ticker, "price": self.price, "percentChange": self.percentChange, "volume": self.volume, "currency": self.currency,
                    "high": self.high, "low": self.low, "dateDelay": self.dateDelay}

