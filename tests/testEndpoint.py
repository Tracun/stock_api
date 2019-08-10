import requests

api_url_base = 'http://localhost:5000/'
endPoint = 'finance/api/v1/stocks'

def testHome():
    response = requests.get(api_url_base)
    print('status_code: ', response.status_code)
    assert(response.status_code == 200)

def testStocks():
    response = requests.get(api_url_base + endPoint)
    print('status_code: ', response.status_code)
    assert(response.status_code == 200)

def testStock(ticker):
    response = requests.get(api_url_base + endPoint + '/{}'.format(ticker))
    print('status_code: ', response.status_code)
    assert(response.status_code == 200)

def testNewTicker(ticker):
    #Not implemented
    assert(True)

if __name__ == '__main__':
    testHome()
    testStocks()
    testStock('PETR4')