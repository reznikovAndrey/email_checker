# Реализовать backend механики. ТЗ.
- Пользователь заходит на сайт
- Пользователь играет в игру
- Пользователь оставляет свою почту
- Backend принимает почту
- Backend смотрит в свою базу играла почта или нет
- Если в базе игры почты нет:
     - Backend проверяет в ESP системе есть такая почта или нет
     - Если почты нет, создает ее в ESP системе
     - Backend записывает в свою базу факт игры
- Если в базе игры почта есть
     - Backend инкрементит в базе кол. игр
- Backend возвращает на фронт результат: 
     - Почта была в ESP или нет 
     - Почта была в базе игры или
     - Кол. игр с учетом этой игры

## Причины выбора FastAPI:
- FastAPI быстрее и легковеснее (в сравнении с `django`).
- FastAPI поддерживает "из коробки" асинхронное выполнение задач (в проекте используется `Background_tasks` для взаимодействия с esp.)
- Статическая типизация для валидации данных (в отличие от `Flask`).
## Описание структуры проекта:
- Основной код приложения находится в пакете `app`. Отдельно от него находятся миграции бд `alembic`, файлы для развертывания проекта `dockerfile` и `docker-compose.yaml`, `.env` для хранения переменных среды, `requirements.txt` с необходимыми библиотеками.
- Стуктура приложения `app`:
```
app
├── api  # эндпоинты
     ├── __init__.py
     ├── users.py  # эндпоинты разделены в зависимости от бизнес логики
     ...
├── db  # все, что иммет отношение к бд
    ├── __init__.py
    ├── database.py  # подключение к бд
    ├── tables.py  # модели таблицы 
├── esp  # моковая имплементация esp
├── models  # pydantic схемы
      ├── __init__.py
      ├── users.py  # модели разделены в зависимости от бизнес логики
      ...
├── services  # бизнес логика всех задач
       ├── __init__.py
       ├── users.py  # каждый сервис отвечает за определенную задачу
       ...
├── __init__.py
├── app.py  # запуск приложения
├── settings.py  # настройки приложения
```
## Технологии:
- FastAPI
- SQLAlchemy + Alembic
- PostgreSQL
- Docker
## Что необходимо улучшить(дополнить):
- покрыть проект тестами
- полноценные crud операции для существующих моделей
- регистрация и авторизация пользователей
## Как запустить проект:
- Склонируйте репозиторий и перейдите в него:
```bash
git clone https://github.com/Another-Andrey/test-task-from-out_of_cloud.git
cd test-task-from-out_of_cloud
```
- Создайте `.env` файл (в качестве примера используйте `.env_example`):
```bash
touch .env
```
- Пример `env_example`:
```
# POSTGRES
POSTGRES_USER=<...>  # default `postgres`
POSTGRES_PASSWORD=<...>  # Ваш пароль
POSTGRES_DB=<...>  # default `postgres`

# app
db_url=postgresql://<POSTGRES_USER>:<POSTGRES_PASSWORD>@db:5432/<POSTGRES_DB>
```
- Запустите контейнеры с бд и приложением:
```bash
docker-compose up
```
- Запустите миграции в бд:
```
docker-compose exec web alembic upgrade head
```
- После применения миграций Вы увидите следующие сообщения:
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> cc15650a2c2f, Add tables `users` and `games`
```
- Документация к API и примеры запросов будут доступны по адресу:
```
http://127.0.0.1:8000/docs
```

## Автор: Андрей Резников
