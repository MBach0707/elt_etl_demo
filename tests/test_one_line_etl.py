from transform import transform
from config import VARIABLES

def test_one_line_etl():
    #Sample test input
    raw_data = {
        'hourly': {
            'time': ['2026-04-19T00:00'],
            'temperature_2m': [8.2],
            'wind_speed_10m': [9.4]
        }
    }
    df = transform(raw_data)
    
    assert df.shape == (1, 3)
    assert df['temperature_2m'].iloc[0] >= VARIABLES['temperature_2m']['min']
    assert df['temperature_2m'].iloc[0] <= VARIABLES['temperature_2m']['max']
    assert df['wind_speed_10m'].iloc[0] >= VARIABLES['wind_speed_10m']['min']
    assert df['wind_speed_10m'].iloc[0] <= VARIABLES['wind_speed_10m']['max']