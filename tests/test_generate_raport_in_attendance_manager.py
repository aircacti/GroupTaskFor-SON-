import pytest

@pytest.mark.run(order=4)
def test_generate_raport_in_attendance_manager(capfd, attendance_manager):
    output = attendance_manager.generate_report()
    assert output == 'Attendance Report:\nUser 6000:\n  - 2024-11-28: False\n'
