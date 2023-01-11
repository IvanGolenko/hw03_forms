# Yatube: новые записи

[![CI](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml)

### Описание
Социальная сеть для публикации дневников: реализована регистрация, размещение публикаций, добавление публикаций в группы.
Дополнения в проекте:
- Настроен эмулятор отправки писем при регистрации и восстановлении пароля.
- Создан и зарегистрирован контекст-процессор, добавляющий текущий год на все страниц. 
- Созданы статические страницы /about/author/ и /about/tech/, добавлены в навигацию сайта.
- Создана страница пользователя profile/<username>/. На ней отображаются посты пользователя.
- Подключен паджинатор - выводит по десять постов.
- Добавлена страница редактирования публикаций, право на редактиование только у автора.

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
### Технологии
- Python 3.7
- Django 2.2.6

### Автор
Иван Голенко
