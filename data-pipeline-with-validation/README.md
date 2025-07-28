# Data Pipeline with Validation

This project demonstrates an ETL pipeline with data validation checks and logging.

##  Pipeline Steps
1. Ingest data from CSV
2. Clean data (drop duplicates)
3. Validate:
   - No nulls in `email`
   - Unique `id`s
4. Save final output if all validations pass

## Folder Structure
- `scripts/etl_pipeline.py` — main ETL script
- `tests/` — test cases for validation and cleaning
- `logs/` — logs of each run
- `reports/` — validation plan and sample output
- `data/` — raw and processed data

## Run
```bash
python scripts/etl_pipeline.py
```

## Tests
```bash
pytest tests/test_etl_pipeline.py
```