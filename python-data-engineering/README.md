# Python for Data Engineering

This project demonstrates a CLI-based Python data cleaning tool, structured for maintainability and testing.

##  Features
- Input: CSV file
- Cleaning: Drops rows with NULLs
- Output: Clean CSV ready for PostgreSQL load
- Logs: Stored in 'logs/cleaning.log'
- Testable design (with 'pytest')

##  Project Structure
'''
python-data-engineering/
├── src/
│   └── clean_csv.py
├── tests/
│   └── test_clean_csv.py
├── data/
│   └── raw_users.csv
├── logs/
├── README.md
'''

##  Run Cleaning
'''bash
python src/clean_csv.py --input data/raw_users.csv --output data/cleaned_users.csv
'''

##  Run Tests
'''bash
pytest tests/test_clean_csv.py
'''