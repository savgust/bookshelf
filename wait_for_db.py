import time
import psycopg2
from psycopg2 import OperationalError
import sys

def wait_for_db():
    print("⏳ Waiting for PostgreSQL to be ready...")
    while True:
        try:
            conn = psycopg2.connect(
                dbname="bookshelf",
                user="postgres",
                password="postgres",
                host="db",
                port="5432",
            )
            conn.close()
            print("✅ PostgreSQL is ready!")
            break
        except OperationalError:
            print("🚫 PostgreSQL not ready, retrying in 1 sec...")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_db()
