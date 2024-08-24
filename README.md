 <h1>Благотворительный фонд поддержки котиков QRKot.</h1>

![example workflow](https://github.com/MrGorkiy/QRkot_spreadsheets/actions/workflows/cat_charity_fund.yml/badge.svg)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![FastAPI-Users](https://img.shields.io/badge/-FastAPI_Users-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://pypi.org/project/fastapi-users/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.sqlalchemy.org/)
[![aiosqlite](https://img.shields.io/badge/-aiosqlite-464646?style=flat&logo=aiosqlite&logoColor=ffffff&color=043A6B)](https://pypi.org/project/aiosqlite/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://alembic.sqlalchemy.org/en/latest/)
[![GoogleAPI](https://img.shields.io/badge/-GoogleAPI-464646?style=flat&logo=GoogleAPI&logoColor=ffffff&color=043A6B)](https://support.google.com/googleapi/?hl=en#topic=7014522)

## Оглавление
1. [Описание](#описание)
2. [Стек технологий](##стек-технологий)
3. [Как запустить проект](##как-запустить-проект)
4. [Автор проекта](##автор-проекта)

## Описание


QRKot Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции. Добавлена возможность формирования отчёта в гугл-таблице. В таблице выводятся закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается. Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

Целевые проекты создаются администраторами сайта. Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых. Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

## Стек технологий

- Python, FastAPI, FastAOI Users
- Pydantic, SQLALchemy, Alembic, aiosqlite
- GoogleAPI


## как запустить проект

- Клонируйте репозиторий и перейдите в папку проекта:
```
git clone https://git@github.com:vikolga/QRkot_spreadsheets.git
```
- Установите и активируйте виртуальное окружение:
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
- Создать и заполнить файл **.env** 
```
APP_TITLE=Приложение QRKot
APP_DESCRIPTION=Сервис сбора пожертвований для поддержки котиков.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secret
FIRST_SUPERUSER_EMAIL=admin@admin.com
FIRST_SUPERUSER_PASSWORD=admin
EMAIL=your@gmail.com
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
```
- Применение миграций
```bash
alembic upgrade head 
```
- Запустить проект
```bash
uvicorn app.main:app --reload
```
Создание миграции First migration
```bash
alembic revision --autogenerate -m "ADD donation" 
```

После запуска проект будет доступен по адресу: http://127.0.0.1:8000

Документация к API досупна по адресам:
- Swagger: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc


## Автор проекта
_[Ольга Викторова](https://github.com/vikolga/)_, python-developer
