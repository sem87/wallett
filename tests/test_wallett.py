import pytest
from wallett.chernovik import new, func_plus  # Импортируем обе функции


class TestChernovik:

    # Тестируем функцию new с разными значениями
    @pytest.mark.parametrize("a, expected", [
        (5, 20),  # 5 * 5 - 5 = 20
        (6, 30),  # 6 * 6 - 6 = 30
        (0, 0),  # 0 * 0 - 0 = 0
        (-2, 6),  # -2 * -2 - (-2) = 6
    ])
    def test_new(self, a, expected):
        assert new(a) == expected

    # Тестируем функцию func_plus с разными значениями
    @pytest.mark.parametrize("d, expected", [
        (4, 3),  # 4 - 1 = 3 (значение по умолчанию)
        (8, 7),  # 8 - 1 = 7
        (1, 0),  # 1 - 1 = 0
    ])
    def test_func_plus(self, d, expected):
        assert func_plus(d) == expected

    # Тестируем значения по умолчанию
    def test_default_values(self):
        assert new() == 20  # a=5 -> 5*5-5 = 20
        assert func_plus() == 3  # d=4 -> 4-1 = 3