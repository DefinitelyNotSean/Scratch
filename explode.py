import pandas as pd
import ast

# Function to convert string representations of lists into actual lists
def convert_to_list(string):
    try:
        return ast.literal_eval(string)
    except (ValueError, SyntaxError):
        return []

# Function to explode the dataframe
def explode_df_individually(df):
    # Convert string representations to actual lists
    for col in df.columns:
        df[col] = df[col].apply(convert_to_list)

    # Container for individually exploded dataframes
    exploded_dfs = []

    # Explode each list column individually
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            # Explode and store each individual dataframe
            exploded_dfs.append(df.explode(col))

    # Initialize final dataframe with the first exploded dataframe
    final_df = exploded_dfs[0]

    # Merge the rest of the exploded dataframes
    for edf in exploded_dfs[1:]:
        final_df = final_df.merge(edf, left_index=True, right_index=True)

    # Forward-fill the values for non-list columns
    final_df.ffill(inplace=True)

    return final_df


# Load the sample data from the provided file
file_path = '/path/to/your/eol data sample.xlsx'
df = pd.read_excel(file_path)

# Apply the function to the dataframe
exploded_df = explode_df_individually(df)

# Define the path for the new Excel file
output_file_path = '/path/to/your/output/exploded_eol_data.xlsx'

# Write the exploded dataframe to an Excel file
exploded_df.to_excel(output_file_path, index=False)
