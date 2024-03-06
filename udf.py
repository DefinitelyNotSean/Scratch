from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import BooleanType
import json

# Create Spark session
spark = SparkSession.builder.appName("Validate JSON without Schema").getOrCreate()

# Example DataFrame with a string column containing JSON
data = [("{'name':'John', 'age':30}",), ("Invalid JSON",), ("{'name':'Jane', 'age':25}",)]
df = spark.createDataFrame(data, ["json_string"])

# Define a Python function to check if a string is valid JSON
def is_valid_json(string):
    try:
        json.loads(string)
        return True
    except ValueError:
        return False

# Register the Python function as a UDF
is_valid_json_udf = udf(is_valid_json, BooleanType())

# Apply the UDF to your DataFrame
df = df.withColumn("is_valid_json", is_valid_json_udf(col("json_string")))

# Show the results
df.show(truncate=False)
