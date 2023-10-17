from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SnowflakeToPySpark").getOrCreate()

# Snowflake options
sfOptions = {
    "sfDatabase" : "YOUR_DATABASE",
    "sfSchema" : "YOUR_SCHEMA",
    "sfRole" : "YOUR_ROLE",
    "sfWarehouse" : "YOUR_WAREHOUSE",
    "sfURL" : "YOUR_SNOWFLAKE_URL",
    "sfRole" : "YOUR_ROLE",
    "dbtable" : "YOUR_TABLE_OR_QUERY",
    "user" : "YOUR_USERNAME",
    "password" : "YOUR_PASSWORD"
}

# Read data from Snowflake
df = spark.read.format("snowflake").options(**sfOptions).load()

df.show()

# If you want to see the schema (to confirm ArrayType or any other type)
df.printSchema()
