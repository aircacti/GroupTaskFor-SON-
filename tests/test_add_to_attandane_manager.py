import pytest

@pytest.mark.run(order=2)
def test_add_to_attendance_manager(capfd, attendance_manager):
    sample_date = '2024-11-28'
    sample_user_id = '6000'
    sample_was = True

    expected_output = f'User with id {sample_user_id} on {sample_date} attendance status marked as {sample_was}.'

    attendance_manager.add(date=sample_date, user_id=sample_user_id, was=sample_was)

    captured = capfd.readouterr()

    assert captured.out.strip() == expected_output
