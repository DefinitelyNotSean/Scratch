import json
import pandas as pd
from prettytable import PrettyTable
from colorama import Fore, Style

# Load the Excel spreadsheet
def load_excel(file_name, sheet_name):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=5, usecols="V:X")
    df.columns = ['name', 'datatype', 'isRequired']
    return {item['name']: item.to_dict() for _, item in df.iterrows()}

# Load JSON data
def load_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    transformed_data = [{'name': item['name'], 'datatype': item['type'], 'isRequired': item['dmslCatalog']['dataQualityDetails']['isOptional']} for item in data['fields']]
    return {item['name']: item for item in transformed_data}

# Compare columns and print results
def compare_columns(excel_data, json_data):
    table = PrettyTable()
    table.field_names = ["Excel Name", "JSON Name", "Excel DataType", "JSON DataType",
                         "Excel IsRequired", "JSON IsRequired", "Match"]

    all_keys = set(excel_data.keys()) | set(json_data.keys())

    for key in all_keys:
        e_item = excel_data.get(key)
        j_item = json_data.get(key)

        if e_item and j_item:
            e_item['isRequired'] = bool(e_item['isRequired'])
            j_item['isRequired'] = bool(j_item['isRequired'])

            if e_item == j_item:
                table.add_row([Fore.GREEN + e_item['name'] + Style.RESET_ALL,
                               Fore.GREEN + j_item['name'] + Style.RESET_ALL,
                               Fore.GREEN + e_item['datatype'] + Style.RESET_ALL,
                               Fore.GREEN + j_item['datatype'] + Style.RESET_ALL,
                               Fore.GREEN + str(e_item['isRequired']) + Style.RESET_ALL,
                               Fore.GREEN + str(j_item['isRequired']) + Style.RESET_ALL,
                               Fore.GREEN + "True" + Style.RESET_ALL])
            else:
                datatype_cell = (Fore.GREEN if e_item['datatype'] == j_item['datatype']
                                 else Fore.LIGHTRED_EX + Style.BRIGHT) + e_item['datatype'] + Style.RESET_ALL
                json_datatype_cell = (Fore.GREEN if e_item['datatype'] == j_item['datatype']
                                       else Fore.LIGHTRED_EX + Style.BRIGHT) + j_item['datatype'] + Style.RESET_ALL

                isrequired_cell = (Fore.GREEN if e_item['isRequired'] == j_item['isRequired']
                                   else Fore.LIGHTRED_EX + Style.BRIGHT) + str(e_item['isRequired']) + Style.RESET_ALL
                json_isrequired_cell = (Fore.GREEN if e_item['isRequired'] == j_item['isRequired']
                                         else Fore.LIGHTRED_EX + Style.BRIGHT) + str(j_item['isRequired']) + Style.RESET_ALL

                table.add_row([Fore.RED + e_item['name'] + Style.RESET_ALL,
                               Fore.RED + j_item['name'] + Style.RESET_ALL,
                               datatype_cell, json_datatype_cell,
                               isrequired_cell, json_isrequired_cell,
                               Fore.RED + "False" + Style.RESET_ALL])
        else:
            excel_name_cell = (Fore.RED + key + Style.RESET_ALL) if e_item else "N/A"
            json_name_cell = (Fore.RED + key + Style.RESET_ALL) if j_item else "N/A"

            datatype_cell = (Fore.RED + e_item['datatype'] + Style.RESET_ALL) if e_item else "N/A"
            json_datatype_cell = (Fore.RED + j_item['datatype'] + Style.RESET_ALL) if j_item else "N/A"

            isrequired_cell = (Fore.RED + str(e_item['isRequired']) + Style.RESET_ALL) if e_item else "N/A"
            json_isrequired_cell = (Fore.RED + str(j_item['isRequired']) + Style.RESET_ALL) if j_item else "N/A"

            table.add_row([excel_name_cell, json_name_cell,
                           datatype_cell, json_datatype_cell,
                           isrequired_cell, json_isrequired_cell,
                           Fore.RED + "False" + Style.RESET_ALL])

    print(table)

# Main function
def main():
    excel_file = 'your_excel_file.xlsx'  # Replace with your file name
    json_file = 'your_json_file.json'    # Replace with your file name

    excel_data = load_excel(excel_file, 'prime_issue')
    json_data = load_json(json_file)
    compare_columns(excel_data, json_data)

if __name__ == "__main__":
    main()
    
    
    json_datatype_cell = (Fore.GREEN if e_item['datatype'] == j_item['datatype']
                      else Fore.LIGHTRED_EX + Style.BRIGHT) + j_item['datatype'] + Style.RESET_ALL


