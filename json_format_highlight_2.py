import json
from termcolor import colored

def colorize_json_element(key, value):
    key_color = 'cyan'

    if isinstance(value, str):
        value_color = 'green'
    elif isinstance(value, (int, float)):
        value_color = 'yellow'
    elif isinstance(value, bool):
        value_color = 'magenta'
    elif value is None:
        value_color = 'white'
    else:
        return colored(key, key_color), value

    return colored(key, key_color), colored(value, value_color)

def format_and_colorize_json(json_data, indent=0):
    if isinstance(json_data, dict):
        formatted_json = '{\n'
        for key, value in json_data.items():
            colored_key, colored_value = colorize_json_element(key, value)
            formatted_json += '  ' * (indent + 1) + f'{colored_key}: {format_and_colorize_json(colored_value, indent + 1)},\n'
        formatted_json = formatted_json.rstrip(',\n') + '\n' + '  ' * indent + '}'
    elif isinstance(json_data, list):
        formatted_json = '[\n'
        for value in json_data:
            formatted_json += '  ' * (indent + 1) + f'{format_and_colorize_json(value, indent + 1)},\n'
        formatted_json = formatted_json.rstrip(',\n') + '\n' + '  ' * indent + ']'
    else:
        _, colored_value = colorize_json_element('', json_data)
        formatted_json = colored_value

    return formatted_json

if __name__ == '__main__':
    json_string = '{"name": "John", "age": 30, "city": "New York", "active": true, "pets": ["dog", "cat"], "extra": null}'
    json_data = json.loads(json_string)
    colored_formatted_json = format_and_colorize_json(json_data)
    print(colored_formatted_json)
