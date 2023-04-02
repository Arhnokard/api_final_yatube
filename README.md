**Проект API_FINAL_YATUBE**
В этом проекте реализовано API с помощью которого можно получать списки постов, групп, коментариев к постам, подписчиков,
а также создавать, редактировать и удалять их.

**Установка проекта на локальной машине**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/scriptable/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

**Примеры запросов к API**

Получение публикачии по id
```
GET http://127.0.0.1:8000/api/v1/posts/{id}
```
Ответ
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

Обновление публикации по id
```
PUT http://127.0.0.1:8000/api/v1/posts/{id}/
{
    "text": "Изменнёный текст поста 1"
}
```

Ответ
```
{
"text": "string",
"image": "string",
"group": 0
}
```

Получение комментария к публикации по id
```
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
{
    "text": "Comment test"
}
```

Ответ
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
