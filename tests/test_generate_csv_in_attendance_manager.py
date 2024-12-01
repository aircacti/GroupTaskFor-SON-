import pytest
import os

@pytest.mark.run(order=5)
def test_generate_csv_in_attendance_manager(capfd, attendance_manager):
    attendance_manager.generate_report()

    expected_output = "User ID,Date,Status\n1,2024-11-28,True"

    assert os.path.exists("attendance_report.csv"), "Plik attendance_report.csv nie istnieje."

    with open("attendance_report.csv", "r") as file:
        content = file.read().strip()

    assert content == expected_output
