import pandas as pd
import mysql.connector
from flask import Flask, jsonify

# Init Flask App
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Homepage!!!'

# API functons
@app.route('/sales')
def get_sales():
    table = pd.read_csv('inventario.csv')
    sales = table['Vendas'].sum()
    response = {'sales' : int(sales)}
    return jsonify(response)

@app.route('/total_products')
def get_total_products():
    table = pd.read_csv('inventario.csv')
    total_products = table['Produtos'].sum()
    response = {'total_products' : int(total_products)}
    return jsonify(response)

@app.route('/total_stock')
def get_total_stock():
    table = pd.read_csv('inventario.csv')
    total_stock = table['Estoque'].sum()
    response = {'total_stock' : int(total_stock)}
    return jsonify(response)

# Execute Flask app
app.run(host='0.0.0.0')