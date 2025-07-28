import pandas as pd
import argparse
import logging
import os
from sqlalchemy import create_engine

# Set up logging
logging.basicConfig(filename='logs/cleaning.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def clean_data(input_path, output_path):
    try:
        df = pd.read_csv(input_path)
        logging.info(f"Loaded data from {input_path}, shape: {df.shape}")

        # Drop rows with any nulls
        df_clean = df.dropna()
        logging.info(f"After dropping nulls, shape: {df_clean.shape}")

        # Save to output CSV
        df_clean.to_csv(output_path, index=False)
        logging.info(f"Cleaned data saved to {output_path}")

        return df_clean

    except Exception as e:
        logging.error(f"Error occurred during cleaning: {e}")
        raise

def insert_to_postgres(df, table_name):
    try:
        engine = create_engine("postgresql://postgres:password@123@localhost:5432/postgres")
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f"Inserted cleaned data into PostgreSQL table '{table_name}'")
    except Exception as e:
        logging.error(f"Error inserting to PostgreSQL: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean a CSV file and load it into PostgreSQL.")
    parser.add_argument("--input", required=True, help="Path to raw input CSV")
    parser.add_argument("--output", required=True, help="Path to cleaned output CSV")
    parser.add_argument("--table", required=False, default="cleaned_users", help="PostgreSQL table name")

    args = parser.parse_args()
    df_clean = clean_data(args.input, args.output)
    insert_to_postgres(df_clean, args.table)