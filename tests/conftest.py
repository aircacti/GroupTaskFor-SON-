import pytest
from main import AttendanceManager, attendance_manager

manager = attendance_manager

@pytest.fixture(scope="module")
def attendance_manager():
    return manager
