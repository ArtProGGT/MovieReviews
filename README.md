# Отзывы к фильмам

Сайт с фильмами, на котором каждый может написать свой отзыв к ним!

## Описание

Сайт с фильмами, созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro.

## Технологии

* Python
* Flask
* WTForms
* SQLAlchemy

## Как запустить

1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```commandline
python -m venv venv
source venv/Scripts/activate
```
3. Установите зависимости
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env и укажите настройки подключения к БД и другие параметры
```
DATABASE_URI=sqlite:///movies.db
SECRET_KEY=YOUR_SECRET_KEY
```
5. Запустите Flask-приложение
```commandline
flask run
```
