import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import attendance_manager

manager = attendance_manager

@pytest.fixture(scope="module")
def attendance_manager():
    return manager



