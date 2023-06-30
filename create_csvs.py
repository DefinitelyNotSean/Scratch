import pandas as pd
import os

def create_csv_from_excel(file_name, sheet_name):
    # read the sheet of the excel file
    df = pd.read_excel(file_name, sheet_name=sheet_name, engine='openpyxl')

    # create output directory if it does not exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # create raw.csv
    raw_df = df.iloc[4:, 0:4]
    raw_df.to_csv('output/raw.csv', index=False)

    # create refined.csv
    refined_df = df.iloc[4:, 12:16]
    refined_df.to_csv('output/refined.csv', index=False)

    # create modeled.csv
    modeled_df = df.iloc[4:, 23:27]
    modeled_df.to_csv('output/modeled.csv', index=False)

# call the function with file name and sheet name
create_csv_from_excel('your_excel_file.xlsx', 'Sheet1')
