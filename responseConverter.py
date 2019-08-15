class ResponseConverter:

    linkGoogleFinance = 'http://www.google.com/googlefinance/disclaimer/'
    URI = 'http://tracun.com/finance/api/v1/stocks/'

    def __init__(self):
        pass

    def tickers(self, tickerList):
        return {'status':200,'assets':tickerList, 'about_stock_market_data':self.linkGoogleFinance}

    def ticker(self, ticker):
        return {'status':200,'ticker':ticker, 'about_stock_market_data':self.linkGoogleFinance}

    def jsonInternalError(self, internalMessage):
        return {'errors':[{'code':500,'message':'Internal Server Error', 'internalMessage':'{}'.format(internalMessage)}]}

    def tickerNotFound(self, ticker):
        return {'errors':[{'code':404,'message':'Not Found', 'message error':'Ticker not found', 'ticker':ticker}]}

    def tickerNotExists(self, ticker):
        return {'errors':[{'code':400,'message':'Not exists', 'message error':'Ticker not exists', 'ticker':ticker}]}

    def tickerAlreadyExists(self, ticker):
        return {'errors':[{'code':200,'message':'Ticker already exists','uri':'{}{}'.format(self.URI, ticker), 'ticker':ticker}]}

    def tickerCreated(self, ticker):
        return {'status':201,'uri':'{}{}'.format(self.URI, ticker), 'message':'Created', 'about_stock_market_data':self.linkGoogleFinance}

