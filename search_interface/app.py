from flask import Flask, render_template
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras
import traceback

load_dotenv()

host = os.environ.get("POSTGRES_HOSTNAME")
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
db = os.environ.get("POSTGRES_DATABASE")

conn = None

def get_connection():
    global conn
    if conn is None or conn.closed == 1:
        print("Creating a new connection")
        conn = psycopg2.connect(host=host, database=db, user=user, password=password)
    return conn

app = Flask(__name__)
@app.route("/")
def search():
    conn = get_connection()
    return render_template('home.html')