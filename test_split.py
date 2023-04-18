from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Folderpath to Business Entity Levels") \
    .getOrCreate()

# Sample data with folderpath column
data = [
    ("/capital two/Enterprise Services/Tech/Card Tech/ISSU-01114101",),
]

# Create DataFrame
schema = "folderpath STRING"
df = spark.createDataFrame(data, schema)

# Split folderpath and create new columns
df = df.withColumn("business_entity_level_1", split(col("folderpath"), "/")[2]) \
    .withColumn("business_entity_level_2", split(col("folderpath"), "/")[3]) \
    .withColumn("business_entity_level_3", split(col("folderpath"), "/")[4])

# Show the resulting DataFrame
df.select("folderpath", "business_entity_level_1", "business_entity_level_2", "business_entity_level_3").show(truncate=False)

# Stop the Spark session
spark.stop()
