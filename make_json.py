# 1.
from pyspark.sql.functions import regexp_replace, from_json
from pyspark.sql.types import MapType, StringType, IntegerType

# Replace formatting to make it JSON-like
formatted_df = df.withColumn('json_like', regexp_replace('raw_string', '(\\w+\\s*\\w*\\s*\\w*\\s*\\w*):(\\d)', '"\\1": \\2'))

# Define the schema
schema = MapType(StringType(), IntegerType())

# Convert to JSON
json_df = formatted_df.withColumn('json', from_json('json_like', schema))

json_df.show(truncate=False)

# 2. 
from pyspark.sql.functions import split, expr

# Split string into array of key-value pairs
df2 = df.withColumn("key_value_pairs", split("raw_string", ", "))

# Convert array to map
df_json = df2.withColumn("json", expr("map_from_entries(transform(key_value_pairs, x -> struct(split(x, ': ')[0] as key, int(split(x, ': ')[1]) as value)))"))

df_json.show(truncate=False)

# 3.
from pyspark.sql.functions import udf
import json

def simple_string_to_json(s):
    return json.dumps(dict(item.split(":") for item in s.split(", ")))

simple_json_udf = udf(simple_string_to_json)

df.withColumn("json", simple_json_udf("raw_string")).show(truncate=False)
