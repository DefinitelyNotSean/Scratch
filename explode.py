import pandas as pd
import ast

# Function to convert string representations of lists into actual lists
def convert_to_list(string):
    try:
        return ast.literal_eval(string)
    except (ValueError, SyntaxError):
        return []

# Function to explode the dataframe
def explode_df_with_list_conversion(df):
    # Convert string representations of lists into actual lists
    for col in df.columns:
        df[col] = df[col].apply(convert_to_list)

    # Identify columns that contain lists
    list_columns = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, list)).any()]

    # Create a copy of the dataframe to avoid modifying the original
    temp_df = df.copy()

    # Explode each list column individually
    for col in list_columns:
        temp_df = temp_df.explode(col)
    
    return temp_df

# Load the sample data from the provided file
file_path = '/path/to/your/eol data sample.xlsx'
df = pd.read_excel(file_path)

# Apply the function to the dataframe
exploded_df = explode_df_with_list_conversion(df)

# Define the path for the new Excel file
output_file_path = '/path/to/your/output/exploded_eol_data.xlsx'

# Write the exploded dataframe to an Excel file
exploded_df.to_excel(output_file_path, index=False)
