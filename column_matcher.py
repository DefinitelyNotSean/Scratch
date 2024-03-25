import json

# Step 1: Read fields from columns.txt and store them in a set
with open('columns.txt', 'r') as file:
    fields = {line.strip() for line in file}

# Step 2: Load the JSON document
with open('source_columns.json', 'r') as file:
    source_columns = json.load(file)

# Step 3: Check each column in the JSON document against the fields set
for column in source_columns:
    attributeName = column['attributeName']
    # Assuming FIELD_X matches exactly "attributeName": "FIELD_X"
    if attributeName in fields:
        print(f'{attributeName} found in columns.txt')
    else:
        print(f'{attributeName} not found in columns.txt')
