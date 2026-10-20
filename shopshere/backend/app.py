import os
from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "shopsphere"),
        password=os.getenv("DB_PASSWORD", "change-me"),
        database=os.getenv("DB_NAME", "shopsphere"),
        connection_timeout=5,
    )

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/products")
def products():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, price FROM products ORDER BY id")
        rows = cursor.fetchall()
        return jsonify(rows)
    except Error:
        app.logger.exception("Could not retrieve products")
        return jsonify({"error": "Database unavailable"}), 503
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
