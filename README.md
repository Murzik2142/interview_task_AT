
# interview_task_AT

## Описание проекта

**interview_task_AT** – это простой Python-проект для обработки текстовых файлов с данными о покупках. Программа читает данные из файла, суммирует количества для каждого товара и выводит итог на консоль.

---

## Структура проекта

```
project/
├── data/                   # Папка для хранения данных
│   └── data.txt            # Входной файл с данными
├── src/                    # Папка с исходным кодом программы
│   └── data_processor.py   # Основной код программы
├── tests/                  # Папка для тестов
│   └── test_data_processor.py  # Unit-тесты
└── README.md               # Документация проекта
```

---

## Требования

- Python 3.6 или выше

---

## Установка

1. Склонируйте репозиторий на ваш компьютер:
   ```bash
   git clone git@github.com:Murzik2142/interview_task_AT.git
   cd nterview_task_AT
   ```

2. Убедитесь, что Python установлен:
   ```
   python3 --version
   ```

---

## Использование

1. Добавьте файл с данными в папку `data`. Пример данных (`data/data.txt`):
   ```
   apple:  10
   banana: 5
   orange: три
   grape:  два

   apple:  3
   banana: 2
   box of oranges
   grape:  6
   ```

2. Перейдите в корень проекта и запустите программу:
   ```bash
   python src/data_processor.py
   ```

3. Результат:
   ```
   Итог по всем покупкам:
   apple: 13
   banana: 7
   grape: 6
   ```

---

## Тестирование

Для проверки работы программы выполните unit-тесты.  
В проекте используется стандартный модуль `unittest`.

1. Перейдите в корень проекта:
   ```bash
   cd path/to/project
   ```

2. Запустите тесты:
   ```bash
   python -m unittest discover -s tests
   ```

3. Результат:
   ```
   .....
   ----------------------------------------------------------------------
   Ran 5 tests in 0.002s

   OK
   ```

---

## Контакты

Автор: **Murzabaev Marat**  
Email: **github-marat@albusfox.ru**  
GitHub: [Murzik2142](https://github.com/Murzik2142)

---

## Лицензия

Этот проект распространяется под лицензией MIT.
