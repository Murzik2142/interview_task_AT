"""
Ожидается, что после обработки файла 'data.txt' на консоль будут выведены следующие строки:

Итог по всем покупкам:
apple: 13
banana: 7
grape: 6

"""


# Определяем класс для обработки данных из файла
class DataProcessor:

    # Метод инициализации (конструктор), принимает имя файла
    def __init__(self, filename):
        # Сохраняем имя файла как атрибут объекта
        self.filename = filename

    # Основной метод для обработки данных
    def process_data(self):
        # Словарь для хранения итоговых результатов
        result = {}

        # Открываем файл через контекстный менеджер
        # Это гарантирует, что файл будет автоматически закрыт после обработки
        with open(self.filename, 'r', encoding='utf-8') as file:
            # Читаем файл построчно
            for line in file:
                # Убираем лишние пробелы и символы переноса строки в начале и конце строки
                line = line.strip()

                # Пропускаем строки, которые не содержат разделителя ':'
                # Например, строку "box of oranges"
                if ':' not in line:
                    continue

                # Разделяем строку на ключ (название продукта) и значение (количество)
                # split(':', 1) означает, что строка будет разделена на 2 части
                key, value = line.split(':', 1)

                # Убираем лишние пробелы вокруг ключа и значения
                key = key.strip()
                value = value.strip()

                # Проверяем, что значение является числом
                # Если значение не число (например, "три" или "два"), то пропускаем строку
                if not value.isdigit():
                    continue

                # Преобразуем значение из строки в целое число
                value = int(value)

                # Добавляем или обновляем данные в словаре
                # Если продукт уже есть в словаре, увеличиваем его количество
                if key in result:
                    result[key] += value
                # Если продукта нет, добавляем его с текущим количеством
                else:
                    result[key] = value

        # После обработки файла выводим итоговые результаты
        print("Итог по всем покупкам:")
        # Перебираем все пары ключ-значение в словаре и выводим их
        for key, value in result.items():
            print(f"{key}: {value}")


# Создаем объект класса DataProcessor, передавая имя файла для обработки
processor = DataProcessor('data.txt')
# Вызываем метод для обработки данных
processor.process_data()