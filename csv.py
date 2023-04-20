from pyspark.sql import SparkSession

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("Read CSV File") \
    .master("local") \
    .getOrCreate()

# Replace the file path with the actual path to your CSV file in the Downloads folder
file_path = "/Users/your_username/Downloads/your_file.csv"

# Read the CSV file
csv_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the first few rows of the DataFrame
csv_df.show()

# Stop the Spark session
spark.stop()
