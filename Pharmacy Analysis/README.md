# Pharmacy Analysis Project

## Overview

The **Pharmacy Analysis** project processes pharmacy-related data, including pharmacy details, claims, and reverts, using **PySpark**. The project aims to extract insights, generate reports, and optimize pharmacy operations based on data analysis.

## Features

- Reads and processes pharmacy, claims, and reverts data from JSON and CSV files.
- Performs data cleaning, transformation, and aggregation using **PySpark**.
- Generates summary reports and key business insights.
- Outputs processed data into structured JSON files for further analysis.

## Installation

### Prerequisites

Ensure you have the following installed before running the project:

- Python **3.7+**
- Java **8 or later** (for Apache Spark)
- Apache Spark **3.5.4** (configured with `SPARK_HOME`)
- Hadoop `winutils.exe` (for Windows users)

### Install Dependencies

To install the required Python packages, run:

```bash
pip install -r requirements.txt
```

Usage

To execute the pharmacy analysis pipeline, run the following command:

```bash
python main.py --pharmacy source/pharmacies --claims source/claims --reverts source/reverts --output output
```

### Command-line Arguments:

- `--pharmacy`  : Path to the pharmacy dataset (CSV files).
- `--claims`    : Path to the claims dataset (JSON files).
- `--reverts`   : Path to the reverts dataset (JSON files).
- `--output`    : Directory where the processed JSON reports will be saved.

## Output

After execution, the script generates the following reports in the `output/` directory:

- `claims_summary.json` – Summary of claims data (including fills, reverts, average price, and total price).
- `common_quantities.json` – Most commonly prescribed quantities for different drugs.
- `top_chains.json` – Top two pharmacy chains based on the lowest unit prices for each drug.



## Troubleshooting

- **PySpark Not Found:** Ensure `SPARK_HOME` and `PYSPARK_PYTHON` are correctly set in the environment variables.
- **Missing Dependencies:** Install them using `pip install -r requirements.txt`.
- **Incorrect File Paths:** Ensure input data is stored in the correct directories.
- **Permission Errors:** Run the script with appropriate permissions.




