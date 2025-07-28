# Performance & Challenges Summary

##  PySpark vs SQL

- PySpark syntax is less concise than SQL but provides better scalability for large datasets.
- Spark SQL queries are almost identical to standard SQL, making migration easy.

##  PySpark vs Pandas

- Pandas is easier for small datasets and quick iterations.
- PySpark is preferred for distributed processing and handling larger datasets.

##  Challenges

- Managing schema inference can be tricky in CSV-based ingestion.
- Column operations in PySpark are verbose compared to Pandas.
- Spark’s lazy evaluation requires understanding of execution plans for performance tuning.

##  Notes

- Joins and aggregations run efficiently in Spark, especially when caching or repartitioning is used.
- Debugging in PySpark requires more setup compared to Pandas.