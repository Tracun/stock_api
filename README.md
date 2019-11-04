# Stock API
> This is an API that provide simple quotation of financial market using the google Finance.


## Running locally

OS X & Linux & Windows:

```sh
pip install requirements.txt
python app.py
```


## Tests

```sh
cd tests
python testEndpoint.py
```

## Sample requests


**GET**


Home
*  ```/```


*  ```/home```


Searches for all tickers
* ```/finance/api/stocks```


Searches for a specific ticker
* ```/finance/api/stocks/{string:ticker}```


**POST**


Save a new ticker
* ```/finance/api/newTicker/{string:ticker}```


## Release History


* 0.0.1
    * Work in progress


## Contributing


Lucas Waiteman Bastos – [@Tracun](https://twitter.com/tracun) – tracuns@gmail.com
https://github.com/tracun/


1. Fork it (<https://github.com/Tracun/stock_api/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

