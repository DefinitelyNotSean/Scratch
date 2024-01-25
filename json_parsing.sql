SELECT 
    TRY_CAST(
        OBJECT_CONSTRUCT(
            SPLIT_PART(value, ':', 1), 
            SPLIT_PART(value, ':', 2)
        ) AS JSON
    ) AS json_column,
    CASE
        WHEN TRY_CAST(
            OBJECT_CONSTRUCT(
                SPLIT_PART(value, ':', 1), 
                SPLIT_PART(value, ':', 2)
            ) AS JSON
        ) IS NULL THEN original_column
        ELSE NULL
    END AS parse_error
FROM (
    SELECT 
        original_column,
        SPLIT(original_column, ', ') AS value
    FROM your_table
)
