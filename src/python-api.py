import os
import pymysql
from flask import Flask, jsonify

DB_HOST = 'value'
DB_USER = 'value'
DB_PASSWORD = 'value'
DB_NAME = 'value'

# Init Flask App
app = Flask(__name__)
minikube_ip = os.getenv('MINIKUBE_IP')

def connect_database():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

@app.route('/')
def homepage():
    return 'Homepage!!!'

# API functons
@app.route('/sales')
def get_sales():
    connection = connect_database()
    cursor = connection.cursor
    cursor.execute("SELECT SUM(Vendas) FROM inventario")
    sales = cursor.fetchone()[0]
    connection.close()
    response = {'sales': int(sales)}
    return jsonify(response)

# Execute Flask app
app.run(host='0.0.0.0', port=5000)