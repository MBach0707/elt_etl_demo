URL = 'https://api.open-meteo.com/v1/forecast'
OUTPUT_FILE_NAME = 'OpenMeteoData.csv'
DB_NAME = 'SQLDatabase'
TABLE_NAME = 'Forecast'
LAT = 55.69
LONG = 12.59
VARIABLES = {
    'temperature_2m': {'min': -60, 'max': 60},
    'wind_speed_10m': {'min': 0, 'max': 200}
}