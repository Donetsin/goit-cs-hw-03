import psycopg2
from contextlib import contextmanager

database = 'task_mng'
user = 'postgres'
password = '567234'
host = 'localhost'
port = '5432'

@contextmanager
def create_connection():
    """ create a database connection to a PostgreSQL database """
    conn = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

    yield conn
    conn.rollback()
    conn.close()
