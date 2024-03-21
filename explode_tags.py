from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, first

# Initialize SparkSession
spark = SparkSession.builder.appName("DynamicColumnsWithJoin").getOrCreate()

# Sample data with additional columns
data = [
    {
        "accountName": "cof-test",
        "region": "West",
        "isActive": True,
        "tags": [
            {"cloudTagKey": "tags.bogie:gear", "cloudTagValue": "waf"},
            {"cloudTagKey": "tags.managedBy", "cloudTagValue": "bog"},
            {"cloudTagKey": "tags.minimumAgeAspect", "cloudTagValue": "7"}
        ]
    },
    {
        "accountName": "cof-next",
        "region": "East",
        "isActive": False,
        "tags": [
            {"cloudTagKey": "tags.location", "cloudTagValue": "NY"},
            {"cloudTagKey": "tags.department", "cloudTagValue": "HR"},
            {"cloudTagKey": "tags.project", "cloudTagValue": "Alpha"}
        ]
    }
]

# Create DataFrame
df = spark.createDataFrame(data)

# Create a version of the DataFrame for the pivot operation
df_tags = (df
           .select(col("accountName"), explode(col("tags")).alias("exploded_tags"))
           .select("accountName",
                   col("exploded_tags.cloudTagKey").alias("cloudTagKey"),
                   col("exploded_tags.cloudTagValue").alias("cloudTagValue"))
           .groupBy("accountName")
           .pivot("cloudTagKey")
           .agg(first("cloudTagValue"))
          )

# Join the pivoted DataFrame back with the original DataFrame
# Assuming 'accountName' is unique, or you have a unique identifier to join on
df_joined = df.join(df_tags, "accountName")

# Show the result
df_joined.show()
