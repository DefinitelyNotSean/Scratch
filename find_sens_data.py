import pandas as pd

# Read the Excel file
df = pd.read_excel('file.xlsx', sheet_name='sean_test', header=6)  # Skip first 6 rows as per your description

# Identify sensitive columns based on your criteria
sensitive_cols = df.loc[df[['F', 'G', 'H', 'I']].notna().any(axis=1), 'Attribute Name'].tolist()

# Open the file for writing
with open('sensitive_cols.py', 'w') as file:
    # Write the sensitive_cols list to the file
    file.write(f'sensitive_cols = {sensitive_cols}\n')
