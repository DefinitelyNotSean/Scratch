from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StringType, ArrayType, StructType, StructField

# Initialize Spark Session
spark = SparkSession.builder.appName("simplified_json_expansion").getOrCreate()

# Sample data
data = [
    ("Business1", "Owner1", "Product1", "Opportunity1", '[{"key" : "ASV", "value": "test"}, {"key" : "ASV2", "value": "test2"}, {"key" : "name", "value": "sean"}, {"key" : "ownerrr", "value": "Bill"}]'),
]

# Define schema
schema = "business STRING, owner STRING, product STRING, opportunity STRING, label STRING"

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Define the schema for the JSON structure in the 'label' column
# json_schema = ArrayType(StructType([
#     StructField("key", StringType()),
#     StructField("value", StringType())
# ]))

json_schema = "ARRAY<STRUCT<key: STRING, value: STRING>>"

# Parse the JSON string in the 'label' column
df = df.withColumn("label_parsed", from_json("label", json_schema))

# Extract and create new columns based on specific keys
df = df.selectExpr(
    "*",
    "filter(label_parsed, x -> x.key = 'ASV')[0].value as label_asv",
    "filter(label_parsed, x -> x.key = 'ASV2')[0].value as label_asv2",
    "filter(label_parsed, x -> x.key = 'name')[0].value as label_name",
    "filter(label_parsed, x -> x.key = 'owner')[0].value as label_owner"
)

df = df.drop('label_parsed')

# Show the result
df.show(truncate=False)
