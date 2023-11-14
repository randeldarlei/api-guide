import pandas as pd
from flask import Flask, jsonify

# Init Flask App
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello World!!!'

# API functons
@app.route('/get_sales')
def get_sales():
    table = pd.read_csv('advertising.csv')
    sales = table['Vendas'].sum()
    response = {'sales': sales}
    return jsonify(response)

# Execute Flask app
app.run(host='0.0.0.0')