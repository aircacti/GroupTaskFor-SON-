import os

import pytest
from import_eksport_files import (export_students_csv, export_students_txt,
                                  import_students_csv, import_students_txt)

#TODO: Refactor whole file
@pytest.fixture
def sample_students():
    return [{'name': 'Jan Kowalski', 'present': False}, {'name': 'Adam Nowak', 'present': False}]


@pytest.fixture
def csv_file_path(tmp_path):
    return os.path.join(tmp_path, 'test_students.csv')


@pytest.fixture
def txt_file_path(tmp_path):
    return os.path.join(tmp_path, 'test_students.txt')


def test_import_students_csv(csv_file_path, sample_students):
    content = "Jan Kowalski\nAdam Nowak\n"
    with open(csv_file_path, mode='w') as f:
        f.write(content)

    imported_students = import_students_csv(csv_file_path)
    assert imported_students == sample_students


def test_export_students_csv(csv_file_path, sample_students):
    export_students_csv(sample_students, csv_file_path)
    with open(csv_file_path, mode='r') as f:
        content = f.read()
    expected_content = 'Name,Present\nJan Kowalski,False\nAdam Nowak,False\n'
    assert content == expected_content


def test_import_students_txt(txt_file_path, sample_students):
    content = "Jan Kowalski\nAdam Nowak\n"
    with open(txt_file_path, mode='w') as f:
        f.write(content)

    imported_students = import_students_txt(txt_file_path)
    assert imported_students == sample_students


def test_export_students_txt(txt_file_path, sample_students):
    export_students_txt(sample_students, txt_file_path)
    with open(txt_file_path, mode='r') as f:
        content = f.read()
    expected_content = "Jan Kowalski: Absent\nAdam Nowak: Absent\n"
    assert content == expected_content

