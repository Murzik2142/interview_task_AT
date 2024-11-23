"""
Ожидается, что после обработки файла 'data.txt' на консоль будут выведены следующие строки:

Итог по всем покупкам:
apple: 13
banana: 7
grape: 6

"""


class DataProcessor:

    def __init__(self, filename):
        self.filename = filename

    def process_data(self):
        result = {}

        # Открываем файл через контекстный менеджер
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if ':' not in line:
                    continue  # Пропускаем строки без разделителя ':'

                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()

                # Пропускаем строки с некорректным значением
                if not value.isdigit():
                    continue

                value = int(value)
                # Добавляем данные в результат
                if key in result:
                    result[key] += value
                else:
                    result[key] = value

        # Вывод результата
        print("Итог по всем покупкам:")
        for key, value in result.items():
            print(f"{key}: {value}")


processor = DataProcessor('data.txt')
processor.process_data()