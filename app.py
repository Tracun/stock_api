from flask_restful import Resource, Api
from flask import Flask, jsonify, render_template
from tickerRequest import TickerRequest

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)

def start():
    app.run(host='0.0.0.0', port=5000)

@app.route('/finance/api/v1/stocks')
def AllStockss():
    tickerRequest = TickerRequest()

    response = tickerRequest.getTickers()
    return jsonify(response)


@app.route('/finance/api/v1/stocks/<string:ticker>')
def Ticker(ticker):
    tickerRequest = TickerRequest()
    response = tickerRequest.getTicker(ticker)
    return jsonify(response)

class NewTicker(Resource):
    def post(self, ticker):  # param is pulled from url string

	    return None

@app.route('/')
@app.route('/home')
@app.route('/finance')
@app.route('/finance/api')
@app.route('/finance/api/v1')
def index():
    return render_template(
        'index.html',
        title='Home Page'
    )

# once we've defined our api functionalities, add them to the master API object
api.add_resource(NewTicker, '/finance/api/v1/newTicker/<string:ticker>')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()

################# Study this case ##########################################
#REF: https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12 ###############
