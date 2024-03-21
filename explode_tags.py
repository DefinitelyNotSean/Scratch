from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, first, lit

# Initialize SparkSession
spark = SparkSession.builder.appName("DynamicColumnsWithExtras").getOrCreate()

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

# Transform DataFrame
df_transformed = (df
                  # Explode 'tags' while keeping all other columns
                  .select("*", explode("tags").alias("exploded_tags"))
                  .select(
                      "accountName",
                      "region",
                      "isActive",
                      col("exploded_tags.cloudTagKey").alias("cloudTagKey"),
                      col("exploded_tags.cloudTagValue").alias("cloudTagValue")
                  )
                  # Group and pivot
                  .groupBy("accountName", "region", "isActive")
                  .pivot("cloudTagKey")
                  .agg(first("cloudTagValue"))
                 )

# Show the transformed DataFrame
df_transformed.show()
