from config import DB_NAME, TABLE_NAME
import pandas as pd
import sqlite3

def load_sqlite(raw_data):
    df = pd.DataFrame(raw_data['hourly'])
    df.to_sql(TABLE_NAME, sqlite3.connect(DB_NAME), if_exists='replace')
    return