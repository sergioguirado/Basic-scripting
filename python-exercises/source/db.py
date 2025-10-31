# db.py

import os
import time
import psycopg2
from psycopg2 import OperationalError
import pandas as pd
from sqlalchemy import create_engine

USER="testuser2"
PASSWORD="testpass"
DATABASE="testdb"
HOST="localhost"
PORT=5432


def get_connection(retries=5, delay=3):
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=HOST,
                database=DATABASE,
                user=USER,
                password=PASSWORD,
                port=PORT
            )
            print("Connection established.")
            return conn
        except OperationalError as e:
            print("PostgreSQL not ready, retrying...", e)
            retries -= 1
            time.sleep(delay)

    raise Exception("Could not connect to database after several retries")

def get_engine():
    return create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

def save_dataframe(df, table_name="sales_with_customers", if_exists="replace"):
    engine = get_engine()
    df.to_sql(table_name, engine, index=False, if_exists=if_exists)
    print(f"✅ Dataframe correctly saved into table '{table_name}'.")
