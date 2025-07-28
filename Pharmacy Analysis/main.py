import argparse
import logging
import time
from pathlib import Path
from pharmacy_analysis import load_csv_files, load_json_files, process_claims, find_top_chains_spark, \
    find_most_common_quantities_spark, setup_logging, save_json


setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Process pharmacy claims data.")
    parser.add_argument("--pharmacy", required=True, help="Path to pharmacy dataset directory")
    parser.add_argument("--claims", required=True, help="Path to claims dataset directory")
    parser.add_argument("--reverts", required=True, help="Path to reverts dataset directory")
    parser.add_argument("--output", required=True, help="Output directory")

    args = parser.parse_args()

    source_dir = Path(args.pharmacy)
    claims_dir = Path(args.claims)
    reverts_dir = Path(args.reverts)
    output_dir = Path(args.output)


    try:
        output_dir.mkdir(exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create output directory: {e}")
        return

    logging.info("Loading data...")
    start_time = time.time()

    try:
        pharmacies = load_csv_files(source_dir)
        claims_df = load_json_files(claims_dir)
        reverts_df = load_json_files(reverts_dir)
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return


    if claims_df.empty or reverts_df.empty:
        logging.warning("Claims or reverts data is empty. Exiting process.")
        return

    logging.info("Processing claims data...")
    try:
        final_summary = process_claims(claims_df, reverts_df)
        save_json(final_summary.to_dict(orient="records"), output_dir / "claims_summary.json")
    except Exception as e:
        logging.error(f"Error processing claims data: {e}")
        return

    logging.info("Finding top pharmacy chains per drug using Spark...")
    try:
        top_chains_output = find_top_chains_spark(claims_df, pharmacies)
        save_json(top_chains_output, output_dir / "top_chains.json")
    except Exception as e:
        logging.error(f"Error in finding top chains: {e}")

    logging.info("Identifying most common quantities using Spark...")
    try:
        quantity_output = find_most_common_quantities_spark(claims_df)
        save_json(quantity_output, output_dir / "common_quantities.json")
    except Exception as e:
        logging.error(f"Error in finding most common quantities: {e}")

    elapsed_time = time.time() - start_time
    logging.info(f"Processing complete! Execution time: {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
