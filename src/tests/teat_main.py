# tests/test_main.py

from src.utils import add_numbers

def test_add_numbers():
    """
        Tests the add_numbers function to ensure it adds correctly.
            """
                assert add_numbers(2, 3) == 5
                    assert add_numbers(-1, 1) == 0
    def test_add_numbers():
            assert add_numbers(2, 3) == 5