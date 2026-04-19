from config import OUTPUT_FILE_NAME

def load_csv(df):
    df.to_csv(OUTPUT_FILE_NAME)
    return