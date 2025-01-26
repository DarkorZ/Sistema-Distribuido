from flask import Flask, request, jsonify
import mysql.connector
from kafka import KafkaProducer
import json
import time
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
# Función para inicializar KafkaProducer con reintentos
def create_kafka_producer(max_retries=10, wait_time=5):
    retries = 0
    while retries < max_retries:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("Conexión exitosa al broker Kafka desde API")
            return producer
        except Exception as e:
            retries += 1
            print(f"No se pudo conectar a Kafka desde API: {e}. Reintentando en {wait_time} segundos... (Intento {retries}/{max_retries})")
            time.sleep(wait_time)
    raise Exception("No se pudo conectar a Kafka después de varios intentos.")

# Inicializa el productor con reintentos
producer = create_kafka_producer()

#conexion con mysql
def connect_to_mysql():
    try:
        db = mysql.connector.connect(
            host='mysql',
            user='user',
            password='password',
            database='pedidos'

        )
        return db
    except mysql.connector.Error as e:
        print(f"no se pudo conectar a MYSQL {e}")
        return None
    

#Endpoint para obtener los pedidos
@app.route('/pedido', methods=['GET'])
def obtener_pedido():
    sucursal = request.args.get('sucursal')
    db=connect_to_mysql()
    if db is None:
        return jsonify({"error:" "NO SE CONECTO A LA BASE DE DATOS"}), 500
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM pedidos"


    if sucursal:
        query += " WHERE sucursal =%s"
        try:
            cursor.execute(query, (sucursal,))  # Los parámetros deben pasarse como una tupla
        except mysql.connector.Error as e:
            return jsonify({"error": f"Error en la consulta: {e}"}), 500
    else:
        try:
            cursor.execute(query)
        except mysql.connector.Error as e:
            return jsonify({"error": f"Error en la consulta: {e}"}), 500
        
    pedidos=cursor.fetchall()
    pedidos_sorted = sorted (pedidos, key=lambda x: x['fecha'], reverse=True)

    return jsonify(pedidos_sorted)


@app.route('/pedido', methods=['POST'])
def crear_pedido():
    data = request.json
    try:
        # Envía el mensaje al topic 'pedidos'
        producer.send('pedidos', data)
        print(f"Pedido enviado a Kafka: {data}")
        return jsonify({"message": "Pedido enviado a Kafka"}), 201
    except Exception as e:
        print(f"Error al enviar el mensaje a Kafka: {e}")
        return jsonify({"error": "No se pudo enviar el pedido a Kafka"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)