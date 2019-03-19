import json

class ResponseConverter:

    linkGoogleFinance = 'http://www.google.com/googlefinance/disclaimer/';

    def __init__(self):
        pass

    def tickers(self, tickerList):
        return {'status':'200','assets':tickerList, 'about_stock_market_data':self.linkGoogleFinance}

    def ticker(self, ticker):
        return {'status':'200','ticker':ticker, 'about_stock_market_data':self.linkGoogleFinance}

    def jsonInternalError(self, internalMessage):
        return {'errors':[{'code':500,'message':'Internal Server Error', 'internalMessage':internalMessage}]}

    def tickerNotFound(self, ticker):
        return {'errors':[{'code':404,'message':'Not Found', 'message':'Ticker not found', 'ticker':ticker}]}

