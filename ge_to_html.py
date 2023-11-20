# Improved HTML template with some basic styling for better appearance

improved_html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Great Expectations Results</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
        }
        h2 {
            color: #5D5C61;
        }
        table {
            margin: 20px auto;
            border-collapse: collapse;
            width: 80%;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #577590;
            color: white;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
        .success {
            color: green;
        }
        .failure {
            color: red;
        }
    </style>
</head>
<body>
    <h2>Great Expectations Validation Results</h2>
    <table>
        <tr>
            <th>Expectation Type</th>
            <th>Parameters</th>
            <th>Success</th>
            <th>Details</th>
        </tr>
        {rows}
    </table>
</body>
</html>
"""

# Sample data (for demonstration purposes)
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

# Generate table rows with styling based on success or failure
rows = ""
for result in great_expectations_data["results"]:
    success_class = "success" if result['success'] else "failure"
    rows += f"""
    <tr>
        <td>{result['expectation_type']}</td>
        <td>{json.dumps(result['kwargs'])}</td>
        <td class="{success_class}">{result['success']}</td>
        <td>{json.dumps(result['result'])}</td>
    </tr>
    """

# Complete HTML with styling
improved_complete_html = improved_html_template.format(rows=rows)

# Write HTML to a file
with open("/mnt/data/great_expectations_results_styled.html", "w") as file:
    file.write(improved_complete_html)

"HTML file created with improved styling. You can download and view it in a web browser."

