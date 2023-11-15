from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
import json

# Initialize Spark session
spark = SparkSession.builder.appName("DataQualityChecks").getOrCreate()

# Perform your data validation
validation_results = ge_df.validate()

# Convert validation results to a JSON serializable dictionary
results_dict = validation_results.to_json_dict()

# Convert the dictionary to a JSON string
results_json = json.dumps(results_dict, indent=4)

# Define the schema for the DataFrame
schema = StructType([
    StructField("dataset_name", StringType(), True),
    StructField("load_timestamp", TimestampType(), True),
    StructField("results", StringType(), True)
])

# Create a DataFrame with the desired columns and schema
data = [("trex", current_timestamp(), results_json)]
results_df = spark.createDataFrame(data, schema)

# Show the DataFrame
results_df.show(truncate=False)

# Optionally, save the DataFrame
# results_df.write.format("your_preferred_format").save("your_preferred_path")
