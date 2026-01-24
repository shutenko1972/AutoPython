<!-- Начало: Effective Mobile 

Автоматизированные тесты для сайта (https://www.saucedemo.com/)

Тестовые сценарии:

1. Успешный логин (standard_user / secret_sauce)
2. Логин с неверным паролем
3. Логин заблокированного пользователя (locked_out_user)
4. Логин с пустыми полями
5. Логин пользователем performance_glitch_user

Минимальные требования для запуска на ПК:

Что должно быть установлено:
Python 3.10+ (обязательно)
Google Chrome (обязательно)
Git (опционально, для клонирования)

Для запуска на ПК:
1. Скопировать всю папку проекта
2. Установка замисимости 
Запустить `install.bat`
3. Запустить тесты
run_simple.bat

Терминал:
1. Создайте виртуальное окружение
python -m venv venv
2. Активируйте (Windows)
venv\Scripts\activate
3. Установите зависимости
pip install -r requirements.txt
4. Запуск тестов
pytest tests/ -v

Docker Desktop:
docker build -t tests .
docker run --shm-size=2g tests

Узнать структуру приложения:
tree      # показать структуру
tree /F   # показать файлы 

Конец -->
