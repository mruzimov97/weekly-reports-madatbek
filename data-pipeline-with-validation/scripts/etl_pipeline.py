import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(filename='../logs/etl_pipeline.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def ingest_data(path):
    logging.info("Ingesting data from %s", path)
    return pd.read_csv(path)

def clean_data(df):
    logging.info("Cleaning data (dropping duplicates)")
    return df.drop_duplicates()

def validate_data(df):
    logging.info("Validating data")
    validation_results = {
        "not_null_email": df["email"].notnull().all(),
        "unique_ids": df["id"].is_unique
    }
    for check, passed in validation_results.items():
        logging.info("Validation %s: %s", check, passed)
    return validation_results

def save_data(df, path):
    logging.info("Saving cleaned and validated data to %s", path)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    input_path = "../data/raw_data.csv"
    output_path = "../data/processed_data.csv"

    df = ingest_data(input_path)
    df_clean = clean_data(df)
    results = validate_data(df_clean)

    if all(results.values()):
        save_data(df_clean, output_path)
        logging.info("ETL pipeline completed successfully.")
    else:
        logging.warning("Validation failed. Pipeline halted.")