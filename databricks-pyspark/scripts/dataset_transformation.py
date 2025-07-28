
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("DatasetTransformation").getOrCreate()

df = spark.read.csv("../data/sample_dataset.csv", header=True, inferSchema=True)

# Filter age > 30
filtered = df.filter(col("age") > 30)

# Add new column
transformed = filtered.withColumn("salary_plus_bonus", col("salary") * 1.1)

# Show result
transformed.show()
