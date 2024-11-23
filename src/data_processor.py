"""
Ожидается, что после обработки файла 'data.txt' на консоль будут выведены следующие строки:

Итог по всем покупкам:
apple: 13
banana: 7
grape: 6

"""


class DataProcessor:

    def __init__(self, filename=None):
        self.filename = filename

    def process_data(self, data=None):
        """
        Обрабатывает данные из файла или переданного списка строк.
        :param data: список строк, если передан. Если None, читаем файл.
        :return: словарь с результатами
        """
        result = {}

        # Если data не передан, читаем строки из файла
        if data is None:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = file.readlines()

        # Обрабатываем каждую строку
        for line in data:
            line = line.strip()

            # Пропускаем строки без разделителя ':'
            if ':' not in line:
                continue

            # Разделяем строку на ключ и значение
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Проверяем, что значение - число
            if not value.isdigit():
                continue

            value = int(value)

            # Обновляем словарь
            if key in result:
                result[key] += value
            else:
                result[key] = value

        return result
        
if __name__ == "__main__":
    # Указываем путь к файлу относительно корня проекта
    filename = "data/data.txt"

    # Создаем экземпляр класса с именем файла
    processor = DataProcessor(filename)

    # Вызываем метод обработки данных
    result = processor.process_data()

    # Выводим результат на консоль
    print("Итог по всем покупкам:")
    for key, value in result.items():
        print(f"{key}: {value}")