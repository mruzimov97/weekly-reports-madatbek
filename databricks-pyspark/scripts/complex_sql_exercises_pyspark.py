
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, avg, rank, sum as _sum

spark = SparkSession.builder.appName("ComplexSQLExercises").getOrCreate()

# Load dataset
df = spark.read.csv("../data/sample_dataset.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("people")

# Sample department data
departments = spark.createDataFrame([
    (1, "HR"), (2, "Engineering"), (3, "Marketing"), (4, "Finance")
], ["id", "department"])
departments.createOrReplaceTempView("departments")

# Join datasets
joined_df = spark.sql("""
    SELECT p.*, d.department
    FROM people p
    JOIN departments d ON p.id = d.id
""")
joined_df.createOrReplaceTempView("people_with_dept")

# Window function: rank employees within department by salary
ranked = spark.sql("""
    SELECT *,
           RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
    FROM people_with_dept
""")
ranked.show()

# Subquery: department with total salary > 100000
high_salary_depts = spark.sql("""
    SELECT department
    FROM people_with_dept
    GROUP BY department
    HAVING SUM(salary) > 100000
""")
high_salary_depts.show()

# Multi-level aggregation: average salary by department for people over 30
avg_salary = spark.sql("""
    SELECT department, AVG(salary) AS avg_salary
    FROM people_with_dept
    WHERE age > 30
    GROUP BY department
""")
avg_salary.show()
