import pandas as pd
from pyspark.sql.types import *

# Read the Excel file
df = pd.read_excel('file.xlsx', sheet_name='sean_test', header=6)  # Skip first 6 rows as per your description

# Dictionary to map spreadsheet datatypes to PySpark DataTypes
data_types_dict = {
    'string': 'StringType()',
    'int': 'IntegerType()',
    'float': 'FloatType()',
    'timestamp': 'TimestampType()',
    'boolean': 'BooleanType()',
    'date': 'DateType()'
}

# Build the schema string
schema_str = 'from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, TimestampType, BooleanType, DateType\n\n'
schema_str += 'schema = StructType([\n'
for index, row in df.iterrows():
    attribute = row['A']  # Adjust column names as per your file
    data_type = row['B']  # Adjust column names as per your file
    if data_type.lower() in data_types_dict.keys():
        schema_str += f'    StructField("{attribute}", {data_types_dict[data_type.lower()]}, True),\n'
schema_str += '])'

# Write the schema code into a Python file
with open('schema.py', 'w') as file:
    file.write(schema_str)
