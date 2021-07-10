import os
import psycopg2
import psycopg2.extras
import traceback

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


def insert_pdf_record(url, title):
    conn = get_connection()

    sql = """
    INSERT INTO pdf 
        (url, title)
        values (%s, %s)
        returning id;
    """

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, [url, title])
    record = cur.fetchone()
    conn.commit()
    cur.close()
    return record['id']

def get_keyword_record_id(word):
    conn = get_connection()

    sql = """
    SELECT id FROM keyword
    WHERE word = %s
    LIMIT 1;
    """

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, [word])
    record = cur.fetchone()
    cur.close()
    if record:
        return record.get('id')
    return None

def insert_keyword_record(word):
    conn = get_connection()

    retrieve_record_id = get_keyword_record_id(word)
    if retrieve_record_id:
        return retrieve_record_id

    sql = """
    INSERT INTO keyword 
        (word)
        values (%s)
        returning id;
    """

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, [word])
    record = cur.fetchone()
    conn.commit()
    cur.close()
    return record['id']

def insert_pdf_keyword_relation_record(pdf_id, keyword_id):
    conn = get_connection()

    sql = """
    INSERT INTO pdf_keyword 
        (pdf_id, keyword_id)
        values (%s, %s);
    """

    cur = conn.cursor()
    cur.execute(sql, [pdf_id, keyword_id])
    conn.commit()
    cur.close()
    return True