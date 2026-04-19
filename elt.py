from extract import extract
from load_sqlite import load_sqlite
from transform_sql import transform_sql

def run_elt():
    raw_data = extract()
    load_sqlite(raw_data)
    transform_sql()
    return