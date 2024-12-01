import pytest

@pytest.mark.run(order=6)
def test_delete_student_in_attendance_manager(capfd, attendance_manager):
    expected_output = f'Attendance entry for user with id 6000 on 2024-11-28 deleted.'

    attendance_manager.delete('2024-11-28', '6000')

    captured = capfd.readouterr()

    assert captured.out.strip() == expected_output

