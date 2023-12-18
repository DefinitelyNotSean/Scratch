SELECT 
    REGEXP_SUBSTR(table_name, '^(ipal_[^_]+)') AS base_name,
    MAX(COALESCE(NULLIF(REGEXP_SUBSTR(table_name, '_v([0-9]+)$'), ''), '0')) AS max_version
FROM information_schema.views
WHERE table_schema = 'phdp' 
    AND table_name LIKE 'ipal%'
GROUP BY base_name;


Base Name Extraction: The REGEXP_SUBSTR(table_name, '^(ipal_[^_]+)') directly extracts the base name from the table name in the SELECT clause. It captures the portion of the table name up to the first underscore following 'ipal'.

Version Number Extraction and Defaulting: The version number extraction and defaulting to '0' for non-versioned tables are combined into a single line using COALESCE and NULLIF. The REGEXP_SUBSTR function extracts the version number, and NULLIF converts any empty result to NULL. COALESCE then defaults these NULL values to '0'.

Grouping and Maximum Version Calculation: The query groups by the base name and calculates the maximum version for each group, just as in the previous query.
