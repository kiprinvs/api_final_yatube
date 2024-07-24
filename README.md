# Описание

Учебный проект API для социальной сети, в которой реализовано размещение постов с фото, комментирование и система подписок.

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kiprinvs/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

# Примеры запросов

### Получение JWT токена

POST запрос на эндпоинт `api/v1/jwt/create/`

```
{
    "username": username,
    "password": password,
}
```
Пример ответа:

```
{
    "refresh": token,
    "access": token
}
```

### Получение списка публикаций

POST запрос на эндпоинт `/api/v1/posts/`. Обязательное поле `text`, поля `image` и `group` по желанию.

```
{
    "text": "Тестовая публикация"
}
```
Пример ответа:

```
{
    "id": 83,
    "text": "Тестовая публикация",
    "author": "admin",
    "image": null,
    "group": null,
    "pub_date": "2024-07-24T12:19:54.008613Z"
}
```

### Полная документация доступна по эндпоинту `redoc/`