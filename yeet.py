import json

# Sample input JSON array
attributes_json = '''
[
    {"attributeName": "Color", "attributeDescription": "Describes the primary color"},
    {"attributeName": "Size", "attributeDescription": "Specifies the size of the item"}
]
'''

# Parse the JSON to a Python list
attributes = json.loads(attributes_json)

# New array to hold the transformed objects
transformed_attributes = []

for attribute in attributes:
    # Creating a new object with BEFORE_TEXT and AFTER_TEXT
    new_attribute = {
        "BEFORE_TEXT": "This is before the attribute details.",
        "attributeName": attribute["attributeName"],
        "attributeDescription": attribute["attributeDescription"],
        "AFTER_TEXT": "This comes after the attribute details."
    }
    transformed_attributes.append(new_attribute)

# Convert the transformed list back to JSON
transformed_json = json.dumps(transformed_attributes, indent=4)

print(transformed_json)
