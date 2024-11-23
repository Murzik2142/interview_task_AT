import unittest
from src.data_processor import DataProcessor  # Импортируем основной код

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.processor = DataProcessor()

    def test_normal_data(self):
        """Тест на корректную обработку нормальных данных"""
        data = [
            "apple: 10",
            "banana: 5",
            "grape: 2",
            "apple: 3"
        ]
        expected = {"apple": 13, "banana": 5, "grape": 2}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_invalid_data(self):
        """Тест на пропуск некорректных строк"""
        data = [
            "apple: 10",
            "banana: five",  # Некорректное значение
            "orange три",    # Нет разделителя ':'
            "grape: 2"
        ]
        expected = {"apple": 10, "grape": 2}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_empty_data(self):
        """Тест на обработку пустых данных"""
        data = []
        expected = {}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_duplicate_keys(self):
        """Тест на объединение значений для одинаковых ключей"""
        data = [
            "apple: 5",
            "apple: 10",
            "apple: 15"
        ]
        expected = {"apple": 30}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)

    def test_mixed_data(self):
        """Тест на смешанные данные"""
        data = [
            "apple: 10",
            "banana: 5",
            "grape: два",  # Некорректное значение
            "box of oranges",  # Строка без разделителя ':'
            "apple: 3",
            "banana: 2"
        ]
        expected = {"apple": 13, "banana": 7}
        result = self.processor.process_data(data)
        self.assertEqual(result, expected)


# Запуск тестов, если файл запускается напрямую
if __name__ == "__main__":
    unittest.main()