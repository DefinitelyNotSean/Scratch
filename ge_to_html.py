import json
from IPython.display import HTML, display

# Sample great_expectations output in JSON format
great_expectations_json = """
{
    "success": true,
    "results": [
        {
            "expectation_type": "expect_column_values_to_be_unique",
            "kwargs": {"column": "customer_id"},
            "success": true,
            "result": {"element_count": 100, "unexpected_count": 0, "unexpected_percent": 0.0}
        },
        {
            "expectation_type": "expect_table_row_count_to_be_between",
            "kwargs": {"min_value": 50, "max_value": 150},
            "success": true,
            "result": {"observed_value": 100}
        },
        {
            "expectation_type": "expect_column_values_to_not_be_null",
            "kwargs": {"column": "order_date"},
            "success": false,
            "result": {"element_count": 100, "unexpected_count": 3, "unexpected_percent": 3.0}
        }
    ]
}
"""

# Parse the JSON string
great_expectations_data = json.loads(great_expectations_json)

# HTML template for displaying the data
html_template = """
<h2>Great Expectations Validation Results</h2>
<table border="1">
    <tr>
        <th>Expectation Type</th>
        <th>Parameters</th>
        <th>Success</th>
        <th>Details</th>
    </tr>
    {rows}
</table>
"""

# Generate table rows from the data
rows = ""
for result in great_expectations_data["results"]:
    rows += f"""
    <tr>
        <td>{result['expectation_type']}</td>
        <td>{json.dumps(result['kwargs'])}</td>
        <td>{'✅' if result['success'] else '❌'}</td>
        <td>{json.dumps(result['result'])}</td>
    </tr>
    """

# Complete HTML
complete_html = html_template.format(rows=rows)

# Display the HTML
display(HTML(complete_html))
