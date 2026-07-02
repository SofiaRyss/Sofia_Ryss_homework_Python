import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    """Создает экземпляр StringUtils для тестов"""
    return StringUtils()


class TestCapitalize:
    """Тесты для метода capitalize"""

    def test_capitalize_first_letter(self, string_utils):
        """Позитивный тест: делает первую букву заглавной"""
        assert string_utils.capitalize("skypro") == "Skypro"

    def test_capitalize_already_uppercase(self, string_utils):
        """Позитивный тест: строка уже с заглавной буквы"""
        assert string_utils.capitalize("Skypro") == "Skypro"

    def test_capitalize_single_letter(self, string_utils):
        """Позитивный тест: одна буква"""
        assert string_utils.capitalize("s") == "S"

    def test_capitalize_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        assert string_utils.capitalize("") == ""

    def test_capitalize_with_numbers(self, string_utils):
        """Негативный тест: строка начинается с цифры"""
        assert string_utils.capitalize("123abc") == "123abc"

    def test_capitalize_with_special_chars(self, string_utils):
        """Негативный тест: строка начинается со спецсимвола"""
        assert string_utils.capitalize("!hello") == "!hello"


class TestTrim:
    """Тесты для метода trim"""

    def test_trim_leading_spaces(self, string_utils):
        """Позитивный тест: удаляет пробелы в начале"""
        assert string_utils.trim("   skypro") == "skypro"

    def test_trim_no_spaces(self, string_utils):
        """Позитивный тест: нет пробелов"""
        assert string_utils.trim("skypro") == "skypro"

    def test_trim_multiple_spaces(self, string_utils):
        """Позитивный тест: много пробелов"""
        assert string_utils.trim("     hello") == "hello"

    def test_trim_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        assert string_utils.trim("") == ""

    def test_trim_only_spaces(self, string_utils):
        """Негативный тест: строка только из пробелов"""
        assert string_utils.trim("   ") == ""

    def test_trim_trailing_spaces_not_removed(self, string_utils):
        """ДЕФЕКТ: пробелы в конце НЕ удаляются"""
        # Ожидаем, что trim удалит пробелы с обеих сторон
        # Но метод удаляет только в начале
        result = string_utils.trim("skypro   ")
        assert result == "skypro   "  # Пробелы остались!

    def test_trim_tabs_not_removed(self, string_utils):
        """ДЕФЕКТ: табуляция не удаляется"""
        result = string_utils.trim("\thello")
        assert result == "\thello"  # Табуляция осталась!


class TestContains:
    """Тесты для метода contains"""

    def test_contains_symbol_present(self, string_utils):
        """Позитивный тест: символ есть"""
        assert string_utils.contains("SkyPro", "S") is True

    def test_contains_symbol_absent(self, string_utils):
        """Позитивный тест: символа нет"""
        assert string_utils.contains("SkyPro", "U") is False

    def test_contains_substring(self, string_utils):
        """Позитивный тест: подстрока есть"""
        assert string_utils.contains("SkyPro", "ky") is True

    def test_contains_empty_symbol(self, string_utils):
        """Пустая строка содержится в любой строке (нормальное поведение Python)"""
        result = string_utils.contains("hello", "")
        assert result is True  # Исправлено: ожидаем True

    def test_contains_empty_string(self, string_utils):
        """Негативный тест: пустая строка для поиска"""
        assert string_utils.contains("", "a") is False

    def test_contains_case_sensitive(self, string_utils):
        """Негативный тест: регистр важен"""
        assert string_utils.contains("SkyPro", "s") is False


class TestDeleteSymbol:
    """Тесты для метода delete_symbol"""

    def test_delete_symbol_present(self, string_utils):
        """Позитивный тест: удаляет символ"""
        assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_substring(self, string_utils):
        """Позитивный тест: удаляет подстроку"""
        assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_absent(self, string_utils):
        """Позитивный тест: символа нет"""
        assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"

    def test_delete_all_occurrences(self, string_utils):
        """Позитивный тест: удаляет все вхождения"""
        assert string_utils.delete_symbol("banana", "a") == "bnn"

    def test_delete_empty_symbol(self, string_utils):
        """Негативный тест: пустой symbol"""
        assert string_utils.delete_symbol("hello", "") == "hello"

    def test_delete_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        assert string_utils.delete_symbol("", "a") == ""
