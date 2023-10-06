import pandas as pd
import pyarrow.parquet as pq

# Read the parquet file into a PyArrow table
table = pq.read_table('path/to/parquet/file')

# Convert the table to a Pandas DataFrame
df = table.to_pandas()

# Get the names of columns with null values
null_cols = df.columns[df.isnull().any()].tolist()

# Print the names of columns with null values
print("Columns with null values:", null_cols)
