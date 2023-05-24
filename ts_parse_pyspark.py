from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import TimestampType, StringType
from datetime import datetime
import pytz

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [("1", "2022-02-11 15:16:29.185 -0500"), ("2", "2022-03-12 16:17:30.186 -0400")]
df = spark.createDataFrame(data, ["id", "time"])

# Define a UDF to convert the string to timestamp
def parse_timestamp(time_str):
    return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f %z')

udf_parse_timestamp = udf(parse_timestamp, TimestampType())

# Apply the UDF to convert the strings to timestamp
df = df.withColumn("time", udf_parse_timestamp(df.time))

# Convert the timestamp to UTC
df = df.withColumn("time_utc", df.time.cast('timestamp')).selectExpr("id", "from_utc_timestamp(time, 'UTC') as time_utc")

# Show the result
df.show(truncate=False)
