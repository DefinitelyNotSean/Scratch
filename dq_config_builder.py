import pandas as pd

# Create a mapping dictionary for data types
mapping = {
    'string': 'StringType',
    'int': 'IntegerType',
    'float': 'FloatType',
    'timestamp': 'TimestampType',
    'boolean': 'BooleanType'
}

# Load the text data
df = pd.read_csv('your_file.txt', sep='\s+', names=['attribute', 'data type', 'required'])

# Iterate over the dataframe rows
for index, row in df.iterrows():
    attr = row['attribute']
    dtype = mapping[row['data type']]
    req = row['required']  

    # Create dictionary and print
    result = {'col': attr, 'type': dtype, 'required': req}
    print(result)
