import pytest
from main import add_student
from unittest.mock import patch

@pytest.mark.run(order=1)
def test_add_student():
    mock_input = ['Jan', 'Kowalski', '12345']
    expected_output = "Jan,Kowalski,12345\n"

    with patch('builtins.input', side_effect=mock_input):
        result = add_student()
        assert result == expected_output