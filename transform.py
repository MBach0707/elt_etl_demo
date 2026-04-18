from config import VARIABLES
import pandas as pd

def transform(raw_data):
    df = pd.DataFrame(raw_data['hourly'])
    for i in VARIABLES.keys():
        df = df[df[i] >= VARIABLES[i]['min']]
        df = df[df[i] <= VARIABLES[i]['max']]
    
    return df