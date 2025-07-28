# Databricks & PySpark

This project demonstrates basic and advanced PySpark usage on Databricks. It includes SQL-like operations, DataFrame transformations, and a comparison with Pandas and SQL.

##  Structure

- `notebooks/` — Exported Databricks notebook (.html)
- `scripts/` — PySpark scripts:
  - `sql_exercises_pyspark.py`: Simple SQL queries using Spark
  - `complex_sql_exercises_pyspark.py`: Advanced SQL with window functions and subqueries
  - `dataset_transformation.py`: Dataset filtering and transformation
- `data/` — Sample CSV dataset
- `performance_notes.md`: Summary of performance and development experience

##  How to Run

1. Upload this project to Databricks workspace.
2. Use a Databricks notebook to test each script.
3. View the notebook export via web browser.

##  Dataset
The sample dataset includes columns: `id`, `name`, `age`, `salary`