import os
import pymysql
from flask import Flask, jsonify, request

DB_HOST = os.getenv('DB_HOST')
DB_USER =os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Init Flask App
app = Flask(__name__)
MINIKUBE_IP = os.getenv('MINIKUBE_IP')

def connect_database():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

@app.route('/')
def homepage():
    return 'Homepage!!!'

@app.route('/get_sales', methods=['GET'])
def get_sales():
    sale = request.args.get('sale')

    if sale is None:
        return jsonify({'error': 'Não existe nenhuma venda com este valor!'}), 400
    
    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT SUM(Vendas) FROM Inventario")
        total_sales = cursor.fetchone()[0]
        connection.close()
        return jsonify({'total_sales': total_sales}), 200
    except Exception as e:
        connection.rollback()
        connection.close()
        return jsonify({'error': str(e)}), 500

@app.route('/post_sales', mehods=['POST'])
def post_sales():
    data = request.get_json()
    new_sale = data.get('sale')

    if new_sale is None:
        return jsonify({'error': 'POR FAVOR, FORNEÇA O VALOR DA NOVA VENDA'}), 400
    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO vendas (Vendas) VALUES (%)", (new_sale))
        connection.commit()
        connection.close()
        return jsonify({'success': True}), 201
    except Exception as e:
        connection.rollback()
        connection.close()
        return jsonify({'error': str(e)}), 500
# Execute Flask app
app.run(host='0.0.0.0', port=5000)