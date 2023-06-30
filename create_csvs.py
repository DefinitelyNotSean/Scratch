import pandas as pd
import os

def create_csv_from_excel(file_name, sheet_name):
    # read the excel file, skipping the first 4 rows
    data = pd.read_excel(file_name, sheet_name=sheet_name, skiprows=range(4), engine='openpyxl')

    # create output directory if it does not exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # create raw.csv
    raw_df = data.iloc[:, 0:4]
    raw_df.to_csv('output/raw.csv', index=False)

    # create refined.csv
    refined_df = data.iloc[:, 12:16]
    refined_df.to_csv('output/refined.csv', index=False)

    # create modeled.csv
    modeled_df = data.iloc[:, 23:27]
    modeled_df.to_csv('output/modeled.csv', index=False)

# call the function with file name and sheet name
create_csv_from_excel('your_excel_file.xlsx', 'Sheet1')
