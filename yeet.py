import json

# Function to transform attributes
def transform_attributes(input_file, output_file):
    # Read the JSON data from the file
    with open(input_file, 'r') as file:
        attributes = json.load(file)

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

    # Write the transformed list back to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(transformed_attributes, file, indent=4)

# File paths
input_file = 'attributes.json'
output_file = 'transformed_attributes.json'

# Call the function with the file paths
transform_attributes(input_file, output_file)

print(f"Transformed attributes have been written to {output_file}.")
