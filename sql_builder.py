import pandas as pd

# Read the Excel file
df = pd.read_excel('file.xlsx', sheet_name='sean_test', header=6)  # Skip first 6 rows as per your description

# Initiate an empty string for the query
query = ''

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Extract the content of the 'Source Query' column
    query_part = row['Source Query']  # replace with the actual column name if different
    if pd.notna(query_part):  # Only process if query is not NaN
        # Append the query part to the main query
        query += str(query_part) + ' '

# Open the file for writing
with open('query.py', 'w') as file:
    # Write the query to the file within triple quotes
    file.write(f'"""\n{query}\n"""\n')
