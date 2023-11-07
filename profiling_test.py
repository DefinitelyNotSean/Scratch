import pandas as pd
from pandas_profiling import ProfileReport

# Replace 'your_data.parquet' with the path to your actual Parquet file
parquet_file_path = 'your_data.parquet'

# Read the Parquet file into a pandas DataFrame
df = pd.read_parquet(parquet_file_path)

# Generate the profiling report
profile = ProfileReport(df, title="Pandas Profiling Report")

# Export the profile report to a HTML file
# Replace 'profile_report.html' with the path and name you want for the report file
profile.to_file("profile_report.html")

print(f"Profile report generated: profile_report.html")
