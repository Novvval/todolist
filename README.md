## Todolist

Приложение по созданию и редактирование целей

Python 3.10, Django, Postgresql

### Как запустить проект

* Создать файл .env в папке todolist
* Создать в нем поля:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=навзание приложения
DB_USER=имя пользователя postgres
DB_PASSWORD=пароль пользователя postgres
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY = секретный ключ
```
* Из папки /todolist запустить manage.py:
```
./manage.py runserver
```
