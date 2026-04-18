from config import URL, LAT, LONG, VARIABLES
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