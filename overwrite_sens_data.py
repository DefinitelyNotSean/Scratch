from pyspark.sql.functions import lit, rand

# Assuming df is your DataFrame
# List of sensitive columns
sensitive_cols = ['a', 'b']

for col in sensitive_cols:
    if str(df.schema[col].dataType) in ['IntegerType', 'LongType']:
        # If the column is of integer type, replace with random integers
        df = df.withColumn(col, (rand()*1000).cast('integer'))
    elif str(df.schema[col].dataType) in ['FloatType', 'DoubleType']:
        # If the column is of float type, replace with random floats
        df = df.withColumn(col, rand())
    elif str(df.schema[col].dataType) == 'StringType':
        # If the column is string type, replace with a constant string
        df = df.withColumn(col, lit('hidden'))
    # Add more conditions here for other data types as required
