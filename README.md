# Анализатор страниц
****
### Hexlet tests and linter status:
[![Actions Status](https://github.com/ttehasi/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ttehasi/python-project-83/actions)
[![my check](https://github.com/ttehasi/python-project-83/actions/workflows/check.yaml/badge.svg)](https://github.com/ttehasi/python-project-83/actions/workflows/check.yaml)
[![Maintainability](https://qlty.sh/badges/37fab6da-add5-4d8c-8ef3-8813871b08ce/maintainability.svg)](https://qlty.sh/gh/ttehasi/projects/python-project-83)
****

[Проект на render.com](https://page-analuzerfromtte.onrender.com)

### Описание проекта
Анализатор страниц это сайт, который анализирует указанные страницы на SEO-пригодность по аналогии с PageSpeed Insights.
****

### Использованные технологии:


| Инструмент                                                                       | Описание                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                                 | "is an extremely fast Python package manager written in Rust. It is designed as a replacement for pip and pip-tools. It can also replace venv and pyenv."                                                                                                                   |            |
| [ruff](https://docs.astral.sh/ruff/)                                             | "Your Tool For Linter and Style Guide Enforcement"                                                                                                                                                                                                                          |
| [Flask](https://flask.palletsprojects.com/en/stable/)                            | "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications"                                                                                                        |
| [Gunicorn](https://docs.gunicorn.org/en/latest/index.html)                       | "Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy." |
| [python-dotenv](https://pypi.org/project/python-dotenv/)                         | "Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles."                                                                                           |
| [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)     | "Bootstrap is a powerful, feature-packed frontend toolkit. Build anything—from prototype to production—in minutes."                                                                                                                                                         |
| [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)       | "SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL."                                                                                                                                                                                                                          |
| [validators](https://validators.readthedocs.io/en/latest/#module-validators.url) | "Python Data Validation for Humans™."                                                                                                                                                                                                                                       |
| [Requests](https://requests.readthedocs.io/en/latest/)                           | "Requests is an elegant and simple HTTP library for Python, built for human beings."                                                                                                                                                                                        |
| [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)          | "Beautiful Soup is a Python library for pulling data out of HTML and XML files."                                                                                                                                                                                            |
---

## Установка
### Склонируйте репозиторий:
```
git clone git@github.com:ttehasi/python-project-83.git
```
### Перейдите в папку проекта:
```
cd python-project-83
```
### Для использования данного приложения вам необходимо настроить .env файл.
После клонирования репозитория, вам необходимо переименовать файл .env_example в .env, внутри файла вы найдете переменные SECRET_KEY и DATABASE_URL, вам необходимо вписать свои значения. 
****
### Следующим шагом с помощью команды ниже, установите необходимые зависимости и сгенерируйте таблицы в базе данных.
```
make build
```
### Запустите приложение командой ниже.

```
make start
```