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
    table = pd.read_csv('inventario.csv')
    sales = table['Vendas'].sum()
    response = {'sales': sales}
    return jsonify(response)

@app.route('/get_total_products')
def get_total_products():
    table = pd.read_csv('inventario.csv')
    total_products = table['Produtos'].sum()
    response = {'total_products': total_products}
    return jsonify(response)

# Execute Flask app
app.run(host='0.0.0.0')