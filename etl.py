from extract import extract
from transform import transform
from load_csv import load_csv

def run_etl():
    raw_data = extract()
    data = transform(raw_data)
    load_csv(data)
    return 