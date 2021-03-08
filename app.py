from flask import Flask
from flask import jsonify

#Custom libraries
import tools.stock_prediction as stp

app = Flask(__name__)



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("")
    return 'Hello World! CD'

@app.route('/symbol/<stock_name>')
def echo(stock_name):
    print(f"This was placed in the url: new-{name}")
    stock_prediction = stp.latest_predictions(symbol=stock_name, root_dir='Stock_Prediction_models')[1]
    #val = {"predicted_values": }
    return stock_prediction.to_json(orient="index")

@app.route('/name/<value>')
def name(value):
    print(f"This was placed in the url: new-{value}")
    val = {"supplied-name": value}
    return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)