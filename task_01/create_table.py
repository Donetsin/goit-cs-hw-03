from psycopg2 import Error

from connect import create_connection

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

if __name__ == '__main__':
    sql_create_users_table = """
        CREATE TABLE  IF NOT EXISTS users
        (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
    """

    sql_create_status_table = """
        CREATE TABLE  IF NOT EXISTS status 
        (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
    """

    sql_create_tasks_table = """
        CREATE TABLE  IF NOT EXISTS tasks 
        (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            status_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (status_id) REFERENCES status(id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """

    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_status_table)
            create_table(conn, sql_create_users_table)
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")
