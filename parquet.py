from pyspark.sql import SparkSession

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("Read Parquet File") \
    .master("local") \
    .getOrCreate()

# Replace the file path with the actual path to your Parquet file in the Downloads folder
file_path = "/Users/your_username/Downloads/your_file.parquet"

# Read the Parquet file
parquet_df = spark.read.parquet(file_path)

# Show the first few rows of the DataFrame
parquet_df.show()

# Stop the Spark session
spark.stop()
