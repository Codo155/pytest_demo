import pytest

# Session-level setup
def pytest_sessionstart(session):
    print("Session setup: Runs once before all tests")

def pytest_sessionfinish(session, exitstatus):
    print("Session teardown: Runs once after all tests")