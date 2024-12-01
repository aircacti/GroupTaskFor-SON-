import pytest

@pytest.mark.run(order=3)
def test_edit_student_in_attendance_manager(capfd, attendance_manager):
    sample_date = '2024-11-28'
    sample_user_id = '6000'
    sample_was = False

    expected_output = f"User with id {sample_user_id} on {sample_date} attendance status updated to {sample_was}."

    attendance_manager.edit(sample_date, sample_user_id, sample_was)

    captured = capfd.readouterr()

    assert captured.out.strip() == expected_output



