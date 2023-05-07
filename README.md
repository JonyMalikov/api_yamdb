# api_yamdb
api_yamdb

## Описание
Этот проект - реализация API к YAMDB. Благодаря ему можно создавать, получать, обновлять и удалять произведения разных категорий (таких, как «Книги», «Фильмы», «Музыка») и разных жанров (например, «Сказка», «Рок» или «Артхаус»). Кроме того, произведения можно оценивать и оставлять к ним отзывы, а к отзывам писать комментарии.

## Установка

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:esfiro4ka/api_yamdb.git

cd api_yamdb
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

source venv/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

- Выполнить миграции:

```
python3 manage.py migrate
```

- Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов

- GET-запрос произведения с id=5

```
GET /api/v1/titles/5/
```

- GET-запрос отзыва c id=2 к произведению с id=5

```
GET /api/v1/titles/5/reviews/2/
```

- POST-запрос произведения

```
POST /api/v1/titles/

Content-type: application/json

{
    "name": "Название",
    "year": 2023,
    "description": "Описание произведения",
    "genre": ["Сказка"],
    "category": "Книга"
}
```

## Стек технологий

Python 3, Django 2.2.16, Django REST Framework, SQLite3, JWT.
