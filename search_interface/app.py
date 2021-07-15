from flask import Flask, render_template, request
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
    if request.method == "GET":
        results=[]
        if request.args.get('keywords') != None:
            for keyword in request.args.get('keywords').split(' '):
                results = results + get_values_with_keyword(keyword.upper())
    return render_template('home.html', results=results)


def get_values_with_keyword(keyword):
    conn = get_connection()

    sql = """
    SELECT url, title from pdf
    WHERE id in ( SELECT pdf_id FROM pdf_keyword
    WHERE keyword_id in (
                        SELECT id FROM keyword
                        WHERE upper(word) = %s )
                    )
    GROUP BY url, title
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, [keyword])
    records = cur.fetchall()
    cur.close()
    return records

if __name__ == '__main__':
    app.run(threaded=True)