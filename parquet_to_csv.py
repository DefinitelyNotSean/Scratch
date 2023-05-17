from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Parquet to CSV") \
    .getOrCreate()

# Read the parquet file
parquet_file_path = "file:///Users/<your_username>/Downloads/yourfile.parquet"
df = spark.read.parquet(parquet_file_path)

# Write to CSV
csv_output_path = "file:///Users/<your_username>/Downloads/output.csv"
df.write.csv(csv_output_path)

# Stop the SparkSession
spark.stop()
