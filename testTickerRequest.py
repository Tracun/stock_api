from tickerRequest import TickerRequest
import json

tickerRequest = TickerRequest()

response = tickerRequest.getTickers()
print(response)
