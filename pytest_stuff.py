# conftest.py


spark-submit --packages net.snowflake:snowflake-jdbc:3.13.4,net.snowflake:spark-snowflake_2.12:2.9.2 ...


def pytest_collection_modifyitems(config, items):
    for item in items:
        # This will prepend the module name to the test name
        item.name = f"{item.module.__name__}_{item.name}"
        item._nodeid = f"{item.module.__name__}::{item.name}"
