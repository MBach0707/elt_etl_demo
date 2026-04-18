from config import URL, LAT, LONG, VARIABLES
import pandas as pd
import requests

def extract():
    params = {
        'latitude': LAT,
        'longitude': LONG,
        'hourly': list(VARIABLES.keys())
    }
    r = requests.get(URL, params=params)

    raw_data = r.json()

    return raw_data


def transform():
    raw_data = extract()
    df = pd.DataFrame(raw_data)
    return df

print(transform())