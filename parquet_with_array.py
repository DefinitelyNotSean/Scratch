from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType

# Create a SparkSession
spark = SparkSession.builder.appName("NullableArrayExample").getOrCreate()

# Define the schema for the DataFrame
schema = StructType([
    StructField("id", StringType(), True),
    StructField("names", ArrayType(StringType(), True), True)
])

# Create the DataFrame
data = [("1", ["John", "Doe", None]), ("2", ["Jane", None, "Doe"])]
df = spark.createDataFrame(data, schema)

# Write the DataFrame to a Parquet file
df.write.mode("overwrite").parquet("/path/to/parquet/file")
