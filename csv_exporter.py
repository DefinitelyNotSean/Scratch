from openpyxl import load_workbook
import csv
import os

def create_csv_from_excel(file_name, sheet_name):
    # load the workbook
    wb = load_workbook(filename=file_name, read_only=True, data_only=True)
    ws = wb[sheet_name]

    # create output directory if it does not exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # define output files
    output_files = {
        'output/raw.csv': [1, 2, 3, 4],   # columns A-D
        'output/refined.csv': [13, 14, 15, 16],   # columns M-P
        'output/modeled.csv': [24, 25, 26, 27]  # columns X-AA
    }

    # for each output file
    for output_file, columns in output_files.items():
        # open the CSV file
        with open(output_file, 'w', newline='') as f:
            c = csv.writer(f)
            # for each row in the worksheet
            for i, row in enumerate(ws.values, start=1):
                # skip the first 4 rows
                if i <= 4:
                    continue
                # write the desired columns to the CSV file
                c.writerow([cell for j, cell in enumerate(row, start=1) if j in columns])

# call the function with file name and sheet name
create_csv_from_excel('your_excel_file.xlsx', 'Sheet1')
