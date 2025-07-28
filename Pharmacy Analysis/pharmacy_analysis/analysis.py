from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, row_number
from pyspark.sql.window import Window
import pandas as pd
from collections import Counter

def find_top_chains_spark(claims_df, pharmacies):


    spark = SparkSession.builder.appName("PharmacyAnalysis").master("local[10]").getOrCreate()

    claims_spark = spark.createDataFrame(claims_df)
    pharmacies_spark = spark.createDataFrame(pharmacies)
    claims_chains = claims_spark.join(pharmacies_spark, on="npi", how="left")
    chain_avg_price = claims_chains.groupBy("ndc", "chain").agg(avg("unit_price").alias("avg_price"))
    window_spec = Window.partitionBy("ndc").orderBy(col("avg_price").asc())
    top_chains = chain_avg_price.withColumn("rank", row_number().over(window_spec)).filter(col("rank") <= 2)
    top_chains_pd = top_chains.toPandas()
    return [
        {"ndc": ndc, "chain": group[["chain", "avg_price"]].to_dict(orient="records")}
        for ndc, group in top_chains_pd.groupby("ndc")
    ]

def find_most_common_quantities_spark(claims_df):

    spark = SparkSession.builder.appName("PharmacyAnalysis").master("local[10]").getOrCreate()
    claims_spark = spark.createDataFrame(claims_df)
    quantity_counts = claims_spark.groupBy("ndc", "quantity").count()
    window_spec = Window.partitionBy("ndc").orderBy(col("count").desc())
    top_quantities = quantity_counts.withColumn("rank", row_number().over(window_spec)).filter(col("rank") <= 5)
    top_quantities_pd = top_quantities.toPandas()
    return [
        {"ndc": ndc, "most_prescribed_quantity": list(group["quantity"])}
        for ndc, group in top_quantities_pd.groupby("ndc")
    ]
