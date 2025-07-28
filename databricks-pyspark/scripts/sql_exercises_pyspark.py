
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("SQLExercises").getOrCreate()

# Load sample dataset
df = spark.read.csv("../data/sample_dataset.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("people")

# 1.  SELECT and WHERE
adults = spark.sql("SELECT * FROM people WHERE age > 30")
adults.show()

# 2. Aggregation
avg_salary = spark.sql("SELECT AVG(salary) AS avg_salary FROM people")
avg_salary.show()

# 3. Join with another small dataset
departments = spark.createDataFrame([
    (1, "HR"), (2, "Engineering"), (3, "Marketing"), (4, "Finance")
], ["id", "department"])

joined = df.join(departments, on="id")
joined.show()
