import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

def main():
    json_string = '{"name": "John", "age": 30, "city": "New York"}'
    formatted_json = format_json(json_string)
    highlighted_json = highlight_json(formatted_json)
    print("Formatted and highlighted JSON:")
    print(highlighted_json)

def format_json(json_string):
    json_data = json.loads(json_string)
    formatted_json = json.dumps(json_data, indent=4, sort_keys=True)
    return formatted_json

def highlight_json(formatted_json):
    highlighted_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())
    return highlighted_json

if __name__ == "__main__":
    main()
