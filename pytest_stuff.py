# conftest.py

def pytest_collection_modifyitems(config, items):
    for item in items:
        # This will prepend the module name to the test name
        item.name = f"{item.module.__name__}_{item.name}"
        item._nodeid = f"{item.module.__name__}::{item.name}"
