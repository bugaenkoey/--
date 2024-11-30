Давай розглянемо найпростіший приклад безперервної інтеграції (CI) за допомогою GitHub і GitHub Actions.

Приклад безперервної інтеграції з GitHub Actions
1. Репозиторій на GitHub:

Створи новий репозиторій на GitHub або використовуй існуючий.

2. Створення простого Python проєкту:

Додай простий Python файл (наприклад, app.py) з таким кодом:

python


def add(a, b):
    return a + b
3. Створення тесту:

Додай тестовий файл (наприклад, test_app.py) з таким кодом:

python


import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

4. Створення GitHub Action:

Створи директорію .github/workflows у корені твого репозиторію.

Всередині цієї директорії створи файл ci.yml з таким вмістом:

yaml


name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
    - name: Run tests
      run: |
        pytest

Як це працює:
Репозиторій GitHub: Коли ти виконуєш push змін до основної гілки твого репозиторію, GitHub запускає описану дію.

GitHub Actions: GitHub Actions автоматично виконує описані кроки у файлі ci.yml.

Checkout: Завантажує код з репозиторію.

Setup Python: Встановлює Python.

Install dependencies: Встановлює залежності проєкту.

Run tests: Виконує тести.

Результат:
Якщо всі тести проходять успішно, то зміни об'єднуються до основної гілки. Якщо тести не проходять, то GitHub повідомить тебе про помилки, і ти зможеш виправити їх перед об'єднанням змін.

Цей простий приклад ілюструє, як можна налаштувати базову систему CI для автоматичного тестування коду перед його об'єднанням до основної гілки.