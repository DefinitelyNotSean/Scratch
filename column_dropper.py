# Step 1: Read the file
with open('your_file.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Strip each line
stripped_lines = [line.strip() for line in lines if line.strip() != '']

# Step 3: Add to list and Step 4: Convert to desired format
formatted_string = "tests = ['" + "', '".join(stripped_lines) + "']"

print(formatted_string)
