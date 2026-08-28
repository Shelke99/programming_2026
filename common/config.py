import psycopg2
from read_properties import properties
from psycopg2 import pool


class ConnectionPooling:
    postgres_pool = {}

def conn():
    try:
        cb_db_details = properties["website_bot_db_details"]
        postgresSQL_pool = psycopg2.pool.ThreadedConnectionPool(int(properties["min_pool_connects"]),
                                                                int(properties["max_pool_connects"]), cb_db_details)
        if ConnectionPooling.postgres_pool == {}:
            ConnectionPooling.postgres_pool['pool'] = postgresSQL_pool
        conn = ConnectionPooling.postgres_pool['pool'].getconn()
        return conn
    except Exception as e:
        return False
