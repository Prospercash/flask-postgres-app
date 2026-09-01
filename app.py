from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("POSTGRES_DB", "flaskdb"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "password")
    )
    return connection

@app.route("/")
def home():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()

    cursor.close()
    connection.close()

    return f"""
        <h1>Flask + PostgreSQL</h1>
        <p>Successfully connected to PostgreSQL!</p>
        <p>Database: {db_version[0]}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
