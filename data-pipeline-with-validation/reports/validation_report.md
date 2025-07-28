# Validation Plan & Output Report

##  Validation Rules Implemented:
1. **Not Null Check** for 'email' column
2. **Uniqueness Check** for 'id' column

##  Output Summary:
- Duplicates removed
- Null values checked
- If all checks pass: Data saved to 'processed_data.csv'
- If any check fails: Pipeline logs warning and halts

##  Log File:
- Location: 'logs/etl_pipeline.log'
- Logs include:
  - Step-by-step progress
  - Validation results
  - Final status

##  Sample Results:
- Input: 5 rows  
- Output after clean: 4 rows  
- Validation: One row had null email → causes failure (expected behavior)

##  Final Outcome:
Logs and validation help ensure clean, trustworthy output before saving.