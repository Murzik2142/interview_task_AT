import unittest
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        """Инициализация экземпляра DataProcessor для тестов"""
        self.processor = DataProcessor()

    def test_process_data_valid(self):
        """Тест обработки корректных данных"""
        data = [
            "apple: 10",
            "banana: 5",
            "grape: 2",
            "apple: 3"
        ]
        expected = {"apple": 13, "banana": 5, "grape": 2}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_process_data_with_invalid_lines(self):
        """Тест обработки данных с некорректными строками"""
        data = [
            "apple: 10",
            "banana: five",  # Некорректное значение
            "grape: два",    # Некорректное значение
            "apple: 3",
            "orange три"      # Некорректная строка
        ]
        expected = {"apple": 13}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_process_data_empty(self):
        """Тест обработки пустого списка строк"""
        data = []
        expected = {}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_process_data_no_colon(self):
        """Тест строки без разделителя ':'"""
        data = [
            "apple: 10",
            "no_colon_here",  # Строка без разделителя
            "grape: 6"
        ]
        expected = {"apple": 10, "grape": 6}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_process_data_duplicate_keys(self):
        """Тест обработки данных с повторяющимися ключами"""
        data = [
            "apple: 10",
            "apple: 5",
            "banana: 2",
            "apple: 3"
        ]
        expected = {"apple": 18, "banana": 2}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()