
import os
from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/build', methods=['GET'])
def get_build():
    return jsonify({
        "time": os.getenv("BUILD_TIME"),
        "user": os.getenv("BUILD_USER"),
        "host": os.getenv("BUILD_HOST"),
        "os": os.getenv("BUILD_OS"),
        "kernel": os.getenv("BUILD_KERNEL"),
        "uuid": os.getenv("BUILD_UUID")
    })

@app.route('/entry', methods=['GET'])
def get_entry():
    try:
        # "db" is the service name we will use in Docker Compose
        conn = psycopg2.connect(host="db", database="ictdb", user="postgres", password="password")
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM students ORDER BY time DESC LIMIT 1;")
        row = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify(row)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

