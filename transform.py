from config import VARIABLES
import pandas as pd

def transform(raw_data):
    df = pd.DataFrame(raw_data['hourly'])
    return df