from config import DB_NAME, TABLE_NAME, VARIABLES
import pandas as pd
import sqlite3

def transform_sql():
    conditions = []
    for var, limits in VARIABLES.items():
        conditions.append(f"{var} >= {limits['min']}")
        conditions.append(f"{var} <= {limits['max']}")
    where_clause = " AND ".join(conditions)

    df = pd.read_sql(f"SELECT * FROM {TABLE_NAME} where {where_clause}", sqlite3.connect(DB_NAME))
    return df